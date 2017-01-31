#!/usr/bin/env python2.6
#! -*- coding: utf-8 -*-

import ps_crypt
import tornado.web
from navbar import navb
from db import db_operation
from login import BaseHandler

def usermes(data,sucess,error):
    '''return value which is from msyql'''
    if not  data:
        suce =  '<script>\nalert ("%s")\nwindow.location.href="/manager_user"\n</script>'% sucess 
        return suce
    err =  '<script>\nalert ("%s") \nwindow.location.href="/manager_user"\n</script>'% error
    return err

class UsersHandler(BaseHandler):
    def get(self):
        name = self.get_secure_cookie("username") 
        navb_data = navb(host='active')
        user_data = db_operation('select * from r_user').select()
        self.render('users.html', username=name)
