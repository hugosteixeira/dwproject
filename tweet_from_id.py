import tweepy
from models import Tweet
from utils import printError

class TweetFromID:
    auth = tweepy.OAuthHandler('jkwDvQkT5Es6S24JiLq2FLxrb', 'ju5ogpsqo3cQLxtgTurMgq7cmWt8CN2H9lQ0F5wGGrmegcvAMp')
    auth.set_access_token('89299395-PpehItyb3bnxSI3TEbve9Y8uDZKKOgaYiQinCCrvg', 'Rh8FHQk0Vd66LCZJIf20DrFzFZfmBZqqPLaAN3hXCmT3n')
    api = tweepy.API(auth)

    def getTweet(self, id):
        tweet = ''
        try:
            tweet =self.api.get_status(id,tweet_mode='extended')        
            tweet = Tweet(tweet,id)
        except:
            printError()
        return tweet