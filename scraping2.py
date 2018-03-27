import os
import re
import urllib3

from bs4 import BeautifulSoup



##Download Parameters
image_type = "Project"
movie = "Avatar"
url = "https://www.google.com/search?q="+movie+"&source=lnms&tbm=isch"
