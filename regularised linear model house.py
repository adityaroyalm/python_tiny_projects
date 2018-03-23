# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:44:15 2017

@author: aditya royal
"""  
###make the variables more normal by log(feature+1)
import matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from scipy.stats import skew
train=pd.read_csv('C:/Users/aditya royal/Desktop/MLsoftaware_projects/house prices/train (3).csv')
test=pd.read_csv('C:/Users/aditya royal/Desktop/MLsoftaware_projects/house prices/test (3).csv')
matplotlib.rcParams['figure.figsize']=(12,6)
prices = pd.DataFrame({"price":train["SalePrice"], "log(price + 1)":np.log1p(train["SalePrice"])})
prices.hist()
all_data=pd.concat(((train.loc[:,'MSSubClass':'SaleCondition'],
                      test.loc[:,'MSSubClass':'SaleCondition'])))
numeric_feats=all_data.dtypes[all_data.dtypes !='object'].index
skewed_feats=train[numeric_feats].apply(lambda x:skew(x.dropna()))
skewed_feats = train[numeric_feats].apply(lambda x: skew(x.dropna()))
skewed_feats=skewed_feats[skewed_feats>0.75].index
all_data[skewed_feats] = np.log1p(all_data[skewed_feats])
all_data = all_data.fillna(all_data.mean())
all_data = pd.get_dummies(all_data)
#creating matrices for sklearn:
X_train = all_data[:train.shape[0]]
X_test = all_data.iloc[train.shape[0]:,]
y = train.SalePrice
from sklearn.linear_model import Ridge
def rmse_cv(model):
    rmse=np.sqrt(-cross_val_score(model,X_train,y,cv=5))
    return(rmse)
#model_ridge=ridge()
alphas=[0.05,0.1,0.3,1,3,5,10,15,30,50,75]
cv_ridge=[rmse_cv(Ridge(alpha=1)).mean() for alpha in alphas]
#cv_ridge=pd.Series(cv_ridge,index=alphas)
#cv_ridge.plot(title='validation-just do it')
#plt.xlabel('alpha')
#plt.ylabel('rmse')
    