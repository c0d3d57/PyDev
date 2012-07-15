# File: main.py
# Author: Shawn Wilkinson

# Global Imports
import time
# My Imports
import FileHelper

# Welcome Message
print("Welcome to Sudoku-Solver.")

# -- Main --

# Create two 9 x 9 Boards
board = FileHelper.BoardFromFile('board.txt') # Fill from File
hints = [['' for col in range(9)] for row in range(9)]

# Fill Hints on Empty Spaces
for x in range(9):
    for y in range(9):
        if board[x][y] == 0:
            hints[x][y] = '123456789'

# Infinite Solving Loop
while 1:
    # Eliminate Horizontal Hint Duplicates
    for x in range(9):
        # Create an Empty List
        list = []
        # Get Values for That Row and Add to List
        for y in range(9):
            if board[x][y] != 0:
                list.append(board[x][y])
        # Loop through and remove that row from hints
        for y in range(9):
            for chr in list:
                hints[x][y] = hints[x][y].replace(str(chr),'')

    # Eliminate Vertical Hint Duplicates
    for x in range(9):
        # Create an Empty List
        list = []
        # Get Values for That Row and Add to List
        for y in range(9):
            if board[y][x] != 0:
                list.append(board[y][x])
        # Loop through and remove that row from hints
        for y in range(9):
            for chr in list:
                hints[y][x] = hints[y][x].replace(str(chr),'')
    
    # Sub-squares Function
    def subSquare(square):
        list = []
        if square == 0:
            for x in range(3):
                for y in range(3):
                    if board[y][x] != 0:
                        list.append(board[y][x])
                for y in range(3):
                    for chr in list:
                        hints[y][x] = hints[y][x].replace(str(chr),'')
        elif square == 1:
            for x in range(3,6):
                for y in range(3):
                    if board[y][x] != 0:
                        list.append(board[y][x])
                for y in range(3):
                    for chr in list:
                        hints[y][x] = hints[y][x].replace(str(chr),'')
        elif square == 2:
             for x in range(6,9):
                for y in range(3):
                    if board[y][x] != 0:
                        list.append(board[y][x])
                for y in range(3):
                    for chr in list:
                        hints[y][x] = hints[y][x].replace(str(chr),'')
        
        elif square == 3:
            for x in range(3):
                for y in range(3,6):
                    if board[y][x] != 0:
                        list.append(board[y][x])
                for y in range(3,6):
                    for chr in list:
                        hints[y][x] = hints[y][x].replace(str(chr),'')
        elif square == 4:
            for x in range(3,6):
                for y in range(3,6):
                    if board[y][x] != 0:
                        list.append(board[y][x])
                for y in range(3,6):
                    for chr in list:
                        hints[y][x] = hints[y][x].replace(str(chr),'')
        elif square == 5:
             for x in range(6,9):
                for y in range(3,6):
                    if board[y][x] != 0:
                        list.append(board[y][x])
                for y in range(3,6):
                    for chr in list:
                        hints[y][x] = hints[y][x].replace(str(chr),'')
                        
        elif square == 6:
            for x in range(3):
                for y in range(6,9):
                    if board[y][x] != 0:
                        list.append(board[y][x])
                for y in range(6,9):
                    for chr in list:
                        hints[y][x] = hints[y][x].replace(str(chr),'')
        elif square == 7:
            for x in range(3,6):
                for y in range(6,9):
                    if board[y][x] != 0:
                        list.append(board[y][x])
                for y in range(6,9):
                    for chr in list:
                        hints[y][x] = hints[y][x].replace(str(chr),'')
        elif square == 8:
             for x in range(6,9):
                for y in range(6,9):
                    if board[y][x] != 0:
                        list.append(board[y][x])
                for y in range(6,9):
                    for chr in list:
                        hints[y][x] = hints[y][x].replace(str(chr),'')
            

    # Eliminate Sub-squares Hint Duplicates
    for i in range(9):
        subSquare(i)

    # Solve Single Hints
    for x in range(9):
        for y in range(9):
            if len(hints[x][y]) == 1: 
                # Say Solved and Location
                print("Solved:", (x+1), ",", (y+1))
                # Set Hint to Board
                board[x][y] = int(hints[x][y])
                # Clear Hint
                hints[x][y] = ''

    # Check For a Solved Board
    exitLoop = True
    for x in range(9):
            for y in range(9):
                    # If a non-blank value is found then don't exit the loop
                    if board[x][y] != 0:
                            exitLoop = False
                    # else: exit loop
    if exitLoop:
            break # Break infinite while loop


    # Pause
    time.sleep(1)
    break

# Print Board and Hints
for row in board:
    print(row)
for row in hints:
    print(row)