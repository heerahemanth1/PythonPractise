#!/usr/bin/env python
# -*- Coding: utf-8 -*-

import random
from sys import argv

def partition(array, p, r):
    x = array[r]
    i = p-1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i+1]
    array[i+1] = array[r]
    array[r] = temp
    return i+1

def quick_sort(array, p, r):
    if p<r:
        piv = partition(array, p, r)
        quick_sort(array, p, piv-1)
        quick_sort(array, piv+1, r)

if __name__ == '__main__':
    if len(argv) > 1:
        array = list(map(int, argv[1:]))
        quick_sort(array, 0, len(array)-1)
    else:
        array = [random.randint(1, 1000) for x in range(1, 11)]
        quick_sort(array, 0, 9)
    
    print(array)