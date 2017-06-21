#!/usr/bin/env python
#coding:utf-8
import codecs
import re
import sys
def many2one(filename):
	with codecs.open(filename,'r','utf8') as f:
		str0 = ""
		for line in f.readlines():
			line = re.sub('"','\\\\\"',line)
			str0 = str0+"\\n"+line.rstrip("\n")			
		with codecs.open("f"+filename.rstrip(".html"),'a','utf8')as p:
			p.write(str0.lstrip("\\n"))
many2one(sys.argv[1])
