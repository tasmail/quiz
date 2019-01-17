import os

from peewee_migrate import Router
from peewee_migrate.router import CURDIR

from server.db.models.question import Question
from server.db.models.question_choice import QuestionChoice
from server.db.models.quiz import Quiz
from server.db.models.quiz_category import QuizCategory
from server.db.models.user import User
from .models.base_model import db
from settings.settings import SETTINGS_DATABASE


def init_db():
    try:
        if SETTINGS_DATABASE.get('sql_log_enabled', False):
            import logging
            logger = logging.getLogger('peewee')
            logger.addHandler(logging.StreamHandler())
            logger.setLevel(logging.DEBUG)

        db.connect()

        router = Router(
            database=db,
            migrate_dir=os.path.join(CURDIR, 'server/db/migrations'))
        router.run()

        data = SETTINGS_DATABASE.get('data', False)
        if data:
            create_db_data(data)

    finally:
        db.close()


def create_db_data(data):
    users = data.get('users', None)
    if users:
        for user in users:
            User.create(user)

    quiz_categories = data.get('quiz-categories', None)
    if quiz_categories:
        for quiz_category in quiz_categories:
            QuizCategory.create(quiz_category)

    quizzes = data.get('quizzes', None)
    if quizzes:
        for quiz in quizzes:
            Quiz.create(quiz)

    questions = data.get('questions', None)
    if questions:
        for question in questions:
            Question.create(question)

    question_choices = data.get('question-choices', None)
    if question_choices:
        for question_choice in question_choices:
            QuestionChoice.create(question_choice)
