#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s :' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('abc')
def now():
    print('2017-08-01')

f = now
f()

