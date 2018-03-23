# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:54:08 2017

@author: aditya royal
"""

obj=[u'a',u'd',u'c',u'f   is a good boy',u'k',u'l',u'o']
print [kk.strip() for k in obj for kk in k.split(" ")]
