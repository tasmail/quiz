# -*- coding= utf-8 -*-
import functools

from settings.settings import SETTINGS_API


def auth():
    def res(f):
        def _request_auth(handler):
            handler.set_status(403)
            handler.finish()
            return False

        @functools.wraps(f)
        def w_f(*args):
            handler = args[0]

            auth_header = handler.request.headers.get('X-API-Key', None)

            if SETTINGS_API.get('key', False) == auth_header:
                f(*args)
            else:
                _request_auth(handler)

        return w_f

    return res
