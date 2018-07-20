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
            valor="INSERT INTO {}({}) VALUES ('{}')".format(table,columns,values)
            print(valor)
            self.cursor.execute(valor)
            self.cursor.commit()
            self.cursor.close()
            return self.cursor.lastrowid
        except:
            printError()

    def select(self,columns, table, whereArg=''):
        try:
            if whereArg != '':
                selectWhere='SELECT {} FROM {} WHERE {};'.format(columns,table,whereArg)
                print(selectWhere)
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
            selectWhere=self.select(columns,table,"Nome="+user.screen_name)
            if selectWhere== ():
                userId = self.insert(table,columns,values)
                return userId
            else:
                userId=selectWhere[0]['idUsuario']
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
                selectWhere=self.select(columns,table,"Texto = '"+values[0]+"'")
                if selectWhere== ():
                    hashtagIds.append(self.insert([table],[columns],values))
                    return hashtagIds
                else:
                    hashtagsIds=hashtagIds=selectWhere[0]['idHashTag']
                    return hashtagsIds
                
                
            return hashtagIds
        except:
            printError()


teste=Dao().insertHashtags([{'text':'pqpqpqpqp'}])
