#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def timer(func):
    '''计算函数运行时间的装饰器'''
    # 装饰器装饰的函数有参数
    def deco(*args,**kwargs):    #添加可变参数*args和**kwargs
        start = time.time()
        func(*args,**kwargs)      #这里也是一样，添加可变参数*args和**kwargs
        stop = time.time()
        print("function |%s| runtime: %f"%(func.__name__,stop-start))
    return deco

@timer
def abc():
    return 1003

if __name__ == "__main__":
    abc()
    pass