# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:24:06 2017

@author: aditya royal
"""


import requests
import re
from urlparse2 import *
from bs4 import BeautifulSoup
iteration=0
a=0
b=0
links=list()
while(iteration<1):
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
                    url_parse=urlparse(url)
                    base_url="{0.scheme}://{0.netloc}".format(url_parse)
                    if re.findall(r'(automobile)|(Automobile)|(AUTOMOBILE)|(AUTOMOTIVE)|(Automotive)|(automotive)',str(link)):
                       if link.get('href').startswith('/'):
                           link=urljoin(base_url,link)
                       else:    
                           links.append(link.get('href'))
            except Exception as e:
                print(e)
         return links
     def extract_emails(links):
         for url in links:
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
         with open('final2.csv', 'a') as f:
             [f.write('{0},{1}\n'.format(key, value)) for key, value in emails.items()]
         return emails
     def main():
         extract_links(r)
         extract_emails(extract_links(r))
         unique_emails(extract_emails(links))
     iteration=iteration+1    
main()
