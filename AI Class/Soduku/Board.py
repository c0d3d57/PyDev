# Name: Board.py
# Author: Shawn Wilkinson

# Global Imports!
import random
import copy
import sys
# My Imports!
import FileHelper
from Tile import *


class Board():
	"""A Soduku Board Consisting of Tile Objects"""

	# -----------------------
	# ----- Constructor -----
	# -----------------------
	
	# Pre-condition: boardArr is a 9x9 matrix with integer values representing
	# 				 spots on the board
	# Post-condition: self.boardArr is has those same interger values now
	#				  assigned to Tile objects.
	def __init__(self, boardArr):
		# Elimiate magic ints with some class consants!
		# Specifies the size of the board in a 2D matrix
		self.SIZE = 9
		# Main Key - Board Array
		self.boardArr = [[ Tile(0) for col in range(self.SIZE)] for row in range(self.SIZE)]
		# Convert boardArr ints to self.boardArr Tile objects
		for x in range(self.SIZE):
			for y in range(self.SIZE):
				# Set Tile and Solved State If Not 0
				self.boardArr[x][y] = Tile( boardArr[x][y] )

	# -------------------------------
	# ----- Quick Solve Methods -----
	# -------------------------------
	
	def numEmpty(self):
		"""Returns the number of empty spaces"""
		spaces = 0
		for x in range(self.SIZE):
			for y in range(self.SIZE):
				if self.boardArr[x][y].getFaceValue() == 0:
					spaces += 1
		return spaces
	
	def horizontalSolve(self):
		"""Solves Tiles that have eight horizontal solid Tiles"""
		for x in range(self.SIZE):
			# Create an empty list
			tmpList = []
			
			# Get values for that row and add to list
			for y in range(self.SIZE):
				if self.boardArr[x][y].getFaceValue() != 0 and self.boardArr[x][y].isSolved() == True:
					tmpList.append( self.boardArr[x][y].getFaceValue() )
			# Loop back around and remove from hints
			for y in range(self.SIZE):
				self.boardArr[x][y].clearHints(tmpList)
				
	def verticalSolve(self):
		"""Solves Tiles that have eight vertical solid Tiles"""
		for y in range(self.SIZE):
			# Create an empty list
			tmpList = []
			
			# Get values for that row and add to list
			for x in range(self.SIZE):
				if self.boardArr[x][y].getFaceValue() != 0 and self.boardArr[x][y].isSolved() == True:
					tmpList.append( self.boardArr[x][y].getFaceValue() )
			
			# Loop back around and remove from hints
			for x in range(self.SIZE):
				self.boardArr[x][y].clearHints(tmpList)
		
	# -----------------------------------	
	# ----- Conflict Helper Methods -----
	# -----------------------------------
	
	def numConflicts(self):
		conflicts = 0
		for x in range(self.SIZE):
			for y in range(self.SIZE):
				if self.boardArr[x][y].isSolved() == False:
					conflicts += self.boardArr[x][y].getConflicts()
					print(self.boardArr[x][y].conflicts)
		return conflicts
		
	def clearConflicts(self):
		for x in range(self.SIZE):
			for y in range(self.SIZE):
				self.boardArr[x][y].clearConflicts()
	
	def horizontalConflictHelper(self):
		for x in range(self.SIZE):
			# Create an empty list
			tmpList = []
			
			# Get values for that row and add to list
			for y in range(self.SIZE):
				tmpList.append( self.boardArr[x][y].getFaceValue() )
					
			for y in range(self.SIZE):
				if self.boardArr[x][y].isSolved() == False:
					self.boardArr[x][y].addConflicts( tmpList )

	
	def verticalConflictHelper(self):
		for y in range(self.SIZE):
			# Create an empty list
			tmpList = []
			
			# Get values for that row and add to list
			for x in range(self.SIZE):
				tmpList.append( self.boardArr[x][y].getFaceValue() )
			
			for x in range(self.SIZE):
				if self.boardArr[x][y].isSolved() == False:
					self.boardArr[x][y].addConflicts( tmpList )
		
	def subSquareConflictHelper(self):
		"""Returns the number of subsquare conflicts in a board"""
		self.subSquareHelper(0,3,0,3)
		self.subSquareHelper(3,6,0,3)
		self.subSquareHelper(6,9,0,3)

		self.subSquareHelper(0,3,3,6)
		self.subSquareHelper(3,6,3,6)
		self.subSquareHelper(6,9,3,6)
		
		self.subSquareHelper(0,3,6,9)
		self.subSquareHelper(3,6,6,9)
		self.subSquareHelper(6,9,6,9)
		
	def subSquareHelper(self, x1, x2, y1, y2):
		"""Returns the number of subsquare conflicts in a board"""
		# Create an empty list
		tmpList = []
		# Other stuff
		for x in range(x1, x2):
			for y in range(y1, y2):
				tmpList.append( self.boardArr[x][y].getFaceValue() )
			if len(tmpList) == 9:
				print (tmpList)
			for y in range(y1, y2):
				if self.boardArr[x][y].isSolved() == False and len(tmpList) == 9:
					self.boardArr[x][y].addConflicts( tmpList )

	# -------------------	
	# ----- Methods -----
	# -------------------
	
	def fillBoard(self):
		"""Fill unsolved board spaces with valid values"""
		for x in range(self.SIZE):
			for y in range(self.SIZE):
				if self.boardArr[x][y].isSolved() == False:
					self.boardArr[x][y].setFaceValue( random.randint(1,9) )
		
	def resolveConflict(self):
		"""Resolve a single set of conflicts"""
			
		# Clear Board
		self.clearConflicts()	
		
		# Horizontal Conflicts
		self.horizontalConflictHelper()
		# Vertical Conflicts
		self.verticalConflictHelper()
		# Sub-Squares Conflicts
		self.subSquareConflictHelper()
		
		# Find a random unsolved value
		unsolved = []
		for y in range(self.SIZE):
			for x in range(self.SIZE):
				if self.boardArr[x][y].isSolved() == False:
					unsolved.append([x,y])
							
		num = random.randint(0, len(unsolved) -1)
		xy = unsolved[num]
		x = xy[0]
		y = xy[1]
					
		# Random New Value
		self.boardArr[x][y].randFill()
		
		# Print Out
		print("Attempted to change [" + str(x) + "," + str(y) + "]" + " of " + str(len(unsolved)) + " blanks to " + str(self.boardArr[x][y].getFaceValue()))
			
	# --------------------------	
	# ----- Special Method -----
	# --------------------------
	
	def __str__(self):
		"""Print out the board in a human readable format"""
		# Tmp string
		tmpStr = ""
		# Loop through board
		for x in range(self.SIZE):
			for y in range(self.SIZE):
				# Add FaceValue to tmpString
				tmpStr += str( self.boardArr[x][y].getFaceValue() ) + " "
				# Formatting
				if y%3 == 2:
					tmpStr += " "
			# Formatting
			# If !=8 to remove two extra newlines at bottom
			if x != 8:
				tmpStr += "\n"
			# Formatting
			if x%3 == 2 and x != 8:
				tmpStr += "\n"
		# Return tmp string
		return tmpStr
		
	# ----------------------
	# -----  Accessors -----
	# ----------------------
		
	def getBoard(self):
		"""Return the board array"""
		return self.boardArr
	

