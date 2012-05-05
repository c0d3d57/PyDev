#Part1
for i in range(10):
	line = ""
	for j in range(10):
		if (i-j) > 0:
			line += str((i-j)) + " "
		else:
			line += "  "
	temp = line[2: len(line)]
	temp = temp[::-1]
	line = temp + " " + line
	print(line)
	
#Part 1
for x1 in range(9, 1, -1):
	line2 = ""
	for x2 in range(1,x1):
		line2 += str(x2) +  " "
	for space in range(10-x1):
		line2 = "  " + line2
	temp2 = line[0: (len(line2)-2)]
	temp2 = temp2[::-1]
	line2 = line2 + " " + temp
	print(line2)