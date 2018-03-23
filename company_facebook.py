# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:32:40 2018

@author: aditya royal
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
browser=webdriver.Chrome('C:/Users/chromedriver.exe',chrome_options=chrome_options)
page=browser.get('http://www.google.com')
search=browser.find_element_by_name('q')
search.send_keys('aditya')
search.send_keys(Keys.RETURN)
time.sleep(5)


