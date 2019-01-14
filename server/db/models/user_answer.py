from peewee import CharField, BooleanField, BlobField, ForeignKeyField

from app_log import log
from server.db.models.question import Question
from server.db.models.question_choice import QuestionChoice
from server.db.models.quiz import Quiz
from server.db.models.user_quiz import UserQuiz
from .errors import Errors
from .base_model import BaseModel


class UserAnswer(BaseModel):
    user_quiz = ForeignKeyField(UserQuiz, backref='answers', index=True)
    question_choice = ForeignKeyField(QuestionChoice, backref='user_choices', index=True)
    is_right = BooleanField(default=False)

    @staticmethod
    def create(data):
        user_quiz_id = data['user_quiz_id']
        question_choice_id = data['question_choice_id']
        user_answers = UserAnswer.select(UserAnswer.id).where(UserAnswer.user_quiz == user_quiz_id,
                                                              Question.question_choice == question_choice_id)
        if user_answers.count():
            return Errors.user_answer_is_already_exists(user_quiz_id, question_choice_id)
        else:
            UserAnswer.insert(user_quiz=user_quiz_id, question_choice=question_choice_id).execute()
            log.info(
                'UserAnswer create OK. user_quiz_id:{}, question_choice_id:{}'.format(user_quiz_id, question_choice_id))
        return Errors.no_error()
