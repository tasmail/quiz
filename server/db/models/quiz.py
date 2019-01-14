from peewee import CharField, BooleanField, BlobField

from app_log import log
from .errors import Errors
from .base_model import BaseModel


class Quiz(BaseModel):
    name = CharField(max_length=128, null=False, unique=True)
    image = BlobField(null=True)

    @staticmethod
    def create(data):
        name = data['name']
        quizzes = Quiz.select(Quiz.id).where(Quiz.name == name)
        if quizzes.count():
            return Errors.quiz_is_already_exists(name)
        else:
            Quiz.insert(name=name).execute()
            log.info('Quiz create OK. name:{}'.format(name))
        return Errors.no_error()
