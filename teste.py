import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Chrome(executable_path='C:\\Users\\hugos\\Desktop\\chromedriver_win32\\chromedriver.exe')
cwd = os.getcwd()
auth = tweepy.OAuthHandler('jkwDvQkT5Es6S24JiLq2FLxrb', 'ju5ogpsqo3cQLxtgTurMgq7cmWt8CN2H9lQ0F5wGGrmegcvAMp')
auth.set_access_token('89299395-PpehItyb3bnxSI3TEbve9Y8uDZKKOgaYiQinCCrvg', 'Rh8FHQk0Vd66LCZJIf20DrFzFZfmBZqqPLaAN3hXCmT3n')
api = tweepy.API(auth)
tweet = api.get_status('997192482843701249')
print(tweet.text.encode('UTF-8').decode('UTF-8'))
