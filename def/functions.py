#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'
import math

#定义一个自己的求绝对值函数
def abs(x):
    if not isinstance(x,(int, float)):
        raise  TypeError('非法数据，只允许输入整数和浮点数')
    if x> 0:
        return x
    else:
        return -x

#空函数
def nop():
    pass

#返回多个值
#游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#print(move(1,4,100,0))

#计算平方
def power(x):
    return x * x







