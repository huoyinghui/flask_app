# -*- coding:utf-8 -*-
# Example command to run the example:
#
#   $ gunicorn flaskapp_aiohttp_wsgi:aioapp -k aiohttp.worker.GunicornWebWorker
#   $ gunicorn main:aioapp -c gunicorn.conf.py -k aiohttp.worker.GunicornWebWorker
#
import logging
from aiohttp import web
from aiohttp_wsgi import WSGIHandler

from app import app


def make_aiohttp_app(app):
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    wsgi_handler = WSGIHandler(app)
    aioapp = web.Application()
    aioapp.router.add_route('*', '/{path_info:.*}', wsgi_handler)
    return aioapp

aioapp = make_aiohttp_app(app)
