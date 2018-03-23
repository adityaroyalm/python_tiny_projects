# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 23:42:32 2017

@author: aditya royal
"""

import requests
obj=requests.get("https://en.wikipedia.org/wiki/Main_Page")
objj=obj.content.decode('utf-8')
nu= objj.find('Did you know')