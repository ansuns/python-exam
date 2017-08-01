#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'
a_string = 'a123'
def foo():
    a_string = '1111111111111111111'
    print (locals())
print (globals())
foo()
print(a_string)