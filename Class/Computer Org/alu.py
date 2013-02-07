# Name: alu.py
# Author: Shawn Wilkinson
# Date: April 4, 2012

# ALU Functions
def addOp(a,b):
	print("Called Add Operation...")
	a = int(a, 2)
	b = int(b, 2)
	return bin(a+b)
	
def subOp(a, b):
	print("Called Subtract Operation...")
	a = int(a, 2)
	b = int(b, 2)
	return bin(a-b)
	
def andOp(a, b):
	print("Called And Operation...")
	a = int(a, 2)
	b = int(b, 2)
	return bin(a&b)

def orOp(a, b):
	print("Called Or Operation...")
	a = int(a, 2)
	b = int(b, 2)
	return bin(a|b)
	
def xorOp(a, b):
	print("Called Xor Operation...")
	a = int(a, 2)
	b = int(b, 2)
	return bin(a^b)
	
def norOp(a, b):
	print("Called Nor Operation...")
	a = int(a, 2)
	b = int(b, 2)
	tmp =  bin(a|b).replace('0', 'a')
	tmp = tmp.replace('1', '0')
	tmp = tmp.replace('a', '1')
	return tmp
	
# Main Program
if __name__ == "__main__":
	var1 = addOp('001', '001')
	var2 = subOp('001', '001')
	var3 = andOp('001', '001')
	var4 = orOp('101', '101')
	var5 = xorOp('001', '001')
	var6 = norOp('101', '101')
	print("Add:" + var1)
	print("Sub:" + var2)
	print("And:" + var3)
	print("Or:" + var4)
	print("Xor:" + var5)
	print("Nor:" + var6)