# reference: https://blog.csdn.net/James_Ray_Murphy/article/details/79173388


import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import ptp

def print_img_info(img):
    print("================打印一下图像的属性================")
    print("图像对象的类型 {}".format(type(img)))
    print(img.shape)
    print("图像宽度: {} pixels".format(img.shape[1]))
    print("图像高度: {} pixels".format(img.shape[0]))
    # GRAYScale 没有第三个维度， 所以这样会报错
    # print("通道: {}".format(img.shape[2]))
    print("图像分辨率: {}".format(img.size))
    print("数据类型: {}".format(img.dtype))


img_gray_read= cv2.imread("./image/filtered_10.png",0)

height,width = img_gray_read.shape
if img_gray_read is None:
    print('empty image')
else:
    print_img_info(img_gray_read)
    img_gray = img_gray_read.astype('float')
    print_img_info(img_gray)
    print('********************The data of img_gray_float:********************')
    print(img_gray)

    img_dct = cv2.dct(img_gray)
    print('********************The data of img_dct:********************')
    print_img_info(img_dct)
    print(img_dct)
    #show the result of dct
    img_dct_log = np.log(abs(img_dct))


    img_dct_integer = np.trunc(img_dct)
    img_dct_integer_log = np.log(abs(img_dct_integer))
    print('********************The data of img_dct_integer:********************')
    print_img_info(img_dct_integer)
    print(img_dct_integer)
    print('********************The data of img_dct_integer_zero:********************')
    img_dct_integer_zero = img_dct_integer
    for i in range(height):
        for j in range(width):
            if i+j > height+width:
                img_dct_integer_zero[i,j] = 0
    print(img_dct_integer_zero)
    img_dct_integer_zero_log = np.log(abs(img_dct_integer_zero))

    img_idct = cv2.idct(img_dct)
    print('********************The data of img_idct********************')
    print_img_info(img_idct)
    print(img_idct)

    img_idct_integer_zero = cv2.idct(img_dct_integer_zero)

    plt.figure("diff for cvshow and pltshow")
    plt.subplot(231); plt.imshow(img_gray_read,cmap="gray"); plt.axis('off'); plt.title('gray')
    plt.subplot(234); plt.imshow(img_gray,cmap="gray"); plt.axis('off'); plt.title('gray_float')

    plt.subplot(232); plt.imshow(img_dct_log,cmap="gray"); plt.axis('off'); plt.title('dct')
    plt.subplot(235); plt.imshow(img_dct_integer_zero_log,cmap="gray"); plt.axis('off'); plt.title('dct_integer_zero')

    plt.subplot(233); plt.imshow(img_idct,cmap="gray"); plt.axis('off'); plt.title('idct')

    plt.subplot(236); plt.imshow(img_idct_integer_zero,cmap="gray"); plt.axis('off'); plt.title('idct_integer_set_q_quarter_to_zero')
    plt.show()
