#codint=utf-8
import os
export = []
for root,dirs,files in os.walk('/exam'):
	export.append("\n %s;%s;%s" % (root,dirs,files))
open('mycd2.cdc','w').write(''.join(export))
