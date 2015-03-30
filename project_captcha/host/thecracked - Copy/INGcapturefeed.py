def main():
	#from selenium import webdriver
	from PIL import Image
	from Naked.toolshed.shell import execute_rb

	import time
	import os
	import shutil
	import urllib
	import re
	file = open(os.path.join("C:\Users\admin\Desktop\project captcha\host", "captextt.txt"), 'r')
	link=file.read()
	data = re.split('"',link)
	urllib.urlretrieve(data[3], "crop.gif")
	
	


	execfile("exp2.py")		
	execfile("clean.py")
	execfile("floodfill.py")
	os.chdir('C:\Users\admin\Desktop\project captcha\host\thecracked - Copy\captcha2')
	execfile("svmtrain.py")
	#success = execute_rb('neural.rb')
	

	#driver.close()
