#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'
print('Hello World!')
#函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
print('a', 'b', 'c', 'd') # a b c d

name = input('please input your name: \n')

print('Hello %s' % name)

a = int(input('input a number:\n'))
if a > 0:
    a = a
else:
    a = -a
print(a)



