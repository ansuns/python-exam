#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'
#Python内建的filter()函数用于过滤序列

def is_odd(n):
    if n % 2 == 1:
        return n

#例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
res = list(filter(is_odd, [234, 3, 31, 31234, 8, 1230 ,12, 41, 11114126]))
print(res)