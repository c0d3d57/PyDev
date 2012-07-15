# File: FileHelper.py
# Author: Shawn Wilkinson

# Load a Board from .txt to a 9x9 Board.
def BoardFromFile(boardFile):
	# Create a 9 x 9 Boards of Zeroes
	board = [[0 for col in range(9)] for row in range(9)]

	# Open File
	f = open(boardFile, 'r')
	
	# Fill Board From File
	for x in range(9):
		for y in range(9):
			# Select Next Character
			char = f.read(1)
			# Eliminate Spaces and Newlines
			# Then Add to Board As Int
			if char == " " or char == '\n':
				board[x][y] = int(f.read(1))
			else:
				board[x][y] = int(char)
	
	return board

# Self Testing and Debugging
if __name__ == '__main__':
	# Load File
	myBoard = BoardFromFile('board.txt')
	# Print Board
	for row in myBoard:
	    print(row)