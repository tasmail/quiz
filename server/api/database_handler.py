import json
from abc import abstractmethod

from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict

from server.api.json_handler import JsonHandler
from server.db.models.base_model import db


class DatabaseHandler(JsonHandler):

    @property
    @abstractmethod
    def model_class(self):
        raise NotImplementedError('Model class must be defined.')

    def initialize(self):
        db.connect()

    def on_finish(self):
        db.close()

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
            res = self.model_class.insert(data).execute()
            self.set_status(201)
            self.write_json(response={'id': res})
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
