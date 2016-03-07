#coding=utf-8
import re
text = 'c++ python2 python3 perl ruby lua java javascript php4 php5 c'
print "原字符串为:\n"+text
m = re.search(r'java',text)


#查找java
print "查找java"
print "m.start() ="+ str(m.start())
print "m.start() ="+ str(m.end())
print "m.group() ="+ str(m.group())


#查询c++
print "查找c++"
rc=re.search(r'c\+\+',text)
print "m.start() ="+ str(m.start())
print "m.start() ="+ str(m.end())

#查询python
print "查询python"
rp=re.findall(r'python',text)
print rp 


#split方法拆分字符
print "split方法拆分字符";
print re.split(r'perl',text)


#sub方法替换字符串
print "sub方法替换字符串"
print re.sub(r'ruby','fortran',text)


