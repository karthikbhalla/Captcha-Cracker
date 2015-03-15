from selenium import webdriver
from PIL import Image
from Naked.toolshed.shell import execute_rb

import time
import os
import shutil
count=0
def find():
	for x in elems:
		for y in ids:
			for z in values:
				if x.get_attribute(y).lower().find(z)!=-1:
					global count
					driver.save_screenshot('screenshot.gif')
					im = Image.open("screenshot.gif")
					width=int(x.get_attribute("width"))
					height=int(x.get_attribute("height"))
					yaxis=x.location['y']
					xaxis=x.location['x']
					bbox = (xaxis,yaxis,xaxis+width,yaxis+height)
					img=im.crop(bbox)
					
					img.save("crop"+str(count)+".gif")
					destinationDir='C:\\Users\\Prasanth\\Desktop\\comb\\Captcha-Cracker-master\\thecracked - Copy'
					if not os.path.exists(destinationDir): 
						os.makedirs(destinationDir)
					#shutil.move("crop"+str(count)+".gif", destinationDir)
					count=count+1
					return


driver = webdriver.Firefox()
driver.get("https://online.ingvysyabank.com/netbanking/BANKAWAY?Action.ING.forgotpwd.Main=Y&AppSignonBankId=IVBL&AppType=corporate&CorporateSignonLangId=001&vFlg=Y&startTran=Y")
for tab in range(0,1):
	elems=driver.find_elements_by_tag_name("img");
	values=['captchaimage','captcha','cap']
	ids=['id','alt','src','class']
	find()
	#driver.refresh()
	time.sleep(2)


execfile("exp2.py")		
execfile("clean.py")
execfile("floodfill.py")
os.chdir('C:\\Users\\Prasanth\\Desktop\\comb\\Captcha-Cracker-master\\thecracked - Copy\\captcha2')
execfile("svmtrain.py")
#success = execute_rb('neural.rb')
box=driver.find_element_by_name('RetailForgotPwdCAPTCHA')
f = open('captext.txt', 'r')
textstring=f.read()
box.send_keys(textstring)

#driver.close()
