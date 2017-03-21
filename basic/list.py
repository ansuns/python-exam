#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
__author__ = 'RoLiHop'
list = [77,88,99,44]
print(len(list))
print(list[0])
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
list.append(10000)
print(list[-1]) #10000
#也可以把元素插入到指定的位置，比如索引号为1的位置：
list.insert(0,888)
print(list)
#要删除list末尾的元素，用pop()方法：,要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
list.pop()
print(list)
