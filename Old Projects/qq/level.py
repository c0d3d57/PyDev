# Level.py
# Author: Super3(super3.org)
# Source: Radomir Dopieralski(qq.readthedocs.org)

import configparser # ConfigParser module has been renamed to configparser in Python 3.0
import pygame

class Level(object):
	# Main Methods
	def load_file(self, filename="level.map"):
		# Map Square Array and Key-Value Pairs
		self.map = []
		self.key = {}
		# Create Parser and Read From File
		parser = configparser.ConfigParser()
		parser.read(filename)
		# Get Tileset Filename and Map
		self.tileset = parser.get("level", "tileset")
		self.map = parser.get("level", "map").split("\n")
		# Get Key-Value Pairs
		for section in parser.sections():
			if len(section) == 1:
				desc = dict(parser.items(section))
				self.key[section] = desc
		# Set Width and Height of Map
		self.width = len(self.map[0])
		self.height = len(self.map)
		
	def get_tile(self, x, y):
		"""Returns what's at the specified position of the map"""
		# Tries to Return Map Character
		try:
			char = self.map[y][x]
		except IndexError:
			return {}
		# Tries to Return Map's Key-Value Pair
		try:
			return self.keys[char]
		except KeyError:
			return {}
	
	# Convenience Methods
	def get_bool(self, x, y, name):
		"""Tell if the specified flag is set for position on the map"""
		value = self.get_tile(x, y).get(name)
		return value in (True, 1, 'true', 'yes', 'True', 'Yes', '1', 'on', 'On')
		
	def is_wall(self, x, y):
		"""Is there a wall?"""
		return self.get_bool(x,y, 'wall')
		
	def is_blocking(self, x, y):
		"""Is this place blocking movement?"""
		if not 0 <= x < self.width or not 0 <= y < self.height:
			return True
		return self.get_bool(x, y, 'block')
		
	# Draw Level
	def render(self):
		wall = self.is_wall
		tiles = self.tileset
		image = pygame.Surface((self.width*MAP_TILE_WIDTH, self.height*MAP_TILE_HEIGHT))
		overlays = {}
		for map_y, line in enumerate(self.map):
			if wall(map_x, map_y):
				# Draw different tiles depending on neighbourhood 
				if not wall(map_x, map_y+1):
					if wall(map_x+1, map_y) and wall(map_x-1, map_y):
						tile = 1, 2
					elif wall(map_x+1, map_y):
						tile = 0, 2
					elif wall(map_x-1, map_y):
						tile = 2, 2
					else:
						tile = 3, 2
				else:
					if wall(map_x+1, map_y+1) and wall(map_x-1, map_y+1):
						tile = 1, 1
					elif wall(map_x+1, map_y+1):
						tile = 0, 1
					elif wall(map_x-1, map_y+1):
						tile = 2, 1
					else:
						tile = 3, 1
				# Add overlays if the wall may be obscuring something
				if not wall(map_x, map_y-1):
					if wall(map_x+1, map_y) and wall(map_x-1, map_y):
						over = 1, 0
					elif wall(map_x+1, map_y):
						over = 0, 0
					elif wall(map_x-1, map_y):
						over = 2, 0
					else:
						over = 3, 0
					overlays[(map_x, map_y)] = tiles[over[0]][over[1]]
			else:
				try:
					tile = self.key[c]['tile'].split(',')
					tile = int(tile[0]), int(tile[1])
				except (ValueError, KeyError):
					# Default to ground tile
					tile = 0, 3
			tile_image = tile[tile[0]][tile[1]]
			image.blit(tile_image, (map_x*MAP_TILE_WIDTH, map_y*MAP_TILE_HEIGHT))
		return image, overlays