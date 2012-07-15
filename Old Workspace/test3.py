# Import a library of functions called 'pygame' and time
import pygame
import time
import random
# Initialize the game engine
pygame.init()

# Define Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Define Pi
pi = 3.141592653

# Set the hight and width of the screen and
# then display the screen
sizeX = 400
sizeY = 400
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set the screen's title
pygame.display.set_caption("My Test Window")

# Loop until the users clicks the close button
done = False 

# Create a timer used to control how often the screen updates
clock = pygame.time.Clock()

while done == False:
	# This limits the whilte loop to a max of 10 times per second. 
	# Leave this out and we will use all the CPU we can
	clock.tick(10)
	
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked closed
			done=True #Flag that we are done so we exit this loop
	
	# All drawing code happens after the for loop but 
	# inside the main while done==False loop
	
	# Clear the screen and set the screen background
	screen.fill(white)
		
	#Print Grid
	for x in range(8):	
		for y in range(8):
			pygame.draw.rect( screen , black ,[x*50 , y*50 ,50 ,50])
			
	#Draw Cicle
	#pygame.draw.circle( screen, red, [50, 50], 5)
	
	#Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()