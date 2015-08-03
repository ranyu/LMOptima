#!/usr/bin/env python
# coding=utf-8

# preprocessing is so important that for NLP, especially RNN trains,this code mainly for 1.spliting the segment text(no english),2.removing the less word sentence,3.removing the redundance and 4.omitting the word not in core word library to form about 1.5G DBG corpus

def load_name_dic():
    #name_dic = ['' for i in xrange(7682053)]
    sys_dic = []
    '''with open('../data/allpeoplenames_total.txt','r') as f:
        for i,data in enumerate(f):
            #print (str(i) + ' '+ data.split()[0].decode('gb18030').encode('utf-8'))
            name_dic[i] = data.split()[0]#.decode('gb18030').encode('utf-8')'''
    with open('../../../asso_unigram.dic','r') as f:
        f.readline()
        f.readline()
        for i,data in enumerate(f):
            sys_dic.append(data.split()[1])
    #return name_dic,sys_dic
    return sys_dic

def split_segment(sys_dic):
    fw = open('../data/PC_DBG/PC-DBG_other','w') 
    with open('../data/PC_DBG/NoEnglish_seg.DBG','r') as f:
        f.readline()
        for i,data in enumerate(f):
            print i
            if len(data.split()[1:]) < 3:
                continue
            for s in data.split()[1:]:
                if s in sys_dic:
                    fw.write(s.decode('gb18030').encode('utf-8')+' ')
                else:
                    fw.write('其他 ')
                '''if s not in name_dic and s in sys_dic:
                    #print chardet.detect(s)
                    fw.write(s+' '.decode('utf-8').encode('gb18030'))
                elif s in name_dic and s in sys_dic:
                    fw.write('他 '.decode('utf-8').encode('gb18030'))
                elif s not in name_dic and s not in sys_dic:
                    #continue
                    fw.write('其他 '.decode('utf-8').encode('gb18030'))'''
            fw.write('\n')
    fw.close()

def main():
    sys_dic = load_name_dic()
    print 'load finish'
    split_segment(sys_dic)

if __name__ == "__main__":
    main()
