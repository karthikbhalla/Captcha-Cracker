from PIL import Image
from operator import itemgetter
import os
import shutil
import sys

sys.setrecursionlimit(10000)
finalx=0
finaly=0

def floodfill(x, y, oldColor, newColor):
    # assume surface is a 2D image and surface[x][y] is the color at x, y.

	pix=im2.getpixel((y,x))
	if (pix!= oldColor):
		global finalx
		finalx=x
		global finaly
		finaly=y
		return
	im2.putpixel((y,x),newColor)

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
xcount=2
im2=Image.open("outputcrop15.gif")
for y in range(im2.size[0]):
	if flag==1:
		floodfill(xcord,ycord,0,255)
		flag=0
		if xcount>1:
			im2.save("exp"+str(xcount)+".gif")
			xcount=xcount-1
	for x in range(im2.size[1]):
		pix = im2.getpixel((y,x))
		if pix!=255:
			xcord=x
			ycord=y
			flag=1
			break
			
im2=Image.open("outputcrop15.gif")
for y in range(finaly,im2.size[0]):
	if flag==1:
		floodfill(xcord,ycord,0,255)
		flag=0
		im2.save("exp"+str(xcount)+".gif")
		print finalx
		print finaly
		xcount=xcount+1
	for x in range(finalx,im2.size[1]):
		pix = im2.getpixel((y,x))
		if pix!=255:
			xcord=x
			ycord=y
			flag=1
			break
			



