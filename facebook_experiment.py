# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:48:18 2018

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:37:41 2018

@author: aditya royal
"""
import pandas as pd
import time
from bs4 import BeautifulSoup
import io
import re
import xlrd
import boto3
s3 = boto3.client('s3')
obj= s3.get_object(Bucket='adityafirstbucket', Key='Book1.xlsx')
df = pd.read_excel(io.BytesIO(obj['Body'].read()))
obj=pd.DataFrame(df.iloc[:,1].values)
li=obj.iloc[0,:]
obj.columns=li
obj.drop([0],inplace=True)
import requests
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
    #for i in range(numOpen):
     #   webbrowser.open('http://google.com' + tag_a[i].get('href'))
    for x in tag_a:
        if (x.get('href').startswith('/url?q=https://www.facebook.com/')):
            if(re.search((str(x.get('href'))[2:-2]),company,flags=re.I)):
                fb_page.append(x.get('href'))