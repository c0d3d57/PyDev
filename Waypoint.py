# Waypoint.py 
# An attempt to make a waypoint based movement system and class
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

# Keep waypoints in order
global wayCount
wayCount = 0

class Block(pygame.sprite.Sprite):
	# Default color of a block
	color = black
	# Default size of a block
	size = 10
	def __init__(self, locX, locY):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		# Create an image of the block, and fill it with a color
		# This could also be an image loaded from the disk
		self.image = pygame.Surface([self.size, self.size])
		self.image.fill(self.color)
		# Set bounds
		self.rect = self.image.get_rect()
		# Set draw location
		self.rect.x = locX
		self.rect.y = locY

# Waypoint Class that derived from the "Sprite" class in Pygame
class Waypoint(Block):
	"""A single navigable waypoint"""
	# Default color of waypoint square and track line
	color = green 
	# To keep waypoints in order
	order = 0
	# Call base class constructor
	def __init__(self, locX, locY):
		Block.__init__(self, locX, locY)
		
# Ship Class that derived from the "Sprite" class in Pygame
class Ship(Block):
	"""A single moveable ship"""
	# Current Navagation Goal
	goX = 0
	goY = 0
	def __init__(self, locX, locY):
		Block.__init__(self, locX, locY)
		self.goX = locX
		self.goY = locY
	def update(self):
		"""Move to current navagation goal or stay still"""
		if self.goX > self.rect.x:
			self.rect.x += 1
		elif self.goX < self.rect.x:
		 	self.rect.x -= 1
		 		
		if self.goY > self.rect.y:
			self.rect.y += 1
		elif self.goY < self.rect.y:
		 	self.rect.y -= 1
	def setGoal(self, x, y):
		"""Set current navagation goal"""
		self.goX = x
		self.goY = y
	def atGoal(self):
		"""If ship is at goal or not"""
		if self.rect.x == self.goX and self.rect.y == self.goY:
			return True
		return False

# Set and Display Screen
sizeX = 800
sizeY = 600
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set Screen's Title
pygame.display.set_caption("Waypoint Example")

# This is a list of 'sprites,' Each waypoint in the program is
# added to this list
# The list is managed by a class called 'RenderPlain.'
waypoint_list = pygame.sprite.RenderPlain()

# List of all ships
ships_list =  pygame.sprite.RenderPlain()

# This is a list of every sprite
# All blocks and the waypoints as well
all_sprites_list = pygame.sprite.RenderPlain()

# Add a ship
aShip = Ship(100, 100)
ships_list.add(aShip)
all_sprites_list.add(aShip)

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
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			wayp = Waypoint(pos[0], pos[1])
			wayp.order = wayCount
			wayCount += 1 #Keep Track of Waypoints
			waypoint_list.add(wayp)
			all_sprites_list.add(wayp)
	
	# Clear the Screen
	screen.fill(white)
	
	# Update ships location
	ships_list.update()
	
	# Get first waypoint
	tmpWayX = 0 
	tmpWayY = 0
	tmpOrder = 10000
	for tmpWay in waypoint_list:
		if tmpOrder > tmpWay.order:
			tmpWayX = tmpWay.rect.x
			tmpWayY = tmpWay.rect.y
			tmpOrder = tmpWay.order
			
	# Give a waypoint if not empty 
	if len(waypoint_list) > 0:
		for tmpShip in ships_list:
			if tmpShip.atGoal():
				tmpShip.setGoal(tmpWayX, tmpWayY)
	else:
		wayCount = 0
			
	# See if the player block has collided with anything
	pygame.sprite.spritecollide(aShip, waypoint_list, True)
	
	# Draw all the sprites
	all_sprites_list.draw(screen)

	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()