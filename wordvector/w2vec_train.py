# -*- coding: utf-8 -*-
import numpy as np
import heapq
from scipy.spatial.distance import cosine

class w2vec:
    def __init__(self):
        self.vocab = {}
        self.vector = {}
        with open('../../word2vec/words','r') as f:
            for data in f:
                con = data.strip().split()
                self.vocab.setdefault(con[0],int(con[1])) 
        with open('./mobile-dbg.bin','r') as f:
            f.readline()
            f.readline()
            f.readline()
            for data in f:
                con = data.strip().split()
                self.vector.setdefault(con[0],[]) 
                for q in con[1:]:
                    self.vector[con[0]].append(float(q)) 

    def __contains__(self,word):
        return (word in self.vocab.keys())

    def similarity(self,w1,w2):
        a1 = np.array(w1)
        a2 = np.array(w2)
        print a1,a2
        return cosine(a1,a2)
    
def get_result(model):
    sentences = []
    #with open('../../LMOptima/rnnlm-0.4b/result/sys_result','r') as f:
    with open('./result','r') as f:
        for data in f:
            sentences.append(data.strip())#.decode('gb18030').encode('utf-8'))
            #sentences.append(data.strip())
    score = 0
    scores = []
    for param_1 in [-1.,-2.,-3.,0,1,2,3,4]:
        for param_2 in [-1.,-2.,-3.,0,1,2,3,4]:
            for p in sentences:
                words = p.split()
                for q in words:
                    print q
                #print words.decode('gb18030').encode('utf-8')
                for q in words[0:-1]:
                    print q,model.__contains__(q)
                    print np.array(model.vector[q])
                    if model.__contains__(q):
                        print words[-1]
                        if model.__contains__(words[-1]):
                            score += pow(model.vocab[q],param_1)*((model.similarity(model.vector[q],model.vector[words[-1]])+2)**param_2)
                        print (score)
                        raw_input()
                scores.append(score)
            for sq in heapq.nlargest(10,range(len(scores)),scores.__getitem__):
                print (sentences[sq],scores[sq])
                for ql in sentences[sq]:
                    print ql
            scores = []
            score = 0
            raw_input()

def main():
    model = w2vec()
    print ('load')
    get_result(model) 
    print ('finish')

if __name__ == "__main__":
    main()
