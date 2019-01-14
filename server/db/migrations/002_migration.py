"""Peewee migrations -- 001_0_void_migration.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['model_name']            # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.python(func, *args, **kwargs)        # Run python code
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.drop_index(model, *col_names)
    > migrator.add_not_null(model, *field_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)

"""

import peewee as pw

from app_log import log
from server.db.models.question import Question
from server.db.models.question_choice import QuestionChoice
from server.db.models.quiz import Quiz
from server.db.models.user import User
from server.db.models.user_answer import UserAnswer
from server.db.models.user_quiz import UserQuiz

try:
    import playhouse.postgres_ext as pw_pext
except ImportError:
    pass

SQL = pw.SQL


def migrate(migrator, database, fake=False, **kwargs):
    log.info('Add column image to Quiz table.')
    migrator.add_columns(Quiz, image=pw.BlobField(null=True))


def rollback(migrator, database, fake=False, **kwargs):
    log.info('Drop column image from Quiz table.')
    migrator.drop_columns(Quiz, image=pw.BlobField(null=True))
