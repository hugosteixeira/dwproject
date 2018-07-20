import os
import pymysql.cursors
import sys
from utils import printError
class DB_helper :
    Q_CREATE_TABLES = [ 'DROP TABLE IF EXISTS `candidato`;',

'''CREATE TABLE `candidato` (
  `idCandidato` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Partido` varchar(45) NOT NULL,
  `Numero` int(11) NOT NULL,
  PRIMARY KEY (`idCandidato`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;''',


'DROP TABLE IF EXISTS `hashtag`;',

'''CREATE TABLE `hashtag` (
  `idHashTag` int(11) NOT NULL AUTO_INCREMENT,
  `Texto` varchar(45) NOT NULL,
  PRIMARY KEY (`idHashTag`),
  UNIQUE KEY `Texto` (`Texto`)
) ENGINE=InnoDB AUTO_INCREMENT=3238 DEFAULT CHARSET=utf8;''',


'DROP TABLE IF EXISTS `lugar`;',

'''CREATE TABLE `lugar` (
  `idLugar` int(11) NOT NULL AUTO_INCREMENT,
  `Estado` varchar(45) NOT NULL,
  `Pais` varchar(45) NOT NULL,
  PRIMARY KEY (`idLugar`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;''',


'DROP TABLE IF EXISTS `sentimento`;',

'''CREATE TABLE `sentimento` (
  `idSentimento` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  PRIMARY KEY (`idSentimento`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;''',

'DROP TABLE IF EXISTS `usuario`;',

'''CREATE TABLE `usuario` (
  `idUsuario` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Followers` int(11) NOT NULL,
  `TotalTweets` int(11) NOT NULL,
  `Lugar_idLugar` int(11) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`),
  KEY `fk_Usuario_Lugar1_idx` (`Lugar_idLugar`),
  CONSTRAINT `fk_Usuario_Lugar1` FOREIGN KEY (`Lugar_idLugar`) REFERENCES `lugar` (`idLugar`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1723 DEFAULT CHARSET=utf8;''',


'DROP TABLE IF EXISTS `tweet`;',

'''CREATE TABLE `tweet` (
  `idTweet` int(11) NOT NULL AUTO_INCREMENT,
  `Texto` varchar(400) NOT NULL,
  `Data` varchar(45) NOT NULL,
  `Replys` int(11) DEFAULT NULL,
  `Retweets` int(11) NOT NULL,
  `Likes` int(11) NOT NULL,
  `Usuario_idUsuario` int(11) NOT NULL,
  `Lugar_idLugar` int(11) DEFAULT NULL,
  `idTweetOrigem` varchar(45) DEFAULT NULL,
  `Lugar` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idTweet`),
  KEY `fk_Tweet_Usuario1_idx` (`Usuario_idUsuario`),
  KEY `fk_Tweet_Lugar1_idx` (`Lugar_idLugar`),
  CONSTRAINT `fk_Tweet_Lugar1` FOREIGN KEY (`Lugar_idLugar`) REFERENCES `lugar` (`idLugar`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tweet_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1660 DEFAULT CHARSET=utf8;''',


'''DROP TABLE IF EXISTS `tweet_has_hashtag`;''',

'''CREATE TABLE `tweet_has_hashtag` (
  `tweet_idTweet` int(11) NOT NULL,
  `hashtag_idHashTag` int(11) NOT NULL,
  PRIMARY KEY (`tweet_idTweet`,`hashtag_idHashTag`),
  KEY `fk_tweet_has_hashtag_hashtag1_idx` (`hashtag_idHashTag`),
  KEY `fk_tweet_has_hashtag_tweet1_idx` (`tweet_idTweet`),
  CONSTRAINT `fk_tweet_has_hashtag_hashtag1` FOREIGN KEY (`hashtag_idHashTag`) REFERENCES `hashtag` (`idHashTag`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_tweet_has_hashtag_tweet1` FOREIGN KEY (`tweet_idTweet`) REFERENCES `tweet` (`idTweet`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;''',


'DROP TABLE IF EXISTS `tweetcandidato`;',

'''CREATE TABLE `tweetcandidato` (
  `Tweet_idTweet` int(11) NOT NULL,
  `Candidato_idCandidato` int(11) NOT NULL,
  `Sentimento_idSentimento` int(11) NOT NULL,
  PRIMARY KEY (`Tweet_idTweet`,`Candidato_idCandidato`),
  KEY `fk_TweetCandidato_Candidato1_idx` (`Candidato_idCandidato`),
  KEY `fk_TweetCandidato_Sentimento1_idx` (`Sentimento_idSentimento`),
  CONSTRAINT `fk_TweetCandidato_Candidato1` FOREIGN KEY (`Candidato_idCandidato`) REFERENCES `candidato` (`idCandidato`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_TweetCandidato_Sentimento1` FOREIGN KEY (`Sentimento_idSentimento`) REFERENCES `sentimento` (`idSentimento`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_TweetCandidato_Tweet1` FOREIGN KEY (`Tweet_idTweet`) REFERENCES `tweet` (`idTweet`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;'''




]
    
    Q_CREATE_DATABASE = "CREATE DATABASE dw"
    Q_DROP_DATABASE = "DROP DATABASE dw"
    DATA_BASE_NAME = "dw"
    SQL_HOST = "localhost"
    SQL_USER = "root"
    SQL_PASSWD = "Arretterr@"
    SQL_SHARSET = "utf8mb4"
    SQL_UNICODE = True
    def __init__ (self):

        self._cursorclass = pymysql.cursors.DictCursor

    def getConn(self, database_name = DATA_BASE_NAME):

        conn = pymysql.connect(host = self.SQL_HOST,
                    user = self.SQL_USER,
                    passwd = self.SQL_PASSWD,
                    db = database_name,
                    charset = self.SQL_SHARSET,
                    use_unicode = self.SQL_UNICODE,
                    cursorclass = self._cursorclass)
        return conn
    

    
    def getCursor(self):
        conn = self.getConn()
        cursor = conn.cursor()
        return cursor

    def INIT_DATA_BASE(self, p_table = False):
        try:
            conn = self.getConn()
        except :

            cursor = self.getConn(database_name = '').cursor()
            cursor.execute(self.Q_CREATE_DATABASE)
            cursor = self.getConn().cursor()
            if p_table:
                for q in self.Q_CREATE_TABLES:
                    print(q)
                    cursor.execute(q)
            else:
                for q in self.Q_CREATE_TABLES:
                    cursor.execute(q)

            return('"DATABASE {} CREATED"'.format(self.DATA_BASE_NAME))

    def DROP_DATA_BASE(self):
        try:
            cursor = self.getCursor()
            cursor.execute(self.Q_DROP_DATABASE)
            return ('"DATABASE {} DROPED"'.format(self.DATA_BASE_NAME))
        except:
            return ("error : DATABASE {} NOT EXIST".format(self.DATA_BASE_NAME))

    def resetDB(self):
        rDrop = self.DROP_DATA_BASE()
        rInit = self.INIT_DATA_BASE()
        return ('try drop result : {}, try creat result : {}'.format(rDrop, rInit))
            
