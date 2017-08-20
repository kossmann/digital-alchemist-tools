#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime

# usage: python timesum.py 10:45 00:50

timeList = map(str,sys.argv[1:])

sum = datetime.timedelta()

for i in timeList:
    if ( i.count(":") + 1 == 1 ):
        h = i
        m = '00'
        s = '00'
    elif ( i.count(":") + 1 == 2 ):
        (h, m) = i.split(':')
        s = '00'
    elif ( i.count(":") + 1 == 3 ):
        (h, m, s) = i.split(':')
    else:
        h = '00'
        m = '00'
        s = '00'
        
    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    
    sum += d

print(str(sum))