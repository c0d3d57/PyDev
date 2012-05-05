# Name: WalkAI.py
# Includes parts from Walk.py
# Objective One: Allow 50 Person objects to freely walk the world
# Author: Super3boy (super3.org)

# Imports
import pygame
import os
import random

# Start PyGame
pygame.init()

# Define Basic Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Fake Constants
DIR_RIGHT, DIR_LEFT = [1, 2]

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
	'''
	Specs :
		Takes an array of images, a location, and fps
		Array of images can be processed with load_sliced_sprites()
	'''
	moving = False
	actualLoc = [0, 0]
	
	def __init__(self, images, x, y, fps):
		pygame.sprite.Sprite.__init__(self)
		self._images = images
		
		# Track the time we started, and the time between updates.
		# Then we can figure out when we have to switch the image.
		self._start = pygame.time.get_ticks()
		self._delay = 1000 / fps
		self._last_update = 0
		self._frame = random.randrange(6)
		self.image = self._images[self._frame]
		self.image.set_colorkey(white)
		# Set Location
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = [x, y]
		actualLoc = [x, y]
		
	def update(self, t):
		# Note that this doesn't work if it's been more than self._delay
		# time between calls to update(); we only update the image once
		# then. but it really should be updated twice
		
		if self.moving == True:
			if t - self._last_update > self._delay:
				self._frame += 1
				if self._frame >= len(self._images): 
					self._frame = 0
					self.image = self._images[self._frame]
					self._last_update = t
				self.image = self._images[self._frame]
				self.image.set_colorkey(white)
				self._last_update = t
		else:
			self.image = self._images[0]
			self._frame = 0
			
	def render(self, screen):
		self.update(pygame.time.get_ticks())
		screen.blit(self.image, self.rect)
			
class Person(AnimatedSprite):
	# Number of pixel the sprite moves per frame
	speed = 3
	# Direction
	direction = DIR_RIGHT
	# If True the Person will turn around and walk the other direction
	# when it reaches the end of world( Not working)
	bounds = False
	
	def __init__(self, images, x, y, speed):
		AnimatedSprite.__init__(self, images, x, y, fps=4)
		self.speed = speed
		
	def moveLeft(self, setSpeed = 0):
		if setSpeed == 0:
			self.rect.x -= self.speed
			self.actualLoc[0] -= self.speed
		else:
			self.rect.x -= setSpeed
	def moveRight(self, setSpeed = 0):
		if setSpeed == 0:
			self.rect.x += self.speed
			self.actualLoc[0] += self.speed
		else:
			self.rect.x += setSpeed
	def flip(self):
		if self.direction == DIR_RIGHT:
			self.direction = DIR_LEFT
		else:
			self.direction = DIR_RIGHT
		# Flip images in array
		tmpImages = []
		for anImage in self._images:
			tmpImages.append(pygame.transform.flip(anImage, 1, 0))
		self._images = tmpImages
		
	def walk(self):
		self.moving = True
		
		if self.direction ==  DIR_RIGHT:
			self.moveRight()
		else:
			self.moveLeft()
		
		if self.bounds == True:
			if self.actualLoc[0] <= 0:
				self.flip()	
			elif self.actualLoc[0] >= background_size[0]:
				self.flip()	
				print(self.actualLoc[0])
			
# Set and Display Screen
sizeX = 800
sizeY = 400
scrollX = 0
scrollSpeed = 5
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set Background and Get Size
background_image = pygame.image.load("scrollback6.png").convert()
background_size = background_image.get_size()

# This is a list of sprites.
# The list is managed by a class called 'RenderPlain.'
sprites = pygame.sprite.RenderPlain()

# Load Sprite and Created Sample Person
walkcycle = load_sliced_sprites(32, 64, "walk1.png")
for i in range(50):
	sprites.add(Person(walkcycle, -random.randrange(1000), 293, random.randrange(5)))

# Set Screen's Title
pygame.display.set_caption("Walk Tests")

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
		
	# Move Camera (Keyboard and Mouse)
	# Splits the screen into 3 main areas. The middle area, where
	# no action is taken to move the camera. The left and right areas
	# where the camera will scroll that direction. The closer the mouse
	# is to the edge of the screen then faster the camera will scroll.
	posX, posY = pygame.mouse.get_pos()
	if (key[pygame.K_LEFT] or  posX <= (sizeX * 0.10)) and scrollX < 0:
		scrollX += scrollSpeed
		for aSprite in sprites:
			aSprite.moveRight(scrollSpeed)
	elif (key[pygame.K_RIGHT] or posX >= (sizeX -(sizeX * 0.10))) and scrollX > -(background_size[0]-sizeX):
		scrollX -= scrollSpeed
		for aSprite in sprites:
			aSprite.moveLeft(scrollSpeed)	
			
	# Show Background
	screen.blit( background_image , [scrollX ,0])
			
	# Update and Draw all the sprites
	for aSprite in sprites:
		aSprite.walk()
		aSprite.render(screen)	

	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()