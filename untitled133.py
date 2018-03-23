# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:31:19 2018

@author: aditya royal
"""

import numpy as np

def rand1():
    randomlist = []
    np.random.seed(123)
    for x in range(10):
        y = np.random.randint(1,10)
        randomlist.append(y)
    return randomlist
def rand2():
    print(rand1())
rand2()
    