from server.api.database_handler import DatabaseHandler
from server.db.models.user import User


class UserHandler(DatabaseHandler):
    @property
    def model_class(self):
        return User
