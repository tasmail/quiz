import json
import operator
from abc import abstractmethod

import peewee
from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict

from server.api.json_handler import JsonHandler
from server.db.models.base_model import db

# Operator mapping
FILTER_MAP = {
    # <
    'lt': operator.lt,
    # >
    'gt': operator.gt,
    # <=
    'lte': operator.le,
    # >=
    'gte': operator.ge,
    # !=
    'ne': operator.ne,
    # LIKE
    'like': operator.mod,
    # ILIKE
    'ilike': operator.pow,
    # IN
    'in': operator.lshift,
    # ISNULL
    'isnull': operator.rshift
}


class DatabaseHandler(JsonHandler):

    @property
    @abstractmethod
    def model_class(self):
        raise NotImplementedError('Model class must be defined.')

    def initialize(self):
        db.connect()

    def on_finish(self):
        db.close()

    def qs_filter(self, qs, value_filter, value, process_value=True):
        neg = False
        if value_filter[0] in '-':
            neg = True
            value_filter = value_filter[1:]
        field_name, _, k = value_filter.rpartition('__')
        if not field_name:
            field_name, k = k, ''

        operation = FILTER_MAP.get(k, operator.eq)

        if neg:
            _operation = operation
            operation = lambda f, x: operator.inv(_operation(f, x))

        fld = getattr(self.model_class, field_name)

        if process_value:
            _v = value.decode()
            if isinstance(fld, peewee.BooleanField) and _v in ('0', 'f'):
                _v = False
            elif k == 'in':
                _v = _v.split(',')
            elif k == 'isnull':
                _v = None
        else:
            _v = value

        return qs.where(operation(fld, _v))

    def get(self, model_id=None):
        if not model_id:
            model_id = self.get_argument('id', None)
        if model_id:
            qs = self.model_class.select().where(self.model_class.id == model_id)
        else:
            limit = self.get_argument('limit', None)
            offset = self.get_argument('offset', 0)
            if limit:
                qs = self.model_class.select().limit(limit).offset(offset)
            else:
                qs = self.model_class.select()

        for k, v in self.request.arguments.items():
            if k in ['id']:
                continue
            else:
                qs = self.qs_filter(qs, k, v[0])

        res = []
        for item in qs:
            res.append(item.to_dict())
        self.write_json(response=res)

    def post(self, *args, **kwargs):
        data = {}
        for argument in self.request.arguments:
            arguments = self.request.arguments[argument]
            if len(arguments):
                data[argument] = arguments[0]
        try:
            res_id = self.model_class.insert(data).execute()
            self.set_status(201)
            qs = self.model_class.select().where(self.model_class.id == res_id).select()
            for item in qs:
                self.write_json(response=item.to_dict())
        except IntegrityError as ex:
            self.send_error(409, message=str(ex))

    def put(self, model_id=None):
        if not model_id:
            model_id = self.get_argument('id', None)
        data = {}
        for argument in self.request.arguments:
            if argument == 'id':
                continue
            arguments = self.request.arguments[argument]
            if len(arguments):
                data[argument] = arguments[0]
        try:
            if not model_id:
                res = self.model_class.insert(data).execute()
                self.set_status(201)
                self.write_json(response={'id': res})
            else:
                self.model_class.update(data).where(self.model_class.id == model_id).execute()
        except IntegrityError as ex:
            self.send_error(409, message=str(ex))

    def delete(self, model_id=None):
        if not model_id:
            model_id = self.get_argument('id', None)
        if not model_id:
            self.set_status(204)
            return
        res = self.model_class.delete().where(self.model_class.id == model_id).execute()
        if not res:
            self.set_status(204)
