# Name: Convert.py
# Author: Shawn Wilkinson

# Imports
import binascii

# Welcome Message
print("Welcome to the Hex and Binary Converter.")

# Vars
sent = True
option = 0

# Main Loop
while sent:
	# Menu
	print("---Menu Options---")
	print("1. Convert Hex to Binary")
	print("2. Convert Binary to Hex")
	print("3. Exit")
	
	# Get Input
	option = int(input("Please enter a number:"))
	
	# Check values
	if option == 1:
		hexd = input("Enter hex value:")
		binary = str(bin(int(hexd, 16))[2:])
		print("Binary Value: " + binary)
	elif option == 2:
		binary = input("Enter binary value:")
		hexd = hex(int(binary, 2))[2:]
		print("Hex Value: " + hexd)
	elif option == 3:
		print("Bye!")
		sent = False
	else:
		print("Invalid option. Try again.")