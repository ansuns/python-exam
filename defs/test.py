#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'YANGS'

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >=0 :
        return x
    else:
        return -x

print(my_abs(-8))

def test(x , y):
    return y, x
res1, res2 = test('A', 'B') #tulp
print(res2)

def powers(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x

    return s
print(powers(51, 4))


def appd(L = None):
    if L is None:
        L = []
    L.append('End')
    return L
print(appd())


#可变参数：
def nop(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：
print(nop(7))
print(nop(7,8,9,11))



#关键字参数

def person(name, age, **kw):
    print('name: %s' % name)
    print('age: %d' % age)
    print('other: %s' % kw)
    if 'jb' in kw:
        print('wow, you has a jb!')

#other: {'address': 'Beijing', 'phone': '13112341234', 'email': 'anj_l@qq.com'}

person('ansuns', 21, address='Beijing', phone='13112341234', email='anj_l@qq.com')

extra = {'address' : 'Beijing', 'phone' : '13112341234', 'email' : 'anj_88@qq.com', 'jb' : 'oo'}
person('miacl', 28, **extra)
#other: {'address': 'Beijing', 'phone': '13112341234', 'email': 'anj_88@qq.com'}
