import tweepy


auth = tweepy.OAuthHandler('jkwDvQkT5Es6S24JiLq2FLxrb', 'ju5ogpsqo3cQLxtgTurMgq7cmWt8CN2H9lQ0F5wGGrmegcvAMp')
auth.set_access_token('89299395-PpehItyb3bnxSI3TEbve9Y8uDZKKOgaYiQinCCrvg', 'Rh8FHQk0Vd66LCZJIf20DrFzFZfmBZqqPLaAN3hXCmT3n')



api = tweepy.API(auth)

public_tweets = api.home_timeline()


for tweet in tweepy.Cursor(api.search,q="#pratodagalera",count=100,since="2010-04-03").items():
    print (tweet.created_at, tweet.text+'\n')
