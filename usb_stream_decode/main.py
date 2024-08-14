
import cv2
import numpy as np

# 读取二进制文件
with open('output_rgb565_1.rgb', 'rb') as f:
    data = f.read()

# 将二进制数据转为16进制字符串,每个16进制数代表4比特，每个字节为8比特。每个字节显示为两位16进制数，（如FF,0A）,因此需要将一些数据进行补零操作。
hex_data = [f'{byte:02X}' for byte in data]

# 打印出前30个数据
print(hex_data[:30])

# 每两个数据进行拼接，生成新的数据列表。如 hex_data[0] = 'FF', hex_data[1] = '0A', 则拼接后的数据为 '0AFF'
new_hex_data = []
for i in range(0, len(hex_data), 2):
    new_hex_data.append(hex_data[i+1] + hex_data[i])

# 打印出前30个拼接后的数据
print(new_hex_data[:30])

# 将拼接好的数据，转换为2进制数
binary_data = [bin(int(data, 16))[2:].zfill(16) for data in new_hex_data]

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

# 打印出前30个RGB888数据
print(rgb888_data[:30])

# 将rgb888_data转换为1920*1080的图像数组
image = np.array(rgb888_data, dtype=np.uint8).reshape((1080, 1920, 3))

# 调用matplotlib库
import matplotlib.pyplot as plt

# 显示图像
plt.imshow(image)
plt.show()






# 将16进制字符串写入文件, 每8组数据一行, 每组数据之间添加空格
# with open('output_rgb565_1.hex', 'w') as f:
#     for i in range(0, len(hex_data), 16):
#         line = ' '.join(hex_data[i:i+16])
#         f.write(line + '\n')


