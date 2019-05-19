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

	# Edges
	for column in range(1, maxColumn):
		netVals[0][column] = grid[0][column-1] + grid[1][column-1] + grid[1][column] + grid[1][column+1] + grid[0][column+1]
		netVals[maxRow][column] = grid[maxRow][column-1] + grid[maxRow-1][column-1] + grid[maxRow-1][column] + grid[maxRow-1][column+1] + grid[maxRow][column+1]

	for row in range(1, maxRow):
		netVals[row][0] = grid[row-1][0] + grid[row-1][1] + grid[row][1] + grid[row+1][1] + grid[row+1][0]
		netVals[row][maxColumn] = grid[row-1][maxColumn] + grid[row-1][maxColumn-1] + grid[row][maxColumn-1] + grid[row+1][maxColumn-1] + grid[row+1][maxColumn]

	# Everything in the middle
	for row in range(1, maxRow):
		for column in range(1, maxColumn):
			netVals[row][column] = grid[row-1][column-1] + grid[row-1][column] + grid[row-1][column+1] + grid[row][column+1] + grid[row+1][column+1] + grid[row+1][column] + grid[row+1][column-1] + grid[row][column-1]

	# EVALUATION METRIC
	for row in range(0, maxRow+1):
		for column in range(0, maxColumn+1):
			state = grid[row][column]

			if (state):
				if netVals[row][column] < lowerBound:
					grid[row][column] = 0

				if netVals[row][column] > upperBound:
					grid[row][column] = 0

			else:
				if (netVals[row][column] == upperBound):
					grid[row][column] = 1

# SELECT START CONFIG
ssc = 1

### R-pentomino
# It is by far the most active polyomino with fewer than six cells
if ssc == 1:
	x = int(HEIGHT/2)
	y = int (WIDTH/2)
	grid[x][y] = 0
	grid[x][y+1] = 1
	grid[x][y+2] = 1
	grid[x+1][y] = 1
	grid[x+1][y+1] = 1
	grid[x+1][y+2] = 0
	grid[x+2][y] = 0
	grid[x+2][y+1] = 1
	grid[x+2][y+2] = 0

### Random
# Randomized start locations
if ssc == 2:
	# CHANGE THIS FOR NUMBER OF STARTING POINTS
	startLocations = 4000

	for i in range(startLocations):
		random.seed()
		valueWidth = random.randint(0, WIDTH-1)
		random.seed()
		valueHeight = random.randint(0, HEIGHT-1)
		grid[valueHeight][valueWidth] = 1


# PYGAME DISPLAY STARTS HERE:
pygame.init()

# CHANGE WINDOW SIZE ACCORDING TO MONITOR SIZE
Window_Size = [1000, 1000]

widthBox = Window_Size[0] / WIDTH
heightBox = Window_Size[1] / HEIGHT

screen = pygame.display.set_mode(Window_Size)
pygame.display.set_caption("Game of Ice")

clock = pygame.time.Clock()

# CHANGE THIS FOR SPEED OF THE UPDATION (This is basically fps limit)
# HIGH NUMBER = FASTER UPDATE
speed_update = 10

done = False

while not done:
	for event in pygame.event.get():
		# MOUSE CLICK - EXIT SCREEN
		if event.type == pygame.QUIT:
			done = True

	# DRAW GRID
	for row in range(WIDTH):
		for column in range(HEIGHT):
			# DEFAULT COLOR: BLACK
			color = pygame.color.THECOLORS['black']

			# IF CELL == ON, CHANGE COLOR TO RED
			if grid[row][column] == 1:
				color = pygame.color.THECOLORS['red']
			
			# DRAW RECTANGLE
			pygame.draw.rect(screen, color, [column*widthBox, row*heightBox, widthBox, heightBox])

	# UPDATE GRID
	updateGrid()

	clock.tick(speed_update)

	# UPDATE THE SCREEN
	pygame.display.flip()

# EXIT PYGAME
pygame.quit()