# Imports
import pygame, sys
from pygame.locals import *

# Start Up PyGame
pygame.init()
# Set Display Screen
screen = pygame.display.set_mode((400, 300))
# Set Window Caption
pygame.display.set_caption("Hello World!")
# Main Game Loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			# Isn't this someone redundant?
			pygame.quit()
			sys.exit()
	pygame.display.update()