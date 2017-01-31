#!/usr/bin/env python2.6
#! -*- coding: utf-8 -*-

import logging
import torndb
from backend.config import Get_data

ratellogger = logging.getLogger()
eratellogger = logging.getLogger('log03')

getdata = Get_data('conf/db.conf')

dbhost = getdata.Show_option_data('db','db_host')
dbname = getdata.Show_option_data('db','db_name')
dbuser = getdata.Show_option_data('db','db_user')
dbpass = getdata.Show_option_data('db','db_pass')
#print dbhost,dbname,dbuser,dbpass

class db_operation(object):
    '''MySQL add del edit select'''
    def __init__(self,sql):
        try:
            db = torndb.Connection(dbhost,dbname,user=dbuser,password=dbpass)
            self.sql = sql
            self.db = db
        except Exception,e:
            eratellogger.error(e)
    
    def select(self):
        try:
            select_data = self.db.query(self.sql)
            return select_data
        except Exception,e:
            eratellogger.error(e)
        finally:
            self.db.close()

    def update(self):
        try:
            update_data = self.db.execute(self.sql)
            return update_data
        except Exception,e:
            eratellogger.error(e)
        finally:
            self.db.close()

    def delete(self):
        try:
            delete_data = self.db.execute(self.sql)
            return delete_data
        except Exception,e:
            eratellogger.error(e)
        finally:
            self.db.close()

