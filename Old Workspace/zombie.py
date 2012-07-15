# Name: Zombie.py
# Author: Super3boy (super3.org)

# Imports
import pygame
import os

# Icon Function
def seticon(iconname):
    """
    give an iconname, a bitmap sized 32x32 pixels, black (0,0,0) will be alpha channel
    the windowicon will be set to the bitmap, but the black pixels will be full alpha channel
    can only be called once after pygame.init() and before somewindow = pygame.display.set_mode()
    """
    icon=pygame.Surface((32,32))
    icon.set_colorkey((100,100,100))#and call that color transparant
    rawicon=pygame.image.load(iconname)#must be 32x32, white is transparant
    for i in range(0,32):
        for j in range(0,32):
            icon.set_at((i,j), rawicon.get_at((i,j)))
    pygame.display.set_icon(icon)

# Start PyGame
pygame.init()

# Define Basic Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Define Game Colors
darkgrey = [84, 87, 106]
lightgrey = [165, 166, 174]

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

# Basic sprite class that is used for the crosshair
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
	def render(self, screen):
		screen.blit(self.image, [self.rect.x, self.rect.y])

# Plays an Animated Sprite
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
		self.x = x
		self.y = y
		# Set bounds
		self.rect = self.image.get_rect()
		# Alive
		self.alive = True
		
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
			# Update Frame and Display Sprite
			self.update(pygame.time.get_ticks())
			screen.blit(self.image, self.location)
			
class Zombie(AnimatedSprite):
	def render(self, screen):
		# Update Frame and Display Sprite
		AnimatedSprite.render(self, screen)
		# Move Zombie and Update Location
		self.location = [self.x-1, self.y]
		self.x, self.y = self.location 
		
class Police(AnimatedSprite):
	def __init__(self, images, x, y, fps = 6):
		# Standard Animated Sprite + Can Fire
		super(Police, self).__init__(images, x, y, fps)
		self.canFire = False
		# Ammo Counter
		
	def render(self, screen):
		# Update Frame
		self.update(pygame.time.get_ticks())
		# Display Sprite
		if self.canFire:
			screen.blit(self.image, self.location)
		else:
			screen.blit(self._images[0], self.location)
		# Draw Ammo 
		for i in range(6):
			pygame.draw.line(screen, darkgrey, [self.x+3+(i*3), self.y-1], [self.x+3+(i*3), self.y-7], 2)
			
# Set and Display Screen
sizeX = 800
sizeY = 200
size = [sizeX, sizeY]
# Load Icon
seticon('icon2.png')
screen = pygame.display.set_mode(size)

# Set Screen's Title and Icon
pygame.display.set_caption("Zombies on Conveyors")

# Sentinel for Game Loop
done = False

# Game Timer
clock = pygame.time.Clock()

# This is a list of sprites.
# The list is managed by a class called 'RenderPlain.'
sprites = pygame.sprite.RenderPlain()
zombie_sprites = pygame.sprite.RenderPlain()

# Load Images and Create Animated Sprite Objects
zombie_sprite = load_sliced_sprites(23, 34, "zombie.png")
zombie_die_sprite = load_sliced_sprites(35, 34, "zombie-die.png")
police_fire = load_sliced_sprites(35, 34, "police-fire.png")
# Load Background
background_image = pygame.image.load("factory-background.png").convert()
# Load Crosshairs
crosshair = Block(50, 50, "crosshair.png")
sprites.add(crosshair)
# Load Police
police = Police(police_fire, 20, sizeY-34)
sprites.add(police)
# Load a Few Zombies
for i in range(3):
	a_zombie = Zombie(zombie_sprite, sizeX+(i*30), sizeY-34)
	sprites.add(a_zombie)
	zombie_sprites.add(a_zombie)

# Hide Mouse
pygame.mouse.set_visible(False)

# Main Game Loop
while done == False:
	# Limit FPS of Game Loop
	clock.tick(30)
	
	# Check for Events
	for event in pygame.event.get(): 
		# Quit Game
		if event.type == pygame.QUIT:
			done = True
		# Spawn a Zombie
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				#print("Zombie Spawned!")
				a_zombie = Zombie(zombie_sprite, sizeX+30, sizeY-34)
				sprites.add(a_zombie)
				zombie_sprites.add(a_zombie)
		# Fire Weapon
		elif event.type != pygame.MOUSEBUTTONDOWN:
			police.canFire = False
		elif event.type != pygame.MOUSEBUTTONUP:
			police.canFire = True
			
	# See if the player block has collided with anything
	block_hit_list = pygame.sprite.spritecollide(crosshair, zombie_sprites, False)
	
	# Check the list of collisions and reset hit blocks 
	if len(block_hit_list) > 0:
		pass
	#	print("Hit")
	#	for i in block_hit_list:
	#		if i._color == red:
	#			print("You lost a life!")
	#			lives -= 1
	#		else:
	#			score += len(block_hit_list)
	#		i.reset_pos()
			
	# Clear the Screen
	screen.fill(white)
	
	# Gets the current mouse position
	# Returns the postition as a list of two numbers
	pos = pygame.mouse.get_pos()
	
	# Set the mouse position to the player block
	crosshair.rect.x = pos[0] + 5
	crosshair.rect.y = pos[1] + 5
	
	# Show Background
	screen.blit( background_image , [0 ,0])
	
	# Display Sprites
	for i in sprites:
		i.render(screen)

	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()