from .example_data import *

LOGGING['handlers']['app'] = {
    'level': 'DEBUG',
    'class': 'logging.StreamHandler',
    'formatter': 'verbose',
}

# API['key'] = 'SOME HASH'

DATABASE['url'] = 'sqlite:///quiz-tas.db'
# DATABASE['sql_log_enabled'] = True
