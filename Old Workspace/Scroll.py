# Scroll.py
# Objective: Create a moveable background
# Author: Super3boy (super3.org)

# Imports
import pygame

# Start PyGame
pygame.init()

# Define Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

class Block(pygame.sprite.Sprite):
	def __init__(self, locX, locY, img):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		# Create an image
		self.image = pygame.image.load(img).convert()
		self.image.set_colorkey(white)
		print(self.image.get_size())
		# Set bounds
		self.rect = self.image.get_rect()
		# Set draw location
		self.rect.x = locX
		self.rect.y = locY
	
# Set and Display Screen
sizeX = 800
sizeY = 400
scrollX = 0
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set Background 
background_image = pygame.image.load("scrollback2.png").convert()
background_size = background_image.get_size()

# Set Screen's Title
pygame.display.set_caption("Scroll Test")

# This is a list of sprites.
# The list is managed by a class called 'RenderPlain.'
sprites = pygame.sprite.RenderPlain()

# Sentinel for Game Loop
done = False

# Key Vars
keyDown = False
keyPress = 0

# Game Timer
clock = pygame.time.Clock()

# Main Game Loop
while done == False:
	# Limit FPS of Game Loop
	clock.tick(30)
	
	# Check for Events
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			keyDown = True
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				keyPress = 1
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				keyPress = 2
		if event.type == pygame.KEYUP:
			keyDown = False
			keyPress = 0

	# Clear the Screen
	screen.fill(white)

	# Show Background
	screen.blit( background_image , [scrollX ,0])
	
	# Set Movement
	if keyDown:
		if keyPress == 1 and scrollX < 0:
			scrollX += 5
		elif keyPress == 2 and scrollX > -(background_size[0]-sizeX):
			scrollX -= 5
	
	print(scrollX)
			
	# Draw all the sprites
	sprites.draw(screen)

	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()