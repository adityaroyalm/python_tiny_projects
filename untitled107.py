# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:41:13 2017

@author: aditya royal
"""
import re
from selenium import webdriver
driver=webdriver.Chrome(executable_path=r'C:\Users\chromedriver.exe')
driver.get("http://www.python.org")
source=driver.page_source
re.findall(r'[\w\.-]+@[\w\.-]+',source)