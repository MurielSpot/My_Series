#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
读取一些固定格式的词向量。
'''

import numpy as np

def read_npy(path):
    return np.load(path)

def read_npz(path):
    raise NotImplementedError()

def read_wv_1(path,ischar,log_path):
    '''
    sgns.target.word-character.char1-2.dynwin5.thr10.neg5.dim300.iter5
    https://github.com/Embedding/Chinese-Word-Vectors
    
    文件格式：一行： ， -0.225854 0.107560 ... 0.144121 0.005673 
    
    ischar 为True时，只取字符的向量，不然取所有词向量。
    
    返回：
        词的列表；
        词向量的列表，列表里每一项为一个numpy数组类型的向量。
    '''
    words=[]
    vecs=[]
    with open(path,"r",encoding="utf-8") as f:
        line=f.readline().strip("\n").split(" ")
        row,col=int(line[0]),int(line[1])
        print(row,col)
        line=f.readline()
        while line:
            if line.strip()!="":
                #print(line)
                line=line.strip().split(" ")
                #print(line,len(line),col)
                if ischar:
                    if len(line[0])==1:
                        if len(line)==col+1:
                            words.append(line[0])
                            vecs.append(np.array([line[1:]],dtype="float32"))
                        else:
                            # 行的列数不对的话，则记录
                            with open(log_path,"a",encoding="utf-8") as f:
                                f.write(str(line))
                else:
                    if len(line)==col+1:
                        words.append(line[0])
                        vecs.append(np.array([line[1:]],dtype="float32"))
                    else:
                        # 行的列数不对的话，则记录
                        with open(log_path,"a",encoding="utf-8") as f:
                            f.write(str(line))
                #print(words)
                #input(len(vecs))
            line=f.readline()
    return words,vecs

if __name__ == "__main__":
    # words,vecs=read_wv_1(r"E:\code\trjcn\brain\code\dataset\sgns.target.word-character.char1-2.dynwin5.thr10.neg5.dim300.iter5",
    #         ischar=True,log_path="./error.wv.log")
    # with open("./wv.words.txt","w",encoding="utf-8") as f:
    #     f.write("\n".join(words))
    # vecs=np.concatenate(vecs,axis=0)
    # print(vecs.shape)
    # np.save("./wv.vecs.npy",vecs)
    
    pass