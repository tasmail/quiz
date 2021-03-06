from peewee import CharField, BooleanField, BlobField, ForeignKeyField

from app_log import log
from server.db.models.quiz import Quiz
from .errors import Errors
from .base_model import BaseModel


class Question(BaseModel):
    question = CharField(max_length=2048, null=False, index=True)
    quiz = ForeignKeyField(Quiz, backref='questions', index=True)
    is_active = BooleanField(default=True)

    class Meta:
        indexes = (
            (('question', 'quiz_id'), True),
        )

    @staticmethod
    def create(data):
        question = data['question']
        quiz_id = data['quiz_id']
        questions = Question.select(Question.id).where(Question.question == question, Question.quiz == quiz_id)
        if questions.count():
            return Errors.question_is_already_exists(question)
        else:
            Question.insert(question=question, quiz_id=quiz_id).execute()
            log.info('Question create OK. question:{}'.format(question))
        return Errors.no_error()
