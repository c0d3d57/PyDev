# Name: Identity.py
# Author: Super3(super3.org)

# Python Imports
import random

# My Imports 
import Names
from Helper import *

# Constants 
NONE = 0
MALE = 1
FEMALE = 2

class Identity(object):
	"""Create a Random Identity"""
	
	# Personal Information
	first = ""
	middle = ""
	last = ""
	
	age = 0
	birthday = 0
	gender = 0
	race = ""
	address = "" # US Based Only
	intrests = ""
	occupation = ""
	
	# Personal Information More 
	ssn = 0
	bloodtype = 0
	weight = 0
	height = 0
	
	# Digital Information
	handle = ""
	email = ""
	password = ""
	website = ""
	avatar = ""
	
	# Main Methods
	def __init__(self, gender, age_range):
		# Set Gender
		self.gender = gender
		# Set Name
		self.fullname = Names.Name(gender)
		self.first = self.fullname.first_name
		self.middle = self.fullname.middle_name
		self.last = self.fullname.last_name
		# Set Age
		self.age = random.randrange(age_range[0], age_range[1])
		# Set Password
		self.password = getRandVal(FiletoArray('data/passwords.txt'))
		# Set Website
		word1 = getRandVal(FiletoArray("data/dictionary.txt"))
		word2 = getRandVal(FiletoArray("data/dictionary.txt"))
		commonTLDS = ["com", "edu", "net", "org"]
		self.website = "http://" + word1 + word2 + "." + getRandVal(commonTLDS)
	def __str__(self):
		tmp = "---Personal Information---\n"
		tmp += "Name: " + str(self.fullname) + "\n"
		if self.gender == MALE:
			tmp += "Gender: MALE\n"
		else: # Assuming FEMALE
			tmp += "Gender: FEMALE\n"
		tmp += "Age: " + str(self.age) + "\n"
		tmp += "\n---Digital Information---\n"
		tmp += "Password: " + self.password + "\n"
		tmp += "Website: " + self.website
		return tmp
	
	# Other Methods
		
# Program Testing
if __name__ == "__main__":
    person = Identity(MALE, [18, 35])
    print(person)
