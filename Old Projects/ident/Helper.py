# Name: Helper.py
# Author: Super3(super3.org)

import random

def FiletoArray(filename):
	"""Converts a .txt file to list"""
	try:
		tmp = [] 
		file = open(filename)
	except: 
		print("Error Reading File:",filename)
	else:
		for line in file:
				line = line.strip()
				line = line.lower()
				tmp.append(line)
		file.close()
	return tmp
	
def ArraytoFile(array, filename):
	"""Converts a list to a .txt file"""
	file = open(filename+'.txt', 'w')
	for line in array:
		file.write(line+"\n")
	file.close()
	
def getRandVal(aList):
	"""Returns a random value from a list"""
	return aList[random.randrange(len(aList))]