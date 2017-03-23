#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        if w < 0 :
            raise ValueError('非法的宽度')
        self._width = w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        if h < 0 :
            raise ValueError('非法的高度')
        self._height = h

    #像素
    @property
    def resolution(self):
        return self._height * self._width

s = Screen()
s.height = 1024
s.width = 800

print(s.resolution)
