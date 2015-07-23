#!/usr/bin/env python
# coding=utf-8

word_dic = []

fw = open('sysdic.wc','w')
with open('./a78_dict/utf8.words.sysdict.mobile.weeklybuild.dic','r') as f:
    for data in f:
        word_dic.append(data.strip().split()[1].decode('utf-8').encode('gbk'))
with open('./weiboseg_nb.bin','r') as f:
    f.readline()
    for data in f:
        if data.strip().split()[0] in word_dic:
            fw.write(data.strip()+'\n')
        #raw_input()
fw.close()
'''with open('./weiboseg_nb.bin','r') as f:
    f.readline()
    for data in f:
        word_dic.append(data.strip().split()[0])
with open('./a78_dict/utf8.words.sysdict.mobile.weeklybuild.dic','r') as f:
    for i,data in enumerate(f):
        if data.strip().split()[1].decode('utf-8').encode('gbk') not in word_dic:
            print data.strip().split()[1]
        print i
        raw_input()'''
