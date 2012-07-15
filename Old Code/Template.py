# Name: Template.py
# Author: Super3boy (super3.org)

# Imports
import pygame

# Start PyGame
pygame.init()

# Define Basic Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Set and Display Screen
sizeX = 400
sizeY = 400
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set Screen's Title
pygame.display.set_caption("Template")

# Sentinel for Game Loop
done = False

# Game Timer
clock = pygame.time.Clock()

# Main Game Loop
while done == False:
	# Limit FPS of Game Loop
	clock.tick(30)
	
	# Check for Events
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True
			
	# Drawing Goes Here

	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()