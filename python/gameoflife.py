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

# MAIN LOOP
def updateGrid():
	# VERSION = 2.5

	# EASY VALS:
	maxColumn = WIDTH - 1
	maxRow = HEIGHT - 1

	# 4 Corners
	netVals[0][0] = grid[0][1] + grid[1][1] + grid[1][0]
	netVals[0][maxColumn] = grid[0][maxColumn-1] + grid[1][maxColumn-1] + grid[1][maxColumn]
	netVals[maxRow][maxColumn] = grid[maxRow][maxColumn-1] + grid[maxRow-1][maxColumn-1] + grid[maxRow-1][maxColumn]
	netVals[maxRow][0] = grid[maxRow][1] + grid[maxRow-1][1] + grid[maxRow-1][0]