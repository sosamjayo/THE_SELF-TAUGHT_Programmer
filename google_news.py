import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site) -> None:
        self.site = site
    
    def print_url(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            print("\n" + url)
    
    def print_jslog(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            jslog = tag.get("jslog")
            if jslog is None:
                continue
            print("\n" + jslog)


news = "https://news.google.com/"
Scraper(news).print_url()
Scraper(news).print_jslog()

