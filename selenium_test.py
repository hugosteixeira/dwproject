from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, timedelta, datetime
import time
driver = webdriver.Chrome()

query='lulalivre'
diaInicial=1
mesInicial=1
anoInicial=2018
diaFinal=1
mesFinal=1
anoFinal=2018
dataInicial= str(anoInicial)+'-'+str(mesInicial)+'-'+str(diaInicial)
dataFinal=str(anoFinal)+'-'+str(mesFinal)+'-'+str(diaFinal)
print(str(dataInicial))
driver.get("https://twitter.com/search?l=pt&q=%23" + query + "%20since%3A" + str(dataInicial) + "%20until%3A" + str(dataFinal) + "&src=typd&lang=pt")
while True:
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.END)
    time.sleep(3)
    elementList = driver.find_elements_by_class_name("js-stream-tweet")
    idTweetList = []
    for tweet in elementList:
        idTweetList.append(tweet.get_attribute("data-tweet-id"))
    print(idTweetList, len(idTweetList))
