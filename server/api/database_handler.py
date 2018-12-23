import json
from abc import abstractmethod

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

    def get(self, *args, **kwargs):
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
        user_id = self.get_argument('id', None)

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        user_id = self.get_argument('id', None)
