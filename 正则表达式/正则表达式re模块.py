#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import re
text = 'c++ python2 python3 perl ruby lua java javascript php4 php5 c'

#match,search,findall,split,sub
re.match(r'c++',text)
re.match(r'c\+\+',text)
re.match(r'java',text)
re.search(r'java',text)

m = re.search(r'java',text)

#print "m.start()="+m.start()


print re.findall(r'python',text)
print re.split(r' perl ',text)
print re.sub(r'ruby','fortran',text)


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


# +   1-inf
# *   0-inf
# ?   0-1, 
# []  or
# {}  repeat
# [^] not
print re.findall(r'p+',text)
#结果 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']

print re.findall(r'p[a-zA-Z]+',text)  #{1,}
#结果 ['python', 'python', 'perl', 'pt', 'php', 'php']

print re.findall(r'c[a-zA-Z]*',text)  #{,inf}
#c后面跟着字母，字母数量为0到正无穷个 显示结果['c', 'cript', 'c']

print re.findall(r'c[^a-zA-Z]*',text)  #{,inf}
#^在大括号内代表"非" c后面跟着非字母的符号 结果['c++ ', 'c', 'c']

print re.findall(r'c[a-zA-Z]?',text)  #{,1}
#结果['c', 'cr', 'c']


print re.findall(r'p[a-zA-Z0-9]{3,}',text)  #{,1}
#p后面至少跟3个字母以上

# |   or
print re.findall(r'[pj][a-zA-Z]+',text)  #{,inf}
#以p或者j后面跟字符的都可以匹配 ['python', 'python', 'perl', 'java', 'javascript', 'php', 'php']

print re.findall(r'p[^0-9]+|j[a-zA-Z]+',text)   
#p或j后面跟字符的

print re.findall(r'p[^0-9 ]+|j[a-zA-Z]+',text) 
#p后面跟着非数字 或 j后面跟着字母 注意^0-9后面的空格表示不包含空格

# ^   start
# $   end
# .   except \n
#以c开头后面跟2个字符的 结果为c++
print re.findall(r'^c..',text) 
#c+表示c后面匹配相同字符 cc或者ccc 
print re.findall(r'c+',text)
#c+后面跟正无穷 
print re.findall(r'c\++',text)
#结束符是c的
print re.findall(r'c$',text)

# \w  [a-zA-Z0-9_], \W 大写代表小写的非
# \d  [0-9], \D  大写代表小写的非
# \s  [ \t\n\r\f\v], \S 大写代表小写的非
print re.findall(r'p\w+',text)
print re.findall(r'p\w+\d',text)
print re.findall(r'p\w+[0-9]',text)
print re.findall(r'p\w{5,9}',text)

# \b  word boundary 一个单词的边界 
# \B  not \b
# \A  input start, ^
# \Z  input end, $
print re.findall(r'\bp[^0-9]',text) #放在单词的开头 ['py', 'py', 'pe', 'ph', 'ph']
print re.findall(r'p[^0-9]\b',text) #放在单词的结尾 ['pt']

# *?  0~inf non-greedy 非贪婪模式 尽可能匹配少
# +?  1~inf non-greedy 贪婪模式
print re.findall(r'p[^0-9]*',text) #贪婪模式
print re.findall(r'p[^0-9]*?',text) #非贪婪模式，尽可能匹配少
print re.findall(r'p[^0-9]+\b',text) #匹配单词边界 ['perl ruby lua java javascript ']
print re.findall(r'p[^0-9]+?\b',text) #匹配边界 ['perl', 'pt']

# ()  group 分组
# (?P<name>pattern)
a=re.search(r'(p[a-zA-Z]+)([0-9])','python2')
print a.group(1), a.group(2)

a=re.search(r'(?P<name>p[a-zA-Z]+)(?P<version>[0-9])','python2')
print a.group('name'), a.group('version')
print a.groupdict()

pattern = re.compile(r'(?P<name>p[a-zA-Z]+)(?P<version>[0-9])')
results = pattern.search('python2')
print results.groupdict()
results = pattern.search('python3')
print results.groupdict()
results = pattern.search('php4')
print results.groupdict()

#########################################
for t in text.split(' '):
    results = pattern.search(t)
    if results:
      print results.groupdict()

