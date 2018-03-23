# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:16:21 2018

@author: aditya royal
"""

import nltk
from nltk.book import *
tokens=nltk.word_tokenize(text1)
text1.pos_tag(tokens)
text1.concordance('monstrous')
text1.similar('monstrous')
text2.common_contexts(['monstrous','very'])