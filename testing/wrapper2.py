#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

def loger(func):
    def inner(*args, **kwargs):
        print('Agument is %s, %s' % (args, kwargs))
        return func(*args, **kwargs)
    return inner

@loger
def add(x, y):
    return x + y

print(add(9, 5))

@loger
def foo2():
    return 2
print(foo2())