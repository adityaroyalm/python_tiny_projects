# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 12:27:23 2017

@author: aditya royal
"""

import requests
import re
import urllib2
import time
from bs4 import BeautifulSoup
iteration=0
a=0
b=0
urlo='http://www.lakesregionchamber.org/list'
links2=list()
while (iteration<1):
     all_url=list()
     links=list()
     emails=dict()
     r=BeautifulSoup(requests.get(urlo).text)
     #r=BeautifulSoup(open('https://drive.google.com/open?id=148ss6LUQzoqr-H8D8eRbqBOPfBg73kJX')
     for x in r.find_all('a'):
         all_url.append(x.get('href'))
     for url in all_url:
         try:
             open_=requests.get(url)
             response=open_.content.decode('utf-8')
             soup=BeautifulSoup(response)
             for link in soup.find_all('a'):
                 if re.findall(r'(automobile)|(Automobile)|(AUTOMOBILE)|(AUTOMOTIVE)|(Automotive)|(automotive)',str(link)):
                     links.append(link.get('href'))
         except Exception as e:
            print e