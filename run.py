#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from tornado.ioloop import IOLoop

settings_found = False
for arg in sys.argv:
    if arg.startswith('--settings'):
        settings_found = True

if not settings_found:
    sys.argv.append('--settings=settings.base')

from server.api_service import ApiService
from server.db.init import init_db
from server.db.models.base_model import db
from settings.settings import SETTINGS_LISTEN

try:
    import os

    import tornado.autoreload
    import tornado.httpserver
    import tornado.ioloop
    import tornado.options
    import tornado.web

    from app_log import log
except Exception as e:
    print("Failed to start Quiz server. {}".format(e))


class Application(tornado.web.Application):
    def __init__(self, handlers, settings):
        super(Application, self).__init__(handlers, **settings)
        self.db = db


def main():
    log.info('')
    log.info('Starting...')
    log.info('')

    try:
        log.info('Initializing database...')
        init_db()
        log.info('Database initialized.')

        app = Application(
            handlers=ApiService.get_handlers(),
            settings=dict()
        )

        port = SETTINGS_LISTEN.get('port', 8888)
        address = SETTINGS_LISTEN.get('address', '0.0.0.0')
        log.info('Listen on http://{}:{}'.format(address, port))
        app.listen(port, address)
    except Exception as e:
        log.error('Failed to start. {}'.format(e))
        raise

    log.info('')
    log.info('Started.')
    log.info('')
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
