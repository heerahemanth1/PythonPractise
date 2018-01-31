# Implementing the Matrix ADT using a 2D Array
from array import Array2D

class Matrix:
    '''
        Matric of numRows x numCols using 2D Array
    '''
    def __init__(self):
        self._theGrid = Array2D(numRows, numCols)
        