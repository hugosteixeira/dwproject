from DAO import Dao
import sys
from extract_tweet_ids import HastagMining
import time
from tweet_from_id import TweetFromID
from models import Tweet,User
from sentiment_analyze import Linguakit

fileOpen = open("Last_id.txt",'w')
lastId = fileOpen.read()
s1 = sys.argv[1]

if s1 == 'newHastag':
    
    candidato, hastag =  sys.argv[2], sys.argv[3]

    dao = Dao()
    r = dao.insert('manager', ['hastag', 'idTweet', 'idCandidato', 'timeStamp'],[hastag, '0', candidato, 0])
    
    print(">>> new hastag saved for mining use 'main.py mineHastag {} {} {}'".format(candidato, hastag, 'p'))

elif s1 == 'minehashtag':
    
    candidato, hastag =  sys.argv[2], sys.argv[3]
    p = False
    if sys.argv[4] == 'p':
        p = True
    mining = HastagMining(hastag, candidato, print_status = p)
    mining.start()

if s1 =='minetweet':
    dao = Dao()
    linguaKit = Linguakit()
    tweetGetter = TweetFromID()
    idList = dao.selectIds(lastId)
    lastId = idList[-1]['idMining']
    for x in idList:
        tweet = Tweet(tweetGetter.getTweet(x['idMining']))
        tweet.candidato = x['idCandidato']
        tweet.sentimento = linguaKit.sent_analyze(tweet.tweetText)
        if tweet.sentimento < 0:
            tweet.sentimento = 1
        elif tweet.sentimento == 0:
            tweet.sentimento = 2
        else:
            tweet.sentimento = 3
        dao.insertTweet(tweet)