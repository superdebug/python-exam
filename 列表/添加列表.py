#encoding=utf-8

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print ("extend方法")
print a

print ("append方法 添加任意对象到列表末端")
a=[1,2,3]
a.append(4)
print (a)


print ("Insert方法 插入任意对象到列表中，可控制位置")
a=[1,2,3,4]
a.insert(1,'ab')
print (a)

