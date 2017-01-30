#!/usr/bin/env python2

import platform


getp=platform.system()


if getp  ==  'Linux'  :
	
	execfile('getip.py')

else :
	print   "No other Platform supported  by US except Linux  "
	execfile('infogather.py')
