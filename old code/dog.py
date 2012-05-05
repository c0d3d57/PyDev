# Purpose: Testing Classes in Python
# Date: May 22, 2011
# Author: Shawn Wilkinson

class Dog():
	name = ""
	weight = 0
	age = 0

	def bark(self):
		print(self.name, "says \"Woof\"")
	
#Create and Use Object	
dog1 = Dog()
dog1.name = "Meeko"
dog1.age = 7
dog1.weight = 15
dog1.bark()
input()