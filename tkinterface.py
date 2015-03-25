#!/usr/bin/python

import Tkinter
from Tkinter import *

class App:
	def __init__(self,master):
		master.minsize(width=250, height=250)
	
top = Tkinter.Tk()

def sbicrack():
   execfile("SBIcapturefeed.py")
   
def ingcrack():
   execfile("INGcapturefeed.py")

 
app = App(top)  
SBI = Tkinter.Button(top, text ="Invoke SBI Cracker", command = sbicrack)
ING = Tkinter.Button(top, text ="Invoke ING Cracker", command = ingcrack)
titlevar = StringVar()
creditsvar=StringVar()
title = Label(top, textvariable=titlevar, relief=RAISED )
credits= Label(top, textvariable=creditsvar, relief=RAISED )

titlevar.set("Welcome to CAPTCHA cracker!")
creditsvar.set("Project work done by:Prasanth Louis, Yedukrishnan AV, and Karthik Bhalla")
title.pack()
SBI.pack()
ING.pack()
credits.pack()
top.mainloop()
