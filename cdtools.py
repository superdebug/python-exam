# coding:utf-8
import os
for root,dirs,files in os.walk('/yc/python-exam'):
	open('mycd.cdc','w').write("%s %s %s" %(root,dirs,files))

