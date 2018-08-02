from utils import tratarValuesDao, printError,tratarColumnsDao
import pymysql.cursors
from DB_helper import DB_helper
from models import Tweet,User
from tweet_from_id import TweetFromID
from sentiment_analyze import Linguakit
from format_place import FormatPlace

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
            columns = ['Texto','Data','Retweets','Likes','Usuario_idUsuario','idTweetOrigem','Lugar_idLugar']
            selectWhere=self.select('*',table,"idTweetOrigem = '"+tweet.id+"'")
            if selectWhere == ():
                lugarId = self.insertLocation(tweet.user.location)
                values = [tweet.tweetText,tweet.tweetDate,tweet.retweetCount,tweet.likes,userId,tweet.id,lugarId]
                tweetId = self.insert(table,columns,values)
                for x in hashtagsIds:
                    self.insertTweetHashtag(tweetId,x)
                self.insertTweetcandidate(tweetId,tweet.candidato,tweet.sentimento)
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
            if selectWhere == ():
                userId = self.insert(table,columns,values)
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
                selectWhere=self.select('*',table,"Texto = '"+values[0]+"'")
                if selectWhere== ():
                    hashtagIds.append(self.insert(table,[columns],values))
                else:
                    hashtagId = selectWhere[0]['idHashTag']
                    hashtagIds.append(hashtagId)
               
            return hashtagIds
        except:
            printError()

    def insertTweetHashtag(self,idTweet,idHashtag):
        try:
            table = 'tweet_has_hashtag'
            columns = ['tweet_idTweet', 'hashtag_idHashTag']
            values = [idTweet,idHashtag]
            selectWhere=self.select('*',table,"tweet_idTweet = '"+str(idTweet)+"' AND hashtag_idHashTag = '"+str(idHashtag)+"'")
            if selectWhere == ():
                result=self.insert(table,columns,values)
            else:
                result=0
            return result
        except:
            printError()
    
    def insertTweetcandidate(self,idTweet,idCandidato,idSentimento):
        try:
            table = 'tweetcandidato'
            columns = ['Tweet_idTweet','Candidato_idCandidato','Sentimento_idSentimento']
            values = [idTweet,idCandidato,idSentimento]
            selectWhere= self.select('*',table,"Tweet_idTweet = '"+str(idTweet)+"'")
            if selectWhere == ():
                result=self.insert(table,columns,values)
            else:
                result = 'error'
            return result
        except:
            printError()

    def insertLocation(self,location):
        try:
            table = 'lugar'
            columns = ['Cidade','Estado','Pais']
            city=location['city']
            state= location['state']
            country= location['country']
            values = [city,state,country]
            selectWhere = self.select('*',table,"Cidade = '"+city+"' AND Estado = '"+state+"'")
            if selectWhere == ():
                result=self.insert(table,columns,values)
            else:
                result = selectWhere[0]['idLugar']
            return result
        except:
            printError()

    def selectIds(self,lastid):

        rangeId = lastid + 2000
        try:
            table = 'manager'
            result = self.select('*',table,"idMining > "+str(lastid)+" and idMining <"+str(rangeId) ) 
            if result != ():
                return result
        except:
            printError()

    def updateSentimento(self):
        try:
            table = 'tweetcandidato'
            select=self.select('*',table,"Sentimento_idSentimento = 3")
            table = 'tweet'
            linguaKit = Linguakit()
            for x in select:
                select2 = self.select('*',table, "idTweet = {}".format(x['Tweet_idTweet']))
                sentimento = linguaKit.sent_analyze(select2[0]['Texto'])[2]
                if sentimento == 'NEGATIVE':
                    sentimento = 1
                elif sentimento == 'NONE':
                    sentimento = 2
                else:
                    sentimento = 3
                print(x['Tweet_idTweet'])
                query = "UPDATE tweetcandidato SET Sentimento_idSentimento = {} WHERE Tweet_idTweet = {}".format(sentimento,x['Tweet_idTweet'])
                print(query)
                self.cursor.execute(query)
                self.dbHelper.conn.commit()
        except:
            printError()

    def updateLugar(self):
        try:
            table = 'lugar'
            select = self.select('*',table)
            formatPlace = FormatPlace()
            print(len(select))
            for x in range(len(select)):
                endereco = "{} {} {}".format(select[x]['Cidade'],select[x]['Estado'],select[x]['Pais'])
                print(endereco)
                endereco = formatPlace.localizationCoord(endereco)
                query = "UPDATE lugar SET lat = {} , lng = {} WHERE idLugar = {}".format(endereco['lat'],endereco['lng'],select[x]['idLugar'])
                print(query)
                self.cursor.execute(query)
                self.dbHelper.conn.commit()
        except:
            printError()
