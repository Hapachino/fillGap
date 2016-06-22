#! python3
# fillGap.py - finds all files with given prefix in folder and locates gaps in numbering and fills the gap

import os, re, shutil

# Arguments: folder, prefix
def fillGap(folder, prefix):

	# Create regex with prefix + number + extension     
	prefixRegex = re.compile(r'(%s)(\d)+(\.[a-zA-Z0-9]+)' % prefix)

  	# Make sure folder path is absolute
  	folder = os.path.abspath(folder)

  	# Create list with all files that match regex
	fileList = []
  	for item in os.listdir(folder):
  		if os.path.isfile(os.path.join(folder, item)) and prefixRegex.search(item):
      			fileList.append(item)

  	# Look for the starting number by incrementing, starting from 0
	Number = 0  
	while True:
  		for filename in fileList:
		mo = prefixRegex.search(filename)
			if Number == int(mo.group(2)):
				fileList.remove(filename)
				Completed = True
		  		break
		Number += 1
		if Completed == True:
  			break

  	# Increment from starting number, finding next largest file and renaming
	nextNumber = Number
  	while True:
  		for filename in fileList:
			mo = prefixRegex.search(filename)
			if nextNumber == int(mo.group(2)):
				# New number including prefixed zero's
				subNumber = '0' * (len(mo.group(2)) - len(Number)) + str(number)
				newFileName = prefixRegex.sub(r'\1%s\3' % subNumber, filename)
				shutil.move(os.path.join(folder, filename), os.path.join(folder, newFileName))
				fileList.remove(filename)
				Number += 1
		if len(fileList) == 0:
			break	
		nextNumber += 1
