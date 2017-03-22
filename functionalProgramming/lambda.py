#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

#匿名函数
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。

g = lambda x : x + 1

'''
等价于
def g(x):
    return x + 1
'''

print(g(3))
