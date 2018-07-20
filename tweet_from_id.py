import tweepy
class Tweet:
    def __init__ (self,tweet):
        self.hashtags=tweet.entities["hashtags"]
        self.nomeUsuario = tweet.user.screen_name
        self.location = tweet.user.location
        self.followersUsuario = tweet.user.followers_count
        self.totalTweetsUsuario = tweet.user.statuses_count
        self.textoTweet = tweet.full_text
        self.tweetDate = tweet.created_at
        self.retweetCount = tweet.retweet_count
        self.likes = tweet.favorite_count
    
    def __str__(self):
        return self.textoTweet



class TweetFromID:
    auth = tweepy.OAuthHandler('jkwDvQkT5Es6S24JiLq2FLxrb', 'ju5ogpsqo3cQLxtgTurMgq7cmWt8CN2H9lQ0F5wGGrmegcvAMp')
    auth.set_access_token('89299395-PpehItyb3bnxSI3TEbve9Y8uDZKKOgaYiQinCCrvg', 'Rh8FHQk0Vd66LCZJIf20DrFzFZfmBZqqPLaAN3hXCmT3n')
    api = tweepy.API(auth)

    def getTweet(self, id):
        tweet = Tweet(self.api.get_status(id,tweet_mode='extended'))
        return tweet