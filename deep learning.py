# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:05:08 2017

@author: aditya royal
"""
import sys
import os
import os.path as osp
import numpy as np
import pandas as pd
from subprocess import check_output
#print(check_output(['ls','C:/Users/aditya royal/Desktop/MLsoftaware_projects/deeplearning']).decode('utf8'))
df=pd.read_csv('C:/Users/aditya royal/Desktop/MLsoftaware_projects/deeplearning/Sheet_1.csv',encoding='latin-1')
df=df.drop(['Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7'],axis=1)
#renaming columns
df=df.rename(columns={'v1':'class','v2':'Responses'})
print(df.head())
df2=pd.read_csv('C:/Users/aditya royal/Desktop/MLsoftaware_projects/deeplearning/Sheet_2.csv',encoding='latin-1')
df2.rename(columns={'v1':'class','v2':'Resumes'})
#output is value,counting number of repeated values
print(df2['class'].value_counts())
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
def wordcloud(dataframe):
    stopwords=set(STOPWORDS)
    wordcloud=WordCloud(background_color='white',stopwords=stopwords).generate(" ".join([i for i in dataframe.str.upper()]))
from wordcloud import WordCloud,STOPWORDS
def wordcloud(dataframe):
    stopwords=set(STOPWORDS)
    wordcloud=WordCloud(background_color='white',stopwords=stopwords).generate(" ".join([i for i in dataframe.str.upper()]))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.title('bag_composition')
wordcoud(df['response_text'])
    