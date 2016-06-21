#! python3
# fillGap.py - finds all files with given prefix
# in folder and locates gaps in numbering and fills the gap


import os, re, shutil

# arguments: folder, prefix
def fillGap(folder, prefix):

  # Create regex with prefix + number + extension
  prefixRegex = re.compile(r'(%s)(\d)+(\.[a-z0-9]+)' % prefix)

  # Make sure folder path is absolute
  folder = os.path.abspath(folder)

  # create list with all files
  fileList = []
  for match in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, match)):
      fileList.append(match)

  # Remove files that do not match prefixRegex    # Unnecessary?
  for filename in fileList:
    if not prefixRegex.search(filename):
      fileList.remove(filename)

  # find match with lowest number and remove from list, and store number as variable
  for filename in fileList:
      
  

  # sort all files from low to high

  # rename files to increment after first match


    


