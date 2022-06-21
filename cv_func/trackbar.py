import cv2
import numpy as np

def adjust_background():
    global img
    img = np.zeros((500,500,3),dtype=np.uint8)
    
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    img[:]=[255,255,255]
    switch = '0:OFF\n1:ON'
    cv2.createTrackbar(switch,'image',0,1,callback)
    cv2.createTrackbar('R','image',0,255,callback)
    cv2.createTrackbar('G','image',0,255,callback)
    cv2.createTrackbar('B','image',0,255,callback)

    while True:
        global r,g,b
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G','image')
        b = cv2.getTrackbarPos('B','image')

        if cv2.getTrackbarPos(switch,'image') == 1 :
            img[:] = [b,g,r]
        else :
            img[:] = [255,255,255]

        if cv2.waitKey(10) & 0xFF == 27:  # ESC(ASCII码为27)
            break

        cv2.imshow('image',img)
    
    cv2.destroyAllWindows()

def callback(object):
    pass

if __name__ == '__main__':
    adjust_background()