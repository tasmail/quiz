from server.api.database_handler import DatabaseHandler


class UserHandler(DatabaseHandler):
    def get(self, *args, **kwargs):
        user_id = self.get_argument('id', None)
        self.write_json(response={})

    def post(self, *args, **kwargs):
        user_id = self.get_argument('id', None)

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        user_id = self.get_argument('id', None)
