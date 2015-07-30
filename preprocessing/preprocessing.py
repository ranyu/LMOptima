#!/usr/bin/env python
# coding=utf-8
# preprocessing is so important that for NLP, especially RNN trains,this code mainly for 1.spliting the segment text(no english),2.removing the less word sentence,3.removing the redundance and 4.omitting the word not in core word library to form about 1.5G DBG corpus

def load_name_dic():
    name_dic = []
    with open('../data/allpeoplenames.txt','r') as f:
        for i,data in enumerate(f):
            print (str(i) + ' '+ data.split()[0].decode('gb18030').encode('utf-8'))
    return name_dic

def split_segment():
    fw = open('../data/PC_DBG/PC-DBG_split','w') 
    with open('../data/PC_DBG/NoEnglish_seg.DBG','r') as f:
        f.readline()
        for data in f:
            print (data.split()[0].decode('gb2312').encode('utf-8'))
            quit()
    fw.close()

def main():
    name_dic = load_name_dic()
    split_segment()

if __name__ == "__main__":
    main()
