#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime
import readline

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

sum = datetime.timedelta()

print 'Type hr(:min(:sec)) ("q" to quit): '

while True:
	line = raw_input('')
    
	if line == 'q':
		break

	timeList = map(str,sys.argv[1:])

	# Format input
	if ( line.count(":") + 1 == 1 ):
		h = line
		m = '00'
		s = '00'
	elif ( line.count(":") + 1 == 2 ):
		(h, m) = line.split(':')
		s = '00'
	elif ( line.count(":") + 1 == 3 ):
		(h, m, s) = line.split(':')
	else:
		h = '00'
		m = '00'
		s = '00'
			
	hour = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
		
	sum += hour

	print("Sum = " + str(sum))
