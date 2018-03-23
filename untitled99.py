# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 01:03:14 2017

@author: aditya royal
"""

import requests
from lxml import etree
address= 'paloncha'
#key='AIzaSyAi0XWQB5J4lA1hER2sGc-osip8i1MxwGs'
#response=requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyB33I9LkXt7FNA4GsmRp_z_YHUQnxaiCFE" %(address))
response=requests.get('https://www.amazon.com/')
statuscode=response.status_code

root=etree.XML(response)
#data2=data['results'][0]['geometry']['location']['lat']
etree.tostring(root,pretty_print=True).decode('utf-8')
