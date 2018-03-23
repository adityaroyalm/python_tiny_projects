# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:36:52 2017

@author: aditya royal
"""
str ="""Email_Address,Nickname,Group_Status,Join_Year
aa@aaa.com,aa,Owner,2014
bb@bbb.com,bb,Member,2015
cc@ccc.com,cc,Member,2017
dd@ddd.com,dd,Member,2016
ee@eee.com,ee,Member,2020"""
import re
for i in re.finditer('([a-zA-Z]+)(@)([a-zA-Z]+).com', str):
    print i.group(0)
data=pd.read_csv('AirPassengrs.csv',parse_dates='Month',index_col='Month')
