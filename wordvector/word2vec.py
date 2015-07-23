#!/usr/bin/env python
# coding=utf-8

import numpy as np
import heapq

def load_dic():
    fea_dic = {}
    fea_index = []
    with open('../../word2vec/weiboseg_nb.bin','r') as f:
        f.readline()
        for i,data in enumerate(f):
            con = data.strip().split()
            fea_dic.setdefault(con[0],con[1:])
            fea_index.append(con[0])
    return fea_dic,fea_index

def cal_pro(fea_dic,fea_index):
    sum = 0
    s = []
    for i in xrange(len(fea_index)):
        print 'goal:',fea_index[i]
        local = np.array(fea_dic[fea_index[i]],dtype=np.float)
        for w in xrange(len(fea_index)):
            trans = np.array(fea_dic[fea_index[w]],dtype=np.float)
            result = np.exp(-np.dot(trans,local))
            s.append(result)
            sum += result 
        for sq in heapq.nlargest(5,range(len(s)),s.__getitem__):
            print fea_index[sq]
        raw_input()
            
        #print 'result',fea_index[np.argmax(el * 1.0/sum for el in s)]
        #print max(el * 1.0/sum for el in s)
        #print sum
        s = []
        sum = 0
def main():
    fea_dic,fea_index = load_dic()
    print 'finish loading dic'
    print len(fea_dic)
    print len(fea_index)
    cal_pro(fea_dic,fea_index)

if __name__ == "__main__":
    main()


