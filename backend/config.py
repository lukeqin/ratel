#!/usr/bin/env python2.6
#! -*- coding: utf-8 -*-

import ConfigParser
config = ConfigParser.ConfigParser()

class Get_data:
    def __init__(self,conf_file):
        self.conf_file = conf_file
        config.read(conf_file)

    def Show_section(self):
        self.section = config.sections()
        return self.section

    def Show_option(self,section):
        self.option = config.options(section)
        return self.option

    def Show_option_data(self,section,option):
        self.option_data = config.get(section,option)
        return self.option_data

'''
if __name__ == "__main__":
    getdata = Get_data('../conf/db.conf')
    print getdata.Show_option_data('db','db_host')
    print getdata.Show_option_data('db','db_name')
    print getdata.Show_option_data('db','db_user')
    print getdata.Show_option_data('db','db_pass')
'''