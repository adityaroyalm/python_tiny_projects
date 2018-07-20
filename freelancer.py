# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 18:26:43 2017

@author: aditya royal
"""
all_url=list()
links=list()
emails=dict()
import requests
import re
from urlparse2 import urljoin
from bs4 import BeautifulSoup
r=BeautifulSoup(open('NHVTMA.html'),'html.parser')
for x in r.find_all('a'):
    all_url.append(x.get('href'))
    for url in all_url:
        try:
            open_=requests.get(url)
            response=open_.content.decode('utf-8')
            soup=BeautifulSoup(response,'html.parser')
            for link in soup.find_all('a'):
                if link.get_text(strip=True).startswith('/'):
                    link=urljoin(url,link)
        except Exception as e:
            print e