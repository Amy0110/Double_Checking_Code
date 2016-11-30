#!/usr/bin/env python
#coding:utf-8
import os
import re
import sys
from decodeformat import DecodeFormat
from info_from_text import TextInfo
from uncompress import uncompress
reload(sys)
sys.setdefaultencoding('utf8')

uncompressed_path = '/home/yindanping/code_data/all_from_liu/uncompress_files'
out_txt_path = '/home/yindanping/code_data/all_from_liu/doctxts'

def rename(uncompressed_path):
	rename_path = '/home/yindanping/code_data/all_from_liu/rename'
	if not os.path.exists(rename_path):
		os.mkdir(rename_path)
	fileID = {}
	index = 0
	ind = 0
	for filename in os.listdir(uncompressed_path):
		fileID[index] = filename
		index += 1
		try:
			
			info = get_doc(uncompressed_path,filename)
			ind += 1
			print index,filename
			print info
			print "---------------------------------------------"
		except:
			pass
		try:
			re_name = info[u'班级'] + '+' + info[u'学号'] + '+' + info[u'学生姓名']
			print 'rename',re_name
			cmd = 'mv ' + uncompressed_path + os.sep + filename + ' ' + rename_path + os.sep + re_name
			os.system(cmd)
			print "successfully rename!"
		except:
			if not info:
				print "no return value from get_doc"
			else:
				print 'need to be analysed'
		print 'index',index

def get_doc(path,filename):
	if len(filename.split(" ")) > 1:
			filename = "'" + filename + "'"
	else:
		pass
	if filename.endswith('rar') or filename.endswith('zip') or filename.endswith(".rar'") or filename.endswith(".zip'"):
		p = uncompress(path,filename,path)
		cmd = 'rm ' + path + os.sep + filename
		os.system(cmd)
		get_doc(p[0],p[1])
	if filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith(".doc'") or filename.endswith(".docx'") or filename.endswith('.pdf') or filename.endswith('.wps'):
		if filename.endswith("'"):
			correct = re.sub("'",'',filename)
			correct = re.sub(' ','',correct)
			cmd = 'mv ' + path + os.sep + filename + ' ' + path + os.sep + correct
			os.system(cmd)
			filename = correct
		print path + '/' + filename
		try:
			Decode = DecodeFormat(docpath = path, docname = filename, outpath = out_txt_path)
			#if Decode.text:
			#	print 'text exists'
			baseinfo = TextInfo(Decode.text,Decode.docname).basicinfo
			#for i in os.listdir(path):
			#	print i
			return baseinfo
		except:
			print "you file %s should be a correct doc!"%path+filename
		#print "*******************************************"
		#print "*******************************************"
		
	elif os.path.isdir(path+os.sep+filename):
		path=path+os.sep+filename
		for filename in os.listdir(path):
			g=get_doc(path,filename)
			if g:
				return g
	else:pass
	

rename(uncompressed_path)