#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

import os
import os.path
print(os.name)
#print(os.uname())#uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
#print(os.environ)

print(os.path.abspath('.'))#一部分放在os.path模块中，这一点要注意一下。

os.path.join(os.path.abspath('.'), 'testdir')
os.mkdir(os.path.abspath('.')+'/testdir')

#删除一个目录
#os.rmdir(os.path.abspath('.')+'/testdir')