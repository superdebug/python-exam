#!/usr/bin/env python
#_*_ coding=utf-8 _*_

name = raw_input('Please input your name:')
age = int(raw_input('age:'))
job = raw_input('job:')
salary = raw_input('Salary:')
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

print '''
Personal information of %s:
	  Name: %s
	  Age : %d
	  Job : %s
	Salary: %s
----------------------------
''' % (name,name,age,job,salary)





print '你好'
