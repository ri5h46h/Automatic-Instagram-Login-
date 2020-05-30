# This code is contributed by Rishabh Narayan ...
#Feel free to modify this code using your ideas ..
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

while True:

    name = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))

    input('Enter anything after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
