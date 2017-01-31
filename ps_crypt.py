#!/usr/bin/env python2.6
#! -*- coding: utf-8 -*-

from passlib.hash import sha256_crypt

def pass_crypt(psstr):
    '''use sha256 encrypt psstr'''
    hash_pass = sha256_crypt.encrypt(psstr)
    return hash_pass

def pass_verify(psstr,db_pass):
    '''use sha256 decode psstr'''
    verify_pass = sha256_crypt.verify(psstr,db_pass)
    return verify_pass

'''
enc = pass_crypt('admin')
print enc
dec = pass_verify('admin', enc)
print dec
'''