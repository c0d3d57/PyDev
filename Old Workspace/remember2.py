# Import
import pygame
import time

# Start Game Engine
pygame.init()

# Set Window
size = [400, 400]
screen  = pygame.display.set_mode(size)

# Set Window Caption
pygame.display.set_caption("My Test Window")

# Set Colors
white = [ 255, 255, 255]
black = [0,0,0]

# Sentinel for While Loop
done = False

# Clock to Limit CPU Usage
clock = pygame.time.Clock()

while done == False:
	#Limit Loop
	clock.tick(25)
	# Check for exit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
	# Draw here
	screen.fill(white)
	pygame.draw.circle( screen, black, [25, 25], 50)
	pygame.display.flip()
	
# Exit Program	
pygame.quit()		
	