#coding=utf-8
file=open('test.txt')

###方法一
while True:
    line=file.readline()
    if not line: break
    print line.strip()

file.close()

###方法二
for line in open('test.txt'):
        print line.strip()

