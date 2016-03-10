# coding: utf-8
import random
charactor='abcdefghijklmnopqrstuvwxyz0123456789'

len_char = len(charactor)-1
# generate name
a=[0]*4
#print '[0]*4='+str([0]*4)
#print a[1]
a[0]=charactor[random.randint(0,len_char)]
a[1]=charactor[random.randint(0,len_char)]
a[2]=charactor[random.randint(0,len_char)]
a[3]=charactor[random.randint(0,len_char)]

name=''.join(a)

# generate password
a=[0]*6
a[0]=charactor[random.randint(0,len_char)]
a[1]=charactor[random.randint(0,len_char)]
a[2]=charactor[random.randint(0,len_char)]
a[3]=charactor[random.randint(0,len_char)]
a[4]=charactor[random.randint(0,len_char)]
a[5]=charactor[random.randint(0,len_char)]

password=''.join(a)

#write file
f=open('a.txt','w')
f.write(name+','+password+'\n')
f.close()

