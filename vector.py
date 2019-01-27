#!/usr/bin/python3
# -*- Coding: utf-8 -*-
# Author - Heera Hemanth Bylla < heerahemanth1@icloud.com >

from marray import Array


class Vector:
    """ Implementation of a mutable sequential storage using the Array ADT.
        Vector utilizes the Array ADT to store elements in a sequence,
        that can be modified in such a way that new elements can inserted
        anywhere in the sequence and elements already in the sequence can
        be removed from any position.
    """

    def __init__(self, size=2):
        self._elements = Array(size)
        self._length = 0
    
    def __str__(self):
        string = 'Vector: ( '
        for i in range(self.length()-1):
            string += str(self._elements[i])+', '
        string += str(self._elements[self.length()-1])+' )'
        return string

    def length(self):
        return self._length
    
    def size(self):
        return len(self._elements)

    def contains(self, item):
        for i in range(self.length()):
            if self._elements[i] == item:
                return i
        return -1
    
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
        return
    
    def get_item(self, ndx):
        try:
            return self._elements[ndx]
        except IndexError as e:
            print('Index out of range.')
            raise e
        return
    
    def set_item(self, ndx, item):
        try:
            self._elements[ndx] = item
        except IndexError as e:
            print('Index out of range.')
            raise e
        return
    
    def insert(self, ndx, item):
        if ndx<0 or ndx>self.length()-1:
            print('Index out of range.')
        else:
            if self.size()>self.length():
                for i in range(self.length(), ndx, -1):
                    self._elements[i] = self._elements[i-1]
                self._elements[ndx] = item
            else:
                temp = Array(self.size()*2)
                for i in range(ndx):
                    temp[i] = self._elements[i]
                temp[ndx] = item
                for j in range(ndx, self.length()):
                    temp[j+1] = self._elements[j]
                self._elements = temp
            self._length += 1
        return

    def remove(self, ndx):
        item = None
        if ndx<0 or ndx>=self.length():
            print('Index out of range.')
        else:
            item = self._elements[ndx]
            if ndx == self.length()-1:
                self._elements[ndx] = None
            else:
                for i in range(ndx, self.length()-1):
                    self._elements[i] = self._elements[i+1]
            self._length -= 1
        return item
    
    def index_of(self, item):
        is_found = self.contains(item)
        if is_found == -1:
            print(item, 'not found.')
        return is_found

    def extend(self, other_vector):
        new_length = self.length()+other_vector.length()
        if new_length<=self.size():
            start_index = self.length()
            for i in range(other_vector.length()):
                self._elements[start_index+i] = other_vector._elements[i]
            self._length += other_vector.length()
        else:
            temp = Vector(new_length)
            temp.extend(self)
            temp.extend(other_vector)
            self._elements = temp._elements
            self._length = new_length
    
    def iterator(self):
        return self._elements.__iter__()


if __name__ == '__main__':
    one = Vector()
    two = Vector(3)
    one.append('heera')
    one.append('hemanth')
    two.append('bylla')
    one.extend(two)
    one.insert(2, 4)
    print(one)
