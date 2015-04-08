#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# A simple native messaging host. Shows a Tkinter dialog with incoming messages
# that also allows to send message back to the webapp.
import time
import struct
import sys
import threading
import subprocess
from subprocess import Popen
import Queue
from tkFileDialog import askopenfile, asksaveasfile

try:
  import Tkinter
  import tkMessageBox
except ImportError:
  Tkinter = None

# On Windows, the default I/O mode is O_TEXT. Set this to O_BINARY
# to avoid unwanted modifications of the input/output streams.
if sys.platform == "win32":
  import os, msvcrt
  msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
  msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

# Helper function that sends a message to the webapp.
def send_message(message):
   # Write message size.
  sys.stdout.write(struct.pack('I', len(message)))
  # Write the message itself.
  sys.stdout.write(message)
  sys.stdout.flush()

# Thread that reads messages from the webapp.
def process_again():
	#print 'hi'
	execfile('C:\\Users\\Prasanth\\Desktop\\project_captcha\\host\\exp2.py')
	p = Popen("C:\\Users\\Prasanth\\Desktop\\project_captcha\\host\\install.bat",creationflags=subprocess.CREATE_NEW_CONSOLE)
	#stdout, stderr = p.communicate()
	
	
def process():
	threadxyz = threading.Thread(target=process_again, args=())
	threadxyz.start()
	
def read_thread_func(queue):
  message_number = 0
  while 1:
    # Read the message length (first 4 bytes).
    text_length_bytes = sys.stdin.read(4)

    if len(text_length_bytes) == 0:
      if queue:
        queue.put(None)
      #sys.exit(0)

    # Unpack message length as 4 byte integer.
    text_length = struct.unpack('i', text_length_bytes)[0]

    # Read the text (JSON object) of the message.
    text = sys.stdin.read(text_length).decode('utf-8')

    if queue:
      queue.put(text)
    else:
      # In headless mode just send an echo message back.
      send_message('{"echo": %s}' % text)

if Tkinter:
  class NativeMessagingWindow(Tkinter.Frame):
    def __init__(self, queue):
      self.queue = queue

      Tkinter.Frame.__init__(self)
      self.pack()

      self.text = Tkinter.Text(self)
      self.text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
      self.text.config(state=Tkinter.DISABLED, height=10, width=40)

      self.messageContent = Tkinter.StringVar()
      self.sendEntry = Tkinter.Entry(self, textvariable=self.messageContent)
      self.sendEntry.grid(row=1, column=0, padx=10, pady=10)

      self.sendButton = Tkinter.Button(self, text="Send", command=self.onSend)
      self.sendButton.grid(row=1, column=1, padx=10, pady=10)
	  
      self.processButton = Tkinter.Button(self, text="Process", command=process)
      self.processButton.grid(row=1, column=2, padx=10, pady=10)

      self.after(100, self.processMessages)

    def processMessages(self):
      while not self.queue.empty():
        message = self.queue.get_nowait()
        if message == None:
          self.quit()
          return
        self.log("Received %s" % message)
        f=open("C:\\Users\\Prasanth\\Desktop\\project_captcha\\host\\write.txt",'w')
        f.write(message)
        f.close()
        process()
        time.delay(5)
        onSend(self)
        
		#f = asksaveasfile(mode='w', defaultextension=".txt", initialfile="write.txt", initialdir="C:\\Users\\Prasanth\\Desktop\\projectcapftcha\\host")
        #if not f:
		#	return
        #f.write(message)
        #f.close()
        

      self.after(100, self.processMessages)

    def onSend(self):
      
      #f = askopenfile(mode='r', defaultextension=".txt", initialfile="captext.txt", initialdir="C:\\Users\\Prasanth\\Desktop\\project_captcha\\host\\captcha2")
	  f2=open('C:\\Users\\Prasanth\\Desktop\\project_captcha\\host\\captcha2\\captext.txt','r')
	  for line in f2:
	   m=line
	  m=m.rstrip('\n')
	  f2.close()
	  text = '{"text": "' + m + '"}'
      #text = '{"text": "' + "hello" + '"}'
	  self.log('Sending %s' % text)
	  try:
	   send_message(text)
	  except IOError:
	   tkMessageBox.showinfo('Native Messaging Example','Failed to send message.')
	   #sys.exit(1)
	  self.log('Sending worked %s' % text)

    def log(self, message):
      self.text.config(state=Tkinter.NORMAL)
      self.text.insert(Tkinter.END, message + "\n")
      self.text.config(state=Tkinter.DISABLED)


def Main():
  if not Tkinter:
    send_message('"Tkinter python module wasn\'t found. Running in headless ' +
                 'mode. Please consider installing Tkinter."')
    read_thread_func(None)
    #sys.exit(0)

  queue = Queue.Queue()

  main_window = NativeMessagingWindow(queue)
  main_window.master.title('Native Messaging Example')

  thread = threading.Thread(target=read_thread_func, args=(queue,))
  thread.daemon = True
  thread.start()

  main_window.mainloop()

  #sys.exit(0)


if __name__ == '__main__':
  Main()
