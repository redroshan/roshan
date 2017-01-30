#!/usr/bin/env  python2


import time
import platform
print "Welcome to SHARPEYE"

time.sleep(2)


print ""
print ""
print "***********************************************"
print "+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+"

x='''
Press  1  To  check my System IP  address  :  
Press  2  To  check my System MAC  address  :  
Press  3  To  check my System OS Type  :  
Press  4  To  check my System OS version   :  
Press  5  To  check my system Configuration   : 
Press  6  To  check  About A particular IP :
'''

print x

ch=int(raw_input())

if ch  ==  1 :
	execfile('verifyplatform.py')
elif ch  ==  2 :
	print "My Mac address e4:02:9b:30:5e:03"
elif ch  ==  3 :
	print "Os Platform type is " + platform.system()
elif ch  == 6 :
	execfile('checkiplive.py')
else :
	print "execute me !!"
