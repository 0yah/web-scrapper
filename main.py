from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Needed to emulate Key strokes
import time

import configparser
config = configparser.ConfigParser()
config.read('auth.ini')

driver = webdriver.Chrome('./chromedriver')

username = config['AUTH']['username']
password = config['AUTH']['password']
#Open a link
driver.get("https://instagram.com")

#Username
#/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input

#Password
#/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input


#Wait for 30 seconds for the page to load
#driver.set_page_load_timeout(30)

time.sleep(20)
username_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username_input.clear()
#username_input.send_keys("YOUR ACCOUNT USERNAME")
username_input.send_keys(username)

password_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password_input.clear()
#password_input.send_keys("YOUR ACCOUNT PASSWORD")
password_input.send_keys(password)

time.sleep(5)
login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login_button.click()

time.sleep(30)


#Not Now Button
not_now_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
not_now_button.click()

time.sleep(30)

#Open DMs Page
driver.get("https://www.instagram.com/direct/inbox/")

time.sleep(60)


#New Message button
new_message_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')
new_message_button.click()


#Wait for the modal to load
time.sleep(30)
#Search for the recepient Input
receipient_input = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input')
receipient_input.send_keys("TARGET ACCOUNT")

time.sleep(30)
#/html/body/div[4]/div/div/div[2]/div[2]/div[2]
suggested=driver.find_elements_by_class_name('body > div.RnEpo.Yx5HN > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div.Igw0E.IwRSH.eGOV_.vwCYk._3wFWr > div.-qQT3')
target = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]')
target.click()
print(len(suggested))
time.sleep(30)




#Proceed Button 
proceed_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button')
proceed_button.click()


#Wait for the page to load(instagram.com/direct)
time.sleep(40)
dm_input = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
dm_input.clear()
dm_input.send_keys("I love you")

dm_input.send_keys(Keys.RETURN)
