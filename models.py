from format_place import FormatPlace
class Tweet:
    def __init__ (self,status):
        self.id = status.id_str

        self.user = User(status.user.screen_name,status.user.followers_count,status.user.statuses_count,FormatPlace(status.user.location).localizationAddress())
        self.hashtags = status.entities["hashtags"]
        self.tweetText = status.full_text
        self.tweetDate = status.created_at
        self.retweetCount = status.retweet_count
        self.likes = status.favorite_count
        self.sentimento = 1
        self.candidato = ''
    
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
