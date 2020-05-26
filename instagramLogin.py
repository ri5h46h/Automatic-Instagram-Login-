from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome("C:\\enter\\the\\path\\to\\chromedriver.exe")
browser.get('https://www.instagram.com')

time.sleep(5)

def instagram_login():
    email = browser.find_element_by_name('username')
    email.send_keys('type_your_instagram username/email/phone_number') #type your username/email/phone no. here
    # email.send_keys(Keys.TAB)
    pswd = browser.find_element_by_name('password')
    pswd.send_keys('type_your_instagram_password_here') #type your password here

    time.sleep(1)

    login = browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button''')
    login.click()

instagram_login()
