#!/usr/bin/env python3
# -*- coding: utf-8 -*-




## Img2Pdf
import os
import glob
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from PIL import Image
##

## 图形化界面 Gui
import sys
from PySide2 import QtWidgets
##

class Img2Pdf(object):
    def __init__(self):
        pass
        
    def img2pdf(self,img_folder,pdf_file,img_type):
        '''
        存img的文件夹里，找到所有符合img_type扩展名的图片，转为pdf。
        '''
        # 如果输入的是.png,把前面的点去掉，得到png
        if len(img_type):
            if img_type[0]==".":
                img_type=img_type[1:]
        # 读取文件夹中的所有指定扩展名的图片
        imgs=glob.glob(os.path.join(img_folder,"*."+img_type))
        if len(imgs)>0:
            # 设置页面大小为a4
            (a4h,a4w)=landscape(A4)#(841.8897637795277,595.2755905511812)前一个值高一点
            cv=canvas.Canvas(pdf_file,pagesize=(a4w,a4h))#第一个参数为横着的长度，第二个参数为竖着的页面长度
            print("页面大小a4纸:横(%f),竖(%f)"%(a4w,a4h))
            for img in imgs:
                print(img)
                # 如果图像的长宽大于a4，则缩小
                (w,h)=Image.open(img).size#返回值，后一个值高一点，对应win10电脑上图片的竖直方向的长度
                print("img 横 竖:",w,h)
                if w>a4w or h>a4h:
                    if w/a4w > h/a4h:
                        h=h/w*a4w#要先算h再更新w，不然后更新h时，w已经改变了，以前的值就丢失了
                        w=a4w
                    else:
                        w=w/h*a4h
                        h=a4h
                print("zoom:",w,h)
                cv.drawImage(img,0,a4h-h,w,h)#五个参数依次是：要是用的图像或视频等，放置图像的x轴坐标，防止图像的y轴坐标，要是用的图像宽度，要使用的图像高度（对应竖直方向）。
                cv.showPage()
            cv.save()
        else:
            print("No imgs to convert.")
        return

if __name__=="__main__":
    #i2p=Img2Pdf()
    #i2p.img2pdf(r"C:\Users\shaw\Pictures\Uplay\ANNO 2070® Complete Edition",r"C:\Users\shaw\Desktop\img.pdf","jpg")
    
    # 任何一个图形化的qt程序必须要创建QApplication的实例。
    # Qt可以接受命令行参数，我们可以把命令行参数传递给QApplication的对象，就像上图代码所示。
    # 也可以像下面一样传递个空数组app = QApplication([])
    app=QtWidgets.QApplication(sys.argv)
    print(sys.argv)
    # Qlabel是一种常见的小组件，他可以呈现诸如html之类的复杂文字或者图片
    label=QtWidgets.QLabel("<font color=red size=40>Hello World!</font>")
    # 调用show 函数让内容出现在显示器上
    label.show()
    # 最后一定要调用exec__函数来让Qt的消息循环之星起来，如果不明白的话，只需要记住写完代码一定要加上这个函数，不然程序会一闪而过就完了。
    sys.exit(app.exec_())
    pass