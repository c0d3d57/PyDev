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

# Set and Display Screen
sizeX = 500
sizeY = 500
size = [sizeX, sizeY]
screen = pygame.display.set_mode(size)

# Set Screen's Title
pygame.display.set_caption("World Grid")

# Grid Settings
width = 20 # X size of grid location
height  = 20 # Y size of grid location

# Make Grid Array
grid = []
for row in range(int(sizeX/width)):
	grid.append([])
	for column in range(int(sizeX/height)):
		grid[row].append(0)
	
# Test Grid Value	
grid[1][5] = 1

# Sentinel for Game Loop
done = False

# Game Timer
clock = pygame.time.Clock()

# Main Game Loop
while done == False:
	# Limit FPS of Game Loop
	clock.tick(25)
	
	# Check for Events
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			gridLocX = int(pos[0] / width)
			gridLocY = int(pos[1] / height)
			grid[gridLocY][gridLocX] = 1
	
	# Clear the Screen
	screen.fill(black)
	
	# Draw Grid
	for column in range(int(sizeX/width)):
		for row in range(int(sizeY/height)):
			if grid[row][column] == 1:
				color = green
			else:
				 color = white
			pygame.draw.rect( screen, color, [column*width,row*height, width, height])
	
	# Update Display
	pygame.display.flip()

# Exit Program
pygame.quit()