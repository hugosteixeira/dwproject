from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from DAO import Dao
#from datetime import date, timedelta, datetime
import time
import math

class HastagMining:
    
    START_TIMESTAMP = 1522540800 #01/04/2018 1514818800
    FINISH_TIMESTAMP = 1532564011
    STEPP_TIMESTAMP = 7200 #o range para captura da lista de tweets ex: um dia, uma hora (cada loop roda uma dia... uma hora...)


    def __init__(self, hastag_name, candidato, print_status = False):
        self._hastag = hastag_name
        self._print_status = print_status
        self._candidato = candidato
        #options = webdriver.ChromeOptions();
        #options.add_argument('headless');
        self._driver = None
        #self._driver = webdriver.Chrome()
    def start(self):

        if self._print_status :
            print('start mining #{} ...'.format(self._hastag))
        dao = Dao()
        timeStamp_tweet_list = dao.select('*',"manager","hastag = '{}' ORDER BY 'timeStamp'".format(self._hastag))
        lastTweetTimeStamp = int(timeStamp_tweet_list[-1]['timeStamp'])
        #self.get_status(lastTweetTimeStamp)
        if lastTweetTimeStamp > self.START_TIMESTAMP :
            self.mining(lastTweetTimeStamp, self.FINISH_TIMESTAMP)

        else :
            self.mining(self.START_TIMESTAMP, self.FINISH_TIMESTAMP)
    
    def mining(self, stamp_start, stamp_finish):
        stamp_start, stamp_finish = int(stamp_start)+1 , int(stamp_finish)
        cont = 5
        pivo = 5
        options = webdriver.ChromeOptions();
        options.add_argument('headless');
        #self._driver = webdriver.Chrome('C:\\Users\\joaov\\Desktop\\dwproject\\chromedriver.exe ', chrome_options = options)
        self._driver = webdriver.Chrome()
        while stamp_start < stamp_finish :
 
            url = "https://twitter.com/search?f=tweets&vertical=default&q=%23{}%20since%3A{}%20until%3A{}&l=pt&src=typd".format(self._hastag, stamp_start, stamp_start + self.STEPP_TIMESTAMP)
            driver = self._driver
            driver.get(url)
            assert "since" in driver.title
            #time.sleep(1)

            elementList = driver.find_elements_by_class_name("js-stream-tweet")
            lasttSizeList = len(elementList)
        
            while True:
                body = driver.find_element_by_tag_name('body')
                body.send_keys(Keys.END)
                time.sleep(1)
                
                #driver.implicitly_wait(1)
                elementList = driver.find_elements_by_class_name("js-stream-tweet")
                sizeList = len(elementList)

                if lasttSizeList == sizeList:
                    break
                elif sizeList > 100:
                    break
                lasttSizeList = len(elementList)
            
            stringList = []
            
            for tweet in reversed(elementList):
                idTweet = tweet.get_attribute("data-tweet-id")
                tweetTimeStamp = tweet.find_elements_by_class_name("js-short-timestamp")[0].get_attribute("data-time")
                #tweetText = tweet.find_element_by_class_name("tweet-text").text
                #lastStamp = int(tweetTimeStamp)
                stringList.append(idTweet+' '+tweetTimeStamp + '\n')
                dao = Dao()
                dao.insert('manager', ['hastag', 'idTweet', 'idCandidato', 'timeStamp'],[self._hastag, idTweet, self._candidato, tweetTimeStamp])
            
            print('...')
            cont+=1
            if cont > pivo:
                pivo+=5
                self.get_status(stamp_start)

            stamp_start = stamp_start + self.STEPP_TIMESTAMP + 1

        self._driver.close()
        self._driver.quit()


    def get_status(self, lastTimeStamp):

        if self._print_status :
            total = self.FINISH_TIMESTAMP - self.START_TIMESTAMP
            current = ((lastTimeStamp - self.START_TIMESTAMP)/ total)*100
            status_string = '>>>{}% mining for #{} completed<<<'.format(round(current,2), self._hastag)
            print(status_string)
        return (status_string)

    
#mining = HastagMining('LulaLivre','Lula', print_status = True)
#mining.start()