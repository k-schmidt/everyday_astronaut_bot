from .config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET_KEY,
)

import tweepy

class Twitter:

    def __init__(self):
        auth = tweepy.OAuthHandler(
                CONSUMER_KEY,
                CONSUMER_SECRET
        )
        auth.set_access_token(
                ACCESS_KEY,
                ACCESS_SECRET_KEY,
        )
        self.api = tweepy.API(auth)


    def send_tweet(self, message):
        self.api.update_status(message)