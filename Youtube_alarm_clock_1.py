# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 23:46:14 2016

@author: Abhishek
"""

import datetime
from time import sleep
import random
import webbrowser


def seconds_elapsed(current,later):
    h1,m1,s1 = current.hour,current.minute,current.second
    h2,m2,s2 = later.hour,later.minute,later.second
    
    current_seconds = h1*60*60 + m1*60 + s1
    later_seconds = h2*60*60 + m2*60 + s2
    return(later_seconds-current_seconds)
    
while True:
    try:
        FMT = '%H:%M:%S'
        
        x = raw_input('please enter the alarm time in HH:MM:SS format\n' )
        alarmtime = datetime.datetime.strptime(x,FMT).time()
        now = datetime.datetime.now().strftime(FMT)
        now = datetime.datetime.strptime(now,FMT).time()
        sleeptime = seconds_elapsed(now,alarmtime)
        
        print sleeptime

    except:
        print 'please enter correct format'
        continue
    else:
        sleep(sleeptime)
        
        f = open('alarm_urls.txt')
        url_list = f.readlines()
        url_index = random.randint(0,5)
        webbrowser.open(url_list[url_index])
        break
