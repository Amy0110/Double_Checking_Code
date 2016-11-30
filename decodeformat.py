#!/usr/bin/env python
#coding:utf-8
import os
import re
import sys
import codecs
import chardet
from pdf2text import convert_pdf
from subprocess import Popen,PIPE
from docx import Document

reload(sys)
sys.setdefaultencoding('utf8')

class DecodeFormat(object):
    def __init__(self,docpath = '.', docname = None, rewrite = 0, outpath = './doctxts'):
        #rewrite is for writing into a formal txt(without blank lines) or not.0 for not,1 for yes.
        #get_info is getting the student information or not,0 for not,1 for yes.
        self.docpath = docpath
        self.docname = docname
        self.outpath = outpath
        self.rewrite = rewrite
        if docname.endswith('.doc'):
            self.text = self.get_doc_text(self.docpath,self.docname,self.outpath)
        if docname.endswith('.docx'):
            self.text = self.get_docx_text(self.docpath,self.docname,self.outpath)
        if docname.endswith('.pdf'):
            self.text = self.get_pdf_text(self.docpath,self.docname,self.outpath)

    def get_doc_text(self,docpath,docname,outpath): 
        #return a list of each line(not blank) of the doc
        if not os.path.exists(outpath):
            os.mkdir(outpath)
        txt_file = outpath + os.sep + docname.rstrip('doc') + 'txt'
        cmd = ['antiword',  docpath + os.sep + docname]
        p = Popen(cmd,  stdout = PIPE)
        stdout, stderr = p.communicate()
        print 'length of stdout:',len(stdout)
        string = stdout.decode('utf-8','ignore')
        with open(txt_file,'w') as p:
            p.write(string)  
        text=[]
        with codecs.open(txt_file,'r','utf-8') as f:
            print "txt exists"
            for line in f.readlines():
                if not line.split():
                    continue
                line = line.strip()
                line = re.sub('\s+','',line)
                text.append(line)
        if self.rewrite == 1:
            with open(txt_file,'w') as p:
                p.write('\n'.join(text))
        return text

    def get_pdf_text(self,docpath,docname,outpath):
        #return a list of each line(not blank) of the doc
        if not os.path.exists(outpath):
            os.mkdir(outpath)
        txt_file = outpath + os.sep + docname.rstrip('pdf') + 'txt'
        string = convert_pdf(docpath+os.sep+docname)
        with open(txt_file,'w') as p:
            p.write(string)
        text=[]
        with codecs.open(txt_file,'r','utf-8') as f:
            for line in f.readlines():
                if not line.split():
                    continue
                line = line.strip()
                line = re.sub('\s+','',line)
                text.append(line)
        if self.rewrite == 1:
            with open(txt_file,'w') as p:
                p.write('\n'.join(text))
        return text


    def get_docx_text(self,docpath,docname,outpath):
        #return a list of each paragraph of the docx
        doc = Document(docpath+os.sep+docname)
        paras = doc.paragraphs
        paratext = [re.sub('\s+','',para.text) for para in paras if para.text.split()] 
        self.runtext = [run.text for para in paras for run in para.runs]
        if self.rewrite == 1:
            if not os.path.exists(outpath):
                os.mkdir(outpath)
            txt_file = outpath + os.sep + docname.rstrip('docx') + 'txt'
            with open(txt_file,'w') as p:
                p.write('\n'.join(paratext))
        return paratext
