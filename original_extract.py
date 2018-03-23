# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:08:50 2017

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:24:06 2017

@author: aditya royal
"""


import requests
import re
try:
    from urlparse2 import urljoin
except Exception:
    from urllib.parse import urljoin
from bs4 import BeautifulSoup
iteration=0
a=0
b=0
links2=list()
while (iteration<1):
     all_url=list()
     links=list()
     emails=dict()
     #r=BeautifulSoup(requests.get(urlo).text)
     r=BeautifulSoup(open('NHVTMA.html'),'html.parser')
     def extract_links(r):
         for x in r.find_all('a'):
             all_url.append(x.get('href'))
         for url in all_url:
            try:
                open_=requests.get(url)
                response=open_.content.decode('utf-8')
                soup=BeautifulSoup(response,'html.parser')
                for link in soup.find_all('a'):
                    if link.startswith('/'):
                            link=urljoin(url,link)
                    if re.findall(r'(automobile)|(Automobile)|(AUTOMOBILE)|(AUTOMOTIVE)|(Automotive)|(automotive)',str(link)):
                        links.append(link.get('href'))
            except Exception as e:
                print(e)
         return links
     a=b
     b=a+2
     links2=links[a:b]
     def extract_emails(links2):
         for url in links2:
             try:
                 response=requests.get(url)
                 if response.status_code!=200:
                     print('connection refused')
                 else:
                     contents=requests.get(url).content.decode('utf-8')
                     emails[url]= re.findall(r'[\w\.-]+@[\w\.-]+',contents)
             except Exception as e: 
                 print(e)
         return emails
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
     def main():
         extract_links(r)
         extract_emails(extract_links(r))
         unique_emails(extract_emails(links2))
     main()
     iteration=iteration+1
     print(emails)