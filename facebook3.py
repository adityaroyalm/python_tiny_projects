# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:58:36 2018

@author: aditya royal
"""

import facebook
import requests
import pandas as pd
import boto3
s3 = boto3.client('s3')
obj = s3.get_object(Bucket='adityafirstbucket', Key='Book1.xlsx')
df = pd.read_excel(io.BytesIO(obj['Body'].read()))
li=list()
graph = facebook.GraphAPI(access_token="your access token", version=2.11)
#site_info = graph.get_object(id="https://developers.facebook.com/docs/graph-api/reference/url/",
                           #  fields="og_object")
#j=(site_info["og_object"]["description"])
for i in range(len(df.index)):
    users = graph.search(type='page',q=str(df.loc[i,'company'])+str(df.loc[i,'city']))
    for user in users['data']:
        li.append('%s %s' % (user['id'],user['name'].encode()))
        break;
