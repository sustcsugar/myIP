import cv2
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STFangsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题

if __name__ == '__main__':
    x_data = np.linspace(1,25,num=25,dtype=int)
    storage_3200 = [56.08,59.98,64.70,71.28,78.49,89.29,89.47,89.16,89.16,89.11,89.07,88.43,87.98,88.25,88.25,87.93,87.89,87.93,88.20,88.29,88.11,88.11,88.11,88.38,88.84]
    quality_3200 = [50,56.25,62.50,68.75,75,81.25,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5,87.5]

    storage_6400 = [64.51,70.07,76.46,85.31,85.22,85.67,85.67,85.40,85.95,86.31,86.50,86.68,86.77,87.04,87.04,86.68,86.41,86.22,86.59,86.22,86.13,85.77,85.77,85.77,85.68]
    quality_6400 = [50,56.25,62.50,68.75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75]

    storage_12800 = [54.87,60.06,65.76,74.23,83.56,83.70,83.56,83.20,83.74,83.83,83.97,83.83,83.65,83.38,82.83,83.33,83.83,83.79,83.83,83.88,83.79,84.06,84.34,84.15,84.11]
    quality_12800 = [50,56.25,62.50,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75,68.75]
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.plot(x_data,quality_3200,'ro--',label="left",markersize=4)
    ax1.set_ylabel('压缩质量(%)',fontsize=15)
    ax1.legend(('压缩质量','1'), loc='upper left')  
    ax1.set_ylim(40,100)
    ax1.grid()
    ax1.set_xlim(0,25)

    ax2 = ax1.twinx()
    ax2.plot(x_data,storage_3200,'bo--',label="right",markersize=4)
    ax2.set_ylabel('存储占用率(%)',fontsize=15)
    ax2.legend(('存储占用率','1'), loc='upper right') 
    ax2.set_ylim(40,100)

    #plt.title('ISO12800',fontsize=18)
    ax1.set_xlabel('帧序号',fontsize=15)

    #plt.text(0,140,'Average Variance:'+str(np.round(average_variance, 3)),fontsize=15)
    
    plt.show()