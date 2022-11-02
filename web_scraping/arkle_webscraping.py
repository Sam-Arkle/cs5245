# Sam Arkle
# Website accessed: https://roysviewfrom.com (roy collects views of fans whose teams are about to play/have played Sheffield United)
# Base page for item page: https://roysviewfrom.com/category/pre-match/page/
# The above base page can be accessed for as many pages as desired. Currently set to just first page.
# Each 'pre-match' page will have roughly 10 links which specify 10 different games:
# Pages currently accessed with default of 1 'base' page accessed:
# https://roysviewfrom.com/2022/10/18/pre-match-view-from-coventry-8/
# https://roysviewfrom.com/2022/10/21/pre-match-view-from-norwich-6/
# https://roysviewfrom.com/2022/10/14/pre-match-view-from-blackpool-5/
# https://roysviewfrom.com/2022/10/07/pre-math-view-from-stoke/
# https://roysviewfrom.com/2022/10/04/pre-match-view-from-qpr-6/
# etc (see generated events.jl for full list)

# Attributes scraped: The above urls which are stored as events which specify which match was played and the date it occurred
# From the above page the comments are scraped. The majority of the comments are from rival fans. On a minority of pages there are also comments from fans of Sheffield United.
# I have scraped beyond the initial requirements. I have used a reg ex(to guarantee the links acquired are those desired). I have set the program so it will not allow for duplicates and can run through 100-odd pages on the website.
import json
import re
from time import sleep
from urllib.request import urlopen
from protego import Protego
import requests
from bs4 import BeautifulSoup


class Event:
    def __init__(self, event_url):
        self.url = event_url
        self.match = event_url.split('from-')[-1]
        self.date = event_url.split('/')[-5: -2]


class Comment:
    def __init__(self, comment_url, text):
        self.url = comment_url
        self.text = text
        # self.position = position


def robot_parser(robot_url='https://roysviewfrom.com/robots.txt'):
    firefox_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
    headers = {'User-Agent': firefox_agent}
    response = requests.get(robot_url, headers=headers)
    parsed_response = Protego.parse(response.text)
    return parsed_response


# As code is currently set, not every page from the pre-match category is collected. This is because
# some pages are collections from various teams. This would muddy the eventual data set and so is not included.
def get_events(event_url='https://roysviewfrom.com/category/pre-match/page/'):
    rp = robot_parser()
    extant_url = set()
    newly_found_url = set()
    event_list = []

    try:
        with open('events.jl', 'r') as file:
            for line in file:
                data = json.loads(line)
                extant_url.add(data["url"])
    except FileNotFoundError as e:
        print('events.jl not found, will be created')

    for page in range(1, 2):
        if rp.can_fetch((event_url + str(page)), '*'):
            firefox_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
            headers = {'User-Agent': firefox_agent}
            html = requests.get((event_url + str(page)), headers=headers).content
            bs = BeautifulSoup(html, 'html.parser')
            # Adding a default delay as non-specified in robots.txt
            sleep(1)
            for link in bs.find_all('a', href=re.compile("[0-9]/pre-")):
                if link.attrs['href'] not in extant_url:
                    event_object = Event(link.attrs['href'])
                    event_list.append(event_object.__dict__)
                    with open('events.jl', 'a') as file:
                        if event_object.url not in newly_found_url:
                            s = json.dumps(event_object.__dict__)
                            file.write(s + '\n')
                            newly_found_url.add(event_object.url)

        else:
            print(f'Parser suggests your agent cannot access {event_url}{page}')
    for event in newly_found_url:
        extant_url.add(event)
    if len(event_list) != 0:
        print('Newly created events: ')
        print(event_list)
    return extant_url


def get_comments(comment_url, list_for_print):
    rp = robot_parser()
    if rp.can_fetch(comment_url, '*'):
        firefox_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
        headers = {'User-Agent': firefox_agent}
        html = requests.get(comment_url, headers=headers).content
        # Again, default delay of one
        sleep(1)
        bs = BeautifulSoup(html, 'html.parser')
        all_results = (bs.select('blockquote.wp-block-quote'))
        if len(all_results) == 0:
            all_results = bs.find_all('p')
        existing_urls = set()
        try:
            with open('comments.jl', 'r') as file:
                for line in file:
                    data = json.loads(line)
                    existing_urls.add(data["url"])
        except FileNotFoundError:
            print('comments.jl not found, will be created')
        with open('comments.jl', 'a') as file:
            if comment_url not in existing_urls:
                comment = Comment(comment_url, str(all_results))
                file.write(json.dumps(comment.__dict__) + '\n')
                list_for_print.append(comment.__dict__)

    else:
        print(f'Parser suggests your agent cannot access {comment_url}')


urls = get_events()
comment_list = []
for url in urls:
    get_comments(url, comment_list)

if len(comment_list) != 0:
    print('Newly created comments:')
    print(comment_list)
