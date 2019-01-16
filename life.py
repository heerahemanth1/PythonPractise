#!/usr/bin/python3
# -*- Coding: utf-8 -*-
# Author - Heera Hemanth Bylla < heerahemanth1@icloud.com >

# Implements the LifeGrid ADT for use with the Game of Life
from marray import Array2D


class LifeGrid:
    """ The LifeGrid is an Abstract Data Type(ADT) for the implementation
        of the GameOfLife. It handles the game grid and it's functions.
        This class is imported into the GameOfLife and used directly.
    """
    # Defines constants to represents the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to dead.
    def __init__(self, numRows, numCols):
        # Allcoate the 2D Array for the grid.
        self._grid = Array2D(numRows, numCols)
        # Clear the grid and set all values to dead.
        self.configure(list())
    
    # Returns the number of rows in the grid.
    def numRows(self):
        return self._grid.numRows()
    
    # Returns the number of columns in the grid.
    def numCols(self):
        return self._grid.numCols()
    
    # Configures the grid to contain the given live cells.
    def configure(self, coordList):
        # Clear the game grid.
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)
        
        # Set the indicated cells to be live.
        for coord in coordList:
            self.setCell(coord[0], coord[1])
    
    # Does the indicated cell contain a live organism?
    def isLiveCell(self, row, col):
        return self._grid[row, col] == LifeGrid.LIVE_CELL
    
    # Clears the indicated cell by setting it to dead.
    def clearCell(self, row, col):
        self._grid[row, col] = LifeGrid.DEAD_CELL
    
    # Sets the indicated cell to be alive.
    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL
    
    # Returns the number of live neighbors for a given cell.
    def numLiveNeighbors(self, row, col):
        if row==0 and col==0:
            live_neighbors_sum = self._grid[row, col+1]\
                                + self._grid[row+1, col]\
                                + self._grid[row+1, col+1]
        elif row==self.numRows()-1 and col==0:
            live_neighbors_sum = self._grid[row-1, col]\
                                + self._grid[row-1, col+1]\
                                + self._grid[row, col+1]
        elif col == 0:
            live_neighbors_sum = self._grid[row-1, col]\
                                + self._grid[row-1, col+1]\
                                + self._grid[row, col+1]\
                                + self._grid[row+1, col]\
                                + self._grid[row+1, col+1]
        elif row==0 and col==self.numCols()-1:
            live_neighbors_sum = self._grid[row, col-1]\
                                + self._grid[row+1, col-1]\
                                + self._grid[row+1, col]
        elif row==self.numRows()-1 and col==self.numCols()-1:
            live_neighbors_sum = self._grid[row-1, col-1]\
                                + self._grid[row-1, col]\
                                + self._grid[row, col-1]
        elif col == self.numCols()-1:
            live_neighbors_sum = self._grid[row-1, col-1]\
                                + self._grid[row-1, col]\
                                + self._grid[row, col-1]\
                                + self._grid[row+1, col-1]\
                                + self._grid[row+1, col]
        elif row == 0:
            live_neighbors_sum = self._grid[row, col-1]\
                                + self._grid[row, col+1]\
                                + self._grid[row+1, col-1]\
                                + self._grid[row+1, col]\
                                + self._grid[row+1, col+1]
        elif row == self.numRows()-1:
            live_neighbors_sum = self._grid[row-1, col-1]\
                                + self._grid[row, col+1]\
                                + self._grid[row, col-1]\
                                + self._grid[row-1, col]\
                                + self._grid[row-1, col+1]
        else:
            live_neighbors_sum = self._grid[row-1, col-1]\
                                + self._grid[row-1, col]\
                                + self._grid[row-1, col+1]\
                                + self._grid[row, col-1]\
                                + self._grid[row, col+1]\
                                + self._grid[row+1, col-1]\
                                + self._grid[row+1, col]\
                                + self._grid[row+1, col+1]
        
        return live_neighbors_sum
