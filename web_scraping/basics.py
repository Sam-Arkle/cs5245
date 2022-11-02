from urllib.request import urlopen
from bs4 import BeautifulSoup

html1 = urlopen('https://www.bbc.com/news')
html2 = urlopen('http://www.pythonscraping.com/pages/page1.html')
html3 = urlopen('https://roysviewfrom.com/')
bs = BeautifulSoup(html3.read(), 'html.parser')
namelist = bs.find_all('span', {'class': 'Pre-Match'})
for name in namelist:
    print(name.getText)
print(bs)