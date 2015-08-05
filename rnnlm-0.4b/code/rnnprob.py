#!/usr/bin/env python
# coding=utf-8

#import numpy as np
import heapq
import os

def load_dic():
    fea_index = []
    core_index = []
    with open('../../core_table/asso_unigram.dic','r') as f:
        f.readline()
        f.readline()
        for i,data in enumerate(f):
            con = data.strip().split()
            core_index.append(con[1])
    with open('../../wordvector/sysdic.wc','r') as f:
        #f.readline()
        for i,data in enumerate(f):
            con = data.strip().split()
            fea_index.append(con[0])
    return fea_index,core_index

def cal_pro(goal,fea_index):
    #sum = 0
    filename = 'output'
    with open('../result/sys_result','w') as fw:
        for w in fea_index:
            #print isinstance(goal,unicode)
            fw.write(goal.decode('utf-8').encode('gb18030')+' '+w+'\n'.decode('utf-8').encode('gb2312'))
            #fw.write(goal.decode('utf-8').encode('gb2312')+' '+w+'\n')
    #os.system('rm '+filename)       
    os.system('./frnn_test.sh > '+ filename)        

def get_result(fea_index):
    s = []
    f1 = open('head1000','w')
    with open('output','r') as fw:
        #for i in xrange(4):
            #fw.readline()
        for data in fw:
            #if data.strip()== '':
                #break
            #print data.strip() == "OOV"
            #print data
            if data.strip() == "OOV":
                s.append(float(-100.0))
            else:
                s.append(float(data.strip().split()[0]))
    word_list = []
    for sq in heapq.nlargest(100,range(len(s)),s.__getitem__):
        con = fea_index[sq].decode('gb18030').encode('utf-8')
        if con not in word_list:
            word_list.append(con)
        #f1.write(str(s[sq])+'\n')
    for i in word_list:
        print i
    f1.close()    
def main():
    fea_index,core_index = load_dic()
    #print 'finish loading dic'
    #print fea_index[0].decode('gb2312').encode('utf-8')
    while True:
        goal = raw_input('Input the word:\n')
        #print goal
        #if goal.decode('utf-8').encode('gb2312') in fea_index:
        #if goal.decode('utf-8').encode('gb2312') in core_index:
        cal_pro(goal,core_index)
        get_result(core_index)
        #else:
            #print 'not in dic'


if __name__ == "__main__":
    main()


