__author__ = 'Skanda'
import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    url_set = set([])
    links_count = 0
    global url_frontier
    page=1
    while page <= max_pages:
            url = url_frontier[0]
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text)
            for link in soup.findAll('a'):
                href = link.get('href')
                if href not in url_frontier:
                    url_frontier.append(href)
                url_set.add(href)
            page += 1
            del url_frontier[0]
    print('links count = ', len(url_set))
    print('url_set : ')
    for u in url_set:
        print(u)


seed_url='http://www.msrit.edu/computer-science-and-engineering/'
url_frontier = []
url_frontier.append(seed_url)


spider(4)
