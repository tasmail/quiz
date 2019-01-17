from peewee import CharField, BooleanField, BlobField, TextField

from app_log import log
from .errors import Errors
from .base_model import BaseModel


class QuizCategory(BaseModel):
    name = CharField(max_length=128, null=False, unique=True, index=True)
    image = BlobField(null=True)
    comments = TextField(null=True)

    @staticmethod
    def create(data):
        name = data['name']
        quizzes = QuizCategory.select(QuizCategory.id).where(QuizCategory.name == name)
        if quizzes.count():
            return Errors.quiz_is_already_exists(name)
        else:
            QuizCategory.insert(name=name, image=data.get('image', None), comments=data.get('comments', None)).execute()
            log.info('QuizCategory create OK. name:{}'.format(name))
        return Errors.no_error()
