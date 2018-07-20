# -*- coding: utf-8 -*-
"""
Created on Sat Oct 07 10:48:21 2017

@author: aditya royal
"""

def duplicate_regression(df,a,b,accu=2):
    import matplotlib.pyplot as plt
    from sklearn import linear_model
    import numpy as np
    regr=linear_model.LinearRegression()
    dfx=df.sort_values(by=a)
    dfx.reset_index(drop=True)
    df_x=dfx.iloc[0:len(dfx)/2,:]
    df_x2=dfx.iloc[len(dfx)/2:,:]
    dfy=df.sort_values(by=b)
    dfy.reset_index(drop=True)
    df_y=dfy.iloc[0:len(dfy)/2,:]
    df_y2=dfy.iloc[len(dfy)/2:,:]
    if (np.absolute(df_x.loc[:,a].corr(df_x.loc[:,b]))>accu*np.absolute(dfx.loc[:,a].corr(dfx.loc[:,b])) or np.absolute(df_x2.loc[:,a].corr(df_x2.loc[:,b]))>accu*np.absolute(dfx.loc[:,a].corr(dfx.loc[:,b]))):
        fitt=regr.fit(df_x.loc[:,a].to_frame(),df_x.loc[:,b].to_frame())
        pred=fitt.predict(df_x.loc[:,a].to_frame())
        fitt2=regr.fit(df_x2.loc[:,a].to_frame(),df_x2.loc[:,b].to_frame())
        pred2=fitt2.predict(df_x2.loc[:,a].to_frame())
        print(plt.plot(df_x.loc[:,a],pred))
        print(plt.plot(df_x2.loc[:,a],pred2))
        print(plt.scatter(dfx.loc[:,a],dfx.loc[:,b]))
    elif(np.absolute(df_y.loc[:,a].corr(df_y.loc[:,b]))>accu*np.absolute(dfy.loc[:,a].corr(dfy.loc[:,b])) or np.absolute(df_y2.loc[:,a].corr(df_y2.loc[:,b]))>accu*np.absolute(dfy.loc[:,a].corr(dfy.loc[:,b]))):
        fitt=regr.fit(df_y.loc[:,a].to_frame(),df_y.loc[:,b].to_frame())
        pred=fitt.predict(df_y.loc[:,a].to_frame())
        fitt2=regr.fit(df_y2.loc[:,a].to_frame(),df_y2.loc[:,b].to_frame())
        pred2=fitt2.predict(df_y2.loc[:,a].to_frame())
        print(plt.plot(df_y.loc[:,a],pred))
        print(plt.plot(df_y2.loc[:,a],pred2))
        print(plt.scatter(dfy.loc[:,a],dfy.loc[:,b]))
    else:
        fitt=regr.fit(dfx.loc[:,a].to_frame(),dfx.loc[:,b].to_frame())
        pred=fitt.predict(dfx.loc[:,a].to_frame())
        print(plt.scatter(dfx.loc[:,a],dfx.loc[:,b]))
        print(plt.plot(dfx.loc[:,a],pred))
    