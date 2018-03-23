# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 01:02:36 2017

@author: aditya royal
"""
import time
from functools import wraps
 
 
def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (function.func_name, str(t1-t0))
               )
        return result
    return function_timer