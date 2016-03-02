#coding=utf-8

liststr = ['haha','gag','hehe','haha']
#for循环

m = []
#删除重复出现的内容
for i in liststr:
        if i not in m:
         m.append(i)

print m

m = set(liststr)

print list(m)
