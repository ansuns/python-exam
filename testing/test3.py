#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call: %s' % func.__name__)
            print('%s %s :' % (text, func.__name__))
            func(*args, **kw)
            print('end call: %s' % func.__name__)
            return func
        return wrapper
    return decorator

@log('abc')
def now():
    print('2017-08-01')

f = now
f()

