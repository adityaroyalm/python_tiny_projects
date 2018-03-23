# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 23:41:24 2017

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 07 16:18:37 2017

@author: aditya royal
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 07 10:48:21 2017

@author: aditya royal
"""

    
def otherfunc(df,a,b,multiplier_x,multiplier_y,lines_x,lines_y):
    print lines_x
    print lines_y
    multiplier_x=1
    multiplier_y=1
    decx=0
    decy=0
    slopex=list()
    import scipy.stats
    slopey=list()
    from sklearn import linear_model
    import matplotlib.pyplot as plt
    import numpy as np
    regr=linear_model.LinearRegression()
    dfx=df.sort_values(by=a)
    dfx.reset_index(drop=True)
    dfy=df.sort_values(by=b)
    dfy.reset_index(drop=True)
    for p in range(lines_x):
        if (lines_x==0):
            break
        df_x=dfx.iloc[p*len(dfx)/lines_x:(p+1)*len(dfx)/lines_x,:]
        decider_x=np.absolute(np.absolute(df_x.loc[:,a].corr(df_x.loc[:,b]))/np.absolute(dfx.loc[:,a].corr(dfx.loc[:,b])))
        if (decider_x>=multiplier_x or decider_x<=1/multiplier_x):
            fitt=regr.fit(df_x.loc[:,a].to_frame(),df_x.loc[:,b].to_frame())
            pred=fitt.predict(df_x.loc[:,a].to_frame())
            print lines_x
            print lines_y
            if(lines_x==lines_y):
                slopex[p], intercept, r_value, p_value, std_err=scipy.stats.linregress(df_x.loc[:,a],pred[p])  
                decx=np.arange(len(slopex)).corr(np.array(slopex))
                print 'o'
                print slopex[p]
                print len(slopex)
    for k in range(lines_y):
        if (lines_y==0):
            break
        df_y=dfy.iloc[k*len(dfy)/lines_y:(k+1)*len(dfy)/lines_y,:] 
        decider_y=np.absolute(np.absolute(df_y.loc[:,a].corr(df_y.loc[:,b]))/np.absolute(dfy.loc[:,a].corr(dfy.loc[:,b])))
        if (decider_y>=multiplier_y or decider_y<=1/multiplier_y):
            fitt=regr.fit(df_y.loc[:,a].to_frame(),df_y.loc[:,b].to_frame())
            pred=fitt.predict(df_y.loc[:,a].to_frame())
            if(lines_x==lines_y):
                slopey[p], intercept, r_value, p_value, std_err=scipy.stats.linregress(df_y.loc[:,a],pred[p])
                decy=np.arange(len(slopey)).corr(slopey)
    if (decx<decy):
        for p in range(lines_x):
            if (lines_x==0):
                break
            df_x=dfx.iloc[p*len(dfx)/lines_x:(p+1)*len(dfx)/lines_x,:]
            decider_x=np.absolute(np.absolute(df_x.loc[:,a].corr(df_x.loc[:,b]))/np.absolute(dfx.loc[:,a].corr(dfx.loc[:,b])))
            if (decider_x>=multiplier_x or decider_x<=1/multiplier_x):
                fitt=regr.fit(df_x.loc[:,a].to_frame(),df_x.loc[:,b].to_frame())
                pred=fitt.predict(df_x.loc[:,a].to_frame())
                print(plt.plot(df_x.loc[:,a],pred))
    
    if(decy<decx):
        for k in range(lines_y):
            if (lines_y==0):
                break
            df_y=dfy.iloc[k*len(dfy)/lines_y:(k+1)*len(dfy)/lines_y,:] 
            decider_y=np.absolute(np.absolute(df_y.loc[:,a].corr(df_y.loc[:,b]))/np.absolute(dfy.loc[:,a].corr(dfy.loc[:,b])))
            if (decider_y>=multiplier_y or decider_y<=1/multiplier_y):
                fitt=regr.fit(df_y.loc[:,a].to_frame(),df_y.loc[:,b].to_frame())
                pred=fitt.predict(df_y.loc[:,a].to_frame())
                print(plt.plot(df_y.loc[:,a],pred))
    if(lines_x!=lines_y):
        for p in range(lines_x):
            if (lines_x==0):
                break
            df_x=dfx.iloc[p*len(dfx)/lines_x:(p+1)*len(dfx)/lines_x,:]
            decider_x=np.absolute(np.absolute(df_x.loc[:,a].corr(df_x.loc[:,b]))/np.absolute(dfx.loc[:,a].corr(dfx.loc[:,b])))
            if (decider_x>=multiplier_x or decider_x<=1/multiplier_x):
                fitt=regr.fit(df_x.loc[:,a].to_frame(),df_x.loc[:,b].to_frame())
                pred=fitt.predict(df_x.loc[:,a].to_frame())
                print(plt.plot(df_x.loc[:,a],pred))
    if(lines_x!=lines_y):
        for k in range(lines_y):
            if (lines_y==0):
                break
            df_y=dfy.iloc[k*len(dfy)/lines_y:(k+1)*len(dfy)/lines_y,:] 
            decider_y=np.absolute(np.absolute(df_y.loc[:,a].corr(df_y.loc[:,b]))/np.absolute(dfy.loc[:,a].corr(dfy.loc[:,b])))
            if (decider_y>=multiplier_y or decider_y<=1/multiplier_y):
                fitt=regr.fit(df_y.loc[:,a].to_frame(),df_y.loc[:,b].to_frame())
                pred=fitt.predict(df_y.loc[:,a].to_frame())
                print(plt.plot(df_y.loc[:,a],pred))
    #original regression line
    #fitt=regr.fit(dfx.loc[:,a].to_frame(),dfx.loc[:,b].to_frame())
    #pred=fitt.predict(dfx.loc[:,a].to_frame())
    #print(plt.plot(dfx.loc[:,a],pred))
    