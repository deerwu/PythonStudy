#encoding:utf-8
import re
a={}
def read(pa):    #读取评论
    with open(pa, 'r') as file:
        comments = file.read()
        return comments
def match(documents):
    with open(documents)as file2:
        for line in file2.readlines():
            test=re.findall(line.strip(),read('/home/oem/Documents/passengers.txt'))
            num = list(test)
            a[line] = num
    with open(m, 'a')as file3:#写入times文件
        for line in a:
            file3.write(str(list(test)))
            file3.write(' ')
            file3.write(line)
            file3.write('\n')
m='/home/oem/Documents/times'

match('/home/oem/Documents/action.txt')#以action文件为例子




