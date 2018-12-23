from peewee import CharField, BooleanField, BlobField

from app_log import log
from .errors import Errors
from .base_model import BaseModel


class Quiz(BaseModel):
    name = CharField(max_length=128, null=False, unique=True)

    @staticmethod
    def create(name):
        quizzes = Quiz.select(Quiz.id).where(Quiz.name == name)
        if quizzes.count():
            return Errors.quiz_is_already_exists(name)
        else:
            Quiz.insert(name=name).execute()
            log.info('Quiz create OK. name:{}'.format(name))
        return Errors.no_error()

    @staticmethod
    def remove(name):
        quizzes = Quiz.select(Quiz.id).where(Quiz.name == name)
        if not quizzes.count():
            return Errors.quiz_not_found(name)
        Quiz.delete().where(Quiz.id == quizzes.get().id).execute()
        log.info('Quiz remove OK. name:{}'.format(name))
        return Errors.no_error()
