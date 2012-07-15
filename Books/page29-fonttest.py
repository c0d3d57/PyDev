# Imports
import pygame, sys
from pygame.locals import *

# Start PyGame and Show Window
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello World!")

# Set Default Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create a Font Object
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

# Main Loop
while True:
	# Clear Screen
	screen.fill(WHITE)
	
	# Draw Text
	screen.blit(textSurfaceObj, textRectObj)
	
	# Event Loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	# Refresh Screen
	pygame.display.update()