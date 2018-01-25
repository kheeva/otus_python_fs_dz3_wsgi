#!/usr/bin/env python3
# coding: utf-8
from config import ENCODING, URLS
import views
import models


def get_view_name(url, urls):
    return urls.get(url, None)


def application(environ, start_response):
    url = environ['PATH_INFO']
    headers = [('Content-Type', 'text/html; charset: {}'.format(ENCODING))]

    view_name = get_view_name(url, URLS)
    if not view_name:
        status = '404 Not Found'
        content = b'Not Found'
    else:
        status = '200 OK'
        content = getattr(views, view_name)(view_name, environ)

    start_response(status, headers)
    return [content]
