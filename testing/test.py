#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s:' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2017-08-01')

f = now
f()
#print(f.__name__)
#print(now.__name__)
