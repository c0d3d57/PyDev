# Tank.py 
# Objective: Add scrollable world to exsisting tank.py
# Objective2: Add a plane
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
class Tank(Block):
	# Stats
	health = 100
	# Number of pixel the sprite moves per frame
	speed = 3
	# Direction
	direction = 1
	def __init__(self, locX, locY, img):
		Block.__init__(self, locX, locY, img)
	# If setSpeed argument is 0 then it will move the
	# tank forward and the default increment, but if it
	# is anything else then that will be the increment
	# instead. 
	def moveLeft(self, setSpeed):
		if setSpeed == 0:
			self.rect.x -= self.speed
		else:
			self.rect.x -= setSpeed
	def moveRight(self, setSpeed):
		if setSpeed == 0:
			self.rect.x += self.speed
		else:
			self.rect.x += setSpeed
	def flip(self):
		if self.direction == 1:
			self.direction = 2
		else:
			self.direction = 1
		self.image = pygame.transform.flip(self.image, 1, 0)
	def update(self):
		"""docstring for update"""
		pass
class Plane(Tank):
	speed = 8
	def __init__(self, locX, locY, img):
		Block.__init__(self, locX, locY, img)
	def update(self):
		"""docstring for update"""
		self.rect.x += self.speed
		
# Set and Display Screen
sizeX = 800
sizeY = 400
scrollX = 0
scrollSpeed = 5
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set Background and Get Size
background_image = pygame.image.load("scrollback2.png").convert()
background_size = background_image.get_size()

# Set Screen's Title
pygame.display.set_caption("Scroll and Tank Tests")

# This is a list of sprites.
# The list is managed by a class called 'RenderPlain.'
sprites = pygame.sprite.RenderPlain()

# Create 2 Tank sprites
aTank = Tank(50, 323, "tank.png")
aPlane = Plane(100, 123, "f22.png")
sprites.add(aTank)
sprites.add(aPlane)

# Sentinel for Game Loop
done = False

# Game Timer
clock = pygame.time.Clock()
time1 = 0
time2 = 0

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
	
	if key[pygame.K_a]:
		aTank.moveLeft(0)
	elif key[pygame.K_d]:
		aTank.moveRight(0)
		
	if key[pygame.K_LEFT] and scrollX < 0:
		scrollX += scrollSpeed
		for aSprite in sprites:
			aSprite.moveRight(scrollSpeed)
	elif key[pygame.K_RIGHT] and scrollX > -(background_size[0]-sizeX):
		scrollX -= scrollSpeed
		for aSprite in sprites:
			aSprite.moveLeft(scrollSpeed)	
	
	# Limits the number of times that tank can change direction
	time1 = int(round(pygame.time.get_ticks()/1000)) - time2
	if key[pygame.K_SPACE] and time1 >= 1:
		aTank.flip()
		time2 += time1	
		time1 = 0
			
	# Show Background
	screen.blit( background_image , [scrollX ,0])
			
	# Update and Draw all the sprites
	sprites.update()
	sprites.draw(screen)

	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()