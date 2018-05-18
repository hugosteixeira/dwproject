from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def login_twitter(driver, username, password):
 
    # open the web page in the browser:
    driver.get("https://twitter.com/login")
 
    # find the boxes for username and password
    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")
 
    # enter your username:
    username_field.send_keys(username)
    driver.implicitly_wait(1)
 
    # enter your password:
    password_field.send_keys(password)
    driver.implicitly_wait(1)
 
    # click the "Log In" button:
    driver.find_element_by_class_name("EdgeButtom--medium").click()

driver = webdriver.Chrome(executable_path='C:\\Users\\joaov\\Desktop\\dwproject\\chromedriver_win32\\chromedriver.exe')
#driver.get("https://twitter.com")
#assert "Python" in driver.title
login_twitter(driver, 'login', 'senha')#senha e nome do twitter (não ia por as minhas em um repositorio publico kkk)
elementList = driver.find_elements_by_class_name("js-stream-tweet")
idTweetList = [tweet.get_attribute("data-tweet-id") for tweet in elementList ]
print(idTweetList, len(idTweetList))
#assert "No results found." not in driver.page_source
driver.close()
