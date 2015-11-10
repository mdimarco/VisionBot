

from mouseUtil import mouseClick
from mouseUtil import mouseMoveHuman
from screenshotUtil import getScreen
from screenshotUtil import screenToPix
from screenshotUtil import divideScreenshot
from skimage.viewer import ImageViewer
from skimage.color import rgb2gray




#Take/Format Screen Shot
screen = getScreen(100,100,1000,1500)
screenAsArr = screenToPix(screen)
screenGray = rgb2gray(screenAsArr)

#Divide up screenshot
slices, startLocs = divideScreenshot(screenGray, 100)


# TODO - Passing slices through developed cv model
# while( True )
#   getAndFormatScreenshot
#   getSlices
#   for each slice
#		if hasTree( slice )
#			moveToAndClick( middle of slice )
#			break
#	if treeFound
#		wait a little bit
#	else
#		move/rotate a bit


##############################
# UNCOMMENT TO VIEW SOME SLICES
##############################
for x in range(25,min(35, len(slices))):
	viewer = ImageViewer( slices[x])
	viewer.show()


##############################
# UNCOMMENT TO VIEW COLOR IMAGE
##############################
#viewer = ImageViewer( screenAsArr )
#viewer.show()



##############################
# UNCOMMENT TO VIEW MOUSE MOVEMENT
##############################
# mouseMoveHuman(100,300, 300, 400)
# mouseMoveHuman(300,400, 500, 200)