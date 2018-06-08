from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import datetime import date, timedelta, datetime
import time
driver = webdriver.Chrome()

query='lulalivre'
initialDate="1/05/2018"
finalDate="1/06/2018"
dataInicial= time.mktime(datetime.datetime.strptime(initialDate, "%d/%m/%Y").timetuple())
dataInicial= time.mktime(datetime.datetime.strptime(finalDate, "%d/%m/%Y").timetuple())
print(str(dataInicial))
while True:
    driver.get("https://twitter.com/search?l=pt&q=%23" + query + "%20since%3A" + str(dataInicial) + "%20until%3A" + str(dataFinal) + "&src=typd&lang=pt")
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.END)
    time.sleep(3)
    elementList = driver.find_elements_by_class_name("js-stream-tweet")
    idTweetList = []
    for tweet in elementList:
        idTweetList.append(tweet.get_attribute("data-tweet-id"))
    print(idTweetList, len(idTweetList))
