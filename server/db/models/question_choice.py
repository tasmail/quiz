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
    def create(choice, question_id, is_right):
        question_choices = QuestionChoice.select(QuestionChoice.id).where(QuestionChoice.choice == choice,
                                                                          QuestionChoice.question == question_id)
        if question_choices.count():
            return Errors.question_choice_is_already_exists(choice)
        else:
            Question.insert(choice=choice, question_id=question_id, is_right=is_right).execute()
            log.info('Question choice create OK. choice:{}'.format(choice))
        return Errors.no_error()

    @staticmethod
    def remove(choice, question_id):
        question_choices = QuestionChoice.select(QuestionChoice.id).where(QuestionChoice.choice == choice,
                                                                          QuestionChoice.question == question_id)
        if not question_choices.count():
            return Errors.question_choice_not_found(choice)
        QuestionChoice.delete().where(QuestionChoice.id << question_choices).execute()
        log.info('Question choice remove OK. question:{}'.format(choice))
        return Errors.no_error()
