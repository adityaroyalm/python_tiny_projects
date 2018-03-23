# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 12:15:23 2018

@author: aditya royal
"""

import pandas as pd
import numpy as np
df=pd.DataFrame({'cancer':np.array((0,0,0,1,1)),'id':np.array((-1,-2,10,-10,-20))})
df=df.sort_values(['id'])
print (df['cancer'])