# Name: Main.py
# Author: Super3 (super3.org)

# Imports
import pygame
import pygame.locals

# My Imports
import level

# Define Basic Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Sentinel for Game Loop
done = False
# Game Timer
clock = pygame.time.Clock()

# Main 
if __name__ == '__main__':	
	# Start Pygame
	pygame.init()
	# Set Screen
	screenX, screenY = [240, 240]
	screen = pygame.display.set_mode((screenX,screenY))
	pygame.display.set_caption("AWG Tiletest")
	
	# Load Level
	myLevel = level.Level()

	# Main Game Loop
	while done == False:
		# Limit FPS of Game Loop
		clock.tick(30)
		
		# Check for Events
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				done = True
		
		# Clear Screen
		screen.fill(white)
		# Display Level
		myLevel.render(screen)
		# Update Screen
		pygame.display.flip()
		
# Exit Program
pygame.quit()