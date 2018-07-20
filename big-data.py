# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:50:38 2018

@author: aditya royal
"""

from mrjob.job import MRJob
from mrjob.step import MRStep
class Task1(MRJob):
    def mapper(self,_,line):
        values=line.split(' ')
        yield(values[2][:4],values[26])
    def reducer(self,keys,values):
        string_values=[x for x in values if x.isdigit()]
        int_values=[int(x) for x in string_values]
        if int_values!=None:
            maxi=max(int_values)
        #mini=min(int_values)
            yield(keys,(maxi))
if __name__ == '__main__':
     Task1.run()