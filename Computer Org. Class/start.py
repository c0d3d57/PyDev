# Name: Start.py
# Author: Shawn Wilkinson
# Date: April 3, 2012

# System Imports
import time
import sys

# My Imports
from alu import *

# Data
binary = ""

# Fake Startup Message Display Code
def displayMsg(msg):
	sys.stdout.write(" " + msg + "... ")
	sys.stdout.flush()
	time.sleep(.5)
	print("Done!")
	
# Add to a List of Fake Startup Messages
startMsg = []
startMsg.append("Powering Up System")
startMsg.append("Clearing Register File")
startMsg.append("Initializing Program Counter")
startMsg.append("Testing Memory")
startMsg.append("Sending Start Instruction")

# Boot Screem
print("----- MIPS OS 1.0 ----------------------")
for msg in startMsg:
	displayMsg(msg)
print(" Ready for Operation...")
print(" Waiting for Instructions...")
print("----------------------------------------\n")

# Register Files
reg = ['00000' for col in range(32)]
mem = ['00000' for col in range(64000)]
pc = 0

# Preload Register Values
preset = True
while preset:
	sys.stdout.write("Pre-set Register Value(Y/N)?...")
	contin = input("")
	if contin == 'N' or contin == 'n':
		preset = False
	else:
		index = int(input("Register Location: "))
		value = str(input("Register Value: "))
		reg[index] = value
# Clear Some Space
print()

# Menu
while True:
	# Get Hex Instruction From User
	hexd = input("Hex Instruction: ")
	# Convert Hex To Binary and Clip Non-Needed Chars
	for i in range(len(hexd)):
		binary += str(bin(int(hexd[i], 16))[2:]).zfill(4)
	# Chop Off The OP Code
	opCode = binary[0:6]
	# Convert Op Code to Int
	opCode = int(opCode, 2)
	
	# Debug Print OP Code
	print("\nGetting OP Code: " + str(opCode))
	print("Binary: " + binary)
	
	# Compare OP Code Values
	# Then Call Needed Function w/ Operands
	if opCode == 0:
		# Get Operands from Instruction
		print("Op Code is 0")
		rs = int(binary[6:11], 2)
		rt = int(binary[11:16], 2)
		rd = int(binary[16:21], 2)
		shift = binary[21:26]
		funct = int(binary[26:32], 2)
		
		# ALU Statements
		# ADD
		if funct == 32:
			reg[rd] = addOp(reg[rs], reg[rt])[2:]
		# SUB
		elif funct == 34:
			# Have to check for negative here
			tmp = subOp(reg[rs], reg[rt])
			if subOp(reg[rs], reg[rt])[:1] == '-':
				reg[rd] = tmp[3:]
			else:
				reg[rd] = tmp[2:]
			print("Sub:" + subOp(reg[rs], reg[rt]))
		# AND
		elif funct == 41:
			reg[rd] = andOp(reg[rs], reg[rt])[2:]	
		# OR
		elif funct == 37:
			reg[rd] = orOp(reg[rs], reg[rt])[2:]
		# XOR
		elif funct == 38:
			reg[rd] = xorOp(reg[rs], reg[rt])[2:]
		# NOR
		elif funct == 39:
			reg[rd] = norOp(reg[rs], reg[rt])[2:]
		
		# Print Operation Value and Destination
		print("Bin Value " + str(reg[rd]) + " stored in register " + str(rd))
		print("Int Value " + str(int(reg[rd],2)) + " stored in register " + str(rd))
		
		# Debug Statements
		#print("OP:" +  opCode)
		#print("RS:" +  rs)
		#print("RT:" +  rt)
		#print("RD:" +  rd)
		#print("Shift:" +  shift)
		#print("Funct:" +  str(funct))
		print("")
	elif opCode == 8:
		print("Op Code is 8")
		print("Called Addi Operation...")
		rs = int(binary[6:11], 2) 
		rt = int(binary[11:16] ,2) # Destination Reg
		immediate = int(binary[16:32], 2) # Constant
		reg[rt] = str( bin( int(reg[rs] ) + immediate ) )
		
		# Print Operation Value and Destination
		print("Value " + str(int(reg[rt], 2)) + " stored in register " + str(rt))
	elif opCode == 35:
		print("Op Code is 35")
		print("Called LW Operation...")
		
		rs = int(binary[6:11], 2) 
		rt = int(binary[11:16],2)
		immediate = int(binary[16:32], 2)
		
		reg[rt] = mem[ rs + immediate ]
		# Print Operation Value and Destination
		print("Bin Value " + str(mem[ rs + immediate ]) + " stored in register " + str(rt))
		print("Int Value " + str(int(mem[ rs + immediate ],2)) + " stored in register " + str(rt))
	elif opCode == 43:
		print("Op Code is 43")
		print("Called SW Operation...")
		
		rs = int(binary[6:11], 2)
		rt = int(binary[11:16],2)
		immediate = int(binary[16:32], 2)
		
		mem[ rs + immediate ] = reg[rt]
		# Print Operation Value and Destination
		print("Bin Value " + str(reg[rt]) + " stored in memory " + str(rs + immediate))
		print("Int Value " + str(int(reg[rt],2)) + " stored in memory " +  str(rs + immediate))
	elif opCode == 2:
		print("Op Code 2")	
		print("Called J Operation...")
		pc = int(binary[6:32], 2) 
		print("Program Counter is now " + str(pc))
	elif opCode == 4:
		print("Op Code is 4")
		print("Called BEQ Operation...")
		rs = int(binary[6:11], 2)
		rt = int(binary[11:16],2)
		immediate = int(binary[16:32], 2)
		
		if reg[rs] == reg[rt]:
			pc = pc + 4 + immediate
		print("Program Counter is now " + str(pc))
	elif opCode == 5:
		print("Op Code is 5")
		print("Called BNE Operation...")
		rs = int(binary[6:11], 2)
		rt = int(binary[11:16],2)
		immediate = int(binary[16:32], 2)
		
		if reg[rs] != reg[rt]:
			pc = pc + 4 + immediate
		print("Program Counter is now " + str(pc))
	else:
		print("Invalid OPCode")
	
	# Clear Binary Var
	binary = ""