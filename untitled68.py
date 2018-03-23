# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:12:33 2017

@author: aditya royal
"""

noise_list = ["is", "a", "this", "..."] 
def _remove_noise(input_text):
    words = input_text.split() 
    noise_free_words = [word for word in words if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words) 
    print noise_free_text

_remove_noise("this is a sample text")
import re
result=re.match('AV','AVGS AV Analytics Vidhya')
print result.group(0)
print result.start()
print result.end()

result = re.search(r'Analytics', 'AV Analytics Analytics AV')
print result.group(0)
print result.start()
print result.end()
result=re.findall(r'AV', 'AVA Analytics Analytics AVA')
print result
result=re.split('y','AV Analytics Analytics AV')
print result
result=re.sub('india','world','av is largest in india')
print result
pattern=re.compile('AV')
