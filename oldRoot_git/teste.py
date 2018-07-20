# coding: utf-8
import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import MySQLdb
import sys
from traceback import print_tb, extract_tb, format_list
from textblob import TextBlob


def printError():
    error = sys.exc_info()
    type = error[0]#tipo do erro
    print('\n'+'Type: \n'+str(type)+'\n')
    value = error[1] # valor do erro
    print('Value: \n'+str(error[1])+'\n')
    tb=error[2]
    print('Traceback:')
    e_tb=extract_tb(tb)
    f_l=format_list(e_tb)#traceback em forma de lista para futuro usos
    print_tb(tb)

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="mydb",charset="utf8mb4", use_unicode = True)
cursor = conn.cursor()
arquivo = open('Bolsomito.txt','r')
idCandidato = '2'
idNegativo = '1'
idNeutro = '2'
idPositivo = '3'
lista=arquivo.read().split()
lista1=[]
for x in range (len(lista)):
    if x%2==0:
        lista1.append(lista[x])


auth = tweepy.OAuthHandler('jkwDvQkT5Es6S24JiLq2FLxrb', 'ju5ogpsqo3cQLxtgTurMgq7cmWt8CN2H9lQ0F5wGGrmegcvAMp')
auth.set_access_token('89299395-PpehItyb3bnxSI3TEbve9Y8uDZKKOgaYiQinCCrvg', 'Rh8FHQk0Vd66LCZJIf20DrFzFZfmBZqqPLaAN3hXCmT3n')
api = tweepy.API(auth)

for x in lista1:
    try:        
        tweet = api.get_status(x,tweet_mode='extended')
        hashtags=tweet.entities["hashtags"]
        nomeUsuario = tweet.user.screen_name
        location = tweet.user.location
        followersUsuario = tweet.user.followers_count
        totalTweetsUsuario = tweet.user.statuses_count
        textoTweet = tweet.full_text
        tweetDate = tweet.created_at
        retweetCount = tweet.retweet_count
        likes = tweet.favorite_count
        idStr = x
        traducao = TextBlob(str(textoTweet)).translate(to='en')
        print(traducao)
        sentimento = traducao.sentiment.polarity
        print(sentimento)
        sentimeto1 = ''
        if sentimento < :
            sentimento1= idNegativo
        elif sentimento == 0.0:
            sentimento1= idNeutro
        else:
            sentimento1=idPositivo
        cursor.execute("""INSERT INTO Usuario (Nome,Followers,TotalTweets) VALUES(%s,%s,%s)""",(nomeUsuario,followersUsuario,totalTweetsUsuario))
        idUsuario = cursor.lastrowid
        hashtagsId=[]
        for y in hashtags:
            try:
                stringName = y['text']
                cursor.execute("""INSERT INTO HashTag (Texto) VALUES(%s)""",[stringName])
                hashtagsId.append(cursor.lastrowid)
            except:
                printError()
        try:
            cursor.execute("""INSERT INTO Tweet (Texto,Data,Retweets,Likes,Usuario_idUsuario,idTweetOrigem,Lugar) VALUES(%s,%s,%s,%s,%s,%s,%s)""",(textoTweet.encode("utf-8"),tweetDate,retweetCount,likes,idUsuario,idStr,location))
            tweetIdBanco = cursor.lastrowid
            cursor.execute("""INSERT INTO tweetcandidato (Tweet_idTweet,Candidato_idCandidato,Sentimento_idSentimento) VALUES(%s,%s,%s)""",(tweetIdBanco,idCandidato,sentimento1))
            for ids in hashtagsId:
                cursor.execute("""INSERT INTO tweet_has_hashtag (tweet_idTweet,hashtag_idHashTag) VALUES(%s,%s)""",(tweetIdBanco,ids))
        except:
            printError()
        conn.commit()
    except:
        printError()
