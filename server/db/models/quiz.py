from peewee import CharField, BooleanField, BlobField, TextField, ForeignKeyField

from app_log import log
from server.db.models.quiz_category import QuizCategory
from .errors import Errors
from .base_model import BaseModel


class Quiz(BaseModel):
    name = CharField(max_length=128, null=False, index=True)
    image = BlobField(null=True)
    category = ForeignKeyField(QuizCategory, backref='quizzes', index=True)
    comments = TextField(null=True)

    class Meta:
        indexes = (
            (('name', 'category_id'), True),
        )

    @staticmethod
    def create(data):
        name = data['name']
        category_id = data['category_id']
        quizzes = Quiz.select(Quiz.id).where(Quiz.name == name, Quiz.category == category_id)
        if quizzes.count():
            return Errors.quiz_is_already_exists(name)
        else:
            Quiz.insert(name=name, category_id=category_id, image=data.get('image', None),
                        comments=data.get('comments', None)).execute()
            log.info('Quiz create OK. name:{}'.format(name))
        return Errors.no_error()
