# Name: Names.py
# Author: Super3(super3.org)
# Data URL: http://www.outpost9.com/files/WordLists.html
# Data Used: Male and Female Name Lists

# Imports
from Helper import *

# Constants 
MALE = 1
FEMALE = 2

# Load Word Lists
male_first_names = FiletoArray('data/names_english_male.txt')
female_first_names = FiletoArray('data/names_english_female.txt')
#abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
last_names = FiletoArray('data/names_english_last.txt')

# Class Definiton
class Name(object):
	# Class Vars
	first_name = ""
	middle_name = ""
	last_name = ""
	format = []
	
	# Load Random Data into Name
	def __init__(self, gender, format = ["FIRST", "MIDDLEI", "LAST"]):
		if gender == MALE:
			self.first_name = getRandVal(male_first_names)
			self.middle_name = getRandVal(male_first_names)
		else: # Assuming FEMALE
			self.first_name = getRandVal(female_first_names)
			self.middle_name = getRandVal(female_first_names)
		self.last_name = getRandVal(last_names)
		# Set String Method Format
		self.format = format
		# Optional Capitalization
		self.cap()
		
	# Get Initial 
	def getInitial(self, string, period = True):
		if period == True:
			return string[0] + "."
		else:
			return string[0]
		
	# Set String Method Format
	def setFormat(self, arg):
		self.format = arg
	
	# Capitalize
	def cap(self):
		"""docstring for cap"""
		self.first_name = self.first_name.capitalize()
		self.middle_name = self.middle_name.capitalize()
		self.last_name = self.last_name.capitalize()
	
	# String Method (Returns Default or Specified Format)
	# Arguments: FIRST FIRSTI MIDDLE MIDDLEI LAST LASTI
	def __str__(self):
		tmp = ""
		for i in self.format:
			if i == "FIRST":
				tmp += self.first_name
			elif i == "FIRSTI":
				tmp += self.getInitial(self.first_name)
			elif i == "MIDDLE":
				tmp += self.middle_name
			elif i == "MIDDLEI":
				tmp += self.getInitial(self.middle_name)
			elif i == "LAST":
				tmp += self.last_name
			elif i == "LASTI":
				tmp += self.getInitial(self.last_name)
			tmp += " "
		tmp.strip()
		return tmp

# Program Testing
if __name__ == "__main__":
    person = Name(MALE)
    print(person)
