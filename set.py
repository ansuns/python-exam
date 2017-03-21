#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'
set1 = set([77,88,99])
set2 = set([45,82,22,'a',True,77])
#取交集
set = set1 & set2
print(set)
#取并集
set = set1 | set2
print(set)