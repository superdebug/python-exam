#coding = utf-8
import os
export = ""
for root,dirs,files in os.walk('/python-exam'):
	export+="\n %s; %s; %s" % (root,dirs,files)
open('mycd.cdc','w').write(export)

