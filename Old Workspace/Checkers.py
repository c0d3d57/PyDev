# Import a library of functions called 'pygame' and time
import pygame
import time
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
pygame.display.set_caption("Checkers Game")

# Loop until the users clicks the close button
done = False 

# Create a timer used to control how often the screen updates
clock = pygame.time.Clock()

#Simple Function
def addPeice(x, y, aColor):
	pygame.draw.circle( screen, aColor, [(50*x)+25, (50*y)+25], 25)	

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
		
	#Print Game Board
	for x1 in range(8):	
		for y1 in range(8):
			if x1%2 == 1 and y1%2==0:
				pygame.draw.rect( screen , black ,[x1*50 , y1*50 ,50 ,50])
			if x1%2 == 0 and y1%2==1:
				pygame.draw.rect( screen , black ,[x1*50 , y1*50 ,50 ,50])
			
	#Start Peices
	for y2 in range(3):
		start = (y2+1)%2
		for x2 in range(start, 9 ,2):
			addPeice(x2, y2, red)
	
	for y3 in range(5,8):
		start2 = (y3+1)%2
		for x3 in range(start2, 9 ,2):
			addPeice(x3, y3, blue)
	
	#Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()