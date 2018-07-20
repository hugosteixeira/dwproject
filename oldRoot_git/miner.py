from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from datetime import date, timedelta, datetime
import time

timeStampInicial = 1527811200 #01/01/2018
timeStampFinal = 1530403200
passo = 86400


driver = webdriver.Chrome()
hastagList = ['pratodagalera']
for hastag in hastagList:

    try:
        arq = open(hastag+'.txt', 'r')
        
    except:
        arq = open(hastag+'.txt', 'w')
        arq.close()
        
    arq = open(hastag+'.txt', 'r')    
    fileList = arq.read().split('\n')
    if len(fileList) > 0  and fileList[0] !="" :
        lastTweetTimeStamp = fileList[-2].split(' ')[1]
        timeStampInicial = int(lastTweetTimeStamp) + 1

        
    while int(timeStampInicial) < timeStampFinal :
        url = "https://twitter.com/search?l=pt&q=%23" + hastag + "%20since%3A" + str(timeStampInicial) + "%20until%3A" + str(timeStampInicial+passo) + "&src=typd&lang=pt"
        driver.get(url)
        assert "since" in driver.title
        time.sleep(1)

        elementList = driver.find_elements_by_class_name("js-stream-tweet")
        lasttSizeList = len(elementList)
        
        while True:
            body = driver.find_element_by_tag_name('body')
            body.send_keys(Keys.END)
            time.sleep(1)
            elementList = driver.find_elements_by_class_name("js-stream-tweet")
            if lasttSizeList == len(elementList):
                break
            lasttSizeList = len(elementList)
        
        string = ''
        for tweet in elementList:
            idTweet = tweet.get_attribute("data-tweet-id")
            tweetTimeStamp = tweet.find_elements_by_class_name("js-short-timestamp")[0].get_attribute("data-time")
            string += idTweet+' '+tweetTimeStamp + '\n'
            #print(idTweet, tweetTimeStamp)
        wArq = open(hastag+'.txt', 'a')
        if string != '':
            print(string)
            wArq.write(string)
        timeStampInicial = int(timeStampInicial) + passo + 1
        
    
    
    
    
    
