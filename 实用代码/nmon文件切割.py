#coding=utf8
#./nmon -fT -s 2 -c 7200
####7200/4= 1800   ,将文件切割成4份，一份1800次
in_file=open('11111.nmon')#填写需要切割的nmon文件
aa=in_file.read().replace('ZZZZ,','ASDFGHZZZZ,')#读取文件为切割做准备
pat='ASDFGH'#需要切割的格式
a=aa.split(pat)#a为切割后的list
nu=len(a)  #判断切割份数 
x=0     
for i in range(1,5):#由于切割成4份，排除第零段的每个文件需要的头文件，\
    #如果需要切割成8份就是range(1,9)
    s=[]
    s.append(a[0])  
    for j in a[x*1800+1:i*1800]:# 将list以1800份为一段切割
        s.append(j)
    x+=1
    f=open('split_%s.nmon'%i,'w')#切割后生成文件
    for i in s:
        f.write(i)      
f.close()


