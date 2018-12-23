import os

APP_NAME = 'Quiz'

DEFAULT_SERVER_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_SERVER_TIME_FORMAT = "%H:%M:%S"
DEFAULT_SERVER_DATETIME_FORMAT = "%s %s" % (
    DEFAULT_SERVER_DATE_FORMAT,
    DEFAULT_SERVER_TIME_FORMAT)


LISTEN = dict(
    # address to bind to
    address='0.0.0.0',

    # port to listen on
    port=8283,
)

API = dict(
    enabled=True,
    # X-API-Key with key value, should be present in the requests header, if specified.
    key=None,
)

DATABASE = dict(
    # Supported URL's mysql://user:passwd@ip:port/my_db / postgresql://postgres:my_password@localhost:5432/my_database
    url='sqlite:///quiz.db',
    sql_log_enabled=False,
    data=[]
)

ANGULAR = dict(
    enabled=False,
    disable_cors=False,
)

if os.name == 'posix':
    LOG_LOCATION = '/var/log/' + APP_NAME
else:
    LOG_LOCATION = os.path.join(os.path.expanduser('~'), 'var\log', APP_NAME)

if not os.path.exists(LOG_LOCATION):
    os.makedirs(LOG_LOCATION)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(module)s:%(lineno)s] %(message)s",
        }
    },
    'handlers': {
        'app': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_LOCATION, "{}.log".format(APP_NAME)),
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'tornado.access': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_LOCATION + '/tornado.access.log',
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'tornado.general': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_LOCATION + '/tornado.general.log',
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'tornado.application': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_LOCATION + '/tornado.application.log',
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'app': {
            'level': 'INFO',
            'handlers': ['app'],
            'propagate': False
        },
        'tornado.access': {
            'level': 'INFO',
            'handlers': ['tornado.access'],
            'propagate': False
        },
        'tornado.application': {
            'level': 'INFO',
            'handlers': ['tornado.application'],
            'propagate': False
        },
        'tornado.general': {
            'level': 'INFO',
            'handlers': ['tornado.general'],
            'propagate': False
        },
    }
}
