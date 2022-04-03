
import cmath
from os import replace
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

__version__ = '0.1'

def random_noise(image, noise_number):
    '''
    添加随机噪点(实际上就是随机在图像上将像素点的灰度值变为255即白色)
    :param image: 需要加噪的图片
    :param noise_num: 添加的噪音点数目,一般是上千级别的
    :return: img_noise
    '''
    img_noise = image
    rows,cols,chn = img_noise.shape

    for i in range(noise_number):
        x = np.random.randint(0,rows)
        y = np.random.randint(0,cols)
        img_noise[x,y,:] = 255
    return img_noise

def img2hex(image,hex_out, mode=0):
    '''
    将图片转换为hex文件, 如果是彩色图片,会转换为gray图.
    :param image: 需要转换的图片
    :param hex_out: 输出hex文件的文件名
    :param mode: 选择输出的格式，0为将原图转为灰度并输出hex，1为RGB转hex输出
    output hex format:  gray:   AA
                        RGB:    AABBCC
    '''
    outfile = open(hex_out,"w")
    img = cv2.imread(image,mode)
    #img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sp = img.shape

    for i in range(sp[0]):
        print("The Current Processing Row:",i)
        for j in range(sp[1]):
            if mode == 0:
                GRAY_string = '{:02X}'.format(img[i,j])
                outfile.write(GRAY_string+'\n')
            else:
                RGB_string = '{:02X}{:02X}{:02X}'.format(img[i,j,0],img[i,j,1],img[i,j,2])
                outfile.write(RGB_string+'\n')
            #print("pixel out:["+i+" , "+j+"]\n")
    outfile.close()

def hex2image(hex,width,height,mode=0):
    '''
    Function: convert hex to image. 
    :param hex: input hex path
    :param width: width of output image
    :param height:height of output image 
    :param mode: mode=0 for grayscale, mode=1 for RGB
    :return: img_out
    input hex format for    gray:   AA or 0xAA
                            RGB:    AABBCC or 0xAABBCC
    '''
    if mode == 0:
        img_out = np.zeros((height,width,1),np.uint8)
    else:
        img_out = np.zeros((height,width,3),np.uint8)

    file_in = open(hex,'r')
    img_hex = file_in.readlines()
   
    data_set = []
    for data in img_hex:
        data = data.strip('\n')

        if data[0:2] == '0x': #如果数据格式为0xff,则取0x之后的数据
            data1 = data[2:]
        else:                  #如果数据格式为ff，则取全部的数值
            data1 = data[:]

        data_clean = data1.replace('x','0')
        data_set.append(data_clean)  #将处理好的数据放到数组里面
    
    for row in range(height):   #将数组按照图片的长宽，进行逐行排布
        for col in range(width):
            if row*width+col < len(data_set):
                #img_out[row,col] = int(data_set[row*width+col],base=16)
                if mode == 0:
                    img_out[row,col] = int(data_set[row*width+col],base=16)
                else:
                    img_out[row,col,0] = int(data_set[row*width+col][0:2],base=16)
                    img_out[row,col,1] = int(data_set[row*width+col][2:4],base=16)
                    img_out[row,col,2] = int(data_set[row*width+col][4:6],base=16)

    return  img_out

def block_hex2image(hex,width,height,blockwidth=16, blockheight=8,mode=0):
    '''
    Function: convert hex to image. 
    :param hex: input hex path
    :param width: width of output image
    :param height:height of output image 
    :param mode: mode=0 for grayscale, mode=1 for RGB
    :return: img_out
    input hex format for    gray:   AA or 0xAA
                            RGB:    AABBCC or 0xAABBCC
    '''
    block_num_x = width / 16
    block_num_y = height / 8

    if mode == 0:
        img_out = np.zeros((height,width,1),np.uint8)
    else:
        img_out = np.zeros((height,width,3),np.uint8)

    file_in = open(hex,'r')
    img_hex = file_in.readlines()
   
    data_set = []
    # 清理数据, 进行格式转换
    for data in img_hex:
        data = data.strip('\n')

        if data[0:2] == '0x': #如果数据格式为0xff,则取0x之后的数据
            data1 = data[2:]
        else:                  #如果数据格式为ff，则取全部的数值
            data1 = data[:]

        data_clean = data1.replace('x','0')
        data_set.append(data_clean)  #将处理好的数据放到数组里面
    
    print('data number is {}'.format(len(data_set)) )
    
    file_out = open('output.log','w')
    for i in range(len(data_set)):
        block_num = int(i/128)
        block_position = (i)%128

        pixel_x = int(block_num % block_num_x) * 16 + int(block_position%16)
        pixel_y = int(block_num / block_num_x) * 8 + int(block_position/16)
        
        output = '{:04} num:{:04} position:{:04};  [{:04},{:04}]:{:03}'.format(i,block_num, block_position, pixel_x,pixel_y,int(data_set[i],base=16))
        file_out.write(output+'\n')
        print(output)
        
        img_out[pixel_y,pixel_x] = int(data_set[i],base=16)

    return  img_out


