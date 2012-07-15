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
	file = open('sort1.txt', 'w')
	for line in _array:
		file.write(line+"\n")
	file.close()

global names
names = []

def addme(aName):
	count = 0
	for i in names:
		if i == aName:
			return False
	names.append(aName)
	return True

test = FiletoArray("getmydata.txt")
for i in test:
	i = i.lower()
	start = i.find("@")
	end = i.find(".", start, len(i))
	print(addme(i[start+1:end]))
names.sort()
ArraytoFile(names)
	

	