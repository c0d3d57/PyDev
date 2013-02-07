# Name: Main.py
# Author: Shawn Wilkinson

# Imports 
from random import choice

# Welcome Message
print("Welcome to the Isolation Game!")

# Make Board
board = [['' for col in range(4)] for row in range(4)]

# Print Board Functin
def show():
	# Tmp string
	tmpStr = ""
	# Loop through board
	tmpStr += "\nBoard:"
	tmpStr += "\n-------------------------\n"
	for x in range(4):
		for y in range(4):
			if board[x][y] == '':
				tmpStr += " |"
			else:
				tmpStr += str( board[x][y] ) + "|"
		tmpStr += "\n-------------------------\n"
	# Return tmp string
	print(tmpStr)

# Select Vars
player = ''
ai = ''
isXO = ''
firstPlay = ''
playBool = False

# Loop For XO State
while 1:
	isXO = str(input("Am I 'x' or 'o'? "))
	if isXO == 'x':
		ai = 'x'
		player = 'o'
		break
	elif isXO == 'o':
		ai = 'o'
		player = 'x'
		break
	else:
		print("Invalid choice. Try again.")

# Loop For First State		
while 1:
	firstPlay = input("Do I got first ('y' or 'n')? ")
	if firstPlay == 'y':
		playBool = True
		break
	elif firstPlay == 'n':
		playBool = False
		break
	else:
		print("Invalid choice. Try again.")
		
# Start and Show Board
board[0][0] = 'x'
board[3][3] = 'o'
show()
	
# Move Functions
def aiMove():
	# Possible Moves
	possMoves = []
	# Find Loc
	for x in range(4):
		for y in range(4):
			if board[x][y] == ai:
				locX = int(x)
				locY = int(y)
				
	# Horizontal
	for x in range(-4, 5):
		if (locX + x) < 4 and (locX + x) >= 0:
			if board[locX + x][locY] == "#" or board[locX + x][locY] == player:
				break
			if board[locX + x][locY] == '':
				possMoves.append( [locX + x, locY] )
	
	# Vertical
	for y in range(-4, 5):
		if (locY + y) < 4 and (locY + y) >= 0:
			if board[locX][locY + y] == "#" or board[locX][locY + y] == player:
				break
			if board[locX][locY + y] == '':
				possMoves.append( [locX, locY + y] )
				
	# Diagonal
	for dia in range(-4, 5):
		if (locY + dia) < 4 and (locY + dia) >= 0:
			if (locX + dia) < 4 and (locX + dia) >= 0:
				if board[locX + dia][locY + + dia] == "#" or board[locX + dia][locY + dia] == player:
				    break
				if board[locX + dia][locY + dia] == '':
					possMoves.append( [locX + dia, locY + dia] )
				
	# Possible Moves Len
	print("Possible Moves: " + str(len(possMoves)))
	if(len(possMoves) == 0):
		print("Gave Over!")
	move = choice(possMoves)
	print(move)
	moveX = move[0]
	moveY = move[1]
	print("Move Choice" + str(moveX) + ":" + str(moveY))
	board[moveX][moveY] = ai
	
	# Clear Old Space
	board[locX][locY] = '#'
def playerMove(PosX, PosY):
	for x in range(4):
		for y in range(4):
			if board[x][y] == player:
				board[x][y] = '#'
	board[PosX][PosY] = player
	
# Game Loop
while 1:
	if playBool == True:
		aiMove()
		playBool = False
	else:
		x = int(input("Enter Player X:"))
		y = int(input("Enter Player Y:"))
		playerMove(x, y)
		playBool = True
	show()