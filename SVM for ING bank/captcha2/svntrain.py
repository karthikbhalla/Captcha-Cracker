from PIL import Image
from operator import itemgetter
import os
import shutil
import math
class VectorCompare:
  def magnitude(self,concordance):
    total = 0
    for word,count in concordance.iteritems():
      total += count ** 2
    return math.sqrt(total)

  def relation(self,concordance1, concordance2):
    relevance = 0
    topvalue = 0
    for word, count in concordance1.iteritems():
      if concordance2.has_key(word):
        topvalue += count * concordance2[word]
    return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))



def buildvector(im):
  d1 = {}

  count = 0
  for i in im.getdata():
    d1[count] = i
    count += 1

  return d1
  
v = VectorCompare()


iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


imageset = []

for letter in iconset:
  for img in os.listdir('./iconset/%s/'%(letter)):
    temp = []
    if img != "Thumbs.db": # windows check...
      temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
    imageset.append({letter:temp})

xcountx=482
for z in range(0,15):	
	guess = []	
	im4 = Image.open("letter"+str(xcountx)+".gif")	
	for image in imageset:
		for x,y in image.iteritems():
		  if len(y) != 0:
			guess.append( ( v.relation(y[0],buildvector(im4)),x) )

		guess.sort(reverse=True)
	print "",guess[0]

	xcountx += 1			
