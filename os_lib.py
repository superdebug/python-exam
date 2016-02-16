#coding=utf-8

import os



#获取当前路径
print "当前路径是\n"
print os.getcwd()

print "\n当前路径下的文件\n"
print os.listdir(os.getcwd())

for x in 'spam':
    print (x)

