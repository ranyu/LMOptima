#!/usr/bin/env python
# coding=utf-8

import sys

fw = open('ngram.txt','w')

with open(sys.argv[1],'r') as f:
    for data in f:
        if data.strip().split()[0] == 'file':
            break
        f.next()
        con = f.next()
        re = con.strip().split('=')[1].split()[3]
        print re
        fw.write(re+'\n')
        for i in xrange(4):
            f.next()
fw.close()
