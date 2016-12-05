from random import randint ,sample #sample是取样
from functools import reduce
sample('abcdefg',randint(3,6)) #随机取样,抽取范围从3-6

#利用字典解析产生随机数据 随机取样球员3-6个，范围是abcdefg,进球数随机为1-4个
#第一轮数据
s1 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6)) }

#第二轮数据
s2 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6)) }

#第三轮数据
s3= {x:randint(1,4) for x in sample('abcdefg',randint(3,6)) }

print(s1.keys()) #获取字典键的集合
print(s2.keys())

#以集合的方式获取字典的键,在python2使用viewkeys ,python3使用keys
print(s1.keys()&s2.keys()) #在集合中使用与(and)的方式，获取s1和s2的公共键

#使用map reduce方式操作
map(dict.keys,[s1,s2,s3])
print(reduce(lambda a,b : a&b ,map(dict.keys,[s1,s2,s3])))
