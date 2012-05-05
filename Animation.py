# Name: Animation.py
# Objective: Create an animated sprite.
# Author: Super3boy (super3.org)
# Credit: Shiny Blog 
# Credit URL: shinylittlething.com/2009/07/21/pygame-and-animated-sprites/

# Imports
import pygame
import os

# Start PyGame
pygame.init()

# Define Basic Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Helper function that loads, and splits the animated
# sprite into an array of images which it returns. 
def load_sliced_sprites(w, h, filename):
	'''
	Specs :
		Master can be any height
		Sprites frames width must be the same width
		Master width must be len(frames)*frames.width
	'''
	images = []
	try:
		master_image = pygame.image.load(filename).convert_alpha()
	except:
		print("Could not open sprite",filename)
	else: 
		# Seems like you can set the two. Intresting.
		# This works, but you can't have one statement on the right
		# of the = sign.
		master_width, master_height = master_image.get_size()
		for i in range(int(master_width/w)):
			images.append(master_image.subsurface((i*w, 0, w, h)))
	return images
	
class AnimatedSprite(pygame.sprite.Sprite):
	"""docstring for AnimatedSprite"""
	def __init__(self, images, x, y, fps = 6):
		pygame.sprite.Sprite.__init__(self)
		self._images = images
		
		# Track the time we started, and the time between updates.
		# Then we can figure out when we have to switch the image.
		self._start = pygame.time.get_ticks()
		self._delay = 1000 / fps
		self._last_update = 0
		self._frame = 0
		self.image = self._images[self._frame]
		# Set Location
		self.location = [x, y]
		#self.x = x
		#self.y = y
		
	def update(self, t):
		# Note that this doesn't work if it's been more than self._delay
		# time between calls to update(); we only update the image once
		# then. but it really should be updated twice
		
		if t - self._last_update > self._delay:
			self._frame += 1
			if self._frame >= len(self._images): 
				self._frame = 0
				self.image = self._images[self._frame]
				self._last_update = t
			self.image = self._images[self._frame]
			self._last_update = t
			
	def render(self, screen):
			self.update(pygame.time.get_ticks())
			screen.blit(self.image, self.location)
			#self.location = [self.x+2, self.y]
			#self.x, self.y = self.location

# Set and Display Screen
sizeX = 400
sizeY = 400
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set Screen's Title
pygame.display.set_caption("Animation Tests")

# Sentinel for Game Loop
done = False

# Game Timer
clock = pygame.time.Clock()

# This is a list of sprites.
# The list is managed by a class called 'RenderPlain.'
sprites = pygame.sprite.RenderPlain()

# Load Image and Create Animated Sprite Object
run = load_sliced_sprites(23, 34, "zombie.png")
mysprite2 = AnimatedSprite(run, 10, 100)
sprites.add(mysprite2)

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
	
	# Play Sprite
	for i in sprites:
		i.render(screen)

	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()