import cv2
import matplotlib.pyplot as plt
import numpy as np

img_origin = cv2.imread('./image/b_channel_filtered_10.jpg')
img_decoder = cv2.imread('./python_out/sample.jpg')

img_diff = (abs(img_origin - img_decoder)) * 10

img_out = np.zeros((720,1280,1),np.uint8)
for i in range(720):
    for j in range(1280):
        img_out[i][j] = 255


cv2.imwrite('./image/white_1280.jpg',img_out,[int(cv2.IMWRITE_JPEG_QUALITY),75])

plt.figure('原始图片与解码图片的对比')
plt.subplot(2,2,1);plt.imshow(img_origin);plt.axis('off');plt.title('origin')
plt.subplot(2,2,2);plt.imshow(img_decoder);plt.axis('off');plt.title('decoder')
plt.subplot(2,2,3);plt.imshow(img_diff);plt.axis('off');plt.title('img_diff')
plt.subplot(2,2,4);plt.imshow(img_out,cmap='gray',vmax=255,vmin=0);plt.axis('off');plt.title('img_out')

plt.show()