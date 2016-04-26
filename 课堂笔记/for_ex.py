real_age = 29

for i in range(10):
 age=input('age:')
 if age>29:
  print 'think smaller!'
 elif age==real_age:
  print '\033[32;1mGood! 10 RMB\33[0m'
  break
 else:
  print 'think bigger!'
 print 'You still got %s shots!' % (9-i)
