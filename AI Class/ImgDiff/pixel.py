# File: pixel.py
# Author: Shawn Wilkinson
# Date: April 10, 2012

class Pixel:
	"""A Pixel Class"""
	def __init__(self, counter, red, green, blue):
		#  Counter Number
		self.i = int(counter)
		# RBG Values
		self.r = int(red)
		self.g = int(green)
		self.b = int(blue)
	def displayInfo(self):
		# Print Out Data Members
		print(str(self.i) + ". " + "R:" + str(self.r) + " B:" + str(self.b) + " G:" + str(self.g))
	# Accessors
	def getRed(self):
		return self.r
	def getBlue(self):
		return self.b
	def getGreen(self):
		return self.g
	def getCounter(self):
		return self.i
	
if __name__ == "__main__":
    pix = Pixel(1, 0, 0, 0)
    pix.displayInfo()