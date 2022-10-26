# from bs4 import BeautifulSoup
# import requests

# import requests
# headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0)   Gecko/20100101 Firefox/78.0", 
# "Referer": "https://www.google.com"}

# response = requests.get(url, headers=headers)




# # response.content
# #response.json()
# #response.text

# soup = BeautifulSoup(response.content, 'html.parser')
# btn=soup.find_all("div", class_="sg-flex sg-flex--justify-content-center button-container--2X-uE")
# print(btn)

from selenium import webdriver
import time
import random

option = webdriver.ChromeOptions()


# url = "https://brainly.pl"
url="https://amiunique.org"


option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

option.add_argument('--disable-blink-features=AutomationControlled')


 
browser = webdriver.Chrome()
browser.get(url)
time.sleep(15)
# doc = browser.find_elements_by_xpath('//*[@id="top"]/nav/ul/li[3]/a')[0]
elem=browser.find_elements_by_class_name("sg-flex sg-flex--justify-content-center button-container--2X-uE")
elem.click()
time.sleep(5)
browser.quit()