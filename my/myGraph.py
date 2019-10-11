#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot
import matplotlib.pyplot as plt

y_train = [0.840,0.839,0.834,0.832,0.824,0.831,0.823,0.817,0.814,0.812,0.812,0.807,0.805]
y_test  = [0.838,0.840,0.840,0.834,0.828,0.814,0.812,0.822,0.818,0.815,0.807,0.801,0.796]

def draw_line(x,y,save_path):
    plt.title("matplotlip plot line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.margins(0)
    plt.plot(x, y, marker='o', mec='r', mfc='w')
    plt.savefig(save_path)
    plt.show()  # 注意plt.savefig()要放在plt.show()之前，不然保存的图片是空白的
    #plt.xticks(x[0:len(x):10], x[0:len(x):10], rotation=45)
    #plt.tick_params(axis="both")


def exam_mnist():
    from sklearn.datasets import fetch_openml
    #mnist = fetch_openml('MNIST original',data_home=r'E:\dataset\img_dataset\mnist')
    #digits = mnist.load_digits(n_class=5)
    #print(digits)
    #X = digits.data y = digits.target printX.shape n_img_per_row = 20 img = np.zeros((10 * n_img_per_row, 10 * n_img_per_row))for i in range(n_img_per_row): ix = 10 * i + 1 for j in range(n_img_per_row): iy = 10* j + 1 img[ix:ix + 8, iy:iy + 8] = X[i * n_img_per_row + j].reshape((8, 8))plt.imshow(img, cmap=plt.cm.binary) plt.title('A selection from the 64-dimensional digits dataset')

import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
tsne = TSNE(n_components=2)
tsne.fit_transform(X)
print(tsne.embedding_)

if __name__ == "__main__":
    #draw_line([1,2,3],[10,3,4],save_path="tmp.jpg")
    #exam_mnist()
    pass
