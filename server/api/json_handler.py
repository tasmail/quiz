import json

import tornado.web

from server.api.auth import auth
from settings.settings import SETTINGS_API


class JsonHandler(tornado.web.RequestHandler):
    """Request handler where requests and responses speak JSON."""

    @auth()
    def prepare(self):
        # Incorporate request JSON into arguments dictionary.
        if self.request.body:
            try:
                if isinstance(self.request.body, bytes):
                    json_data = json.loads(self.request.body.decode("utf-8"))
                else:
                    json_data = json.loads(self.request.body)
                for item in json_data:
                    data = json_data.get(item, False)
                    self.request.arguments[item] = [data]
            except ValueError:
                message = 'Unable to parse JSON.'
                self.send_error(400, message=message)  # Bad Request

    def write_error(self, status_code, **kwargs):
        response = dict(error_type='http_' + str(status_code), error='Unknown error')
        if 'message' in kwargs:
            response['error'] = str(kwargs.get('message', response['error']))
        elif 'exc_info' in kwargs:
            response['error'] = str(kwargs.get('exc_info', response['error']))

        self.write_json(response)

    def write_json(self, response=None):
        output = json.dumps(response)
        self.write(output)

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

        if SETTINGS_API.get('disable_cors'):
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Access-Control-Allow-Headers", "x-requested-with, content-type")
            self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')

    def options(self):
        if SETTINGS_API.get('disable_cors'):
            self.set_status(204)
            self.finish()
