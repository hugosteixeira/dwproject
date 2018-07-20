from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from datetime import date, timedelta, datetime
import time


arq = open('hastags.txt','r')
hastagList = arq.read().split('\n')

driver = webdriver.Chrome()
for hastag in hastagList:
    timeStampInicial = 1514818800 #01/01/2018
    timeStampFinal = 1528329600
    passo = 86400
    
    print('iniciando #'+hastag+'...')
    time.sleep(3)
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
        url = "https://twitter.com/search?f=tweets&vertical=default&q=%23" + hastag + "%20since%3A" + str(timeStampInicial) + "%20until%3A" + str(timeStampInicial+passo) + "&l=pt&src=typd"
        driver.get(url)
        assert "since" in driver.title
        time.sleep(1)

        elementList = driver.find_elements_by_class_name("js-stream-tweet")
        lasttSizeList = len(elementList)
        
        while True:
            body = driver.find_element_by_tag_name('body')
            body.send_keys(Keys.END)
            time.sleep(2)
            
            #driver.implicitly_wait(1)
            elementList = driver.find_elements_by_class_name("js-stream-tweet")
            if lasttSizeList == len(elementList):
                break
            lasttSizeList = len(elementList)
        
        stringList = []
        for tweet in elementList:
            idTweet = tweet.get_attribute("data-tweet-id")
            tweetTimeStamp = tweet.find_elements_by_class_name("js-short-timestamp")[0].get_attribute("data-time")
            tweetText = tweet.find_element_by_class_name("tweet-text").text
            print(tweetText)
            '''for hastag in tweetHastags:
                text = hastag.text
                print(text)'''
            stringList.append(idTweet+' '+tweetTimeStamp + '\n')
            #print(idTweet, tweetTimeStamp)
        wArq = open(hastag+'.txt', 'a')
        string = ''.join((reversed(stringList)))
        if string != '':
            print(lasttSizeList)
            wArq.write(string)
        timeStampInicial = int(timeStampInicial) + passo + 1
        
    
    
    
    
    
