#!/usr/bin/python3
# -*- Coding: utf-8 -*-
# Author - Heera Hemanth Bylla < heerahemanth1@icloud.com >

# Program for playing the Game of Life
from life import LifeGrid

# Define the initial configuration of live cells.
INIT_CONFIG = [ (1, 1), (1, 2), (2, 2), (3, 2) ]

# Set the size of the grid.
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations.
NUM_GENS = 8

# Generates the next generation of organisms.
def evolve( grid ):
    pass

# Prints the text-based representation of the game grid.
def draw( grid ):
    pass

def main():
    # Construct the game grid and configure it.
    grid = LifeGrid( GRID_WIDTH, GRID_HEIGHT )
    grid.configure( INIT_CONFIG )

    # Play the game.
    draw( grid )
    for i in range( NUM_GENS ):
        evolve( grid )
        draw( grid )