#!/usr/bin/env python
#coding:utf-8
import codecs
import re
import sys
def one2many(filename):
	with codecs.open(filename,'r','utf8') as f:
		for line in f.readlines():
			line = re.sub('\\\\\"','"',line)
			lines = line.split("\\n")	
			with codecs.open(filename+'.html','a','utf8')as p:
				for l in lines:
					p.write(l)
					p.write("\n")
one2many(sys.argv[1])
