#!/usr/bin/python3
# -*- Coding: utf-8 -*-
# Author - Heera Hemanth Bylla < heerahemanth1.gmail.com >

from marray import Array


class Vector:
    def __init__(self):
        self._elements = Array(2)
        self._size = 2
        self._length = 0
        