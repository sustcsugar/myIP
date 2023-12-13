# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 11:16:16 2023

@author: shig
"""

import numpy as np
import cv2

img_2 = np.array([
                    [1,2,3,4,5,6,7,8,9,10],
                    [1,2,3,4,5,6,7,8,9,10],
                    [1,2,3,4,5,6,7,8,9,10],
                    [1,2,3,4,5,6,7,8,9,10],
                    [1,2,3,4,5,6,7,8,9,10],
                    [1,2,3,4,5,6,7,8,9,10],
                    [1,2,3,4,5,6,7,8,9,10],
                    [1,2,3,4,5,6,7,8,9,10],
                    [1,2,3,4,5,6,7,8,9,10],
                    [1,2,3,4,5,6,7,8,9,10],
                 ],dtype='uint8'
                )



print(img_2)  
print("数据类型",type(img_2))           #打印数组数据类型  
print("数组元素数据类型：",img_2.dtype) #打印数组元素数据类型  
print("数组元素总数：",img_2.size)      #打印数组尺寸，即数组元素总数  
print("数组形状：",img_2.shape)         #打印数组形状  
print("数组的维度数目",img_2.ndim)      #打印数组的维度数目  

cv2.imshow('test', img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()