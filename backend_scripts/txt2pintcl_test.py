import re

inhibitlayer=['M6','M10']
side_index = {'left':1, 'top':2, 'right':3, 'bottom':4}
#Sample: OUT[11:0] M4  bottom
pattern1 = r'(\w+)\s*\[(\d+):(\d+)\]\s+(\w+)\s+(\w+)'
#Sample: LD M4 bottom
pattern2 = r'(\w+)\s+(\w+)\s+(\w+)'


order=1
def print_pin(pin, layer, side):
    global order
    if re.match('^\d+$',layer):
        print("Format Error!\nPlease use METAL[1-5]\n")
        exit()

    if layer in inhibitlayer:
        print("Please do not use {} for pin.This will cause DRC error.".format(layer))
        exit()

    if re.match('^\S*$',pin):
        set_pin_tcl = "set_pin_physical_constraints -pin_name {} -layers {} -width 0.28 -depth 0.28 -side {} -order {}\n".format(pin, layer, side_index[side], order)
        order = order + 1
    return set_pin_tcl



f = open('ACCUM.pin','r')
ofile = open('ACCUM_pin.tcl','w')

pin = f.readlines()

for line in pin:
    if re.match(pattern1,line):
        result = re.match(pattern1,line)
        name    = result.group(1)
        msb     = (int)(result.group(2))
        lsb     = (int)(result.group(3))
        layer   = (result.group(4))
        side    = (result.group(5))

        print("######### {:<10} {:<10} {:<10} {:<10} {:<10}  ###########".format('name','msb','lsb','layer','side'))
        print("######### {:<10} {:<10} {:<10} {:<10} {:<10}  ###########".format(name,msb,lsb,layer,side))

        if msb > lsb:
            for i in range(lsb,msb+1):
                result = print_pin("{}[{}]".format(name,i),layer,side)
                ofile.write(result)
                print(result)
        else:
            for i in range(msb,lsb+1):
                result = print_pin("{}[{}]".format(name,i),layer,side)
                print(result)
                ofile.write(result)

    elif re.match(pattern2,line):
        result  = re.match(pattern2,line)
        name    = result.group(1)
        layer   = result.group(2)
        side    = result.group(3)

        print("######### {:<10} {:<10} {:<10} ###########".format('name','layer','side'))
        print("######### {:<10} {:<10} {:<10} ###########".format(name,layer,side))
        result = print_pin(name,layer,side)
        ofile.write(result)
        print(result)


 