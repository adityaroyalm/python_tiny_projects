# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:37:41 2018

@author: aditya royal
"""
import pandas as pd
import xlrd
import openpyxl as xl
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import boto3
import io
s3 = boto3.client('s3')
obj = s3.get_object(Bucket='adityafirstbucket', Key='tesder.csv')
df = pd.read_csv(io.BytesIO(obj['Body'].read()))
browser = webdriver.Chrome('C:/Users/chromedriver.exe')
obj=pd.DataFrame(ws.values)
li=obj.iloc[0,:]
obj.columns=li
obj.drop([0],inplace=True)
import requests
import webbrowser
tag_a=list()
fb_page=list()

generic_address='https://www.google.com/search?q=facebook %s &oq=facebook %s /&aqs=chrome..69i57j69i64.17167j1j7&sourceid=chrome&ie=UTF-8'
for company in obj.iloc[:,0]:
    company_google= generic_address%(company,company)
    real_page=requests.get(str(company_google))
      #hit return after you enter search text
       #sleep for 5 seconds so you can see the results
    soup=BeautifulSoup(real_page.text,'html.parser')
    tag_a=soup.find_all('a')
    numOpen = min(5, len(tag_a))
    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))
    for x in tag_a:
        if x.get('href').startswith('/url?q=https://www.facebook.com/') and company in x.get('href'):
            fb_page.append(x.get('href'))
            browser.get(x.get('href'))
            time.sleep(5)