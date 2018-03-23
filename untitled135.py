# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 00:43:41 2018

@author: aditya royal
"""

class Inst:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("Hello, I am %s, and my name is %s" %(self, self.name))

inst=Inst('somename')
inst.introduce()