# Main.py
# Author: Super3(super3.org)
# Source: Radomir Dopieralski(qq.readthedocs.org)

import pygame 
import pygame.locals
from level import *
import configparser

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

if __name__ == "__main__":
    screen = pygame.display.set_mode((424, 320))

    MAP_TILE_WIDTH = 24
    MAP_TILE_HEIGHT = 16
    MAP_CACHE = {
        'ground.png': load_tile_table('ground.png', MAP_TILE_WIDTH,
                                      MAP_TILE_HEIGHT),
    }

    level = Level()
    level.load_file('level.map')

    clock = pygame.time.Clock()

    background, overlay_dict = level.render()
    overlays = pygame.sprite.RenderUpdates()
    for (x, y), image in overlay_dict.iteritems():
        overlay = pygame.sprite.Sprite(overlays)
        overlay.image = image
        overlay.rect = image.get_rect().move(x * 24, y * 16 - 16)
    screen.blit(background, (0, 0))
    overlays.draw(screen)
    pygame.display.flip()
    
    