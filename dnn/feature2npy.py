#!/usr/bin/env python
# coding=utf-8

import numpy as np

TRAIN_LINE_NUM = 171147
TEST_LINE_NUM = 20000

train = np.zeros((TRAIN_LINE_NUM,300),dtype=np.float32)
test = np.zeros((TEST_LINE_NUM,300),dtype=np.float32)
with open('./X.r','r') as f:
    for i,data in enumerate(f):
        for j,ele in enumerate(data.strip().split()):
            if i < TRAIN_LINE_NUM:
                train[i][j] = float(ele)
            else:
                test[i-TRAIN_LINE_NUM][j] = float(ele)

np.save('data/X_train.npy',train)
np.save('data/X_test.npy',test)

tr_label = np.zeros((TRAIN_LINE_NUM),dtype=np.int)
te_label = np.zeros((TEST_LINE_NUM),dtype=np.int)
with open('./label.r','r') as f:
    for i,data in enumerate(f):
        for ele in data.strip().split():
            if i < TRAIN_LINE_NUM:
                tr_label[i] = float(ele)
            else:
                te_label[i-TRAIN_LINE_NUM] = float(ele)
np.save('data/Y_train.npy',tr_label)
np.save('data/Y_test.npy',te_label)


