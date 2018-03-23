# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:54:14 2017

@author: aditya royal
"""
original_tweet=u'I luv my &lt;3 iphone &amp; you’re awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com'

import HTMLParser
html_parser=HTMLParser.HTMLParser()
tweet=html_parser.unescape(original_tweet)
APPOSTOPHES = {"s" : " is", "'re" : " are"} ## Need a huge dictionary
words = tweet.split()
reformed = [APPOSTOPHES[word] if word in APPOSTOPHES else word for word in words]
reformed = " ".join(reformed)
print reformed
