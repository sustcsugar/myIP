import numpy as np
import matplotlib.pyplot as plt
import math


def dct1(x):
    F = np.zeros(len(x))
    for m in range(len(F)):
        F[m] = 0
        for k in range(len(x)):
            F[m] = x[k] * math.cos(math.pi / len(x) * m * (k + 1/2)) + F[m]
    return F

def idct1(F):
    x = np.zeros(len(F))

def dct2(x):
    return x

def idct2(F):
    return x




if __name__ == "__main__":
    
    x = np.arange(100)
    F = dct1(x)

    F_wave = [[0 for i in range(len(x))] for i in range(len(F))]

    for m in range(len(F_wave)):
        for k in range(len(F_wave[m])):
            F_wave[m][k] = 2 * F[m] / len(x) * math.cos( math.pi / len(x) * (m + 1/2) * (k+1) )
    
    print('F_wave is : {}'.format(F_wave))

    print("x is : {}".format(x))
    print('result of dct is :')
    for i in F:
        print("{:.2f}".format(i),end=' ')

    plt.subplot(7,2,1);  plt.plot(x); plt.title('x')
    plt.subplot(7,2,3);  plt.plot(F); plt.title('F')
    plt.subplot(7,2,2);  plt.plot(F_wave[0]); plt.title('F_wave_0')
    plt.subplot(7,2,4);  plt.plot(F_wave[1]); plt.title('F_wave_1')
    plt.subplot(7,2,6);  plt.plot(F_wave[2]); plt.title('F_wave_2')
    plt.subplot(7,2,8);  plt.plot(F_wave[3]); plt.title('F_wave_3')
    plt.subplot(7,2,10); plt.plot(F_wave[4]); plt.title('F_wave_4')
    plt.subplot(7,2,12); plt.plot(F_wave[5]); plt.title('F_wave_5')
    plt.subplot(7,2,14); plt.plot(F_wave[6]); plt.title('F_wave_6')
    plt.show()

