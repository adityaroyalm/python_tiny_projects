# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 13:54:27 2017

@author: aditya royal
"""

import facebook
import requests
graph = facebook.GraphAPI(access_token='EAACEdEose0cBABjMwUfZCUoKZC9uieWU3rSQXatJH3fOsuXgvwArhMPVa0jtzMilfjroAVCh8TuZAyp0ZCCrJpJu45f0UIeuIyaBMbRzTwqdwNST5hbaMkA3vZBVLZBneXtpOFjwBaZAtLZAhQ9ZCFB3W7e2idxBWfEXy9rd3pAunCGZBVUDpLtRlwsoZBxZAAts79AZD', version='2.7')
posts = graph.get_object(id='me')
post_id_1='355653191275220_607814462725757'
post_id_2='355653191275220_614157325424804'
post_ids = [post_id_1, post_id_2]
event_ids = ["1024123750994999"]
events = graph.get_objects(ids=post_ids, fields='reactions')

# Each given id maps to an object the contains the requested fields.
#for event_id in event_ids:
 #   print(posts[event_id]['attending_count'])
post_id_1='355653191275220_607814462725757'
post_id_2='355653191275220_614157325424804'
post_ids = [post_id_1, post_id_2]
posts = graph.get_objects(ids=post_ids)

# Each given id maps to an object.
for post_id in post_ids:
    print(posts[post_id]['created_time'])
# Writes 'Hello, world' to the active user's wall.
#graph.put_object(parent_object='me', connection_name='feed',
 #                message='Hello, world')

# Writes a comment on a post
#graph.put_object(parent_object=post_id_1, connection_name='comments',
 #                message='First!')