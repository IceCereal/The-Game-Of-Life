"""
	Conway's game of life
	Author: IceCereal
"""

# IMPORTS
import random
import pygame

# HEIGHT & WIDTH OF THE GRID
HEIGHT = 200
WIDTH = 200

# GRID AND IT'S CORRESPONDING EQUIVALENCY VALUES
grid = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
netVals = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

# RANGE FOR EACH CELL
lowerBound = 2
upperBound = 3
