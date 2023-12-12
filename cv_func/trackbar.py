import cv2
import numpy as np

def adjust_background():
    global img
    img = np.zeros((500,500,3),dtype=np.uint8)
    
    cv2.namedWindow('color-testing@Sugar',cv2.WINDOW_NORMAL)
    img[:]=[255,255,255]
    switch = '0:OFF\n1:ON'
    cv2.createTrackbar(switch,'color-testing@Sugar',0,1,callback)
    cv2.createTrackbar('R','color-testing@Sugar',0,255,callback)
    cv2.createTrackbar('G','color-testing@Sugar',0,255,callback)
    cv2.createTrackbar('B','color-testing@Sugar',0,255,callback)

    while True:
        global r,g,b
        r = cv2.getTrackbarPos('R','color-testing@Sugar')
        g = cv2.getTrackbarPos('G','color-testing@Sugar')
        b = cv2.getTrackbarPos('B','color-testing@Sugar')

        if cv2.getTrackbarPos(switch,'color-testing@Sugar') == 1 :
            img[:] = [b,g,r]
        else :
            img[:] = [255,255,255]

        if cv2.waitKey(10) & 0xFF == 27:  # ESC(ASCII码为27)
            break

        cv2.imshow('color-testing@Sugar',img)
    
    cv2.destroyAllWindows()

def callback(object):
    pass

if __name__ == '__main__':
    adjust_background()