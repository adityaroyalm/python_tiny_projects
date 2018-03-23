# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 17:19:50 2017

@author: aditya royal
"""

import pandas as pd
import numpy as np
df_train=pd.read_csv(r'C:\Users\aditya royal\Desktop\MLsoftaware_projects\quora\train.csv')
df_train.head()
from matplotlib import pyplot as plt
quids=pd.Series(df_train['qid1'].tolist()+df_train['qid2'].tolist(),index=range(len(df_train['qid1'])+len(df_train['qid2'])))
plt.hist(quids.value_counts(),bins=50)
plt.yscale('log')
plt.figure(figsize=(12,5))
quest=pd.Series(df_train['question1'].tolist()+df_train['question2'].tolist())
##finding the unique questions##
unique_index=np.unique(np.array(quids),return_index=True)[1].tolist()
unique_quest=quest[unique_index].astype(str)
#doing some EDA on unique_quests,duplicate_quests#
plt.hist(unique_quest.apply(len))
plt.yscale('log')
import collections
dupli= [item for item, count in collections.Counter(quids).items() if count > 1]
plt.hist(quest[dupli].astype(str).apply(len))
plt.yscale('log')
##we can see that if the question has more than 450 words it is not dulicated.
sorte=quids.sort_values()
from itertools import groupby
frequent=[list(j) for i,j in groupby(sorte)]
frequent.sort(key=len,reverse=True)
twenty=frequent[1:20]

#plt.bar(x=[x[i][1] for x in twenty for i in range(len(twenty))],y=[len(x) for x in twenty])
plt.show()
from nltk.corpus import stopwords
stops=set(stopwords.words('english'))
def word_match_share(row):
    q1words={}
    q2words={}
    for word in str(row['question1']).lower().split():
        if word not in stops:
            q1words[word]=1
    for word in str(row['question2']).lower().split():
        if word not in stops:
            q2words[word]=1
    if len(q1words) == 0 or len(q2words) == 0:
        return 0
    shared_words_in_q1=[w for w in q1words.keys() if w in q2words]
    shared_words_in_q2=[w for w in q2words.keys() if w in q1words]
    R=(len(shared_words_in_q1)+len(shared_words_in_q2))/(len(q1words)+len(q2words))
    return R
train_word_match = df_train.apply(word_match_share, axis=1, raw=True)
plt.figure(figsize=(15, 5))
plt.hist(train_word_match[df_train['is_duplicate'] == 0], bins=20, normed=True, label='Not Duplicate')
plt.hist(train_word_match[df_train['is_duplicate'] == 1], bins=20, normed=True, alpha=0.7, label='Duplicate')
plt.legend()
plt.title('Label distribution over word_match_share', fontsize=15)
plt.xlabel('word_match_share', fontsize=15)
