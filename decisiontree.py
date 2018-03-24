# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 17:14:45 2018

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:19:40 2018

@author: aditya royal
"""
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np
#classification problem
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as  plt
df=pd.read_excel('C:/Users/aditya royal/Downloads/MortgageDefaulters.xlsx',sheetname='MortgageDefaulters')
df=pd.get_dummies(df,columns=['First_home','OUTCOME','State'],drop_first=True)

x_train,x_valid,y_train,y_valid=train_test_split(df.drop(['OUTCOME_non-default'],axis=1),df['OUTCOME_non-default'],random_state=2)
x_valid,x_test,y_valid,y_test=train_test_split(x_valid,y_valid,random_state=2)
df['orig_apprd_val_amt']=[np.median(df['orig_apprd_val_amt'].values) if x==0 else x for x in df['orig_apprd_val_amt'].values ]
df['Tot_mthly_debt_exp']=[np.median(df['Tot_mthly_debt_exp'].values) if x==0 else x for x in df['Tot_mthly_debt_exp'].values ]
df_new=pd.DataFrame(columns=['leaf_nodes','train_accuracy','validation_accuracy'])
for k in range(2,10):
    #changing the number of leaf nodes
    clf=DecisionTreeClassifier(max_leaf_nodes=k)
    clf.fit(x_train,y_train)
    predicted_train=clf.predict(x_train)
    predicted_valid=clf.predict(x_valid)
    accuracy_train=accuracy_score(y_train,predicted_train)
    accuracy_valid=accuracy_score(y_valid
                                  ,predicted_valid)
    #appending observations to dataframe columns
    df_new=df_new.append({'leaf_nodes':k,'train_accuracy':accuracy_train,'validation_accuracy':accuracy_valid},ignore_index=True)
plt.plot(df_new['leaf_nodes'],df_new['train_accuracy'],label='training')
plt.plot(df_new['leaf_nodes'],df_new['validation_accuracy'],label='validation')
plt.legend()
plt.xlabel('leaf_nodes')
plt.ylabel('accuracy')
bestvalidscore=max(df_new['validation_accuracy'])
plt.axhline(bestvalidscore,linestyle=':')
plt.show()
########test datset
clf=DecisionTreeClassifier(max_leaf_nodes=3)
clf.fit(x_train,y_train)
predicted=clf.predict(x_test)
test_accuracy=accuracy_score(y_test,predicted)