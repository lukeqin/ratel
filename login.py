#!/usr/bin/env python2.6
#! -*- coding: utf-8 -*-

import ps_crypt
import tornado.web
from datetime import datetime
from db import db_operation
from backend.navbar import navb

def login_time():
    '''user login time'''
    now_time = datetime.now()
    date = now_time.strftime('%Y-%m-%d %I:%M:%S %p')
    return date

def pscheck(name,passwd):
    data = db_operation('select name,password from r_user where name="%s"' % name).select()
    if data:
        db_pass = data[0]['password']
        if ps_crypt.pass_verify(passwd,db_pass):
            return True
        else:
            return False
    else:
        return False

class BaseHandler(tornado.web.RequestHandler):
    '''set COOKIE'''
    def get_current_user(self):
        return self.get_secure_cookie("username")

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        name = self.get_argument('username')
        passwd = self.get_argument('password')
        if not pscheck(name,passwd):
            return self.write('''<script>
                alert ("用户名或密码错误!")
                window.location.href="/"
                </script>
            ''')
        else:
            db_operation('UPDATE r_user set LOGINT="%s" where NAME="%s"' % (login_time(),name)).update()
            self.set_secure_cookie("username",name)
            self.redirect('/admin')

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("username")
        self.redirect("/")

class AdminHandler(BaseHandler):
     @tornado.web.authenticated
     def get(self):      
        name = self.get_secure_cookie("username") 
        navb_data = navb(host='active') 
        self.render('admin.html',navb=navb_data, username=name)

class NopageHandler(BaseHandler):
    def get(self):
        name = self.get_secure_cookie("username") 
        navb_data = navb(host='active')
        self.render('nopage.html', username=name)

'''
dbt = db_operation('show databases').select()
print dbt
'''
