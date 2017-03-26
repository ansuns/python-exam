#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

#装饰器

def now():
    print('2017-03-22')

f = now
#函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
print(f.__name__)

'''
现在，假设我们要增强now()函数的功能，比如，在函数调用
前后自动打印日志，但又不希望修改now()函数的定义，这种在代码
运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
'''