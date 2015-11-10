
import pyscreenshot as ImageGrab
import numpy as np
# Takes a screenshot based on the specified
# parameters (start location and end location)
#Example: getScreen(10,10,500,500)
def getScreen(starti,startj,endi,endj):
	#Take screenshot
	return ImageGrab.grab( bbox=(starti,startj,endi,endj) )
	


#Converts a screen returned by getScreen
#into a 3-D numpy array.
#
# The numpy array will be m*n*3, with each
# of the 3 corresponding to Red, Green, or Blue 
# 
#
def screenToPix(imScreen):
	#Create pixels array
	pixels = np.ndarray( shape=(imScreen.height,imScreen.width,3), dtype=np.uint8 )
	for row in xrange(imScreen.height):
		for col in xrange(imScreen.width):
			#color is R,G,B,A format, only retrieving R,G,B
			for color in xrange(3):
				pixels[row,col,color] = imScreen.getpixel( (col,row) )[color]
	return pixels





#Takes in a grayscale m*n matrix and divides
#it into multiple slices of size "size"
#
#return		slices: sliced arrays (size x size)
#			startLocs: starting locations of slices
def divideScreenshot(screenGray, size):
	#Split into multiple nxn slices
	slices = []
	startLocs = []
	rows = screenGray.shape[0]
	cols = screenGray.shape[1]

	rowStarts = range(0,rows,size)
	colStarts = range(0,cols,size)

	for rowStart in rowStarts:
		rowEnd = rowStart+size
		for colStart in colStarts:
			colEnd = colStart+size
			slices.append( screenGray[ rowStart:rowEnd, colStart:colEnd ] )
			startLocs.append( (rowStart, colStart) )
	return slices,startLocs