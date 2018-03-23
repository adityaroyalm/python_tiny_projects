# -*- coding: utf-8 -*-
"""
Created on Sun May 14 14:24:21 2017

@author: aditya royal
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
BASE_URL = "http://www.chicagoreader.com"
def get_category_links(section_url):
    html=urlopen(BASE_URL,'html.parser')