#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

a=[1,2,3,4,5]
print "----------- index and slice ----------"

print a[0]
print a[-1]
print a[0:4]
print a[0:5:2]

print "------------ ref and copy -----------"

a_ref=a

a[2]=100

print "a="+str(a)
print "a_ref="+str(a_ref)

a_copy = a[:] #赋值整个列表
print "a_copy="+str(a_copy)
print "------------ list methods ----------"
a.append(300)
print "After append: a="+str(a)

a.insert(1,50)
print "After insert: a="+str(a)

a.pop() #最后一位被弹出
print "After pop: a="+str(a)

a.sort()
print "After sort: a="+str(a)

a.reverse() #列表反转
print "After reverse: a="+str(a)

del a[0]
print "After del: a="+str(a)

print "------------ ref and copy ------------"
print "a="+str(a)
print "a_ref="+str(a_ref)   #被应用的内容和原来的a的内容完全一直
print "a_copy="+str(a_copy)  #a的副本不会有任何改动


b=[a,a_ref,a_copy] #由于b列表内放的是a和a的引用，所以如果a变动了，a的引用也会变动
c=[1,[1,2,3],'abc']

a+[100,200]
d=a*2

a.count(1)
a.count(5)

#将列表转换成元组给一个新的值
t=tuple(a)
t.count(1)


