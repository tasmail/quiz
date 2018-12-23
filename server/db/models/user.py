from peewee import CharField, BooleanField, BlobField

from app_log import log
from .errors import Errors
from .base_model import BaseModel


class User(BaseModel):
    login = CharField(max_length=128, null=False, unique=True)
    password = CharField(max_length=128, null=False)
    is_admin= BooleanField(default=False)
    image = BlobField()

    @staticmethod
    def create(login, password, image, is_admin=False):
        users = User.select(User.id).where(User.login == login)
        if users.count():
            return Errors.user_is_already_exists(login)
        else:
            User.insert(login=login, password=password, image=image, is_admin=is_admin).execute()
            log.info('User create OK. login:{}'.format(login))
        return Errors.no_error()

    @staticmethod
    def remove(login):
        users = User.select(User.id).where(User.login == login)
        if not users.count():
            return Errors.user_not_found(login)
        User.delete().where(User.id == users.get().id).execute()
        log.info('User remove OK. login:{}'.format(login))
        return Errors.no_error()
