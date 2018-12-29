#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, run

import logging
logger = logging.getLogger(__name__)


@route('/receive')
def receive():
    logger.info('123')
    return "Hello World!"


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
