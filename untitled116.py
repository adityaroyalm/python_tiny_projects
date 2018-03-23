# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:04:59 2017

@author: aditya royal
"""
import csv
emails={'a':'sfdsdfs','h':'sdfdfsd','d':'dfadf'}
with open('final9.csv', 'a') as f:
    writer=csv.writer(f)
    writer.writerows(emails.items())