from bs4 import BeautifulSoup as bs
import requests


class Scraper:
    def __init__(self, headers):
        self.headers = headers

    def make_soup(self, page):
        r = requests.get(page, headers=self.headers)
        if r.status_code == 200:
            return bs(r.content, 'lxml')
        else:
            print("There was a problem while getting the html code!")

    def find_elems(self, soup, path):
        elems = soup.select(path)
        return elems