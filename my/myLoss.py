#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def mse(logits,labels):
    '''
    logits,labels都是一维numpy数组。
    rmse等于logits和labels求差值，再平方，所以结果的logits和labes的平方相加取均值。
    '''
    return np.sum(np.square(logits-labels))/len(logits)

def rmse(logits,labels):
    '''
    logits,labels都是一维numpy数组。
    rmse等于logits和labels求差值，再平方，所以结果的logits和labes的平方相加取均值再开根号。
    即mse加上一个根号。
    '''
    return np.sqrt(mse(logits=logits,labels=labels))

def r_squared(mse,var):
    assert var>=1e-12
    return 1-mse/var
    

if __name__=="__main__":
    a=np.array([3,10,11])
    b=np.array([2,4,10])
    print(rmse(a,b))
    pass