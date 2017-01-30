#!/usr/bin/env python2

#import os
#import commands
import webbrowser


x='''
Enter any Messages for check your pattern
'''

print x

s=raw_input()

if 'lo' in s :

#	commands.getoutput('firefox http://www.google.com/search?q=' +s)
	webbrowser.open_new_tab('http://www.google.com/search?q='+s)

else :
	print "no match found !!"
