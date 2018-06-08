# coding: utf-8
import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="root",
                  db="mydb")
cursor = conn.cursor()
arquivo = open('lulalivre.txt','r')
lista=arquivo.read().split()
lista1=[]
for x in range (len(lista)):
    if x%2==0:
        lista1.append(lista[x])


cwd = os.getcwd()
auth = tweepy.OAuthHandler('jkwDvQkT5Es6S24JiLq2FLxrb', 'ju5ogpsqo3cQLxtgTurMgq7cmWt8CN2H9lQ0F5wGGrmegcvAMp')
auth.set_access_token('89299395-PpehItyb3bnxSI3TEbve9Y8uDZKKOgaYiQinCCrvg', 'Rh8FHQk0Vd66LCZJIf20DrFzFZfmBZqqPLaAN3hXCmT3n')
api = tweepy.API(auth)

for x in lista1:
    tweet = api.get_status(x)
    hashtags=tweet.entities["hashtags"]
    nomeUsuario = tweet.user.screen_name
    location = tweet.user.location
    followersUsuario = tweet.user.followers_count
    totalTweetsUsuario = tweet.user.statuses_count
    textoTweet = tweet.text
    tweetDate = tweet.created_at
    retweetCount = tweet.retweet_count
    likes = tweet.favorite_count
    idStr = x
    print(x)
    cursor.execute("""INSERT INTO Usuario (Nome,Followers,TotalTweets) VALUES(%s,%s,%s)""",(nomeUsuario,followersUsuario,totalTweetsUsuario))
    idUsuario = cursor.lastrowid
    hashtagsId=[]
    for y in hashtags:
        stringName = y['text']
        cursor.execute("""INSERT INTO HashTag (Texto) VALUES(%s)""",[stringName])
        hashtagsId.append(cursor.lastrowid)
    try:
        cursor.execute("""INSERT INTO Tweet (Texto,Data,Retweets,Likes,Usuario_idUsuario,idTweetOrigem,Lugar) VALUES(%s,%s,%s,%s,%s,%s,%s)""",(textoTweet.encode("utf-8"),tweetDate,retweetCount,likes,idUsuario,idStr,location))
        tweetIdBanco = cursor.lastrowid
        for ids in hashtagsId:
            print(tweetIdBanco)
            print(ids)
            cursor.execute("""INSERT INTO tweet_has_hashtag (tweet_idTweet,hashtag_idHashTag) VALUES(%s,%s)""",(tweetIdBanco,ids))
    except:
        print('oi')
    conn.commit()
