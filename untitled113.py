# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:56:30 2017

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:24:06 2017

@author: aditya royal
"""


import requests
import re
import urllib2
import time
from bs4 import BeautifulSoup
iteration=0
r=BeautifulSoup(open('C:/Users/aditya royal/Downloads/NHVTMA.html'),'html.parser')
a=0
b=0
emails=dict()
while (iteration<1):
     a=b
     b=a+2
     links2=links[a:b]
     def extract_emails(links2):
         for url in links2:
             try:
                 response=requests.get(url)
                 if response.status_code!=200:
                     print 'connection refused'
                 else:
                     contents=requests.get(url).content.decode('utf-8')
                     emails[url]= re.findall(r'[\w\.-]+@[\w\.-]+',contents)
             except Exception as e: 
                 print(e)
         return emails
     def main():
         extract_emails(links)
     main()
     iteration=iteration+1