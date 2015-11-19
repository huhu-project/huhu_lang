#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import re
veriler = [2,1,2,3]

def get_function(name):
	return 

def _yaz(veri=None):
	if veri:
		print(veri)

def _for(list, function):
	for i in list:
		function(i)

s = 'yaz veri dön veriler'
match=re.search(r'(.*) (.*) dön (.*)', s)
# output = "for i in %s:\n%s(i)" % (match.group(3), match.group(1))
# output = 'exec "try: print(66)\nexcept: problem=sys.exc_info()"'
#print(eval(output))

print(match.group(3))

_for( [1,2,3], _yaz )


exec("""def a(x):
   return x+1""")


print(a(2333))