# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 20:40:29 2017

@author: aditya royal
"""

def factorial(x):
    result=1
    for i in range(2,x+1):
        result*=i
    return result
if __name__ == "__main__":
    import sys
    x=int(sys.argv[1])
    print factorial(x)
    