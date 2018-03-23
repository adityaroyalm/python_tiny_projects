# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:17:21 2017

@author: aditya royal
"""

import requests
response=requests.get('https://business.keenechamber.com/list/category/automotive-and-transportation-12')
tabala=response.content