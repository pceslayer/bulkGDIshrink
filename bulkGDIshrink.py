import os,glob,fnmatch
from gditools import gdishrink

def makedir(make):
	if not os.path.exists(make):
		try:
			os.mkdir(make)
		except OSError:  
			print ("Creation of the directory %s failed" % make)
		else:  
			print ("Successfully created the directory %s " % make)
	
path = os.getcwd()

# define the name of the gdishrank directory to be created
shrink = path+'shrank'

makedir(shrink)

matches = []
for root, dirnames, filenames in os.walk(path):
    for filename in fnmatch.filter(filenames, '*.gdi'):
        matches.append(os.path.join(root, filename))
	for match in matches:
		drive, folder = os.path.splitdrive(match)
		folder, filename = os.path.split(folder)
	makedir(shrink+folder)
	gdishrink(match, shrink+folder)
