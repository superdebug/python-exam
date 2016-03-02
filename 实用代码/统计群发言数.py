#coding=utf-8
import re
qqDic={}
qqNameList=[]
myfile=open(u"d://python，安全测试群.txt","r")
Content=myfile.readlines()
myfile.close()

for i in Content: 
    i=i.decode("utf-8").encode("gbk","ignore")
    #print i+"****"
    if i.find("201")==0 and (i.find("(")>0 and i.find(")")>0) or (i.find("<")>0 and i.find("qq.com>")>0) :  
        qqName=i[20:].split("\n")[0]
        
        qqNameList.append(qqName)
        
      
mylist=list(set(qqNameList))  
for i in mylist:
    qqDic[i]=qqNameList.count(i)    
myqqDic=sorted(qqDic.iteritems(),key=lambda d:d[1],reverse=True)

for i in myqqDic:
    print i[0]+":"+str(i[1])
   

