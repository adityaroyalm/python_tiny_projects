# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:15:33 2017

@author: aditya royal
"""
import re

def _remove_regex(input_text, regex_pattern):
    urls = re.finditer(regex_pattern, input_text) 
    for i in urls: 
        input_text = re.sub(i.group(0).strip(), '', input_text)
    return input_text

regex_pattern = "#[\w]*"  

print _remove_regex("remove this #hashtag from analytics vidhya", regex_pattern)
