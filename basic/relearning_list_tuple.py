#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

#list是一种有序的集合，可以随时添加和删除其中的元素。类似PHP数组
#常用操作：追加到list末尾：list.append(),添加到指定位置：list.insert(),删除末尾list.pop()

classmates = ['bob', 'joe', 'marr']
print(classmates)
#长度
print(len(classmates))
#ist是一个可变的有序表，所以，可以往list中追加元素到末尾,但是tuple是固定的不变的
classmates.append('ansuns')
classmates.append([7,8])
print(classmates)


#tuple 元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

lang = ('php' , 'asp', 'java', 'python')
print(lang)
print(len(lang))

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t1 = (1,)
print(t1)