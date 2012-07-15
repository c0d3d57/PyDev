# Imports 
import pygame
import time
import random

# Start PyGame
pygame.init()

# Define Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Set and Display Screen
sizeX = 255
sizeY = 255
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set Screen's Title
pygame.display.set_caption("My Test Window")

# Grid Settings
width = 20 # X size of grid location
height  = 20 # Y size of grid location
margin = 5 # Margin between each grid location

# Make Grid Array
grid = []
for row in range(10):
	grid.append([])
	for column in range(10):
		grid[row].append(0)
	
# Test Grid Value	
grid[1][5] = 1

# Sentinel for Game Loop
done = False

# Game Timer
clock = pygame.time.Clock()

# Main Game Loop
while done == False:
	# Limit FPS of Game Loop
	clock.tick(25)
	
	# Check for Events
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			gridLocX = int(pos[0] / (width+margin))
			gridLocY = int(pos[1] / (height+margin))
			grid[gridLocY][gridLocX] = 1
	
	# Clear the Screen
	screen.fill(black)
	
	# Draw Grid
	for column in range(10):
		for row in range(10):
			if grid[row][column] == 1:
				color = green
			else:
				 color = white
			pygame.draw.rect( screen, color, [column*width+margin*column+margin,row*height+margin*row+margin, width, height])
	
	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()