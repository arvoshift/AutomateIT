import os
import re
import urllib
import urllib.request

from bs4 import BeautifulSoup



##Download Parameters
image_type = "Project"
movie = "Avatar"
url = "https://www.google.com/search?q="+movie+"&source=lnms&tbm=isch"


header = {'User-Agent': 'Mozilla/5.0'}
#soup = BeautifulSoup(urllib.urlopen(urllib.Request(url, headers=header)))
soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url, headers=header)), "lxml")

images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})][:5]
for img in images:
	print("image source: ", images)

for img in images:
	raw_img = urllib.request.urlopen(img).read()
	cntr = len([i for i in os.listdir(".") if image_type in i]) + 1
	f = open(image_type + "_"+ str(cntr)+".jpg", 'wb')
	f.write(raw_img)
	f.close()

