gequ=['�������ǰ�','ȫ��ͨ��','�뿪����','�������','�����߲���','ĪʧĪ��']
countStr=raw_input('����������ѭ�����ŵı�����')
count=int(countStr)
qizhong=raw_input('������Ŀǰ�������ĸ�����')
tiaoguo=raw_input('�������������ĸ�����')
i=1
while i<=count:	
	i+=1
	print '---------------ѭ����ʼ--------------'
	for danqu in gequ:
		if danqu==qizhong:
			break
		if danqu==tiaoguo:
			continue
		print '��',i-1,'�β��ŵĸ���',danqu
