#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'
import logging
import pdb
#断言，相当于PHP的die() eixt()
'''
def foo(s):
    n = int(s)
    assert n != 0 , 'n is zero'
    return 10 / n
foo(0)
'''
#logging
'''
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
'''
#pdb
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
