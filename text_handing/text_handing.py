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

