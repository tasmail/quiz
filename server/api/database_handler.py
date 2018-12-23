from server.api.json_handler import JsonHandler
from server.db.models.base_model import db


class DatabaseHandler(JsonHandler):

    def initialize(self):
        db.connect()

    def on_finish(self):
        db.close()
