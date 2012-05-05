# Sorting an Integer Array with Binary Search
# Should work in Python 3.1
# Author: Shawn Wilkinson

# This is the Integer Array
intArr = [2, 5, 6, 9, 11, 16, 34, 54, 65, 72, 80, 99, 101]

# The sort function
def sort(theArray, findThis): 
	minVal = 0
	maxVal = len(theArray)
	while minVal <= maxVal:
		midVal = int((minVal + maxVal) / 2)
		if findThis > theArray[midVal]:
			minVal = midVal + 1
		elif findThis <  theArray[midVal]:
			maxVal = midVal - 1
		else:
			return midVal
	#If nothing is found
	return -1 
	
# Use and output function
output = sort(intArr, 9)
print("The index location is",output)