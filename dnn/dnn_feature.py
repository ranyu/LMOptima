#!/usr/bin/env python
# coding=utf-8

def load_dic():
    fea_dic = {}
    fea_index = {}
    with open('../../word2vec/weiboseg_nb.bin','r') as f:
        f.readline()
        for i,data in enumerate(f):
            con = data.strip().split()
            fea_dic.setdefault(con[0],con[1:])
            fea_index.setdefault(con[0],i)
    return fea_dic,fea_index

def load_feature(fea_dic,fea_index):
    fw = open('feature.r','w')
    fws = open('label.r','w')
    with open('../../../data/segment/weibo_seg_clean','r') as f:
        for j,data in enumerate(f):
            con = data.strip().split()
            for i,ele in enumerate(con):
                if ele not in fea_dic.keys():
                    for sl in fea_dic['</s>']:
                        fw.write(sl+' ')
                    fw.write('\n')
                else:
                    for sl in fea_dic[ele]:
                        fw.write(sl+' ')
                    fw.write('\n')
                if i != len(con)-1:
                    next = con[i+1]
                    print 'fff',next
                    if next not in fea_dic.keys():
                        fws.write(str(fea_index['</s>'])+'\n')
                    else:
                        fws.write(str(fea_index[next])+'\n')
                else:
                    fws.write(str(fea_index['</s>'])+'\n')
            print j
    fw.close()
    fws.close()

def main():
    fea_dic,fea_index = load_dic()
    #print fea_index['</s>']

    print 'finish loading dic'
    load_feature(fea_dic,fea_index)

if __name__ == "__main__":
    main()