def read_isp_file(file_name,write_file):
    '''
    读取isp的地址文件
    param: file 输入的文件
    '''
    file_in = open(file_name,'r')
    lines = file_in.readlines()
    write_file.write("//"+file_name+ "\n")
    for line in lines:
        if(len(line) > 100):
            element = line.split(',')
            write_file.write(element[5]+' : '+element[2]+"\n")
            print(element[5]+' : '+element[2]+'\n')
    write_file.write("\n\n")
 
def img_resize(img_name):
    img = cv2.imread(img_name,0)
    cv2.imshow("origin_img",img)
    shrink_img1 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_NEAREST)
    shrink_img2 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
    shrink_img3 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)
    shrink_img4 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    cv2.imshow("shrink_img1",shrink_img1)
    cv2.imshow("shrink_img2",shrink_img2)
    cv2.imshow("shrink_img3",shrink_img3)
    cv2.imshow("shrink_img4",shrink_img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_decoder_hexfile(file_name):
    '''
    将decoder输出的仿真文件转为图片(sim.dat)
    :param hex: hex文件的路径
    :return: img_out
    file_name = "sim.dat"
    '''
    file_in = open(file_name,'r')
    hex_line = file_in.readlines()
    img_width = int(hex_line[0])
    img_height = int(hex_line[1])
    img_out = np.zeros((img_width,img_height,3),np.uint8)
    
    for i in range(img_height):
        for j in range(img_width):
            r = int(hex_line[i*img_width+j+2][0:2],base=16)
            b = int(hex_line[i*img_width+j+2][4:6],base=16)
            g = int(hex_line[i*img_width+j+2][2:4],base=16)
            img_out[i,j,0] = b
            img_out[i,j,1] = g
            img_out[i,j,2] = r

def checkerboard_picture_gen(height, width, size, low = 0,high=255):
    '''
    生成棋盘格图像, 用于测试. 
    height: 图像的高度
    width: 图像的宽度
    size: 棋盘格小方块的大小(方形)
    '''
    img_out = np.zeros((height,width,1),np.uint8)
    for i in range(height):
        #print(i,end=":\t")
        for j in range(width):
            width_num = (int)(j/size)
            height_num = (int)(i/size)
            #print("width_num  is:", end=" ")
            #print(width_num, end="\t")
            #print("height_num is:",end=" ")
            #print(height_num)
            #print("("+str(height_num%2)+","+str(width_num%2)+")",end=" ")
            if  height_num%2==0 and width_num%2==0:
                img_out[i,j] = high
            elif height_num%2==0 and width_num%2==1:
                img_out[i,j] = low
            elif height_num%2==1 and width_num%2==0:
                img_out[i,j] = low
            elif height_num%2==1 and width_num%2==1:
                img_out[i,j] = high
        #print()

    return img_out

def gradient_gray_img(width, height):
    '''
    生成灰度渐变图, 用于测试. 
    height: 图像的高度
    width: 图像的宽度
    low: 最低像素值
    high: 最高像素值
    '''
    img_out = np.zeros((height,width,1),np.uint8)
    for i in range(height):
        for j in range(width):
            img_out[i][j] = (int)((i * j)**0.5 % 256)
    return img_out

def gen_gray_jpeg(img):
    '''
    生成单通道的jpeg图像,用于测试
    img - string : 输入的RGB三通道图像路径
    '''
    name = img[0:-4]
    rgb_img = cv2.imread(img,1)
    b,g,r = cv2.split(rgb_img)
    cv2.imwrite(name+'_b_channel.jpg', b, [int(cv2.IMWRITE_JPEG_QUALITY),75])
    cv2.imwrite(name+'_g_channel.jpg', g, [int(cv2.IMWRITE_JPEG_QUALITY),75])
    cv2.imwrite(name+'_r_channel.jpg', r, [int(cv2.IMWRITE_JPEG_QUALITY),75])

if __name__ == '__main__':
    #### hex to image
    #hex = './jpeg_output/jpeg_out.dat'
    #img = hex2image(hex,1920,1080,0)
    ##r,g,b = cv2.split(img)
    ##img_bgr = cv2.merge([b,g,r])
    #cv2.imwrite('./python_out/jpeg_out.jpg',img)
    #plt.imshow(img,cmap='gray',vmin=0,vmax=255)
    #plt.show()
    data = './jpeg_output/720p_block.dat'
    img = block_hex2image(data,1280,720)
    cv2.imwrite('./python_out/720p_block.jpg',img)
    plt.imshow(img,cmap='gray',vmax=255,vmin=0)
    plt.show()

# generate checkboard
#   img = checkerboard_picture_gen(720,1280,1,64,192)
#   cv2.imwrite('./image/checkboard_1280x720_16.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),75])
#   plt.imshow(img,cmap='gray',vmin=0,vmax=255)
#   plt.show()

# generate gray
    #img = gradient_gray_img(256,256)
    #cv2.imwrite('./image/gradient_gray.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),75])
    #plt.imshow(img,cmap='gray',vmin=0,vmax=255)
    #plt.show()