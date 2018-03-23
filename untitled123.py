# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:00:13 2018

@author: aditya royal
"""
for x in range(100,1000):
    if (str(x)[1]!=str(x)[0])&(str(x)[1]!=str(x)[2])&(str(x)[0]!=str(x)[2]) :
        if int(str(x)[::-1])%7==0:
            if int(x)%7==0:
                print x
        
        