import codecs
import re

 
f=codecs.open('beijing_jt.csv','r','utf-8')
read_tmp_total=f.readlines()
f.close()
 
# get linenum and stations information
s_tmp=''.join(read_tmp_total[1:40])   #read_list
#print s_tmp
jt_info=s_tmp.split(',')
for key in  jt_info:
  print key

#站名以尾部的换行回车分开
jt_stations = jt_info[0].split('\r\n \r\n')

 
print jt_info
for keys in jt_info:
 print keys
