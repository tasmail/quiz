import os

from peewee_migrate import Router
from peewee_migrate.router import CURDIR

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
    users = load_data(data)

def load_data(data):
    users = {}
    return users
