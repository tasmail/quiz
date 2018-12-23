import logging
import os
from logging.config import dictConfig

import sys

from settings.settings import SETTINGS_LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log = logging.getLogger('app')


def _setup_logging():
    global is_logging_initialized
    is_logging_initialized = True
    dictConfig(SETTINGS_LOGGING)


if not hasattr(sys.modules[__name__], 'is_logging_initialized'):
    _setup_logging()
