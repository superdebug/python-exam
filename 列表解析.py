from random import randint

#生成从-10到10之间的随机数，生成10个
data = [randint(-10,10) for _  in range(10)]
print (data)

data2 = list(filter(lambda x: x>=0,data))
print(data2)

