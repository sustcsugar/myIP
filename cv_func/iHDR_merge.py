from os import replace
import numpy as np
import cv2
import matplotlib.pyplot as plt
import hexfunc as hex_func

image_L="../img/HDR_L.bmp"
image_R="../img/HDR_R.bmp"



img_L = cv2.imread(image_L,0)
img_R = cv2.imread(image_R,0)

img_L_valid = img_L[0::2,:]
img_R_valid = img_R[0::2,:]
img_L_debayer_rggb = cv2.cvtColor(img_L_valid, cv2.COLOR_BayerRG2BGR)
img_L_debayer_bggr = cv2.cvtColor(img_L_valid, cv2.COLOR_BayerBG2BGR)
img_L_debayer_grbg = cv2.cvtColor(img_L_valid, cv2.COLOR_BayerGR2BGR)
img_L_debayer_gbrg = cv2.cvtColor(img_L_valid, cv2.COLOR_BayerGB2BGR)

img_merge = img_L
img_merge[0::2,:] = img_L_valid
img_merge[1::2,:] = img_R_valid


image_linear="../img/linear_L.bmp"
img_linear = cv2.imread(image_linear,0)
img_linear_debayer = cv2.cvtColor(img_linear, cv2.COLOR_BayerGB2BGR)

img_half=img_L_valid
img_half=img_linear[0::2,:]
img_linear_half_debayer = cv2.cvtColor(img_half, cv2.COLOR_BayerGB2BGR)


output_path="../img_output"
print(output_path+"/linear_fll")
cv2.imwrite(output_path+"/img_linear_full.jpg", img_linear)
cv2.imwrite(output_path+"/img_linear_full_debayer.jpg", img_linear_debayer)
cv2.imwrite(output_path+"/img_linear_half.jpg", img_half)
cv2.imwrite(output_path+"/img_linear_half_debayer.jpg", img_linear_half_debayer)

cv2.imshow("linear mode",img_linear)
cv2.imshow("linear debayer",img_linear_debayer)
cv2.imshow("half debayer",img_linear_half_debayer)

# cv2.imshow("HDR_L",img_L_valid)
# cv2.imshow("HDR_R",img_R_valid)
# cv2.imshow("HDR_L_debayer_rggb",img_L_debayer_rggb)
# cv2.imshow("HDR_L_debayer_bggr",img_L_debayer_bggr)
# cv2.imshow("HDR_L_debayer_grbg",img_L_debayer_grbg)
# cv2.imshow("HDR_L_debayer_gbrg",img_L_debayer_gbrg)
# cv2.imshow("HDR_merge",img_merge)

cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.figure('output')
# plt.imshow(img_L,cmap='gray',vmax=255,vmin=0); plt.title('img_L');plt.axis('off')
# plt.imshow(img_R,cmap='gray',vmax=255,vmin=0); plt.title('img_R');plt.axis('off')
# plt.imshow(img_L_valid,cmap='gray',vmax=255,vmin=0); plt.title('img_L_valid');plt.axis('off')
# plt.imshow(img_R_valid,cmap='gray',vmax=255,vmin=0); plt.title('img_R_valid');plt.axis('off')
# plt.show()
# plt.imshow(img_L_debayer); plt.title('img_L_debayer');plt.axis('off')
# plt.show()
# plt.imshow(img_R_debayer); plt.title('img_R_debayer');plt.axis('off')
# plt.show()