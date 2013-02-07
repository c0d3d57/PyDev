#!/usr/bin/env python
# Filename: notebook.py
# Project Github: http://github.com/super3/ClassDev
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# --- Imports ---
import re
from datetime import datetime

# --- Globals ---
supportedPages = ['WRITING', 'DRAWING', 'PICTURE']

# --- Classes ---
class Page:
	"""
	A single page of a notebook. Is abtract.

	Data members:
	pageNumber -- Passed paged order in the notebook
	format -- Tells tells how to render the text data
	text -- Contains the unrendered text data

	"""

	# Main
	def __init__(self, pageNumber, format):
		"""Try to create a page object."""
		# Cast the Data
		pageNumber = int(pageNumber)
		format = str(format)

		# Make Sure Passed Values are Logical
		if pageNumber < 1:
			raise ValueError('Invalid Page Number.')
		if not self.isInList(supportedPages, format):
			raise ValueError('Invalid Page Format.')

		# Inserting Checked Values to Object
		self.pageNumber = pageNumber
		self.format = format
		self.text = ""

	# Accessors / Mutators
	def getPageNumber(self):
		return pageNumber
	def setPageNumber(self, pageNumber):
		if pageNumber < 1:
			raise ValueError('Invalid Page Number.')
		self.pageNumber = pageNumber
	def setText(self, text):
		self.text = text
	def getText(self):
		return self.text

	# Helper
	def isInList(self, searchList, targetItem):
		"""Helper function. Returns true if item is in list."""
		for item in searchList:
			if str(item) == str(targetItem):
				return True
		return False

class Notebook:
	"""
	A notebook, which contains multiple pages of notes.

	Data members:
	title -- Text title 
	dateCreated -- Date of the creation
	dateModified -- Date of the last modification
	pageList -- Contains a list of ordered pages

	"""

	# Main
	def __init__(self, title):
		"""Try to create a notebook object."""
		# Cast the Data
		title = str(title)

		# Make Sure Passed Values Fit Format Rules
		if not re.match('^[a-zA-Z0-9_]+$', title): 
			raise ValueError('Title is not Alphanumeric.') 

		# Inserting Checked Values to Object
		self.title = title
		self.dateCreated = datetime.now()
		self.dateModified = datetime.now()
		pageList = []

	# Pages
	def addPage(self, format):
		"""Add a page of the specified format to the notebook."""
		try:
			self.pageList.append(Page(self.numPages()+1, format))
		except ValueError:
			print("Unable to add page.")
	def numPages(self):
		"""Returns number of pages in the notebook."""
		return len(pageList)
	def removePage(self, pageNum):
		"""Removed the specified page number from the notebook."""
		if numPages >= 1:
			for page in self.pageList:
				if page.getPageNumber() == pageNum:
					self.pageList.remove(page)

# Unit Testing
if __name__ == '__main__':
	note = Notebook('TestNoteBook1')