# Imports 
import pygame, sys
from pygame.locals import *

# Start PyGame
pygame.init()

# Set Up the Window
screen = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")

# Default Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clear the Screen
screen.fill(WHITE)

# Draw on the Surface Object
pygame.draw.polygon(screen, GREEN, ((146,0), (291,106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(screen, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(screen, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(screen, RED, (200, 150, 100, 50))

# Some Sort of Pixel Object
pixObj = pygame.PixelArray(screen)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# Main Game Loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()