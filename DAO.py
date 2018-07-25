from utils import tratarValuesDao, printError,tratarColumnsDao
import pymysql.cursors
from DB_helper import DB_helper
from models import Tweet,User
from tweet_from_id import TweetFromID

class Dao:
    def __init__(self):
        self.dbHelper = DB_helper()
        self.cursor = self.dbHelper.getCursor()

    def insert(self, table,columns,values):
        try:
            columns = tratarColumnsDao(columns)
            values = tratarValuesDao(values)
            valor="INSERT INTO {}({}) VALUES ('{}')".format(table,columns,values)
            self.cursor.execute(valor)
            self.dbHelper.conn.commit()
            return self.cursor.lastrowid
        except:
            printError()

    def select(self, columns, table, whereArg=''):
        try:
            if whereArg != '':
                selectWhere='SELECT {} FROM {} WHERE {};'.format(columns,table,whereArg)
                self.cursor.execute(selectWhere)
                result = self.cursor.fetchall()
                
            else:
                self.cursor.execute('SELECT {} FROM {};'.format(columns,table))
                result = self.cursor.fetchall()
            return result
        except:
            printError()



    def insertTweet(self,tweet):    
        try:
            userId = self.insertUser(tweet.user)
            hashtagsIds = self.insertHashtags(tweet.hashtags)
            table = 'Tweet'
            columns = ['Texto','Data','Retweets','Likes','Usuario_idUsuario','idTweetOrigem','Lugar']
            values = [tweet.tweetText,tweet.tweetDate,tweet.retweetCount,tweet.likes,userId,tweet.id,tweet.user.location]
            selectWhere=self.select('*',table,"idTweetOrigem = '"+tweet.id+"'")
            if selectWhere == ():
                tweetId = self.insert(table,columns,values)
            else:
                tweetId = selectWhere[0]
            return tweetId
        except:
            printError()

    def insertUser(self,user):
        try:
            table = 'Usuario'
            columns = ['Nome','Followers','TotalTweets']
            values = [user.userName,user.usersFollowers,user.usersTweets]
            selectWhere=self.select('*',table,"Nome= '"+user.userName+"'")
            print(selectWhere)
            if selectWhere == ():
                userId = self.insert(table,columns,values)
            else:
                userId=selectWhere[0]
            return userId
        except:
            printError()

    def insertHashtags(self,hashtags):
        try:
            table = 'Hashtag'
            columns = 'Texto'
            hashtagIds = []
            for hashtag in hashtags:
                values = [hashtag['text']]
                selectWhere=self.select('*',table,"Texto = '"+values[0]+"'")
                if selectWhere== ():
                    hashtagIds.append(self.insert(table,[columns],values))
                else:
                    hashtagIds.append(selectWhere[0])
                
            return hashtagIds
        except:
            printError()

#dao = Dao()
#tweetGetter = TweetFromID()
#tweet = tweetGetter.getTweet('1021183317406896128')
#teste = dao.insertTweet(tweet)

