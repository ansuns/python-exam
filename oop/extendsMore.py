#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'


class A(object):
    def run(self):
        print('A is running!')

class B(object):
    def run(self):
        print('B is running!')

#多重继承：

class C(A, B):
    pass

c =  C()
c.run() # A is runnig!
#多重继承遵循广度优先的原则
