# **********************************************************
# * Author : SHI Gang
# * Email : 1144392179@qq.com
# * Create time : 2022-02-17 17:32:20
# * Last modified :2022-02-17 17:32:20
# *
# * Filename : creaticcfp.py
# * Description : 根据dc生成的面积报告, 自动计算指定长宽比与填充率的floorplan的大小
# * Sample: python creaticcfp.py --aspect_ratio 1:2 --fill 50 --arealog top_denoise_sram.area.log --cellname top_denoise_sram
# * Copyright (c) : AnLab 2021. All rights reserved.
# **********************************************************

import argparse
import re
import os

parse = argparse.ArgumentParser(description='根据dc生成的综合报告, 计算出后端floorplan的大小')
parse.add_argument('--aspect_ratio',type=str,required=True,default='1:1',help='W:H or WxH')
parse.add_argument('--fill',type=int,required=True,default=40,help='填充率 0-100')
parse.add_argument('--arealog',type=str,required=True,help='面积报告文件')
parse.add_argument('--cellname',type=str,required=True,help='cellname')
args = parse.parse_args()

aspect_ratio = args.aspect_ratio
fill = args.fill
area_log_file=args.arealog
cellname = args.cellname

# **********************************************************
#             read area from log
# **********************************************************

if not os.path.isfile(area_log_file):
    print("{} doesn't exist".format(area_log_file))
    exit()
else:
    f = open(area_log_file, 'r')

info = f.readlines()
flag=False

for line in info:
    if re.match('Total cell area:\s*(\d+.\d+)',line):
        flag=True
        area = (float)(re.findall('.*Total cell area:\s*(\d+\.\d+)',line)[0])

f.close()

if  flag==False or area==0:
    print("Can't find area in {}".format(area_log_file))
    exit()
else:
    print("DC output area is {}".format(area))


# **********************************************************
#             read aspect ratio
# **********************************************************
x = (int)((re.findall('(\d+)[:x](\d+)',aspect_ratio))[0][0])
y = (int)((re.findall('(\d+)[:x](\d+)',aspect_ratio))[0][1])

# **********************************************************
#             calculate the result
#             x*a * y*a = area / fill
# **********************************************************
a = (area * 100 / 70 / (x*y))**0.5
width = x*a
height = y*a
print("core width is:\t{:.2f}".format(width))
print("core height is:\t{:.2f}".format(height))

out = '''creat_floorplan -control_type width_and_height \
-core_width {:.2f} -core_height {:.2f} \
-start_first_row -bottom_io2core 9 -top_io2core 9 -left_io2core 9 -right_io2core 9
'''.format(width,height)

result = open("{}_icc.fp".format(cellname),'w')
result.write(out)
result.close()