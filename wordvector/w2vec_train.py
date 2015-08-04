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
        #print a1,a2
        return np.dot(a1,a2)
def load_dic():
    dic = []
    with open('../core_table/asso_unigram.dic') as f:
        f.readline()
        f.readline()
        for data in f:
            dic.append(data.strip().split()[1].decode('gb18030').encode('utf-8'))
        return dic

def get_result(model,sys_dic):
    sentences = []
    #with open('../../LMOptima/rnnlm-0.4b/result/sys_result','r') as f:
    with open('result/sys_result','r') as f:
        for data in f:
            sentences.append(data.strip())#.decode('gb18030').encode('utf-8'))
            #sentences.append(data.strip())
    score = 0
    scores = []
    for param_1 in [-1.]:#[-1.,-2.,-3.,0,1,2,3,4]:
        for param_2 in [-1.]:#[-1.,-2.,-3.,0,1,2,3,4]:
            print param_1,param_2
            for i,p in enumerate(sentences):
                words = p.split()
                if words[1] in answer:
                    print words[1],i,answer.index(words[1])
                for q in words[0:-1]:
                    print i
                    if model.__contains__(q):
                        if model.__contains__(words[-1]):
                            score += pow(model.vocab[q],param_1)*((model.similarity(model.vector[q],model.vector[words[-1]])+2)**param_2)
                scores.append(score)
                score = 0
            print 'calculation finish'
            for sq in heapq.nlargest(10,range(len(scores)),scores.__getitem__):
                for an in sentences[sq]:
                    print an
                print sco
                    print (sentences[sq],scores[sq])
            scores = []
            raw_input()
def gene_text(goal,fea_index):
    with open('result/sys_result','w') as f:
        for w in fea_index:
            f.write(goal+' '+w.decode('gb18030').encode('utf-8')+'\n')


def main():
    model = w2vec()
    print ('load')
    sys_dic = load_dic()
    while True:
        goal = raw_input('Input the word:\n')
        gene_text(goal,sys_dic)
        get_result(model,sys_dic) 
    print ('finish')

if __name__ == "__main__":
    main()
