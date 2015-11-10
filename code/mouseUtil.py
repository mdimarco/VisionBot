from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap


import sys
import time

#Mouse event handler
def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(
                    None, 
                    type, 
                    (posx,posy), 
                    kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

#Moves mouse instantly
def mouseMove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);

#Mouse click instantly
def mouseClick(posx,posy):
        # uncomment this line if you want to force the mouse 
        # to MOVE to the click location first (I found it was not necessary).
        #mouseEvent(kCGEventMouseMoved, posx,posy);
        mouseEvent(kCGEventLeftMouseDown, posx,posy);
        mouseEvent(kCGEventLeftMouseUp, posx,posy);

#Generates a path from a start location to end location
def getpath(start, end):
    if(start < end):
        return range(start, end)
    else:
        return range(start, end, -1)

#Moves the mouse in a (more) human way
def mouseMoveHuman(startx, starty, endx, endy):
    #For now just does linear movement
    xPath = getpath(startx, endx)
    yPath = getpath(starty, endy)
    #Move x
    for x in xPath:
        mouseMove(x,starty)
        time.sleep(0.5/len(xPath))
    #Move y
    for y in yPath:
        mouseMove(xPath[-1], y)
        time.sleep(0.5/len(yPath))

