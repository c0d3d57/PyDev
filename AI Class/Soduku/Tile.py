# Name: File.py
# Author: Shawn Wilkinson

# Imports
import random
import copy

class Tile():
	"""A Single Soduku Tile"""
	
	# -----------------------
	# ----- Constructor -----
	# -----------------------
	
	def __init__(self, faceValue):
		# Main Key - FaceValue
		self.faceValue = faceValue
		# Property - Is Solved
		if self.faceValue == 0:
			self.solved = False
		else:
			self.solved = True
		# Property - Hints
		if not self.solved:
			self.hints = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		else:
			self.hints = []
		# Property - Conflicts
		self.conflicts = []
	
	# ---------------------		
	# ----- Assessors -----
	# ---------------------
	
	def getFaceValue(self):
		"""Get faceValue of Tile"""
		return self.faceValue
	def isSolved(self):
		"""Get if Tile is solved or not"""
		return self.solved
	def getHints(self):
		"""Get hints for Tile"""
		return self.hints
	def getConflicts(self):
		"""Return number of conflicts"""
		conflicts = 0 
		for con in self.conflicts:
			if con == self.getFaceValue():
				conflicts += 1
		return conflicts
		
	# --------------------
	# ----- Mutators -----  # TODO: Error Checking?
	# --------------------
	
	def setFaceValue(self, faceValue): # Private Method Please
		"""Set faceValue of Tile"""
		self.faceValue = faceValue
	def setSolved(self, solved):	   # Private Method Please
		"""Set isSolved of Tile"""
		self.solved = solved 	
	def setHints(self, hints): 		   # Private Method Please
		"""Set hints of Tile"""
		self.hints = hints
		
	def addConflicts(self, myConflicts):
		for con in myConflicts:
			self.conflicts.append( con )
	def clearConflicts(self):
		self.conflicts = []
		
	# -------------------	
	# ----- Methods -----
	# -------------------
	
	# Precondition: A random unsorted list (that should not contain duplicates -
	# 				we actually thow an error in this case) that contains all
	# 				are in this Tile's sub-sqaure, horizontal, or vertical path
	# 				and are already solved
	# Postconditon: A reduced number of choices or hints to randomly pick from 
	def clearHints(self, hintList):
		# Check to make sure their are no duplicates by comparing the length of
		# the input list .vs a list that has all its duplicates removed
		if len(hintList) != len( list(set(hintList)) ):
			print("Error Tile.clearHints() - Duplicate Solved Hints")
		else:
			# Everything went as expected
			pass
			
		# Reset to the old hints
		self.hints = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		
		# Loop through hints and remove them
		for aHint in hintList:
			# Attempt to remove an overlapping hint
			try:
				# Lets hope thats it is there
				self.hints.remove(aHint)
			except ValueError:
				# Oops its not, just keep moving
				pass
		
		# If there is only one hint then we might as well solve the tile
		if len(self.hints) == 1 and self.isSolved() == False:
			self.setFaceValue( self.hints[0] ) # Assume first hint value is last one
			self.setSolved( True ) # Set tile to solved
			self.setHints( [] ) # Empty list to clear hints
			print("Solved!")
			
	# This function is implemented for the conflict resolution algorithm
	# The idea is that you fill a random value to the Tile, and then try 
	# to reduce the number of board conflicts. It is important that a tile 
	# with a temporary value via randFill not be set to solved UNDER ANY
	# CIRCUMSTANCES. Is solved is reserved for original states, or definitive
	# values found through the hints. The board that contains these Tile objects
	# will make the executive decision on a solved board/tiles. 
	def randFill(self):
		"""Fill the faceValue with the best conflict hint value"""
		# Set best value as the first one
		currentFace = self.getFaceValue()
		bestConflicts = 99999
		bestFace = 0
		
		# Go through all the possible faceValues and check their conflicts
		for i in range(1, 10):
			if not i == currentFace:
				
				self.setFaceValue( i )
				
				if self.getConflicts() == bestConflicts:
					bestFace.append( i )
				elif self.getConflicts() < bestConflicts:
					bestFace = [i]
					bestConflicts = self.getConflicts()
					
				# Testing 
				print( str(i) + ":" + str(self.getConflicts()) + ":" + str(bestConflicts) )
				
		# Change to best value
		self.setFaceValue( bestFace[random.randint(0, len(bestFace) -1)] )
		
# Self Testing and Debugging
if __name__ == '__main__':
	# Tile without a Value
	print("Creating a tile without a FaceValue...")
	tile = Tile(5)
	tile.setSolved( False )
	tile.addConflicts( [1, 2, 3, 4, 5, 5, 5, 6, 7, 9, 1, 1, 9, 2, 8, 7] )
	
	print( "Tile's Conflicts: " + str(tile.getConflicts()) )
	print( tile.conflicts ) 
	print( tile.getFaceValue() ) 
	
	tile.randFill()
	
	print( "Tile's Conflicts: " + str(tile.getConflicts()) )
	print( tile.conflicts ) 
	print( tile.getFaceValue() ) 