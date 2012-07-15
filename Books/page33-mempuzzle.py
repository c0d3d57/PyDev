# Memory Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified" BSD license

# Imports
import sys, random, pygame
from pygame.locals import *

# Settings
FPS = 30 # frames per second, the general speed of the prograan 
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 40 # size of box height & width in pixels
GAPSIZE = 10 # size of grap between boxes in pixels
BOARDWIDTH = 10 # number of colums of icons
BOARDHEIGHT = 7 # number of rows of icons
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * BOXSIZE + GAPSIZE)) / 2 )
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE + GAPSIZE)) / 2 )

#			  R    G    B
GRAY      = (100, 100, 100)
NAVYBLUE  = ( 60,  60, 100)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
ORANGE    = (255, 128,   0)
PURPLE    = (255,   0, 255)
CYAN      = (  0, 255, 255)

# More Colors
BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

# Constants to Strings
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

# More Stuff
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, 'Board is too big for stuff def.'

# Main Game Method
def main():
		# Start Up PyGame
		global FPSCLOCK, DISPLAYSURF
		pygame.init()
		FPSCLOCK = pygame.time.Clock()
		DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

		# Mouse Cords
		mousex = 0
		mousey = 0

		# Set Window Caption
		pygame.display.set_caption('Memory Game')

		# Board and Boxes
		mainBoard = getRandomizedBoard()
		revealBoxes = generateRevealBoxesData(False)

		# Store the (x,y) for the first box clicked
		firstSelection = None

		# Start Up Board
		DISPLAYSURF.fill(BGCOLOR)
		startGameAnimation(mainBoard)

		# Main Game Loop
		while True:
			mouseClick = False

			# Drawing the Windowd
			DISPLAYSURF.fill(BGCOLOR)
			drawBoard(mainBoard, revealBoxes)

			# Event Handling Loop
			for event in pygame.event.get():
					if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
						pygame.quit()
						sys.exit()
					elif event.type == MOUSEMOTION:
							mousex, mousey = event.pos
					elif event.type == MOUSEBUTTONUP:
							mousex, mousey = event.pos
							mouseClicked = True
					boxx, boxy = getBoxAtPixel(mousex, mousey)