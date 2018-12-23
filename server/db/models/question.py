from peewee import CharField, BooleanField, BlobField, ForeignKeyField

from app_log import log
from server.db.models.quiz import Quiz
from .errors import Errors
from .base_model import BaseModel


class Question(BaseModel):
    question = CharField(max_length=2048, null=False)
    quiz = ForeignKeyField(Quiz, backref='questions', index=True)
    is_active = BooleanField(default=True)

    class Meta:
        indexes = (
            (('question', 'quiz_id'), True),
        )

    @staticmethod
    def create(question, quiz_id):
        questions = Question.select(Question.id).where(Question.question == question, Question.quiz == quiz_id)
        if questions.count():
            return Errors.question_is_already_exists(question)
        else:
            Question.insert(question=question, quiz_id=quiz_id).execute()
            log.info('Question create OK. question:{}'.format(question))
        return Errors.no_error()

    @staticmethod
    def remove(question, quiz_id):
        questions = Question.select(Question.id).where(Question.question == question, Question.quiz == quiz_id)
        if not questions.count():
            return Errors.question_not_found(question)
        Question.delete().where(Question.id << questions).execute()
        log.info('Question remove OK. question:{}'.format(question))
        return Errors.no_error()
