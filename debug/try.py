#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

try:
    10 /0
except ZeroDivisionError as e:
    print('erro: %s' % e)
finally:
    print('finally')
print('end')
