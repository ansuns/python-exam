#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

class Student(object):
    @property
    def score(self):
        return self._score

    #这里不定义则score限制无效
    #@score.setter
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score between 0 - 100')
        self._score = value

st = Student()
st.score = 333
print(st.score)