from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())


def get_links(article_url):
    html = urlopen('https://en.wikipedia.org{}'.format(article_url))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = get_links('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = get_links(newArticle)


# Program not finished, check chap six of the scraper book to get the actual six degrees working.
