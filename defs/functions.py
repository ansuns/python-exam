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
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * n
    return s

#给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
###可变参数
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的
#是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum = 0
    for item in numbers:
        sum = sum + item * item
        return sum

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age , **kw):
    print('name:' ,name, 'age:' , age, 'other:', kw)

#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
#>>> person('Michael', 30)
#name: Michael age: 30 other: {}

#也可以传入任意个数的关键字参数：

#>>> person('Bob', 35, city='Beijing')
#name: Bob age: 35 other: {'city': 'Beijing'}
#>>> person('Adam', 45, gender='M', job='Engineer')
#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

'''
关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收
到name和age这两个参数，但是，如果调用者愿意提供更多的参
数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其
他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

命名关键字参数

对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

仍以person()函数为例，我们希望检查是否有city和job参数：

defs person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
但是调用者仍可以传入不受限制的关键字参数：

>>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可
以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

'''
##########################################################################
'''

#汉诺塔
def hnt(n, a, b, c):
    if n == 1 :
        print('%c-->%c' %(a ,c))
    else:
        hnt(n - 1, a, c, b)
        print('%c-->%c' %(a ,c))
        hnt(n - 1, b, a, c)


hnt(3, 'A', 'B', 'C')






