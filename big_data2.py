# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 19:05:28 2018

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 15:55:35 2018

@author: aditya royal
"""
#from sklearn import tree
import seaborn as sns
import matplotlib.pyplot as plt
#from sklearn.metrics import accuracy_score
#import pandas as pd
#from sklearn.cluster import KMeans
#from sklearn.model_selection import train_test_split
#import numpy as np
#from sklearn.metrics import r2_score
#from datetime import datetime
#from sklearn import linear_model
#from collections import Counter
#import dataset
#df=pd.read_csv('C:/Users/aditya royal/final.txt',sep=' ')
# assigning column names
#df.columns=['id','year-mm-day','windspeedgust','temp','alt_inches']
######function to find***,na in a column and replace them with mean of that column
def preprocessing(c):
    mask=list()
    for x in df.iloc[:,c]:
        try:
            if '*' in str(x):
                mask.append(False)
            else:
               mask.append(True) 
        except:
            mask.append(True)
    digits=[y for x,y in zip(mask,df.iloc[:,c]) if x]
    meandigit=pd.DataFrame([float(x) for x in digits]).mean()
    df.iloc[:,c]=[y if x else meandigit[0] for x,y in zip(mask,df.iloc[:,c])]
    df.iloc[:,c].fillna(meandigit[0],inplace=True)
# ####creating seperately year and month ,so that it will be easy for analysis
#df['year']=[x[0:4] for x in pd.Series(df.loc[:,'year-mm-day'],dtype=str)]
#df['month']=[x[4:6] for x in pd.Series(df.loc[:,'year-mm-day'],dtype=str)]
#####deleting year-mm-day column
#del df['year-mm-day']
#preprocessing(1)
#preprocessing(2)
#preprocessing(3)
#preprocessing(4)
####### performing k-means clustering on the dataset
##creating train,test split
#train,test=train_test_split(df.iloc[:,:6],random_state=42)
#unique_id=np.unique(df['id'])
#kmeans=KMeans(n_clusters=6).fit(np.array(train.iloc[:,1:6].values))
#result_id=kmeans.predict(np.array(train.iloc[:,1:6].values))
#labels=kmeans.labels_

##matching and seeing what are the station id_s which are grouped together
#fi=[[]*1500 for x in range(np.unique(kmeans.labels_).shape[0]+1)]
#i=0
#j=0
#for x in np.unique(labels):
#    i=0
#    for y in result_id:
#        if y==x:
#            fi[j].append(train.iloc[i,0])
#        i=i+1
#    j=j+1
#j=0
#i=0
#for i in range(len(fi)):
 ##   sorting the list in descending order on number of counts for a particular cluster
#    fi[i]=sorted(Counter(fi[i]).items(),key=lambda x:x[1],reverse=True)
########Decision tree classifier
#i=0
#train=train.reset_index(drop=True)
#test=test.reset_index(drop=True)

#clf=tree.DecisionTreeClassifier()
#clf.fit(np.array(train.iloc[:,[1,2,3,5]].values),np.array(train.iloc[:,4].values))
#result=clf.predict(np.array(test.iloc[:,[1,2,3,5]].values))
#accuracy=accuracy_score(np.array(test.iloc[:,4].values),result)
#p=0
#a=list()
#b=list()
#bi=list()
# representing output for clustering
#import matplotlib.pyplot as plt
#for cl in range(len(fi)):
 #   a=list()
  #  b=list()
   # g=pd.DataFrame()
    #for x,y in fi[cl]:
    
     #   a.append(x)
      #  b.append(y)
    #bi.append(len(np.unique(a)))
    #g['station_id']=a
    #g['count_in_cluster']=b 
    #fig=sns.stripplot(g['station_id'],g['count_in_cluster'],data=g)
    #fig.set_xticklabels(fig.get_xticklabels(),rotation=90)
    #plt.title('CLUSTER'+str(cl))
    #plt.show()
wrong=list()
for x,y in zip(result,test.iloc[:,4].values):
    if int(x)!=int(y):
        wrong.append(y)
plt.hist([[int(x) for x in wrong],list([int(x) for x in df['year'].values])],alpha=0.5,label=['wrong_classified','total_values'])
plt.xlabel('year')
plt.legend()

