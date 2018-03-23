# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 13:54:27 2017

@author: aditya royal
"""

import facebook
import json
import requests
graph = facebook.GraphAPI(access_token='EAACEdEose0cBAOIqqSLeV0lvaqNuZBVz91S5ZBv8vKlY2kGEyqGsEWPdUrH8qEAWALWHM72yeExsIxPXuNDloF2i0XT6GvOZBFSIoJ4ZCkccCLFkgq8ZA7Kt2mqWoy5OD2M3vfuoxCqMZANENIEHmMZAakxqD5vkCQkcGSZBNmdw7hbaFiEKj9uBKpUcZD', version='2.7')
posts = graph.get_object(id='me')
event_ids = ["102412794999"]
feeds=graph.get_connections(posts['id'],'feed')
result=json.dumps(feeds)
k=feeds['data']
listt=[]
for key in range(len(k)):
    listt.append(k[key]['id'])
post = graph.get_objects(ids=listt, fields='reactions')
list2=[]
l=[]
o=[]
for Key in post:
   l.append(post[Key])
for x in range(len(l)):
   if len(l[x])==2:
       o.append(l[x]['reactions']['data'])
for i in o:
    for j in i:
           list2.append(j['type'])
unique_list=set()
unique=[x for x in list2  if x not in unique_list and (unique_list.add(x) or True)]
for x in unique:
    print(x,list2.count(x))
