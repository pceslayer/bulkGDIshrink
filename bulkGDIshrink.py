import os,glob,fnmatch
from gditools import gdishrink

#Function to create directories
def makedir(make):
	if not os.path.exists(make):
		try:
			os.mkdir(make)
		except OSError:  
			print ("Creation of the directory %s failed" % make)
		else:  
			print ("Successfully created the directory %s " % make)
	
#Get current working directory
path = os.getcwd()

#Set external output directory
shrinkpath = path+'shrank' #Comment out to specify external output drive/directory
#shrinkpath = 'F:\\shrank' #Uncomment to specify external output drive & directory

makedir(shrinkpath)

matches = []
for root, dirnames, filenames in os.walk(path):
    for filename in fnmatch.filter(filenames, '*.gdi'):
        matches.append(os.path.join(root, filename))
	for match in matches:
		drive, folder = os.path.splitdrive(match)
		folder, filename = os.path.split(folder)
	makedir(shrinkpath+folder)
	gdishrink(match, shrinkpath+folder)
