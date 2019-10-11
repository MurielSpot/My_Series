#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf

## cnn ###########################################################
def sentence_conv(inputs,filter_height,filter_num,strides=[1,1,1,1],padding="VALID",is_train=None,scope=None):
    '''
    对文本进行卷积，所以只在词方向做卷积。
    卷积操作：输入是[bs,h,w,channel]，卷积核形状[h,w,in channel,out channel]。
    池化操作：输入是[bs,h,w,channel]，池化ksize[1,h,w,1]，batch和channels上不做池化。strides：[1,h,w,1]。
    
    inputs：[bs,h,w,channel]。
    filter_height: 卷积核高度，即对几个词汇做卷积。
    filter_num: 卷积核数量，即输出通道数。
    strides: [1, 1, 1, 1]第一维和最后一维一定为1，
    padding: VALID不填充,SAME填充。
    
    例子：输入[bs,h,w,1]=>卷积，池化=>[bs,1,1,fn]
    '''
    with tf.variable_scope(scope or "sentence_conv"):
        
        print("sentence conv input:",inputs.name,inputs.shape)

        # [bs,h,w,c]=>[bs,h-fh+1,1,fn]
        filter_width=inputs.get_shape()[2]
        filter_in_channel=inputs.get_shape()[3]
        filter=tf.get_variable("filter",shape=[filter_height,filter_width,filter_in_channel,filter_num],dtype='float32',trainable=is_train)
        bias=tf.get_variable("bias",shape=[filter_num],dtype='float32',trainable=is_train)
        conv_op=tf.nn.conv2d(inputs,filter,strides,padding)+bias
        
        print("sentence conv output:",conv_op.name,conv_op.shape)
        
        # [bs,h-fh+1,1,fn]=>[bs,1,1,fn]
        maxpool_height=inputs.get_shape()[1]-filter_height+1
        maxpool_op=tf.nn.max_pool(conv_op,ksize=[1,maxpool_height,1,1],strides=[1,1,1,1],padding="VALID")
        
        print("sentence maxpool output:",maxpool_op.name,maxpool_op.shape)
        return maxpool_op
    
def sentence_multi_conv(inputs,filter_heights,filter_nums,strides=[1,1,1,1],padding="VALID",is_train=None,scope=None):
    '''
    对文本进行卷积，所以只在词方向做卷积。
    filter_heights:卷积核的高度列表。
    filter_nums:也是一个列表，包含不同高度卷积核对应的卷积核数量。
    
    例子：输入[bs,h,w,1]=>卷积，池化=>[bs,1,1,fn]=>多种卷积核拼接=>[bs,1,1,f1n+f2n+f3n+...]
    '''
    with tf.variable_scope(scope or "sentence_multi_conv",reuse=tf.AUTO_REUSE):
        assert len(filter_heights) == len(filter_nums)
        outs = []
        for filter_height,filter_num in zip(filter_heights,filter_nums):
            if filter_num==0:
                continue
            out = sentence_conv(inputs,filter_height,filter_num,strides=strides,padding=padding,is_train=is_train,scope="sentence_conv_{}".format(filter_height))
            outs.append(out)
        concat_out = tf.concat(outs,-1)
        print("sentence_multi_conv output:",concat_out.name,concat_out.shape)
        return concat_out

## rnn ###########################################################
def sentence_unirnn():
    pass

def sentence_birnn():
    pass

def sentence_multi_birnn():
    pass

## attention ###########################################################
def attention(inputs,is_train=None):
    '''
    当前attention的规则：
    注意力矩阵求法：aw=softmax((inputs*w+b1)*b2)
    返回结果：max_pool(inputs*aw)
    
    例子：[bs,...,x,W_dim]=>W形状[W_dim,W_dim],b1和b2[W_dim]=>注意力矩阵与输出相同[bs,...,x,W_dim]
                        =>取倒数第二维最大值，即不同卷积核提取特征中最大的那个，输出维度减小一维，得[bs,...,W_dim]
    '''
    W_dim=inputs.shape.as_list()[-1]
    W=tf.get_variable(initializer=tf.truncated_normal(shape=(W_dim,W_dim),stddev=0.1,dtype=tf.float32),name="attention_weight",trainable=is_train)
    b1=tf.get_variable(initializer=tf.constant(0.1,shape=[W_dim],dtype=tf.float32),name="attention_bias_1",trainable=is_train)
    b2=tf.get_variable(initializer=tf.constant(0.1,shape=[W_dim],dtype=tf.float32),name="attention_bias_2",trainable=is_train)
    # 得到attention矩阵
    MW_b1=tf.tensordot(inputs,W,axes=1)+b1#inputs的最后一维，和w的第一维做矩阵乘法
    MW_b1_b2=tf.multiply(tf.tanh(MW_b1),b2)
    attention_matrix=tf.nn.softmax(MW_b1_b2)
    # 得到新的矩阵
    outputs=tf.multiply(inputs,attention_matrix)
    # maxpooling [batch_size,...,x,W_dim] =》[batch_size,...,1,W_dim] 对axis=2做池化
    print(W.shape)
    print(outputs.shape)
    return tf.reduce_max(outputs,axis=[-2])

def cos_tensor(a,b):
    '''
    两个张量求余弦值，对两者的最后一维一一对应求余弦。
    要求两个张量形状一样。
    a`b/(|a|`|b|)
    
    注意！！！分母为0时，cos得到的结果对应约等于-1，而不是无穷大或者负无穷大，也不是1.
    '''
    assert a.shape.as_list()==b.shape.as_list()
    
    # 开始计算cos
    dot=tf.reduce_sum(tf.multiply(a,b),axis=[-1])
    abs_a=tf.reduce_sum(tf.square(a),axis=[-1])
    abs_b=tf.reduce_sum(tf.square(b),axis=[-1])
    abs_ab=tf.sqrt(tf.multiply(abs_a,abs_b))
    cos=tf.div(dot,abs_ab)
    
    # 这时的cos并非最终结果，需要将分母是0的位置的值换成-inf，再clip
    inf_minus=tf.ones(shape=abs_ab.shape.as_list())*(-1e12)# 建立一个无穷负值的张量
    tag=tf.less(abs_ab,1e-12)
    cos=tf.where(tag,inf_minus,cos)
    
    cos=tf.clip_by_value(cos,-0.99999,0.99999)
    return cos
    

if __name__ == "__main__":
    #x=tf.truncated_normal([3,4,5])
    #a=tf.Variable([[[[2,2],[0,0]],[[2,3],[0,1]]]],dtype="float32")
    #b=tf.Variable([[[[-2,-2],[1,0]],[[0,0],[-1,0]]]],dtype="float32")
    a=tf.Variable([[1,2,3]],dtype="float32")
    b=tf.maximum(1.5,a)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        o1=sess.run(b)
        print(o1,o1.shape)
    pass