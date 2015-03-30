from PIL import Image
from operator import itemgetter
import os
import shutil
xcount=0
for l in range(0,2):
		im3 = Image.open("output"+str(xcount)+".gif")
		im3 = im3.convert("P")	
		im4 = Image.new("P",im3.size,255)
		for x in range(0,im3.size[1]):
			 for y in range(0,im3.size[0]):
				try:
					a=x+1
					b=y+1
					c=x-1
					d=y-1
					pix1=im3.getpixel((y,a))
					pix2=im3.getpixel((b,x))
					pix3=im3.getpixel((d,x))
					pix4=im3.getpixel((y,c))
					pix5=im3.getpixel((y,x))
					if (pix1==255 and pix2==255 and pix3==255 and pix4==255):
						im3.putpixel((y,x),255)
					if ( pix2==255 and pix3==255 and pix4==255):
						im3.putpixel((y,x),255)
					if (pix1==255  and pix3==255 and pix4==255):
						im3.putpixel((y,x),255)
					if (pix1==255 and pix2==255 and pix4==255):
						im3.putpixel((y,x),255)
					if (pix1==255 and pix2==255 and pix3==255):
						im3.putpixel((y,x),255)
					if (pix2==255 and pix3==255 and pix1==0 and pix4==0):
						im3.putpixel((y,x),255)
					if (pix1==255 and pix4==255 and pix2==0 and pix3==0):
						im3.putpixel((y,x),255)
				
				except:
						im3.putpixel((y,x),255)
						continue
						
					

					
			
im3.save("clean"+str(xcount)+".gif")