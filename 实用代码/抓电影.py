#coding:utf-8
#used PYTHON 2.5
#the program can get the www.dytt8.net's movie of newest 170s
#before using you have to let the program in Python27 fold,and bulid a new fold which named "dytt" in Python 27
#made by Zhaoshuo,qq:2090737490
import urllib
urls = ['']*170
con = urllib.urlopen("http://www.dytt8.net").read()
#print con
title = con.find(r'<!--{start:')
#print title
end = con.find(r'<!--}end:')

href = con.find(r'<a href',title)
#print href
html = con.find(r'.html',href)
#print html
url = 'http://www.dytt8.net/'+con[href+9:html+5]
#print url
time = 0


while href < end and html!= -1 and href != -1 and time <=170:
    
    urls[time] = url
    #print urls[time]
    href = con.find(r'<a href',html)
    #print href
    html = con.find(r'.html',href)
    #print html
    url = 'http://www.dytt8.net/'+con[href+9:html+5]
    #print url
    time += 1
    #print time,'finished'
time = 0
while time <= 170:
    contect = urllib.urlopen(urls[time]).read()
    title = contect.find(r'<tbody>')
    href = contect.find(r'href=',title)
    end = contect.find(r'">',href)
    #print title
    #print href
    #print end
    ftp = contect[href+6:end]
    #print ftp
    name_first = ftp.find(r'com].')
    name_last = ftp.find(r'.',name_first+5)
    name = ftp[name_first+5:name_last]
    #print name_first
    #print name_last
    print 'downloading:',name
    open(r'dytt/'+name+'.txt','w+').write(ftp)
    time +=1
else:
    print 'finished downloaded for:',time

