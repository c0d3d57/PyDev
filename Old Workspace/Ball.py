# Purpose: Testing Classes in Python
# Date: May 22, 2011
# Author: Shawn Wilkinson

#Imports
import pygame
import time

#Ball Class
class Ball():
	# --- Class Attributes ---
	# Ball Position
	x=0
	y=0
	
	# Ball's Vector
	changeX = 0
	changeY = 0
	
	# Ball Size
	size = 10
	
	# Ball Color
	color = [0,0,0]
	
	# --- Class Methods ---
	def move(self):
		self.x += self.changeX
		self.y += self.changeY
	
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

# Initialize the Game Engine
pygame.init()

# Set and Display Screen
size = [400, 400]
screen = pygame.display.set_mode(size)

# Define Colors
black = [0, 0 ,0]
white = [255, 255, 255]
blue = [ 0, 0 , 255]
green = [ 0, 255, 0]
red = [255, 0, 0]

# Set Window Title
pygame.display.set_caption("Python Ball Test")

# Loop until the users clicks the close button
done = False

#Create a timer used to control how often the screen updates
clock= pygame.time.Clock()

#Create a ball and set position
ball1 = Ball()
ball1.x = 100
ball1.y = 100
ball1.changeX = 2
ball1.changeY = 1

while done == False:
	#Limit updates on screen
	clock.tick(25)
	#Check for close event
	for event in pygame.event.get():
		 if event.type == pygame.QUIT:
		 	done = True
	#Clear the Screen
	screen.fill(white)
	#Animate Ball
	ball1.move()
	ball1.draw(screen)
	#Update Display
	pygame.display.flip()
	
#Exit Program
pygame.quit()
	
	