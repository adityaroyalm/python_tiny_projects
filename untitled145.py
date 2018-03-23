# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:19:40 2018

@author: aditya royal
"""
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as  plt
df=pd.read_excel('C:/Users/aditya royal/Downloads/MortgageDefaulters.xlsx',sheetname='MortgageDefaulters')
df=pd.get_dummies(df,columns=['First_home','OUTCOME','State'],drop_first=True)

x_train,x_test,y_train,y_test=train_test_split(df.drop(['OUTCOME_non-default'],axis=1),df['OUTCOME_non-default'],random_state=2)
df['orig_apprd_val_amt']=[np.median(df['orig_apprd_val_amt'].values) if x==0 else x for x in df['orig_apprd_val_amt'].values ]
df['Tot_mthly_debt_exp']=[np.median(df['Tot_mthly_debt_exp'].values) if x==0 else x for x in df['Tot_mthly_debt_exp'].values ]
df_new=pd.DataFrame(columns=['neighbors','train_accuracy','validation_accuracy'])
for k in range(1,10):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    predicted_train=knn.predict(x_train)
    predicted_test=knn.predict(x_test)
    accuracy_train=accuracy_score(y_train,predicted_train)
    accuracy_valid=accuracy_score(y_test,predicted_test)
    df_new=df_new.append({'neighbors':k,'train_accuracy':accuracy_train,'validation_accuracy':accuracy_valid},ignore_index=True)
plt.plot(df_new['neighbors'],df_new['train_accuracy'],label='training')
plt.plot(df_new['neighbors'],df_new['validation_accuracy'],label='validation')
plt.legend()
plt.xlabel('neighbors')
plt.ylabel('accuracy')
plt.legend('neighbors vs accuracy')
bestvalidscore=max(df_new['validation_accuracy'])
plt.axhline(bestvalidscore)
plt.show()