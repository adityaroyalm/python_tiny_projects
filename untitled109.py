# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 14:13:28 2017

@author: aditya royal
"""
from bs4 import BeautifulSoup
import requests
import requests.exceptions
#from urllib.parse import urlsplit
from collections import deque
import re
new_urls = deque(['http://www.themoscowtimes.com/'])