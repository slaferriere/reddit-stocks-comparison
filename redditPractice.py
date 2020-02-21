#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:11:30 2020

@author: slaferriere
"""

import praw


reddit = praw.Reddit(client_id='ze-7yR87wM5GRQ',
                     client_secret='oYssobY3zwk0FMiOrw64LndiNPw',
                     user_agent='my user agent')

subreddit = reddit.subreddit('wallstreetbets')

msftComments = 0

for submission in subreddit.search('msft', time_filter = 'day'):
    if not submission.stickied:
        print('Title: {}, \nUpvotes: {}, \nDownvotes: {}'.format(submission.title,
                                                             submission.ups,
                                                             submission.downs))
        
        submission.comments.replace_more(limit=None)
        comments = submission.comments.list() #Will print every single comment and reply
        
        for comment in comments:
            print( 20 *'-')
            print(comment.body.encode("utf-8", errors='ignore')) #Ignoring empjis
            if ('MSFT' in comment.body or 'msft' in comment.body):
                msftComments += 1
                
print(msftComments)
