# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:11:14 2017

@author: aditya royal
"""

from bs4 import BeautifulSoup
r=BeautifulSoup(open('C:/Users/aditya royal/Downloads/NHVTMA.html'),'html.parser')
all_url=list()
for x in r.find_all('a'):
    all_url.append(x.get('href'))
