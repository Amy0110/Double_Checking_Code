#!/usr/bin/env python
#coding:utf-8
import os

def re_empty_dir(filepath):
    index = 0
    for filename in os.listdir(filepath):
        print index
        index += 1
        if os.path.isfile(filepath + os.sep + filename):
            continue
        if len(os.listdir(filepath + os.sep + filename)) == 0:
            print filename
            cmd = 'rm -rf  '+ filename
            os.system(cmd)
            print "remove",filename
re_empty_dir('.')
        
    
