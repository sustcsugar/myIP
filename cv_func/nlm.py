import cv2 as cv
import numpy as np


def nlm(img_in,img_out,windowsSize=5,searchSize=21):

    for x in img_in:
        for y in x:
            print(y)






if __name__ == '__main__':
    img = cv.imread('D:/Python/PycharmProjects/opencv/lena.png',cv.IMREAD_GRAYSCALE)
    img_out = np.zeros(img.shape,np.uint8)
    nlm(img,img_out)
    cv.imshow('img_out',img_out)
    cv.waitKey(0)
    cv.destroyAllWindows()
        
