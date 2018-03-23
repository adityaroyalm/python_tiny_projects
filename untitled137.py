# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:27:34 2018

@author: aditya royal
"""
year=1988
station='adi'
#output=dict()
try:
    if year in output[station]:
        pass
    else:
        output.setdefault(station,[]).append(year)
except:
    output.setdefault(station,[]).append(year)