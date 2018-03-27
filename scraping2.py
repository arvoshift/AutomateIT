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

