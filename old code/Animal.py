# Purpose: Testing Classes in Python
# Date: May 22, 2011
# Author: Shawn Wilkinson

class Animal():
	def __init__(self):
		print("An animal has been born!")
	def eat(self):
		print("Munch munch munch...")
	def makeNoise(self):
		print("Grrr...")
		
class Cat(Animal):
	def makeNoise(self):
		print("Meow")
	
class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("A dog has been born!")
		
	def makeNoise(self):
		print("Bark")
		
#Animal
pet1 = Animal()
pet1.eat()
pet1.makeNoise()

#Cat
pet2 = Cat()
pet2.eat()
pet2.makeNoise()

#Dog
pet3 = Dog()
pet3.eat()
pet3.makeNoise()

input()