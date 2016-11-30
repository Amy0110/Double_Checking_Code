#!/usr/bin/env python
#coding:utf-8
import sys
import re
import zhon
from zhon import hanzi

reload(sys)
sys.setdefaultencoding('utf8')

class TextInfo(object):
    def __init__(self,text = None,docname = None):
        self.text = text
        self.docname = docname
        self.basicinfo = self.info_from_text(self.text)
    def info_from_text(self,text):
        #text is a list
        if not text:
            print "error! Text list of %s is empty."%self.docname 
        p0 = re.compile('[0-9]+')
        p1 = re.compile(u'课题名称')
        p2 = re.compile(u'学生姓名')
        p3 = re.compile(u'班级')
        p4 = re.compile(u'学号')
        p5 = re.compile(u'日期')
        index = 0
        d = {}
        for paratext in text:
            if index > 20:
                break
            index += 1
            if p1.search(paratext):
                items = re.findall('[%s]' % zhon.hanzi.characters,paratext)
                k=''.join(items[:4])
                v=''.join(items[4:])
                d[k] = v 
            elif p2.search(paratext):
                items = re.findall('[%s]' % zhon.hanzi.characters,paratext)
                k=''.join(items[:4])
                v=''.join(items[4:])
                d[k] = v 
            elif p3.search(paratext):
                items = re.findall('[%s]' % zhon.hanzi.characters,paratext)
                k = ''.join(items)
                v = p0.search(paratext).group()
                d[k] = v 
            elif p4.search(paratext):
                items = re.findall('[%s]' % zhon.hanzi.characters,paratext)
                k = ''.join(items)
                try:
                    v = p0.search(paratext).group()
                except:
                    print "error in ",paratext
                d[k] = v 
            elif p5.search(paratext):
                items = re.findall('[%s]' % zhon.hanzi.characters,paratext)
                k = ''.join(items)
                try:
                    v = '/'.join(p0.findall(paratext))
                except:
                    print "error with",paratext
                d[k] = v 
            else:continue
        for k,v in d.items():
            print k,v
        return d

