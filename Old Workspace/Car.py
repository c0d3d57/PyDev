# Car Example With PyGame
# Author: Shawn Wilkinson

# Imports
import pygame
import random

# Set Color
black = [0, 0, 0]
white = [255, 255, 255]

# A Car class that is derived from the "Sprite" class in Pygame
class Car(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		# Create image and fill with color
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		# Don't really know that this rect thing is
		self.rect = self.image.get_rect()
	def move(self, direction):
		if direction == 1:
			self.rect.y -= 1
		elif direction == 2:
			self.rect.x += 1
		elif direction == 3:
			self.rect.y += 1
		elif direction == 4:
			self.rect.x -= 1
		
# Start Pygame and it's window
pygame.init()
screenX = 800
screenY = 600
screen = pygame.display.set_mode([screenX, screenY])

# This is a list of every sprite
all_sprites = pygame.sprite.RenderPlain()

# Create a car called player and add to all_sprites
player = Car(black, 10,20)
player.rect.x = 400
player.rect.y = 400
all_sprites.add(player)

# Sent. for the while loop
done = False

# Set a clock to limit the loop
clock = pygame.time.Clock()

# Holds the direction
direct = 0

# ----- Main Program Loop ----- 
while done == False:
	# Check for Events
	for event in pygame.event.get():
		# See if the user is trying to quit
		if event.type == pygame.QUIT:
			done = True
		# If the user has hit a key check to see if they hit
		# the arrow keys or wasd keys. If they have then send
		# that info to the class
		if event.type == pygame.KEYDOWN:
			direct = 0
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				direct = 1
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				direct = 3
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				direct = 4
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				direct = 2
		if event.type == pygame.KEYUP:
			direct = 0
	
	if direct != 0:
		player.move(direct)
				
	# Clear the screen
	screen.fill(white)
	
	# Draw the player
	all_sprites.draw(screen)
	
	# Limit to 30 FPS
	clock.tick(30)
	
	# Update the screen 
	pygame.display.flip()
	
# Exit Program
pygame.quit()
		