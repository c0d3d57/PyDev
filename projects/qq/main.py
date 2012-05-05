# Main.py
# Author: Super3(super3.org)
# Source: Radomir Dopieralski(qq.readthedocs.org)

import pygame 
import pygame.locals

def load_tile_table(filename, width, height):
	"""Load tileset into image array."""
	try: 
		tile_table = []
		image = pygame.image.load(filename).convert()
	except:
		print("Could not load tileset:", filename)
	else:
		image_width, image_height = image.get_size()
		for tile_x in range(0, int(image_width/width)):
			line = []
			tile_table.append(line)
			for tile_y in range(0, int(image_height/height)):
				rect = (tile_x*width, tile_y*height, width, height)
				line.append(image.subsurface(rect))
	return tile_table
	
# When __name__ == '__main__' the program is being run by itself,
# otherwise it is being imported from another module. 
if __name__ == '__main__':	
	# Start Pygame
	pygame.init()
	# Set Screen
	screen = pygame.display.set_mode((400,400))
	screen.fill((255, 255, 255))
	# Load and Display Tileset
	table = load_tile_table("ground.png", 24, 16)
	for x, row in enumerate(table):
		for y, tile in enumerate(row):
			screen.blit(tile, (x*32, y*24))
	# Update Screen
	pygame.display.flip()
	# Check for Exit
	while pygame.event.wait().type != pygame.locals.QUIT:
		pass
