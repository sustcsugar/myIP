import numpy as np
import matplotlib.pyplot as plt
import cv_func.hexfunc as hex

img_raw = hex.hex2image('./cv_func/raw_rggb.hex',746,585)

height = img_raw.shape[0]
width = img_raw.shape[1]
x = np.arange(0,width/2)
y = np.arange(0,(height-1)/2)
xx,yy = np.meshgrid(x,y)

#r = np.zeros_like(img_raw,dtype=np.uint8)
#gr = np.zeros_like(img_raw,dtype=np.uint8)
#gb = np.zeros_like(img_raw,dtype=np.uint8)
#b = np.zeros_like(img_raw,dtype=np.uint8)
#r[::2,::2] = img_raw[::2,::2]
#gr[::2,1::2] = img_raw[::2,1::2]
#gb[1::2,::2] = img_raw[1::2,::2]
#b[1::2,1::2] = img_raw[1::2,1::2]
r = img_raw[:height-1:2,::2]
gr = img_raw[:height-1:2,1::2]
gb = img_raw[1:height-1:2,::2]
b = img_raw[1:height-1:2,1::2]


fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(xx[0:16,0:16],yy[0:16,0:16], r[0:16,0:16],color='red')
ax.plot_surface(xx[0:16,0:16],yy[0:16,0:16], b[0:16,0:16],color='blue')
ax.plot_surface(xx[0:16,0:16],yy[0:16,0:16],gr[0:16,0:16],color='green')
ax.plot_surface(xx[0:16,0:16],yy[0:16,0:16],gb[0:16,0:16],color='green')
plt.show()

