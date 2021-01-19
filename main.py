from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

WEB_ADDRESS = "http://www.everydayastronaut.com/upcoming-launches/"

def get_html(website):
    fp = Request(website, headers={"User-Agent": "Mozilla/5.0"})
    web_bytes = urlopen(fp).read()
    html = web_bytes.decode("utf8")
    return html

def load_html_into_bs4(html):
    return BeautifulSoup(html, "html.parser")

def get_html_and_load(website):
    html = get_html(website)
    return load_html_into_bs4(html)

def get_html_body_main(soup):
    return soup.body.main

def main(website=WEB_ADDRESS):
    soup = get_html_and_load(website)
    articles = get_html_body_main(soup).find_all("a", "cs-overlay-link")
    for article in articles:
        article_url = article.get('href')
        article_soup = get_html_and_load(article_url)
        table_rows = article_soup.find_all("tr")
        for tr in table_rows:
            print(tr.th.h6.get_text(), "\t", tr.td.get_text())
            print(tr.td.find_all("a"))
        break
    return articles




if __name__ == "__main__":
    main()