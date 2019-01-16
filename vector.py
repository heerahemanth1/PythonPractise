#!/usr/bin/python3
# -*- Coding: utf-8 -*-
# Author - Heera Hemanth Bylla < heerahemanth1.gmail.com >

from marray import Array


class Vector:
    """ Implementation of a mutable sequential storage using the Array ADT.
        Vector utilizes the Array ADT to store elements in a sequence,
        that can be modified in such a way that new elements can inserted
        anywhere in the sequence and elements already in the sequence can
        be removed from any position.
    """

    def __init__(self):
        self._elements = Array(2)
        self._size = 2
        self._length = 0
    
    def length(self):
        return self._length
    
    def size(self):
        return self._size

    def contains(self, item):
        for i in range(self.length()):
            if self._elements[i] == item:
                return True
        return False
    
    def append(self, item):
        if self.length() < self.size():
            self._elements[self.length()] = item
            self._length += 1
        else:
            temp = Array(self.size()*2)
            for i in range(self.length()):
                temp[i] = self._elements[i]
            temp[self.length()] = item
            self._elements = temp
            self._length += 1
            self._size *= 2
        