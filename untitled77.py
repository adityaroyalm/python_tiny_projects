# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:28:20 2017

@author: aditya royal
"""

from sklearn.metrics import log_loss
p=df_train['is_duplicate'].mean()
log_loss(df_train['is_duplicate'], np.zeros_like(df_train['is_duplicate'])+p)

