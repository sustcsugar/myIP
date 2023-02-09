import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

def psnr(img1, img2):
    mse = np.mean( (img1/1.0 - img2/1.0) ** 2 )
    if mse < 1.0e-10:
        return 100
    return 10 * math.log10(255.0**2/mse)


if __name__ == '__main__':
    gt = cv.imread('/Users/sugar/Downloads/filtered_30.png')
    img = cv.imread('/Users/sugar/Downloads/frame_30.png')
    print(psnr(img,gt))