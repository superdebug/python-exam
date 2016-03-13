#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke
#支持中文及utf8
import codecs
import re
#读取cvs文件数据，含中文数据，然后存入字典
# read the file

# f=codecs.open('beijing_jt.csv','r','utf-8')
# read_list=[]
# read_tmp=f.readline()

# for i in range(0,39):
#    read_tmp=f.readline()
#    read_list.append(read_tmp)
    
# f.close()
#打开中文编码的文件
f=codecs.open('beijing_jt.csv','r','utf-8')
read_tmp_total=f.readlines()
f.close()

# get linenum and stations informationi
#读取第2-39行
s_tmp=''.join(read_tmp_total[1:40])   #read_list
print s_tmp
jt_info=s_tmp.split(',')

jt_stations = jt_info[-1].split('\r\n \r\n')


print jt_info[1]
# convert stations info format
station_pattern = (r'(?P<number>[0-9]+)\s(?P<name>\D+)')

station_list = []
stations = re.findall(station_pattern,jt_info[-1]) 
for tmp in stations:
    print tmp[0],tmp[1].strip()
    station_list.append(tmp[1].strip())
    
print "-------------------------------------------------"

for tmp in jt_stations:
    stations = re.search(station_pattern,tmp.strip())
    print stations.group('number'),stations.group('name')

result={}
result[jt_info[1]]=station_list

print result


