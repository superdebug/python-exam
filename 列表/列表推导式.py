#encoding=utf-8
print ("\n生成数字")
print [x for x in range(1,11)]

print ("\n 取出1-100所有值的平方")
print [x*x for x in range(1,100)]


print "\n 生成字符串"
print ['the %s ' % d  for d in range(1,10)]


print ("\n 生成元组") 
print [(x,y) for x in range(2) for y in range(3)]


print("\n 生成字典")
print dict([ (x,y) for x in range(3) for  y in range(2)])
