# coding:utf-8
import os
def cdWalker(cdrom,cdcfile):
	export = ""
	for root,dirs,files in os.walk(cdrom):
		export+="\n %s;%s;%s" % (root,dirs,files)
	open(cdcfile,'w').write(export)
if __name__=='__main__':   #调用模块的时候使用
	CDROM='/exam'
	cdWalker(CDROM,'/exam/cdc/cdtools.cdc')

