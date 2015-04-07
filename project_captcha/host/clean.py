from PIL import Image
from operator import itemgetter
import os
import shutil
xcount=0
for l in range(0,1):
	for r in range(0,2):
		im3 = Image.open("C:\\Users\\Prasanth\\Desktop\\project_captcha\\host\\output"+str(xcount)+".gif")
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
					pix6=im3.getpixel((y+1,x+1))
					pix7=im3.getpixel((y,x-1))
					pix8=im3.getpixel((y+1,x-1))
					pix9=im3.getpixel((y+2,x))
					pix10=im3.getpixel((y+2,x+1))
					pix11=im3.getpixel((y+1,x+2))
					pix12=im3.getpixel((y,x+2))
					pix13=im3.getpixel((y-1,x+1))
					pix14=im3.getpixel((y-1,x))
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
					if(pix5==0 and pix6==0 and pix1==0 and pix2==0 and pix7==255 and pix8==255 and pix9==255 and pix10==255 and pix11==255 and pix12==255 and pix13==255 and pix14==255 ):
						im3.putpixel((y,x),255)
						im3.putpixel((y,x+1),255)
						im3.putpixel((y+1,x),255)
						im3.putpixel((y+1,x+1),255)
				
				except:
						im3.putpixel((y,x),255)
						continue
							
		im3.save("C:\\Users\\Prasanth\\Desktop\\project_captcha\\host\\output"+str(xcount)+".gif")
		#print 'done cleaning'
		#xcount=xcount+1
#print 'finally done'