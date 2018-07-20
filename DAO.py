from utils import tratarListaDao, printError
import pymysql.cursors
from DB_helper import DB_helper
from models import Tweet

class Dao:
    def __init__(self):
        self.dbHelper = DB_helper()
        self.cursor = self.dbHelper.getCursor()

    def insert(self, table,columns,values):
        try:
            columns = tratarListaDao(columns)
            values = tratarListaDao(values)
            self.cursor.execute('INSERT INTO %s(%s) VALUES %s',(table,columns,values))
            self.cursor.commit()
            self.cursor.close()
            return self.cursor.lastrowid
        except:
            printError()

    def select(self,columns, table, whereArg=''):
        try:
            whereArg = tratarListaDao(whereArg)
            if whereArg != '':
                self.cursor.fetchall('SELECT %s FROM %s WHERE %s',(columns,table,whereArg))
            else:
                self.cursor.fetchall('SELECT %s FROM %s',(columns,table,))
            self.cursor.commit()
            return self.cursor.lastrowid
        except:
            printError()



    def insertTweet(self,tweet):
        try:
            userId = self.insertUser(tweet.user)
            hashtagsIds = self.insertHashtags(tweet.hashtags)
            table = 'Tweet'
            columns = ['Texto','Data','Retweets','Likes','Usuario_idUsuario','idTweetOrigem','Lugar']
            values = [tweet.tweetTexto,tweet.tweetDate,tweet.retweetCounttweet.likes,userId,tweet.id,tweet.user.location]
            tweetId = self.insert(table,columns,values)
            return tweetId
        except:
            printError()

    def insertUser(self,user):
        try:
            table = 'Usuario'
            columns = ['Nome','Followers','TotalTweets']
            values = [user.screen_name,user.followers_count,user.statuses_count]
            userId = self.insert(table,columns,values)
            return userId
        except:
            printError()

    def insertHashtags(self,hashtags):
        try:
            table = 'Hashtag'
            columns = ['Texto']
            hashtagIds = []
            for hashtag in hashtags:
                values = [hashtag.text]
                hashtagIds.append(self.insert(table,columns,values))
            return hashtagIds
        except:
            printError()