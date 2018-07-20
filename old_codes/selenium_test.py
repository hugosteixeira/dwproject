from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#from datetime import date, timedelta, datetime
import time








options = webdriver.ChromeOptions();

options.add_argument('headless');

driver = webdriver.Chrome(chrome_options=options)

url = "https://twitter.com/search?l=pt&q=%23lulalivre%20since%3A1514822594%20until%3A1914822595&src=typd&lang=pt"
driver.get(url)
#assert "since" in driver.title
time.sleep(2)

#elementList = driver.find_elements_by_class_name("js-initial-focus")


tweetText = driver.find_elements_by_class_name("tweet-text")
for i in tweetText:
    print(i.text)
driver.close()
driver.quit()


driver = webdriver.Chrome(chrome_options=options)

url = "https://twitter.com/search?l=pt&q=%23lulalivre%20since%3A1514822594%20until%3A1914822595&src=typd&lang=pt"
driver.get(url)
#assert "since" in driver.title
time.sleep(2)

#elementList = driver.find_elements_by_class_name("js-initial-focus")


tweetText = driver.find_elements_by_class_name("tweet-text")
for i in tweetText:
    print(i.text)
driver.close()
driver.quit()
    

        
    
    
    
    
    
