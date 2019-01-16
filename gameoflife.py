#!/usr/bin/python3
# -*- Coding: utf-8 -*-
# Author - Heera Hemanth Bylla < heerahemanth1@icloud.com >

# Program for playing the Game of Life
from life import LifeGrid

# Define the initial configuration of live cells.
INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]

# Set the size of the grid.
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations.
NUM_GENS = 8

# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells
    liveCells = list()

    # Iterate over the elements of the grid
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            neighbors = grid.numLiveNeighbors(i, j)
            if (neighbors==2 and grid.isLiveCell(i, j)) or neighbors==3:
                liveCells.append((i, j))
    grid.configure(liveCells)

# Prints the text-based representation of the game grid.
def draw(grid):
    symbols = {0:'-', 1:'@'}
    print()
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            print(symbols.get(grid._grid.__getitem__((i, j))), end=' ')
        print()
    return

def main():
    # Construct the game grid and configure it.
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # Play the game.
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)
    return

main()