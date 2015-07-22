#!/usr/bin/env python
# coding=utf-8

import numpy as np

def load_dic():
    fea_dic = {}
    fea_index = {}
    with open('../../word2vec/weiboseg_nb.bin','r') as f:
        f.readline()
        for i,data in enumerate(f):
            con = data.strip().split()
            fea_dic.setdefault(con[0],con[1:])
            fea_index.setdefault(i,con[0])
    return fea_dic,fea_index

def cal_pro(fea_dic,fea_index):
    sum = 0
    for i in xrange(len(fea_dic)):
        sum = sum(np.exp(-np.dot(w,fea_dic[i])) for w in fea_dic)
        for w in fea_dic:
            p = np.exp(-np.dot(w,fea_dic[i]))*1.0/sum
            print p
        sum = 0
        raw_input()
def main():
    fea_dic,fea_index = load_dic()
    print 'finish loading dic'
    print len(fea_dic)
    print len(fea_index)
    cal_pro(fea_dic,fea_index)

if __name__ == "__main__":
    main()


