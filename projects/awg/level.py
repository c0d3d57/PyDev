# Name: Level.py
# Author: Super3 (super3.org)

import pygame
import pygame.locals
import configparser
from sys import argv

class Level(object):
	# Constructor
	def __init__(self, filename="level.map"):
		# Load File 
		self.load_file(filename)
	
	# Main Methods
	def load_file(self, filename):
		"""Load level file and tileset"""
		# Map Square Array and Key-Value Pairs
		self.map = []
		self.key = {}
		# Create Parser and Read From File
		parser = configparser.ConfigParser()
		parser.read(filename)
		# Get Tileset Filename and Map
		self.scale = int(parser.get("level", "scale"))
		self.tileset = parser.get("level", "tileset")
		self.tileset = "img/" + self.tileset
		self.tile = self.load_tile_table(self.tileset, self.scale, self.scale)
		self.map = parser.get("level", "map").split("\n")
		# Get Key-Value Pairs
		for section in parser.sections():
			if len(section) == 1:
				desc = dict(parser.items(section))
				self.key[section] = desc
		# Set Width and Height of Map
		self.width = len(self.map[0])
		self.height = len(self.map)
	
	def load_tile_table(self, filename, width, height):
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
		
	def get_tile(self, x, y):
		"""Returns what's at the specified position of the map"""
		# Tries to Return Map Character
		try:
			char = self.map[y][x]
		except IndexError:
			return {}
		# Tries to Return Map's Key-Value Pair
		try:
			return self.key[char]
		except KeyError:
			return {}
			
	def render(self, screen):
		"""Draws all the tiles on the screen"""
		for x in range(self.width):
			for y in range(self.height):
				# Turn Tile into Tileset Location
				tileLoc = self.get_tile(x, y)['tile'].split(',')
				# Turn Tiletset Location to Image
				tile = self.tile[int(tileLoc[0])][int(tileLoc[1])]
				# Drawn on Screen
				screen.blit(tile, (x*self.scale, y*self.scale))
				
# Main 
if __name__ == '__main__':	
	# Start Pygame
	pygame.init()
	# Set Screen
	screenX, screenY = [240, 240]
	screen = pygame.display.set_mode((screenX,screenY))
	pygame.display.set_caption("AWG Tiletest")
	screen.fill((255,255,255))
	# ARGV
	script, aMap = argv
	# Load and Display Level
	myLevel = Level(aMap)
	myLevel.render(screen)
	# Update Screen
	pygame.display.flip()
	# Check for Exit
	while pygame.event.wait().type != pygame.locals.QUIT:
		pass