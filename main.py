from html_utils.HtmlParser import HtmlParser
from launch.Launch import Launch
from twitter.Twitter import Twitter

WEB_ADDRESS = "http://www.everydayastronaut.com/upcoming-launches/"

def main(website=WEB_ADDRESS):
    soup = HtmlParser.get_html_and_load(website)
    articles = HtmlParser.get_html_body_main(soup).find_all("a", "cs-overlay-link")
    for article in articles:
        article_url = article.get('href')
        launch = Launch(article_url)
        message = launch.form_message()
        twitter = Twitter()
        twitter.send_tweet(message)
        break
    return articles

if __name__ == "__main__":
    main()