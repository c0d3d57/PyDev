# Imports
import pygame, sys
from pygame.locals import *

# Start PyGame
pygame.init()

# Settings and Clock
FPS = 30 # frames per second
fpsClock = pygame.time.Clock()

# Set Up the Window
screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Animation")

# Set Default Color
WHITE = (255, 255, 255)

# Load Image and Set Vars
catImg = pygame.image.load("source/cat.png")
catx = 10
caty = 10
direction = 'right'

# Main Game Loop
while True:
	# Clear Screen
	screen.fill(WHITE)
	
	# Direction Statements
	if direction == 'right':
		catx += 5
		if catx == 280:
			direction = 'down'
	elif direction == 'down':
		caty += 5
		if caty == 220:
			direction = 'left'
	elif direction == 'left':
		catx -= 5
		if catx == 10:
			direction = 'up'
	elif direction == 'up':
		caty -= 5
		if caty == 10:
			direction == 'right'
	
	# Draw It
	screen.blit(catImg, (catx, caty))
	
	# Event Loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	# Update Display
	pygame.display.update()	
	
	# Limit to FPS
	fpsClock.tick(FPS)