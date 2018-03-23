# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:18:28 2017

@author: aditya royal
"""
from pandas import DataFrame
n=10
import numpy as np
df = DataFrame(np.random.randint(4, size=(n, 2)), columns=list('ab'))
kj=df.loc[df['a'].isin([1, 2]).tolist(),:]