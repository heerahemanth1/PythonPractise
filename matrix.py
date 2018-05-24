# Implementing the Matrix ADT using a 2D Array
from array import Array2D

class Matrix:
    '''
        Matric of numRows x numCols using 2D Array
    '''
    def __init__(self):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    # Returns the number of rows
    def numRows(self):
        return self._theGrid.numRows()

    # Returns the number of columns
    def numCols(self):
        return self._theGrid.numCols()

    # Returns the element at (i, j)
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    # Sets the value of element at (i, j) to scalar
    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    # Scales the matrix by the given scalar
    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self._theGrid[r, c] += scalar

    # Creates and returns a new matrix that is the transpose of this
    def transpose(self):
        transpose_matrix = Matrix(self.numCols(), self.numRows())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                transpose_matrix[c, r] = self._theGrid[r, c]
        return transpose_matrix

    # Creates and returns a new matrix that results from matrix addition
    def __add__(self, rhsMatrix):
        assert self.numRows() == rhsMatrix.numRows() and \
                self.numCols() == rhsMatrix.numCols(), \
                "Matrix sizes are not compatible for the add operation."
        # Create the new matrix
        new_matrix = Matrix(self.numRows(), self.numCols())
        # Add the matrices
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                new_matrix[r, c] = self._theGrid[r, c] + rhsMatrix._theGrid[r, c]
        return new_matrix

    # Matrix Subtraction
    def __sub__(self, rhsMatrix):
        assert self.numRows() == rhsMatrix.numRows() and \
                self.numCols() == rhsMatrix.numCols(), \
                "Matrix sizes are not compatible for the add operation."
        # Create the new matrix
        new_matrix = Matrix(self.numRows(), self.numCols())
        # Add the matrices
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                new_matrix[r, c] = self._theGrid[r, c] - rhsMatrix._theGrid[r, c]
        return new_matrix

    # Matrix Multiplication
    def __mul__(self, rhsMatrix):
        assert self.numCols() == rhsMatrix.numRows(), \
            "Matrix sizes are not compatible for the add operation."
        new_matrix = Matrix(self.numRows(), rhsMatrix.numCols())
        for r in range(self.numRows()):
            for c in range(rhsMatrix.numCols()):
                sum = 0
                for rr in range(rhsMatrix.numRows()):
                    sum += self._theGrid[r, rr] * rhsMatrix._theGrid[rr, r]
                new_matrix[r, c] = sum
        return new_matrix