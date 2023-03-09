from html.parser import HTMLParser
from urllib import parse
import requests
from bs4 import BeautifulSoup
r = requests.get('www.w3schools.com/')
soup = BeautifulSoup(r.content, 'html.parser')

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
        parse.para = set()
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
                                
    def page_links(self):
        return self.links
        
    def error(self, message):
        pass