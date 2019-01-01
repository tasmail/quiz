from server.api.database_handler import DatabaseHandler
from server.db.models.question import Question
from server.db.models.question_choice import QuestionChoice
from server.db.models.quiz import Quiz
from server.db.models.user import User
from server.db.models.user_answer import UserAnswer
from server.db.models.user_quiz import UserQuiz


class QuestionHandler(DatabaseHandler):
    @property
    def model_class(self):
        return Question


class QuestionChoiceHandler(DatabaseHandler):
    @property
    def model_class(self):
        return QuestionChoice


class QuizHandler(DatabaseHandler):
    @property
    def model_class(self):
        return Quiz


class UserHandler(DatabaseHandler):
    @property
    def model_class(self):
        return User


class UserAnswerHandler(DatabaseHandler):
    @property
    def model_class(self):
        return UserAnswer


class UserQuizHandler(DatabaseHandler):
    @property
    def model_class(self):
        return UserQuiz
