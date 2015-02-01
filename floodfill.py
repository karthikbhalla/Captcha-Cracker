from PIL import Image
from operator import itemgetter
import os
import shutil
import sys

sys.setrecursionlimit(10000)
im2=Image.open("outputcrop15.gif")

def floodfill(x, y, oldColor, newColor):
    # assume surface is a 2D image and surface[x][y] is the color at x, y.
	pix=im2.getpixel((y,x))
	if (pix!= oldColor):
		return
	im2.putpixel((y,x),newColor)
	print 'hi'
	try:
		floodfill(x + 1, y, oldColor, newColor) # right
		floodfill(x - 1, y, oldColor, newColor) # left
		floodfill(x, y + 1, oldColor, newColor) # down
		floodfill(x, y - 1, oldColor, newColor)
	except:
		return
	
flag=0	
xcord=0
ycord=0
for y in range(im2.size[0]):
	if flag==1:
		break
	for x in range(im2.size[1]):
		pix = im2.getpixel((y,x))
		if pix!=255:
			xcord=x
			ycord=y
			flag=1
			break
			
floodfill(xcord,ycord,0,255)
im2.save("exp.gif")

