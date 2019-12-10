#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def read_csv(path):
    #print("按pandas格式写入csv文件，文件包含表头和索引：",path)
    return pd.read_csv(path,index_col=0)

def write_csv(data,path,index=True,header=True):
    '''读取数据时，将第一列作为索引。不存表头。'''
    data.to_csv(path,index=index,header=header)
    return

def exam_1(data,add_data):
    '''添加数据的例子'''
    # 新建表头为1，2，3的空表
    df=pd.DataFrame(columns=[1,2,3])
    # 添加一行数据
    df2=pd.Series({1:2, 2:22, 3:222})
    df=df.append(df2,ignore_index=True)#如果添加的数据时series类型的，则ignoreindex需要为True
    # 添加数据
    print(type(df))
    df=df.append(df)#如果添加的是dataframe类型，则可以不为True
    # 打印一行
    print(df.loc[0])
    # 打印一列
    print(df[1])
    return

if __name__ == "__main__":
    df=pd.DataFrame({1:[1,2,3],2:[2,2,2],3:[3,4,5]},columns=[1,2,3])
    print(df)
    df=df.drop([1],axis=1)
    print(df.values)
    pass