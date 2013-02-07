# Shawn Wilkison
# November 26, 2012

# Valid Literals
data = [ '3', '13.', '.328', '41.16', '+45.80' '+0', '-01', '-14.4',
'1e12', '+1.4e6', '-2.e+7', '01E-06', '-.4E-7', '00e0']

# Regular Expression Functions
def reg1(char):
	return char == '+' or char == '-' or reg2(char)

def reg2(char):
	return char.isdigit()

def reg3(char):
	return char == '.' or reg2(char)

def reg4(char):
	return char == 'e' or char == 'E' or reg1(char)

# Regular Expression Tester Class
class RegTester:
	def __init__(self, lit):
		"""
		Data members:
		lit -- The string to be tested
		litLen -- The length of the tested string
		seek -- Current tested character

		Methods:
		check1-check4 -- Tests regular expression, and then moves the seeker forward
		checkEnd -- See if the seeker is at the end of the string
		run -- Does expressions linearly (1232412)
		"""
		self.lit = lit
		self.litLen = len(lit)
		self.seek = 0
	def check1(self):
		if reg1(self.lit[self.seek]):
			self.seek += 1
			return True
		return False
	def check2(self):
		if reg2(self.lit[self.seek]):
			self.seek += 1
			while(self.seek < self.litLen):
				if reg2(self.lit[self.seek]):
					self.seek += 1
				else: 
					break
		else:
			return False
		return True
	def check3(self):
		if reg3(self.lit[self.seek]):
			self.seek += 1
			return True
		return False
	def check4(self):
		if reg4(self.lit[self.seek]):
			self.seek += 1
			return True
		return False

	def checkEnd(self):
		return self.seek >= self.litLen

	def run(self):
		if not self.checkEnd():
			return self.check1() 

		if not self.checkEnd():
			return self.check2()

		if not self.checkEnd():
			return self.check3()

		if not self.checkEnd():
			return self.check2()

		if not self.checkEnd():
			return self.check4()

		if not self.checkEnd():
			return self.check1()

		if not self.checkEnd():
			return self.check2()

		return False			 

# Unit Tests
for i in data:
	test = RegTester(i)
	print(i + " : " + str(test.run()))