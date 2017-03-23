#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

class Student(object):
    #读取
    @property
    def score(self):
        return self._score
#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
    #设置、修改
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('必须是一个数字')
        if value < 0 or value > 100:
            raise ValueError('值介于0！100')
        self._score = value



s = Student()
s.score = 90 #值介于0！100
print(s)

