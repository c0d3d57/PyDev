# Name: Tetris.py
# Author: Super3.org(super3.org)
# Objective: Make a basic tetris game

# Imports
import pygame

# Start PyGame
pygame.init()

# Define Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]
yellow = [255, 255, 0]
lightblue = [102, 204, 255]
orange = [255, 102, 0]
purple = [204, 0, 255]

# Define Block Constants
LPIECE = 1 
LINEPIECE = 2
BLOCKPIECE = 3
ZPIECE = 4
TPIECE = 5

class Piece(pygame.sprite.Sprite):
	def __init__(self, locX, locY, type):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		# Create an image
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(white)
		# Set bounds
		self.rect = self.image.get_rect()
		# Set draw location
		self.rect.x = locX
		self.rect.y = locY

# Set and Display Grid/Screen
width = 35 # X size of grid location
height  = 35 # Y size of grid location
sizeX = 10
sizeY = 18
size = [sizeX*width, sizeY*height]
screen = pygame.display.set_mode(size)

# Set Screen's Title
pygame.display.set_caption("Tetris")

# Make Grid Array
grid = []
for row in range(width):
	grid.append([])
	for column in range(height):
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
	clock.tick(1)
	
	# Check for Events
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True
	
	# Clear the Screen
	screen.fill(black)
	
	# Update Grid
	for column in range(height, 0, -1):
		for row in range(width, 0, -1):
			if grid[row][column] == 1 and row < sizeX:
				grid[row][column] = 0
				grid[row+1][column] = 1
	
	# Draw Grid
	for column in range(height):
		for row in range(width):
			if grid[row][column] == 1:
				color = green
			else:
				 color = white
			pygame.draw.rect( screen, color, [column*width,row*height, width, height])
	
	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()