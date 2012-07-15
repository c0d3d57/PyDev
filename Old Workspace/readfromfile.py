# Read From File
file = open("test.txt")
for line in file:
		line = line.strip()
		print(line)
file.close()
# Keep Running
input()