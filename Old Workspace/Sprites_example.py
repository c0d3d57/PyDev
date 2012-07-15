# Sample Python / PyGame Program
# Simpson College Computer Science

# Imports
import pygame
import random

# Set Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
colorList = [blue, green, black, red]

# Ball Class that is derived from the "Sprite" class in Pygame
class Block(pygame.sprite.Sprite):
	"""Some Class Named Block"""
	# Keep color for later
	_color = black
	# Constructor. Pass the color of the block and its (x,y) position
	def __init__(self, color, width, height):
		# Call the parent class (Sprite) constructor 
		pygame.sprite.Sprite.__init__(self)
		# Create an image of the block, and fill it with a color
		# This could also be an image loaded from the disk
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		#Set color here as well
		self._color = color
		self.rect = self.image.get_rect()
	# Reset the position of the block
	def reset_pos(self):
		self.rect.y = random.randrange(-150, -30)
		self.rect.x = random.randrange(0, screenX)
	# Move the position of the block
	def update(self):
		# Move the block down one pixel
		self.rect.y += 1		
		# Make the block loop back around
		if self.rect.y > screenY:
			self.reset_pos()

# Start Pygame and it's window
pygame.init()
screenX = 700
screenY = 400
screen = pygame.display.set_mode([screenX, screenY]) # What would happen if you made this a tuple instead?

# This is a list of 'sprites,' Each block in the program is
# added to this list
# The list is managed by a class called 'RenderPlain.'
block_list = pygame.sprite.RenderPlain()

# This is a list of every sprite
# All blocks and the player clock as well
all_sprites_list = pygame.sprite.RenderPlain()

for i in range(50):
	# Select a random color
	
	index = random.randrange(4)
	# This represents a block and makes one
	block = Block(colorList[index], 20, 15)
	
	# Set a random location for the block 
	block.rect.x = random.randrange(screenX)
	block.rect.y = random.randrange(screenY)
	
	# Add the block to the list of objects
	block_list.add(block)
	all_sprites_list.add(block)
	
# Create a red player block
player = Block(red, 20, 15)
all_sprites_list.add(player)

# Sent. for the while loop
done = False

# Set a clock to limit the loop
clock = pygame.time.Clock()

# A varible for the score
score = 0

# A varibles for lives
lives = 3

# Mouse Down
isDown = False

# ------ Main Program Loop-----
while done == False:
	# Check for an Exit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			print("Mouse Down!")
			isDown = True
			
	# Clear the screen
	screen.fill(white)
	
	# Gets the current mouse position
	# Returns the postition as a list of two numbers
	pos = pygame.mouse.get_pos()
	
	# Set the mouse position to the player block
	player.rect.x = pos[0]
	player.rect.y = pos[1]
	
	# Moves all the blocks
	block_list.update()
	
	# See if the player block has collided with anything
	block_hit_list = pygame.sprite.spritecollide(player, block_list, False)
	
	# Check the list of collisions and reset hit blocks 
	if len(block_hit_list) > 0 and isDown == True:
		for i in block_hit_list:
			if i._color == red:
				print("You lost a life!")
				lives -= 1
			else:
				score += len(block_hit_list)
			i.reset_pos()
			
		#Print Score
		print(score)
		
	# Check to see if you lost the game
	if lives <= 0:
		done = True
		print("Game Over!")
		
	# Reset isDown
	isDown = False
		
	# Draw all the sprites
	all_sprites_list.draw(screen)
	
	# Limit to 30 FPS
	clock.tick(30)
	
	# Update the screen
	pygame.display.flip()
	
# Exit Program
pygame.quit()