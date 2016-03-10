#!/usr/bin/env python
# coding: utf-8
# read file
#将文件内容读取后通过md5加密保存为另外一个文件


f=open('a.txt','r')
name_password = f.readline().strip().split(',')
f.close()

# md5 process
import hashlib
password_md5 = hashlib.md5(name_password[1]).hexdigest()

# write file
f=open('a_md5.txt','w')
f.write(name_password[0]+','+password_md5+'\n')

f.close()
