from peewee import ForeignKeyField

from app_log import log
from server.db.models.quiz import Quiz
from server.db.models.user import User
from .errors import Errors
from .base_model import BaseModel


class UserQuiz(BaseModel):
    user = ForeignKeyField(User, backref='quizzes', index=True)
    quiz = ForeignKeyField(Quiz, backref='users', index=True)

    class Meta:
        indexes = (
            (('user_id', 'quiz_id'), True),
        )

    @staticmethod
    def create(data):
        user_id = data['user_id']
        quiz_id = data['quiz_id']
        user_quizzes = UserQuiz.select(UserQuiz.id).where(UserQuiz.name == user_id, UserQuiz.quiz == quiz_id)
        if user_quizzes.count():
            return Errors.user_quiz_is_already_exists(user_id, quiz_id)
        else:
            UserQuiz.insert(user_id=user_id, quiz_id=quiz_id).execute()
            log.info('UserQuiz create OK. user_id:{}, quiz_id:{}'.format(user_id, quiz_id))
        return Errors.no_error()
