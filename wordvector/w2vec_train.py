# -*- coding: utf-8 -*-
from gensim.models import Word2Vec,Phrases
import numpy as np
   
def get_result():
    sentences = []
    with open('../../LMOptima/rnnlm-0.4b/result/sys_result','r') as f:
        for data in f:
            sentences.append(data.strip().decode('gb18030').encode('utf-8'))
    score = 0
    scores = []
    for param_1 in [-1.]:
        for param_2 in [5]:
            for p in sentences:
                words = p.split()
                for q in words[0:-1]:
                    print q
                    score += pow(model.vocab[q].count,param_1)*(model.similarity(q,words[-1])+2**param_2)
                scores.append(score)
            score = 0
            print sentences[np.argmax(scores)]

'''def get_result(model):
    best_result = 0
    best_param_1 = 0
    best_param_2 = 0
    max_re = 0
    max_scores = 0
    for param_1 in [-1.]:
        for param_2 in [5]:
            #print param_1,param_2
            scores = np.zeros((1040,5))
            for question_number in xrange(1040):
                sen_0 = sentences[5*question_number]
                sentence_length = len(sen_0)
                for i in xrange(5):
                    different_word = sentences[5*question_number+i][different_word_index[question_number]]
                    if model.__contains__(different_word):
                        for j in xrange(sentence_length):
                            if j != different_word_index[question_number] and model.__contains__(sen_0[j]):
                                scores[question_number,i] += pow(model.vocab[sen_0[j]].count,param_1)*((model.similarity(different_word,sen_0[j])+2)**param_2)
            scores_amax = np.argmax(scores,1)
            letter = ['a','b','c','d','e']
            filename = 'submit.csv'
            with open(filename,'w') as fw:
                fw.write('Id,Answer\n')
                for i in xrange(1040):
                    fw.write(str(i+1)+','+str(letter[scores_amax[i]]+'\n'))
'''
def main():
    model = Word2Vec.load_word2vec_format('../../word2vec/weiboseg.bin',binary = True)
    print 'load'
    get_result() 
    print 'finish'

if __name__ == "__main__":
    main()
