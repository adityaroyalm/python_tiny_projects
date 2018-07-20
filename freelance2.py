# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:58:36 2018

@author: aditya royal
"""

import facebook-sdk
import requests
graph = facebook.GraphAPI(access_token="EAAW7mSr2MAcBALWFJiA22ZBxwOWZB7WbBLj2WiWLHT2nqd91ji5dtwjTk6KV6sYp89cleFPwmE3q4DqqGTzK16rEIlbWvZBx6GSvAdQolwkaQK1q9oMZC4gy3TA2dW5X3ll8nVrfPSaTeiux9PmjTpi7TgUwvHxCnTpnfY8yNPGQEdkE5IZA68ASWKTDk6UUZD", version=2.11)
#site_info = graph.get_object(id="https://developers.facebook.com/docs/graph-api/reference/url/",
                           #  fields="og_object")
#j=(site_info["og_object"]["description"])
users = graph.search(type='user',q='Mark Zuckerberg')
for user in users['data']:
    print('%s %s' % (user['id'],user['name'].encode()))