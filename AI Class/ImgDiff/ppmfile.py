# File: ppmfile.py
# Author: Shawn Wilkinson
# Date: April 19, 2012

# System Imports
import sys
import pygame
import random

# My Imports
from pixel import *

class PPMFile:
	"""A PPM File Class"""
	def __init__(self, filePath):
		# Read In The File ( Read Only )
		self.imgFile = open(filePath, 'r')
		
		# Get File Info
		self.fileType = self.nextLine() # Should be P3
		self.comment = self.nextLine() # Comment
		self.size = self.nextLine() # Image Size
		self.maxColor = int(self.nextLine()) # Max Color Value
		
		# Get Image Size
		sizeArr = self.size.split(' ')
		self.sizeX = int(sizeArr[0])
		self.sizeY = int(sizeArr[1])
		
		# Image Pixel List
		self.counter = 0
		self.pixels = []
		
		# Load Pixels
		self.loadPixels()
		
	def loadPixels(self):		
		# Filler Input for Loop
		rgbVals = "filler"
		maxVal = 0
		# Pixel Adding Loop
		while True:	
			# Grab Pixels and Remove Breakline
			rgbVals = self.nextLine()
			# Check to See if End of File
			# If So, Break Pixel Adding Loop
			if rgbVals == "":
				break
			# Get Rid of Tab Char
			rgbVals = rgbVals.replace('\t', ' ')
			# Split Into An Array of Vals
			rgbArr = rgbVals.split(' ')
			# Get Rid of Extra Element
			rgbArr.remove('')
			
			# Status Update
			# Checks the Number of Current Pixels .vs the Image Size and Gives a Percent
			# Uses maxVal so it Won't Repeat a Percent, and Only Displays in 10% Intervals
			percent = int((int(self.counter) / (self.sizeX * self.sizeY))*100)
			if percent % 10 == 0 and maxVal < percent:
				print("Loading in Pixels..." + str(percent) + "%")
				maxVal = percent
				
			# Magic
			for i in range( int(len(rgbArr)/3) ):
				#print("Rows" + str(i))
				val1 = (i*3)
				val2 = (i*3) + 1
				val3 = (i*3) + 2
				self.pixels.append( Pixel(self.countUp(), rgbArr[val1], rgbArr[val2], rgbArr[val3]) )
			

	# Return Next Line of the File
	def nextLine(self):
		return self.imgFile.readline().strip('\n')
		
	# Display the Number and RGB Value of All Pixels in the Image
	def displayRaw(self):
		for i in self.pixels:
			i.displayInfo()
		
	# Increment the Number Counter and Return the Value
	def countUp(self):
		self.counter += 1
		return self.counter
		
	# Display Basic PPM File Info
	def displayInfo(self):
		if self.fileType == "P3":
			print("Valid File.")
		else:
			print("Invalid File.")
		print("Image Size X: " + str(self.sizeX))
		print("Image Size Y: " + str(self.sizeY))
		print("Image Max Color: " +  str(self.maxColor) + "\n")
		
	# Get a Single Pixel
	def getPixel(self, id):
		return self.pixels[id]
	
	# Set a Single Pixel to Red
	def setConflictPixel(self, id):
		self.pixels[id] = Pixel(self.pixels[id].getCounter(), 255, 0 , 0)
		
	# Get Sizes
	def getSizeX(self):
		return self.sizeX
	def getSizeY(self):
		return self.sizeY
		
	# Display Image
	def display(self):
		# Setup Basic PyGame Stuff
		screen = pygame.display.set_mode((self.sizeX, self.sizeY))
		clock = pygame.time.Clock()
		running = True
		
		# Main Game Loop
		while running:
			for x in range(self.sizeX-1):
				for y in range(self.sizeY-1):
					# Get Point
					getNum = x + (self.sizeX * (self.sizeY - y - 1)) + 1
					red = self.pixels[getNum].getRed()
					green = self.pixels[getNum].getGreen()
					blue = self.pixels[getNum].getBlue()
			
					# Plot Point
					# self.sizeY-y makes it flip somehow
					screen.set_at((x, self.sizeY-y), (red, green, blue))
			
			# Look For Exit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			
			# Refresh Display
			pygame.display.flip()
			clock.tick(100)
	
	# Display Image
	def displayRect(self, leastX, mostX, leastY, mostY):
		# Setup Basic PyGame Stuff
		screen = pygame.display.set_mode((self.sizeX, self.sizeY))
		clock = pygame.time.Clock()
		running = True
		
		# Main Game Loop
		while running:
			for x in range(self.sizeX-1):
				for y in range(self.sizeY-1):
					# Get Point
					getNum = x + (self.sizeX * (self.sizeY - y - 1)) + 1
					red = self.pixels[getNum].getRed()
					green = self.pixels[getNum].getGreen()
					blue = self.pixels[getNum].getBlue()
					
					#pygame.draw.line(screen, (0,0,255), (leastX, self.sizeY-leastY), (mostX, self.sizeY-mostY), 5) 
					pygame.draw.line(screen, (0,0,255), (leastX, self.sizeY-leastY), (leastX, self.sizeY-mostY), 3)
					pygame.draw.line(screen, (0,0,255), (mostX, self.sizeY-leastY), (mostX, self.sizeY-mostY), 3) 
					
					pygame.draw.line(screen, (0,0,255), (leastX, self.sizeY-leastY), (mostX, self.sizeY-leastY), 3)
					pygame.draw.line(screen, (0,0,255), (leastX, self.sizeY-mostY), (mostX, self.sizeY-mostY), 3) 
			
					# Plot Point
					# self.sizeY-y makes it flip somehow
					screen.set_at((x, self.sizeY-y), (red, green, blue))
			
			# Look For Exit
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			
			# Refresh Display
			pygame.display.flip()
			clock.tick(100)
		
if __name__ == "__main__":
    ppm = PPMFile('background/image005.ppm')
    ppm.displayInfo()
    #for i in range(10000):
    #	ppm.setConflictPixel(i)
    ppm.display()
    #ppm.displayRaw()