import tweepy
from models import Tweet
from utils import printError

class TweetFromID:
    auth = tweepy.OAuthHandler('Consumer Key (API Key)', 'Consumer Secret (API Secret)')
    auth.set_access_token('Access Token', 'Access Token Secret')
    api = tweepy.API(auth)

    def getTweet(self, id):
        tweet = ''
        try:
            tweet =self.api.get_status(id,tweet_mode='extended')        
            tweet = Tweet(tweet,id)
        except:
            printError()
        return tweet