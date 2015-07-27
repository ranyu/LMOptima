#!/usr/bin/env python
# coding=utf-8

#import numpy as np
import heapq
import os

def load_dic():
    fea_index = []
    with open('../../wordvector/sysdic.wc','r') as f:
        #f.readline()
        for i,data in enumerate(f):
            con = data.strip().split()
            fea_index.append(con[0])
    return fea_index

def cal_pro(goal,fea_index):
    #sum = 0
    s = []
    filename = 'output'
    with open('../result/sys_result','w') as fw:
        for w in fea_index:
            #print isinstance(goal,unicode)
            fw.write(goal.decode('utf-8').encode('gb2312')+' '.decode('utf-8').encode('gb2312')+w+'\n')
    os.system('./test.sh > '+ filename)        

def get_result(fea_index):
    s = []
    with open('output','r') as fw:
        for i in xrange(3):
            fw.readline()
        for data in fw:
            if data.strip()== '':
                break
            s.append(float(data.strip().split()[0]))
    for sq in heapq.nlargest(50,range(len(s)),s.__getitem__):
        print fea_index[sq]
    
def main():
    fea_index = load_dic()
    print 'finish loading dic'
    print len(fea_index)
    while True:
        goal = raw_input('Input the word:\n')
        if goal in fea_index:
            cal_pro(goal,fea_index)
            get_result(fea_index)
        else:
            print 'not in dic'


if __name__ == "__main__":
    main()


