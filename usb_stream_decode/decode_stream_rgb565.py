import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


# 创建一个Tkinter根窗口，但不显示它
root = tk.Tk()
root.withdraw()

# 弹出文件选择对话框，并获取所选文件的路径
file_path = filedialog.askopenfilename()

# 读取文本文件
# with open('bushound_rgb565_ov5640_color.txt', 'r') as file:
# with open('/Users/sugar/work/python/myIP/usb_stream_decode/bushound-mipi-tx-process.txt', 'r') as file:
# with open('bushound_rgb565_ov5640_length_proc.txt', 'r') as file:
if file_path:
    with open(file_path, 'r') as file:
        print(f'Reading File : {file_path}')
        data = file.read()
else:
    print('No file selected')
    exit()



# 将文本数据按照每两个字符一组分割成列表
data_list = [data[i:i+2] for i in range(0, len(data), 2)]
print(data_list[:10])
print(len(data_list))


# 每两个数据进行拼接，生成新的数据列表。如 hex_data[0] = 'FF', hex_data[1] = '0A', 则拼接后的数据为 '0AFF'
data_pixel = []
for i in range(0, len(data_list)-1, 2):
    data_pixel.append(data_list[i+1] + data_list[i])

print(data_pixel[:10])

# 将拼接好的数据，转换为2进制数
binary_data = [bin(int(data, 16))[2:].zfill(16) for data in data_pixel]


# 打印出前30个2进制数据
print(binary_data[:30])

# 将2进制数据，按照5，6，5的方式， 拆分为3部分，代表R，G，B三个通道的数据
rgb_data = []
for data in binary_data:
    r = data[:5]
    g = data[5:11]
    b = data[11:]
    rgb_data.append((r, g, b))

# 打印出前30个RGB数据
print(rgb_data[:30])


# 将565格式的RGB数据，转换为RGB888格式
rgb888_data = []
for r, g, b in rgb_data:
    r = int(r, 2) << 3
    g = int(g, 2) << 2
    b = int(b, 2) << 3
    rgb888_data.append((r, g, b))

# 转换为10进制数字
rgb888_data = [(r, g, b) for r, g, b in rgb888_data]

# 打印出前30个RGB888数
print(rgb888_data[:30])

# 将rgb888_data转换为1920*1080的图像数组，没有数据的填充为0
image = np.zeros((1080, 1920, 3), dtype=np.uint8)
for i, (r, g, b) in enumerate(rgb888_data[:2073600]):
    x = i % 1920
    y = i // 1920
    image[y, x] = (r, g, b)

# 打印出图像的前10个像素
print(image[:10, :10])


# 显示图像
plt.imshow(image)
plt.show()
