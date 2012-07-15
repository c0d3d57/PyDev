# Imports
import pygame
import time

# Start Game Engine
pygame.init()

# Set Window
size = [400,400]
screen = pygame.display.set_mode(size)

# Set Colors
black = [0, 0, 0]
white = [ 255, 255, 255]

# Set Window Title
pygame.display.set_caption("My Test Window")

# Sentinel for Loop
done = False

# Create a clock to limit loop
clock = pygame.time.Clock()

while done == False:
	# Limit Loop to 25 cycles per second
	clock.tick(25)
	# See if the user is try to quit
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
	# Clear the screen
	screen.fill(white)

	#All drawing code goes here
	pygame.draw.circle(screen, black, [25,25], 10)
	pygame.display.flip()

#Exit Program 
pygame.quit()