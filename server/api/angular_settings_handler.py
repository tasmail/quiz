from server.api.json_handler import JsonHandler
from settings.settings import SETTINGS_ANGULAR


class AngularSettingsHandler(JsonHandler):
    def get(self):
        self.write_json(response=SETTINGS_ANGULAR)
