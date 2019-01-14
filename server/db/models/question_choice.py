from peewee import CharField, BooleanField, ForeignKeyField

from app_log import log
from server.db.models.question import Question
from .errors import Errors
from .base_model import BaseModel


class QuestionChoice(BaseModel):
    choice = CharField(max_length=2048, null=False)
    question = ForeignKeyField(Question, backref='choices', index=True)
    is_right = BooleanField(default=False)

    class Meta:
        indexes = (
            (('choice', 'question_id'), True),
        )

    @staticmethod
    def create(data):
        choice = data['choice']
        question_id = data['question_id']
        is_right = data.get('is_right', False)

        question_choices = QuestionChoice.select(QuestionChoice.id).where(QuestionChoice.choice == choice,
                                                                          QuestionChoice.question == question_id)
        if question_choices.count():
            return Errors.question_choice_is_already_exists(choice)
        else:
            QuestionChoice.insert(choice=choice, question_id=question_id, is_right=is_right).execute()
            log.info('Question choice create OK. choice:{}'.format(choice))
        return Errors.no_error()
