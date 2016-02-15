#coding=utf-8
#逻辑判断 判断输入的参数
import os,sys

print sys.argv[1]

CDROM= '/exam'

def cdWalker(cdrom,cdcfile):
	export=""
	for root,dirs,files in os.walk(cdrom):
		export+= "\n %s;%s;%s" % (root,dirs,files)
	open(cdcfile,'w').write(export)

if "-e" == sys.argv[1]:
	cdWalker(CDROM,sys.argv[2])
	print "记录光盘信息到 %s" % sys.argv[2]
else:
	print """ pdc 使用方式：
	python pycdc.py -e mycd1-1.cdc 
	#将光盘内容记录为 mycd1-1.cdc
	"""

