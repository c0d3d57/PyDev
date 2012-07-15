# Imports
import pygame, time, sys
from pygame.locals import *

# Start PyGame
pygame.init()
screen = pygame.display.set_mode((400,300))

# Main Game Loop
while True:
	soundObj = pygame.mixer.Sound('source/beep1.ogg')
	soundObj.play()
	time.sleep(1)
	soundObj.stop()
	