# Self Testing and Debugging
if __name__ == '__main__':
	# Create a Board from File
	print("Creating a Board...")
	board = Board( FileHelper.BoardFromFile('board.txt') )
	
	# Print Initial Board
	print("Initial Board...")
	print( str(board) + "\n\n" )
	
	# Main Operation - Quick Solve
	numEmpty = 10000 # Random High Value to Insure One Loop
	# If there are less empty spaces then before then loop again
	# if not then proceed with conflict resolution 
	#while numEmpty > board.numEmpty():
	#	numEmpty = board.numEmpty()
	#	board.horizontalSolve()
	#	board.verticalSolve()
	
	# Print Quicksolved Board
	print("Quicksolve Board...")
	print( str(board) + "\n\n" )
	
	# Fill Board Spaces 
	print("Filling Board Spaces...")
	board.fillBoard()
	
	# Print Filled Board
	print("Filled Board...")
	print( str(board) + "\n\n" )
	
	# Print Initial Conflicts
	print ( "Initial Conflicts: " + str(board.numConflicts()) )
		
	# Main Operator - First Conflict Resolution 
	board.resolveConflict()
	print ( "Current Conflicts: " + str(board.numConflicts()) )
	print( str(board) + "\n\n" )
	
	# Main Operation - Conflict Resolution 
	while board.numConflicts() > 0:
		board.resolveConflict()
		print ( "Current Conflicts: " + str(board.numConflicts()) )
		print( str(board) + "\n\n" )
		
	# Print Solved Board
	print("Solved Board...")
	print( board )