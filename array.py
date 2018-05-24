#!/usr/bin/python3
# -*- Coding: utf-8 -*-
# Author - Heera Hemanth Bylla < heerahemanth1@icloud.com >
import ctypes

class Array:
    '''
        Creates an array ADT with size elements
        Array size is to be passed
    '''
    def __init__(self, size):
        assert size>0, "Array size must be greater than 0."
        self._size = size
        # Creating the array in memory
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element
        self.clear(None)

    # Returns the size of the array
    def __len__(self):
        return self._size

    # Gets the contents of the index element
    def __getitem__(self, index):
        assert index>=0 and index<=self._size, "Array subscript out of range"
        return self._elements[index]

    # Puts the value in array at index position
    def __setitem__(self, index, value):
        assert index>=0 and index<=self._size, "Array subscript out of range"
        self._elements[index] = value

    # Clears the array by setting all elements to a given value
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements
    def __iter__(self):
        return _ArrayIterator(self._elements)

# Iterator for the Array ADT
class _ArrayIterator:
    '''
        Iterator for the Array ADT
        Array of elements passed as theArray
    '''
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


# Implementation of Array2D ADT using an array of arrays
class Array2D:
    '''
        2D Array implemented using Array of Arrays
    '''

    # Creates a 2D Array of size numRows x numCols
    def __init__(self, numRows, numCols):
        # Creates a 1D Array of length numRows
        self._theRows = Array(numRows)

        # Creates a 1D Array for each row of the 2D Array
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    # Returns the number of rows
    def numRows(self):
        return len(self._theRows)

    # Returns the number of columns
    def numCols(self):
        return len(self._theRows[0])

    # Clears the Array by setting every element to a given value
    def clear(self, value):
        for i in range(self.numRows()):
            row.clear(value)

    # Gets the contents of the element at position [i, j]
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of Array subscripts"
        row, col = ndxTuple
        return self._theRows[row][col]

    # Sets the contents of the element at position [i, j] to value
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of Array subscripts"
        row, col = ndxTuple
        assert row >= 0 and row <= self.numRows() and col >= 0 and col <= self.numCols(), \
        "Array subscripts out of range"
        self._theRows[row][col] = value
        return

if __name__ == '__main__':
    Array(3)
