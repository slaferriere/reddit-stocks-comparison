#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 00:49:43 2020

@author: slaferriere
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import datetime


def plotCommentCount(filename):
    
    yDict = {}
    X_data = []
    y_data = []

    dataset = pd.read_csv("\\Reddit Data\\" + filename)
    data = dataset.iloc[:, 5:6].values
    for timeStamp in data:
        timeStamp = timeStamp.tolist()
        date = timeStamp[0]
        date = date.split()
        date = date[0]      
        if date not in X_data:
            X_data.append(date)
        if date not in yDict:
            yDict[date] = 1
        else:
            yDict[date] += 1
    for date in yDict.keys():
        y_data.append(yDict[date])


    plt.plot(X_data, y_data)
    plt.title('Number of posts per day')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.show()

plotCommentCount('tsla.csv')