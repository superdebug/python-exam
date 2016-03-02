#coding=utf-8


t=frozenset('haha') ##不能进行添加，修改和删除
##成员操作 in not in
print 'a' in t
print 'h' in t
print 'jay' in t


##判断两个集合是否相等，只和元素本身有关，和顺序有关
print set('abc')==set('cba')

##并集，交集，差集
print ("并集，交集，差集")
print set('abc')|set('cbdef') ##并集
print set('abc')&set('cbdef') ##交集
print set('abc')-set('cbdef') ##差集
