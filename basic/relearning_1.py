#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'
#数据类型和变量

#转义符\
print('I\'m o\'k')

print('''
   ...line1
   ...line2
   ...line3
''')

#两位小数
print('账户余额：%.2f' % 88.666) #88.67
print('百分比: %d%%' % 8)

#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85

r = (85 - 72) / 85

print('提高了 %.2f' % r)
