from random import randint
#对字典的值进行排序

#随机生成一个字典序列，键的内容是xyzabc,取值范围60-100
d={x:randint(60,100) for x in 'xyzabc'}

#方法一、生成元组类型的列表
result=sorted(zip(d.values(),d.keys()))
print(result)

#方法二、 字典内置方法.items()方法会自动生成元组类型字典
#但是键在前，值在后，无法比较，因此在用sorted排序的时候需要用lambda表达式进行调整

print(d.items())
d2 = sorted(d.items(),key=lambda x: x[1],reverse=False)
print(d2)



