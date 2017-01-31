#!/usr/bin/env python2.6
#! -*- coding: utf-8 -*-

import os
import sys
import tornado.ioloop
import tornado.web
import tornado.httpserver
import logging
import logging.config
import ConfigParser
from tornado.options import define,options

from login import LoginHandler
from login import LogoutHandler
from login import AdminHandler
from login import NopageHandler
from backend.user import UsersHandler

ratellogger = logging.getLogger()
eratellogger = logging.getLogger('log03')

define("port", default=6666, help="run on the given port", type=int)

'''
class testHandler(tornado.web.RequestHandler):
    def get(self):
        ratellogger.info('testGandler get.')
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + "get")
    
    def post(self):
        ratellogger.info('testGandler post.')
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + "post")
'''  
settings = {
    "static_path":os.path.join(os.path.dirname(__file__), "static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template"),
    "cookie_secret": "rgjnUYvXSWSHPjPG6VXDefrn6pT5okNqnS9LtM5izCc=",
    "login_url":"/",
}

application = tornado.web.Application([
    #(r"/test", testHandler),
    (r'/',LoginHandler),
    (r'/logout',LogoutHandler),
    (r'/admin',AdminHandler),
    (r'/musers',UsersHandler),
    (r'/nopage',NopageHandler),
], **settings)

def initLog():
    try:
        logging.config.fileConfig(fname='conf/log.conf', defaults=None, disable_existing_loggers=True)
        return 0
    except Exception, e:
        eratellogger.error(e)
 
if __name__ == "__main__":
    if initLog():
        eratellogger.error('Log modul initialization failed!')
    else:
        ratellogger.info('Log modul initialization successful!')
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

