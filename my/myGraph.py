#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图

import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.manifold import TSNE

y_train = [0.840,0.839,0.834,0.832,0.824,0.831,0.823,0.817,0.814,0.812,0.812,0.807,0.805]
y_test  = [0.838,0.840,0.840,0.834,0.828,0.814,0.812,0.822,0.818,0.815,0.807,0.801,0.796]

def draw_roc(label,pred,pos_label,save_path=None,title=None):
    label=np.array(label)
    pred=np.array(pred)
    fpr,tpr,thresholds=metrics.roc_curve(label,pred,pos_label=pos_label)
    auc=metrics.auc(fpr, tpr)
    print("fpr,tpr,thresholds,auc:",fpr,tpr,thresholds,auc)
    
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',lw=lw, label='ROC curve (area = %0.2f)' % auc)
    plt.plot([0,1],[0,1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0,1.0])
    plt.ylim([0.0,1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    if title:
        plt.title(title)
    plt.legend(loc="lower right")
    if save_path is None:
        plt.show()
    else:
        plt.savefig(save_path)
        plt.ion()
        plt.pause(1)
        plt.close()
    return

# def draw_bar(x,y,save_path=None,line_style="b-",img_name="line graph",x_name="x axis",y_name="y axis",x_lim=None,y_lim=None):
#     plt.title(img_name)
#     plt.xlabel(x_name)
#     plt.ylabel(y_name)
#     plt.margins(0)
#     if x_lim:
#         plt.xlim((x_lim[0],x_lim[1]))
#     else:
#         plt.xlim((min(x)-0.1,max(x)+0.1))
#     if y_lim:
#         plt.ylim((y_lim[0],y_lim[1]))
#     else:
#         plt.ylim((min(y)-0.1,max(y)+0.1))
#     plt.bar(x,y,line_style)
#     if save_path is not None:
#         plt.savefig(save_path)
#         plt.ion()
#         plt.pause(1)
#         plt.close()
#     else:
#         plt.show()  # 注意plt.savefig()要放在plt.show()之前，不然保存的图片是空白的
#     return

def draw_line(x,y,save_path=None,line_style="b-",img_name="line graph",x_name="x axis",y_name="y axis",x_lim=None,y_lim=None):
    plt.title(img_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.margins(0)
    if x_lim:
        plt.xlim((x_lim[0],x_lim[1]))
    else:
        plt.xlim((min(x)-0.1,max(x)+0.1))
    if y_lim:
        plt.ylim((y_lim[0],y_lim[1]))
    else:
        plt.ylim((min(y)-0.1,max(y)+0.1))
    plt.plot(x,y,line_style)
    if save_path is not None:
        plt.savefig(save_path)
        plt.ion()
        plt.pause(1)
        plt.close()
    else:
        plt.show()  # 注意plt.savefig()要放在plt.show()之前，不然保存的图片是空白的
    return

def draw_dot(x,y,save_path=None,dot_color="b",img_name="line graph",x_name="x axis",y_name="y axis",x_lim=None,y_lim=None):
    plt.title(img_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    if x_lim:
        plt.xlim((x_lim[0],x_lim[1]))
    else:
        plt.xlim((min(x)-0.1,max(x)+0.1))
    if y_lim:
        plt.ylim((y_lim[0],y_lim[1]))
    else:
        plt.ylim((min(y)-0.1,max(y)+0.1))
    plt.scatter(x,y,color=dot_color)
    if save_path is not None:
        plt.savefig(save_path)
    plt.show()
    return

def draw_dot_3d(x,y,z,save_path=None,dot_color="b",img_name="dot graph",x_name="x axis",y_name="y axis",z_name="z axis"):
    fig=plt.figure()
    ax=Axes3D(fig)
    # 添加坐标轴(顺序是Z, Y, X)
    ax.set_zlabel(z_name,fontdict={"size":15,"color":"red"})
    ax.set_ylabel(y_name,fontdict={"size":15,"color":"blue"})
    ax.set_xlabel(x_name,fontdict={"size":15,"color":"green"})
    
    ax.scatter(x,y,z,c=dot_color,label="label")
    plt.legend(loc="upper right")
    if save_path is not None:
        plt.savefig(save_path)
    plt.show()
    return

def draw_tsne(data,to_dim,plot_style="b."):
    '''
    注意里面会初始化一个tsne对象，所以重复调用这个函数得到的结果之间应该是没有关联的，所以只能一次性地使用这个函数。
    '''
    assert isinstance(data,np.ndarray)#or isinstance(data,numpy.ndarray)
    tsne=TSNE(n_components=to_dim)
    results=tsne.fit_transform(data)
    plt.plot(results[:,0],results[:,1],plot_style)
    
    print(tsne.embedding_)
    plt.colorbar()
    plt.show()
    
    #plt.embedding_2d(results)

def gen_colors(start,num,del_color=["#000000"],step=None):
    '''
    start:随便给的开始数值，相邻的数字颜色也比较相近。
    num:要取几个颜色。
    del_color:表示某些颜色不考虑，del_color的值应该用16进制传入。
    step:默认为None，即根据num值来自动确定相邻颜色跨度，这种方法比较好。颜色从start开始，start+step对应的数为下一个数值，但是step不能取的太大，因为rgb颜色是有限的，取太大数值就循环了。
    
    返回一个长度为num的列表,每个颜色都用rgb格式的六个数字表示，在列表里存储为一个个字符串。
    '''
    assert isinstance(del_color,list)
    #16777215==0xffffff
    colors=[]
    cnt=0
    if step is None:
        step=16777215//num
    while cnt<num:
        start+=step
        now_seed=start%16777216
        now_seed="#%06x"%(now_seed)
        #print(type(now_seed),now_seed)
        if now_seed in del_color:
            continue
        colors.append(now_seed)
        cnt+=1
    print(colors)
    # r=0#[0,255]
    # g=0
    # b=0
    assert num==len(colors)
    return colors
    # return "#%02x%02x%02x"%(r,g,b)

def sns_example():
    import pandas as pd
    # tips = sns.load_dataset("tips")
    # print(tips.info())
    # input(tips)
    #data=pd.DataFrame({'x':np.array([1,2,3,1]),'y':np.array([2,3,4,1]),"class":[3,3,2,2]})
    # data=pd.DataFrame({"x":[1,2,33,3,3,4,1,1],"y":[2,3,4,5,6,7,9,10],"month":["8","10","8","3","3","8","10","8"]})
    # data["month"]=data["month"].astype('category')
    # print(data.info())
    # print(data["month"].values)
    # print(data.month.values)
    
    sns.palplot(sns.color_palette("Set1",9))
    sns.palplot(sns.color_palette("Set2",9))
    sns.palplot(sns.color_palette("Set3",9))
    sns.palplot(sns.color_palette("hls",9))
    sns.palplot(sns.color_palette("Paired",9))
    sns.palplot(sns.color_palette('Accent',8))
    sns.palplot(sns.light_palette('green',8))
    sns.palplot(sns.color_palette('RdBu',8))
    sns.palplot(sns.color_palette('Blues_d',8))
    sns.palplot(sns.color_palette('pastel',8))
    
    
    # lab=[1,2,3,4,1,2]
    # plt.scatter(data["x"],data["y"],color=colors[0],label = lab[0])
    # plt.scatter([1,0],[2,2],color=colors[1],label = lab[1])
    #sns.set()
    #current_palette = sns.color_palette()
    #sns.palplot(current_palette)
    #x=np.array([[1,2],[2,3],[3,4],[1,1]])
    #sns.scatterplot(x=data['x'], y=data['y'],hue=data["month"].values,data=data,palette="Set3")
    #plt.legend(loc="upper right")
    #sns.palplot(sns.color_palette("hls", 36))#palplot是创建调色板  color_palette（颜色空间，设置几种颜色块）
    #plt.show()
    #sns.palplot(sns.color_palette("Paired",36)) #两种分割的渐变
    #sns.palplot(sns.color_palette("Set2", 36))
    plt.legend(loc='upper left')
    plt.show()
    return

def random_color():
    raise NotImplementedError()

if __name__ == "__main__":
    #sns_example()
    #draw_dot_3d(x=[1,2],y=[2,3],z=[1,1])
    
    # plt.ylim((0,1000))
    # plt.ylabel("Number of judgement reports")
    # fig=plt.bar(["Group-1","Group-2","Group-3","Group-4"],[620,852,623,557],width=0.2,fc="black")
    # for rec in fig:
    #     plt.text(rec.get_x(),rec.get_height()+5,rec.get_height())
    # # print(fig.get_width)
    # plt.savefig("./group.png")
    # plt.show()
    
    group=np.array([[2,18,6.679032],[1,34,13.828638],[37,82,46.707865],[86,174,108.509474]])
    x=[1,2,3,4]
    xname=["Group-1","Group-2","Group-3","Group-4"]
    plt.ylabel("Punishment Period (months)")
    
    colors=sns.color_palette("Set1",9)
    
    plt.plot(x,group[:,0],marker="s",color=colors[0],label="Minimum")
    plt.plot(x,group[:,1],marker="*",color=colors[1],label="Maximum")
    plt.plot(x,group[:,2],marker="o",color=colors[2],label="Average")
    
    for i in range(3):
        for j in range(4):
            plt.text(x[j]+0.1,group[j][i]-4,"%.2f"%(group[j][i]))
    plt.xticks(x, xname)#, rotation=45)
    
    plt.legend(loc="upper left")
    plt.savefig("./sentence.png")
    plt.show()
    # X = np.array([[1,0,0], [1,1,0], [1, 0,0], [1, 1, 0]])
    # draw_tsne(X,2)
    # Y=np.array([[0,0,0], [1,1,1], [2,3,2], [3,2,3]])
    # #draw_dot_3d([1,2,3,4],[1,2,3,4],[0,0,1,1])
    # tsne=TSNE(n_components=2)
    # res=tsne.fit_transform(X)
    # print(res)
    # print(res[:,0])
    # print(res[:,1])
    
    #plt.scatter(x=[i for i in range(10)],y=[i for i in range(1,11)],c=gen_colors(10,10),marker="*",s=200)
    # color1=plt.cm.Set1(2)
    # color2=plt.cm.Set2(3)
    # color3=plt.cm.Set3(4)
    # print(color1,color2,color3)
    # plt.scatter(x=[i for i in range(10)],y=[i for i in range(1,11)],c=[color1,color2,color3],marker="*",s=200)
    
    # for i in range(1):
    #     #color=plt.cm.Set3(i)
    #     plt.scatter(x=i,y=i,c="#00ff00",marker="*",s=150)
    # plt.show()
    # gen_colors(16777216,20)
    pass
