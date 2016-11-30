#!/usr/bin/env python
#coding:utf-8
import os
import sys
import re

#if the corresponding dir exists in outputpath,do not compress the file then.
def un_rar(path,file_name,outputpath=None):
	formal_file_name=re.sub(' ','',file_name)
	if os.path.isdir(outputpath+os.sep+formal_file_name.split('.')[0]):
		print 'exist in outputpath',formal_file_name
		pass
	else:
		os.mkdir(outputpath+os.sep+formal_file_name.split('.')[0].lstrip("'"))
		if formal_file_name != file_name:
			file_name = "'" + file_name + "'"
		cmd="rar x "+path+os.sep+file_name+" "+outputpath+os.sep+formal_file_name.split('.')[0]
		print cmd
		os.system(cmd)
	return (outputpath,file_name.split('.')[0])

def un_zip(path,file_name,outputpath=None):
	formal_file_name=re.sub(' ','',file_name)
	if formal_file_name != file_name:
		print "input filename should be with no space,replace the space first please!",file_name
	if os.path.isdir(outputpath+os.sep+formal_file_name.split('.')[0]):
		print 'exist in outputpath',formal_file_name
		pass	
	else:
		os.mkdir(outputpath+os.sep+formal_file_name.split('.')[0].lstrip("'"))
		if formal_file_name != file_name:
			file_name = "'" + file_name + "'"
		cmd="unzip -O GBK "+path+os.sep+file_name+" -d "+outputpath+os.sep+formal_file_name.split('.')[0]
		os.system(cmd)
	return (outputpath,file_name.split('.')[0])

def uncompress(path,file_name,outputpath=None):
    print "start uncompress"
    if file_name.endswith(".zip") or file_name.endswith(".zip'"):
        p=un_zip(path,file_name,outputpath)
    elif file_name.endswith(".rar") or file_name.endswith(".rar'"):
        p=un_rar(path,file_name,outputpath)
    else:
        print "not .rar or .zip!"
    return p

