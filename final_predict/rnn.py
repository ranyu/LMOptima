#!/usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers.core import Dense,Dropout,Flatten,Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM,SimpleDeepRNN,SimpleRNN,GRU
from keras.utils import np_utils
from keras.optimizers import SGD
from keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import roc_auc_score

def load_feature(num):
    i = 1
    train_x = np.load('./5_feature/%d.npy' %(i))
    for i in range(2,7):
        X = np.load('./5_feature/%d.npy' %(i))
        train_x = np.concatenate((train_x,X),axis=0)
    vali_x = np.load('./5_feature/%d.npy' %(i))
    for i in range(8,9):
        X = np.load('./5_feature/%d.npy' %(i))
        vali_x = np.concatenate((vali_x,X),axis=0)
    return train_x,vali_x

def load_label(num):
    i = 1
    filename = ('../input/train/subj5_series%d_events.csv' %(i))
    labels = pd.read_csv(filename)
    labels = labels.drop(['id'],axis=1).shift(-1)

    for i in range(2,7):
        filename = ('../input/train/subj5_series%d_events.csv' %(i))
        Y = pd.read_csv(filename)
        Y = Y.drop(['id'],axis=1).shift(-1)
	Y.loc[len(Y)-1] = [0.0 for j in xrange(6)]
        labels = np.concatenate((labels,Y),axis=0)
        
    filename = ('../input/train/subj5_series%d_events.csv' %(i))
    vali_labels = pd.read_csv(filename)
    vali_labels = vali_labels.drop(['id'],axis=1).shift(-1)
    for i in range(8,9):
        filename = ('../input/train/subj5_series%d_events.csv' %(i))
        Y = pd.read_csv(filename)
        Y = Y.drop(['id'],axis=1).shift(-1)
	Y.loc[len(Y)-1] = [0.0 for j in xrange(6)]
        vali_labels = np.concatenate((vali_labels,Y),axis=0)
    return labels,vali_labels

def build_model():
    input_dim = 256
    model = Sequential()
    #model.add(Embedding(input_dim,10))
    #model.add(Dropout(0.25))
    model.add(SimpleDeepRNN(input_dim,10,truncate_gradient=3,activation='tanh',return_sequences=True))
    model.add(Dropout(0.5))
    model.add(SimpleDeepRNN(10,15,init='uniform',activation='tanh',return_sequences=True)) 
    model.add(Dense(15,6,init='uniform',activation='sigmoid'))
    #model.add(Activation('sigmoid'))
    #sgd = SGD(lr=0.001,decay=1e-6,momentum=0.9,nestrov=True)
    #model.compile(loss='mean_squared_error',optimizer=sgd)
    model.compile(loss='binary_crossentropy',optimizer="rmsprop")
    '''
    model.add(Embedding(input_dim,10))
    model.add(SimpleDeepRNN(10,15)) 
    model.add(SimpleDeepRNN(15,6,init='uniform',activation='sigmoid',inner_activation='tanh')) 

    sgd = SGD(lr=0.001,decay=1e-6,momentum=0.9,nestrov=True)
    model.compile(loss='mean_squared_error',optimizer=sgd)'''
    return model

def iter_batch(train_x,train_labels,BATCH_SIZE):
    num = np.random.randint(0,len(train_x)-BATCH_SIZE)
    print num
    batch_X = np.zeros((BATCH_SIZE,150,256))
    batch_Y = np.zeros((BATCH_SIZE,150,6))
    for i in xrange(BATCH_SIZE):
	batch_X[i] = train_x[i*num:i*num+150,:]
	batch_Y[i] = train_labels[i*num:i*num+150,:]
    #print batch_X,batch_Y
    #print batch_X.shape,batch_Y.shape
    return batch_X,batch_Y
     
def score(model,vali_x,vali_labels,BATCH_SIZE):
    predicted = model.predict_proba(vali_x,batch_size=BATCH_SIZE)
    print predicted.reshape(-1)
    print vali_labels.reshape(-1)
    score = roc_auc_score(np.array(vali_labels.reshape(-1)),np.array(predicted.reshape(-1)))
    return score

def main():
    BATCH_SIZE=256
    EPOCH = 1000
    for i in range(5,6):
        train_x,vali_x = load_feature(i)
        train_labels,vali_labels = load_label(i)
        print train_x.shape,vali_x.shape
        print train_labels.shape,vali_labels.shape
	valibatch_x,valibatch_y = iter_batch(vali_x,vali_labels,BATCH_SIZE)
    	model = build_model()
    	print train_labels
	for j in xrange(EPOCH):
	    batch_x,batch_y = iter_batch(train_x,train_labels,BATCH_SIZE)
    	    model.train_on_batch(batch_x,batch_y,accuracy=True)
	    '''if j % 2 == 0:
    	    	print score(model,valibatch_x,valibatch_y,BATCH_SIZE)'''

if __name__ == "__main__":
    main()
