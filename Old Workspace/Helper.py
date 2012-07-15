# Name: Helper.py
# Author: Super3(super3.org)

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
	
def ArraytoFile(_array, filename):
	"""Converts a list to a .txt file"""
	file = open(filename+'.txt', 'w')
	for line in _array:
		file.write(line+"\n")
	file.close()
	
def getVal(aList):
	"""Returns a random value from a list"""
	return aList[random.randrange(len(aList))]