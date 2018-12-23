import datetime
import json

from peewee import Model, AutoField, DateTimeField
from playhouse.db_url import connect

from settings.base import DEFAULT_SERVER_DATETIME_FORMAT
from settings.settings import SETTINGS_DATABASE

db = connect(SETTINGS_DATABASE.get('url'))


class BaseModel(Model):
    id = AutoField(primary_key=True)
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    @classmethod
    def insert(cls, __data=None, **insert):
        if not (insert.get('created_at') and insert.get('updated_at')):
            insert['created_at'] = insert['updated_at'] = datetime.datetime.now()
        return super(BaseModel, cls).insert(__data, **insert)

    @classmethod
    def update(cls, __data=None, **update):
        update['updated_at'] = datetime.datetime.now()
        return super(BaseModel, cls).update(__data, **update)

    class Meta:
        database = db

    def to_dict(self):
        r = {}
        for k in self._meta.fields.keys():
            try:
                val = getattr(self, k)
                if isinstance(val, datetime.date) \
                        or isinstance(val, datetime.datetime) or isinstance(val, datetime.time):
                    r[k] = val.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
                else:
                    r[k] = val
            except:
                r[k] = json.dumps(getattr(self, k))
        return r
