# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:08:32 2017

@author: aditya royal
"""

from nltk.stem.wordnet import WordNetLemmatizer
lem=WordNetLemmatizer()
from nltk.stem.porter import PorterStemmer
stem=PorterStemmer()
word='multiplying'
print lem.lemmatize(word)
print stem.stem(word)
