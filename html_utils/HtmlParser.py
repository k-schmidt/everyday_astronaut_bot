from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

class HtmlParser:

    @staticmethod
    def get_html(website):
        fp = Request(website, headers={"User-Agent": "Mozilla/5.0"})
        web_bytes = urlopen(fp).read()
        html = web_bytes.decode("utf8")
        return html

    @staticmethod
    def load_html_into_bs4(html):
        return BeautifulSoup(html, "html.parser")

    @classmethod
    def get_html_and_load(cls, website):
        html = cls.get_html(website)
        return cls.load_html_into_bs4(html)

    @staticmethod
    def get_html_body_main(soup):
        return soup.body.main