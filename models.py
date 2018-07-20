class Tweet:
    def __init__ (self,tweet):
        self.id = tweet.id_str
        self.user = User(tweet.user.screen_name,tweet.user.followers_count,tweet.user.statuses_count,tweet.user.location)
        self.hashtags=tweet.entities["hashtags"]
        self.tweetText = tweet.full_text
        self.tweetDate = tweet.created_at
        self.retweetCount = tweet.retweet_count
        self.likes = tweet.favorite_count
        self.sentimento = 1
    
    def __str__(self):
        return self.tweetText

class User:
    def __init__(self,userName,usersFollowers,usersTweets,location):
        self.userName = userName
        self.usersFollowers = usersFollowers
        self.usersTweets = usersTweets
        self.location = location

    def __str__(self):
        return self.userName
