from DAO import Dao
import sys
from extract_tweet_ids import HastagMining
import time

s1 = sys.argv[1]

if s1 == 'newHastag':
    
    candidato, hastag =  sys.argv[2], sys.argv[3]

    dao = Dao()
    r = dao.insert('manager', ['hastag', 'idTweet', 'idCandidato', 'timeStamp'],[hastag, '0', candidato, 0])
    
    print(">>> new hastag saved for mining use 'main.py mineHastag {} {} {}'".format(candidato, hastag, 'p'))

elif s1 == 'mine':
    
    candidato, hastag =  sys.argv[2], sys.argv[3]
    p = False
    if sys.argv[4] == 'p':
        p = True
    mining = HastagMining(hastag, candidato, print_status = p)
    mining.start()