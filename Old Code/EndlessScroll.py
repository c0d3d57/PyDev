# EndlessScroll.py 
# Objective: Make an endless scrollable world.
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
		# Set bounds
		self.rect = self.image.get_rect()
		# Set draw location
		self.rect.x = locX
		self.rect.y = locY
		
# Set and Display Screen
sizeX = 800
sizeY = 400
scrollX = 0
scrollSpeed = 5
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set Background and Get Size
background_image = pygame.image.load("scrollback4.png").convert()
background_size = background_image.get_size()

# Set Screen's Title
pygame.display.set_caption("Enless Scroll Test")

# This is a list of sprites.
# The list is managed by a class called 'RenderPlain.'
sprites = pygame.sprite.RenderPlain()

# Sentinel for Game Loop
done = False

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

	# Clear the Screen
	screen.fill(white)

	# Set Movement
	key=pygame.key.get_pressed()  #checking pressed keys
	
	if key[pygame.K_LEFT]:
		scrollX += scrollSpeed
	elif key[pygame.K_RIGHT]:
		scrollX -= scrollSpeed

	# Show Background
	screen.blit( background_image , [scrollX ,0])
			
	# Update and Draw all the sprites
	sprites.update()
	sprites.draw(screen)

	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()