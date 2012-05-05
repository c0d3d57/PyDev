# Name: ReadFile.py
# Author: Super3(super3.org)
# Source: Zed A. Shaw(http://learnpythonthehardway.org)

from sys import argv
script, filename = argv

txt = open(filename)
print("Here's your file:",filename)
print(txt.read())
txt.close()

