import bs4
myfile = open('python.html')
soup = bs4.BeautifulSoup(myfile, "lxml")
#Making the soup
print("BeautifulSoup Object:", type(soup))

# Find Elements by tags
print(soup.find_all('a'))
print(soup.find_all('strong'))
# Find Elements by id
print(soup.find('div', {"id": "inventor"}))

print(soup.select('#inventor'))
#find elements by css print
print(soup.select('.wow'))

from lxml import html
import requests

# EOF
print("Facebook URL:", soup.find_all('a')[0]['href'])
print("Inventor:", soup.find('div', {"id": "inventor"}).text)
print("Span content:", soup.select('span')[0].getText())

