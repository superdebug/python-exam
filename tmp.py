from random import randint
import timeit
#data = [randint(-10, 10) for _ in range(10)]
#print (filter(lambda x: x >= 0, data))
print  timeit(x for x in range(10))
