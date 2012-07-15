# File: main.py
# Author: Shawn Wilkinson
# Date: April 10, 2012

# System Imports
import sys
import pygame

# My Imports
from pixel import *
from ppmfile import *

class Main:
	def __init__(self):
		# Bounds of Cloud
		self.leastX = 1000
		self.mostX = -1000
		self.leastY = 1000
		self.mostY = -1000
	
	def rgbThreshold(self, left, right, thres):
		result = abs(left-right)
		if result <= thres:
			return False
		else:
			return True
			
	def findBounds(self, x, y):
		if x < self.leastX:
			self.leastX = x
		if x > self.mostX:
			self.mostX = x	
		if y < self.leastY:
			self.leastY = y
		if y > self.mostY:
			self.mostY = y
	
	def printBounds(self):
		print("LeastX: " + str(self.leastX))
		print("MostX: " + str(self.mostX))
		print("LeastY: " + str(self.leastY))
		print("MostY: " + str(self.mostY))
		
	def drawBounds(self):
		pass
	
	# Compare Files Function
	# Assumes That They Are the Same Size
	def compareFile(self, ppmLeft, ppmRight, thres):
		# Final Picture From Background Image
		finalPix = ppmLeft
		
		# Loop Through Image
		for x in range(ppmLeft.getSizeX()-1):
			for y in range(ppmLeft.getSizeY()-1):
				getNum = x + (ppmLeft.getSizeX() * (ppmLeft.getSizeY() - y - 1)) + 1
				# Set Their Pixels to Local Vars
				leftPix = ppmLeft.getPixel(getNum)
				rightPix = ppmRight.getPixel(getNum)
				# Check for Image Differences
				if self.rgbThreshold(leftPix.getRed(), rightPix.getRed(), thres):
					finalPix.setConflictPixel(getNum)
					self.findBounds(x, y)
				if self.rgbThreshold(leftPix.getGreen(), rightPix.getGreen(), thres):
					finalPix.setConflictPixel(getNum)
					self.findBounds(x, y)
				if self.rgbThreshold(leftPix.getBlue(), rightPix.getBlue(), thres):
					finalPix.setConflictPixel(getNum)
					self.findBounds(x, y)
					
				#if self.
		
		# Print Bounds
		self.printBounds()		
							
		# Display Annotated Result
		finalPix.displayRect(self.leastX, self.mostX, self.leastY, self.mostY)

if __name__ == "__main__":
	# Read In Files
	ppm1 = PPMFile('background/image001.ppm')
	#ppm2 = PPMFile('background/image005.ppm')
	ppm3 = PPMFile('background/image009.ppm')
	#ppm4 = PPMFile('background/image011.ppm')
	#ppm5 = PPMFile('background/image015.ppm')
	
	# Compare PP1 and PPM2
	runIt = Main()
	runIt.compareFile(ppm1, ppm3, 40)