# -*- coding: utf-8 -*-
import numpy as np
import heapq

class w2vec:
    def __init__(self):
        self.vocab = {}
        self.vector = {}
        with open('../../word2vec/words','r') as f:
            for data in f:
                con = data.strip().split()
                self.vocab.setdefault(con[0],int(con[1])) 
        with open('./modify_cbow.bin','r') as f:
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

    def similarity(self,a1,a2):
        return np.inner(a1,a2)
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
                print words
                for q in words[0:-1]:
                    print i
                    if i > 100:
                        break
                    print q,words[-1]
                    q = q.decode('utf-8').encode('gb18030')
                    if model.__contains__(q) and model.__contains__(words[-1].decode('utf-8').encode('gb18030')):
                        print '??'
                        a1 = np.array(model.vector[q])
                        a2 = np.array(model.vector[words[-1].decode('utf-8').encode('gb18030')])
                        score += pow(model.vocab[q],param_1)*((np.inner(a1,a2)+2)**param_2)
                        #score += model.similarity(a1,a2)
                scores.append(score)
                score = 0
            print 'calculation finish'
            for sq in heapq.nlargest(50,range(len(scores)),scores.__getitem__):
                print sentences[sq]
                print scores[sq]
            scores = []
            raw_input()
def gene_text(goal,fea_index):
    sentences = []
    for w in fea_index:
        sentences.append(goal+' '+'\n')
    #return sentences
    with open('result/sys_result','w') as f:
        for w in fea_index:
            f.write(goal+' '+w+'\n')


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





