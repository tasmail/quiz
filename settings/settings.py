from simple_settings import settings as ss


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


settings = AttrDict(ss.as_dict())
SETTINGS_LOGGING = settings.get('LOGGING')
SETTINGS_LISTEN = settings.get('LISTEN')
SETTINGS_API = settings.get('API')
SETTINGS_DATABASE = settings.get('DATABASE')
SETTINGS_ANGULAR = settings.get('ANGULAR')
SETTINGS_DEFAULT_SERVER_DATETIME_FORMAT = settings.get('DEFAULT_SERVER_DATETIME_FORMAT')