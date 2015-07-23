#!/usr/bin/env python
# coding=utf-8

import numpy as np
import heapq

def load_dic():
    fea_dic = {}
    fea_index = []
    with open('./sysdic.wc','r') as f:
        #f.readline()
        for i,data in enumerate(f):
            con = data.strip().split()
            fea_dic.setdefault(con[0],con[1:])
            fea_index.append(con[0])
    return fea_dic,fea_index

def cal_pro(goal,fea_dic,fea_index):
    sum = 0
    s = []
    local = np.array(fea_dic[goal],dtype=np.float)
    for w in xrange(len(fea_index)):
        trans = np.array(fea_dic[fea_index[w]],dtype=np.float)
        result = np.exp(-np.dot(trans,local))
        s.append(result)
        sum += result 
    for sq in heapq.nlargest(50,range(len(s)),s.__getitem__):
        print fea_index[sq]

def main():
    fea_dic,fea_index = load_dic()
    print 'finish loading dic'
    print len(fea_dic)
    print len(fea_index)
    while True:
        goal = raw_input('Input the word:\n')
        if goal in fea_index:
            cal_pro(goal,fea_dic,fea_index)
        else:
            print 'not in dic,print again!'


if __name__ == "__main__":
    main()


