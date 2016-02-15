#coding=utf-8
#函数化编程
import os
def cdWalker(cdrom,cdcfile):
	export = ""
	for root,dirs,files in os.walk(cdrom):
		export+="\n %s;%s;%s" % (root,dirs,files)
	open(cdcfile,'w').write(export)
cdWalker('/exam','cd1.cdc')

