import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site) -> None:
        self.site = site
    
    def sp(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        return sp
    
    def print_url(self):
        for tag in self.sp().find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            print("\n" + url)

    def read_news(self):
        with open("google_news.txt", "w") as file:
            for tag in self.sp().find_all("a"):
                text = tag.text
                file.write("\n" + text)


url = "https://news.google.com/topstories?hl=ja&gl=JP&ceid=JP:ja"
Scraper(url).read_news()

