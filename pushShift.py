#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:57:34 2020

@author: slaferriere
"""

import pandas as pd
import requests
import json
import csv
import time
import datetime
from exportCSV import updateSubs_file

def main():
    
    sub = 'wallstreetbets'
    start_date = 1546300800 # Jan 01, 2019
    end_date = 1548979200 # Dec 31, 2019
    query = 'tsla'
    
    subCount = 0
    global subStats
      

    
    data = getPushshiftSubmissionData(query, start_date, end_date, sub)
    
    while len(data) > 0:
        for submission in data:
            collectSubData(submission)
            subCount+=1
            
            # Calls getPushshiftData() with the created date of the last submission
        print(len(data))
        print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
        start_date = data[-1]['created_utc']
        data = getPushshiftSubmissionData(query, start_date, end_date, sub)
    
    print(len(data))
    updateSubs_file(subStats)


def getPushshiftSubmissionData(query, start_date, end_date, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?title='+str(query)+'&size=1000&after='+str(start_date)+'&before='+str(end_date)+'&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']

def getPushshiftCommentData(query, start_date, end_date, sub):
    url = 'https://api.pushshift.io/reddit/comment/search/?subreddit='+str(sub)+'&aggs=subreddit&q='+str(query)+'&size=1000&after='+str(start_date)+'&before='+str(end_date)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']


def collectSubData(subm):
    
    subData = list() #list to store data points
    title = subm['title']
    url = subm['url']
    
    try:
        flair = subm['link_flair_text']     # Removes flair if one
    except KeyError:
        flair = "NaN"   
        
    author = subm['author']
    sub_id = subm['id']
    score = subm['score']
    created = datetime.datetime.fromtimestamp(subm['created_utc']) #1520561700.0
    numComms = subm['num_comments']
    permalink = subm['permalink']
    
    subData.append((sub_id,title,url,author,score,created,numComms,permalink,flair))
    subStats[sub_id] = subData
    
def collectCommentData(comment):
    
    subData = list()
    author = comment['author']
    body = comment['body']
    
    
    
    
main()