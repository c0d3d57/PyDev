# Author: Shawn Wilkinson (super3.org)
# Date: 6-5-11

# Factors that make the data seem artifical
# Addresses consisting of large amounts of numbers or start with numbers
# Addresses that seem very long

# ---- Imports ----
import random
import string
from sys import argv

# ---- Set Globals ----

global commonEmailProviders
global allTLDS, commonTLDS, commonTLDSx
global dictionary, shortWords, fnames, lnames
global keywords

# ---- Set Simplify Functions ----
def FiletoArray(_file):
	"""Converts a .txt file to list"""
	tmp = []
	file = open(_file)
	for line in file:
			line = line.strip()
			line = line.lower()
			tmp.append(line)
	file.close()
	return tmp
	
def ArraytoFile(_array):
	"""Converts a list to a .txt file"""
	file = open('test.txt', 'w')
	for line in _array:
		file.write(line+"\n")
	file.close()
	
def getVal(aList):
	"""Returns a random value from a list"""
	return aList[random.randrange(len(aList))]

# ---- Data Section ----

# Fill Domain+ Vars
commonEmailProviders = ["hotmail.com", "msn.com", "aol.com", "yahoo.com", "gmail.com", "comcast.net"]
dictionary = FiletoArray("data/dictionary.txt")

# Fill TLD Vars
commonTLDS = ["com", "edu", "net", "org"]
commonTLDSx = commonTLDS + ["biz", "info", "mobi", "jobs", "name", "tel", "gov", "mil"]
allTLDS = FiletoArray("data/tlds.txt")

# Fill Username Vars
fnames =  FiletoArray("data/fnames.txt")
lnames = FiletoArray("data/lnames.txt")
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# Take all words from dictionary 6 letters or less
shortWords = []
for i in dictionary:
	if len(i) <= 6:
		shortWords.append(i)
keywords = ["FIRST", "LAST", "SHORTWORD", "INITIAL", "INITIALS", "NUM1", "NUM2", "NUM3", "NUM4"]

# ---- Domain Function Section ----
def giveTLD(arg): 
	"""Returns a TLD"""
	# Arg(0) for common TLDS
	# Arg(1) for extended common TLDS
	# Arg(2 and other) for all TLDS
	if arg == 0:
		return getVal(commonTLDS)
	elif arg == 1:
		return getVal(commonTLDSx)
	else:
		return getVal(allTLDS)
		
def giveDomain(arg):
	"""Returns a Domain"""
	# Arg(0) for common email providers
	# Arg(1 and other) for a word
	if arg == 0:
		return getVal(commonEmailProviders)
	else:
		return getVal(dictionary)
		
def giveNum(arg):
	"""Returns a random number. Argument is number of digits."""
	range_start = 10**(arg-1)
	range_end = (10**arg)-1
	return random.randrange(range_start, range_end)
	
def giveUser(arg):
	"""Returns random username in the requested format"""
	# Keywords: FIRST LAST SHORTWORD INITIAL INITIALS NUM1 NUM2 NUM3 NUM4
	user = ""	
	for i in arg:
		if i == "FIRST":
			user += getVal(fnames)
		elif i == "LAST":
			user += getVal(lnames)
		elif i == "SHORTWORD":
			user += getVal(shortWords)
		elif i == "INITIAL":
			user += getVal(abc)
		elif i == "INITIALS":
			user += getVal(abc) + getVal(abc)
		elif i == "NUM1" or i == "NUM2" or i == "NUM3" or "NUM4":
			index = int(i[3])
			user += str(giveNum(index))
		#elif i == "DOT":
			#user += "."
	return user

# ---- Email Testing ----

# Blank List to Hold Emails
emailList = []

# Generate Emails and Add to List
for i in range(2000):
	myList = []
	for x in range(3):
		myList.append(getVal(keywords)) 
	#print(myList)
	email = giveUser(myList) + "@" + giveDomain(0)
	emailList.append(email)
	print(email)
	
# Sort Alphabetically and Add to File
emailList.sort()	
ArraytoFile(emailList)

# Keep Running
input()