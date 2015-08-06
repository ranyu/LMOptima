# -*- coding: utf-8 -*-
import numpy as np
import heapq
import c1

class w2vec:
    def __init__(self):
        self.vocab = {}
        self.vector = {}
        with open('./WORDS.PART','r') as f:
            for data in f:
                con = data.strip().split()
                self.vocab.setdefault(con[0],int(con[1])) 
        with open('./dbg_0803.bin.part1','r') as f:
            f.readline()
            f.readline()
            f.readline()
            for data in f:
                con = data.strip().split()
                self.vector.setdefault(con[0],[]) 
                self.vector[con[0]] = np.array(con[1:],dtype=np.float)

    def __contains__(self,word):
        return word in self.vocab

def load_dic():
    dic = []
    with open('../core_table/asso_unigram.dic') as f:
        f.readline()
        f.readline()
        for data in f:
            dic.append(data.strip().split()[1].decode('gb18030').encode('utf-8'))
        return dic

def get_result(model,sys_dic,sentences):
    score = 0
    scores = []
    for param_1 in [-1.,-2.,1.,2.]:
        for param_2 in [-1.,-2.,1.,2.]:
            print param_1,param_2
            for i,p in enumerate(sentences):
                words = p.split()
                for q in words[0:-1]:
                    #print q,words[-1]
                    if model.__contains__(q) and model.__contains__(words[-1]): #and q in sys_dic and words[-1] in sys_dic:
                        score += c1.inner_product(model.vector[q],model.vector[words[-1]],model.vocab[q],param_1,param_2)
                scores.append(score)
                score = 0
            print 'calculation finish'
            for sq in heapq.nlargest(50,range(len(scores)),scores.__getitem__):
                print sentences[sq]
                #print scores[sq]
            scores = []
            #raw_input()
def gene_text(goal,fea_index):
    sentences = []
    for w in fea_index:
        sentences.append(goal+' '+w+'\n')
    return sentences

def main():
    model = w2vec()
    print ('load')
    sys_dic = load_dic()
    while True:
        goal = raw_input('Input the word:\n')
        text = gene_text(goal,sys_dic)
        get_result(model,sys_dic,text) 
    print ('finish')

if __name__ == "__main__":
    main()
