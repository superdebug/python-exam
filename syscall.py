import os
export = []
for root,dirs,files in os.walk('/python-exam'):
	export.append("\n %s;%s;%s" % (root,dirs,files))
	print root,dirs,files
	open('mycd.cdc','w').write(''.join(export))
