# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 12:02:57 2017

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
a=0
b=0
#urlo='http://www.lakesregionchamber.org/list'
links2=list()
while (iteration<1):
     all_url=list()
     links=list()
     emails=dict()
     #r=BeautifulSoup(requests.get(urlo).text)
     r=BeautifulSoup(open('https://drive.google.com/open?id=148ss6LUQzoqr-H8D8eRbqBOPfBg73kJX'))
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
                 print'erros is'+ e
         return emails
         print emails
     checker=set()    
     def unique_emails(emails):
         for key in emails:
             value = list()
             for emailid in emails[key]:
                 if emailid not in checker:
                     checker.add(emailid)
                     value.append(emailid)
             emails[key] = value
         return emails
         print emails
     def main():
         extract_links(r)
         extract_emails(extract_links(r))
         unique_emails(extract_emails(links2))
     main()
     iteration=iteration+1
