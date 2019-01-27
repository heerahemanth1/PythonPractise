#!/usr/bin/python3
# -*- Coding: utf-8 -*-
# Author - Heera Hemanth Bylla < heerahemanth1@icloud.com >

from marray import Array2D


# An ADT to represent GrayScaleImage
class GrayScaleImage(Array2D):
    """ GrayScaleImage is a representation of a Z x Z matrix containing
        pixel density values(0-255) of a gray scale image.
    """

    def width(self):
        ''' Returns the width of the image.
        '''
        return self.numCols()
    
    def height(self):
        ''' Returns the height of the image.
        '''
        return self.numRows()

    def getitem(self, row, col):
        ''' Returns the density at a particular pixel represented by
            (row, col) tuple indicating the position of the pixel.
        '''
        return self.__getitem__((row, col))

    def setitem(self, row, col, value):
        ''' Sets the density value of a pixel at given position.
        '''
        self.__setitem__((row, col), value)
        return
 

if __name__ == '__main__':

    image = GrayScaleImage(5, 4)
    image.clear(1)
    print(image)
