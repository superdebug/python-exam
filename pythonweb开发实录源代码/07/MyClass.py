mystr=raw_input('����������Ҫ֪���Ķ���')
class MyWorld:
	#������˶���
	def person (self):
		self.mytalk='�ҿ��������������'
		self.mylimbs='Ҳ������֫�����������'
		self.myeyes='�����üĿ������'
		print '�����ˣ�����ҿ���%s,%s,%s'%(self.mytalk,self.mylimbs,self.myeyes)
	#����������
	def pig (self):
		self.mytalk='�ߺߺߺ�'
		self.myspecialty='�Է���˯��'
		self.mymaster='˭���Һã�˭�����ҵ�����' 
		print '�������ҵ��ص����%s,%s,%s'%(self.mytalk,self.myspecialty,self.mymaster)
	#����Ĺ�������
	def rooster (self):
		self.mywork='������������ʱ�����'
		self.mymotto='��ν�ż����裬˵�ľ�����'
		print '���ǹ������ҿ���%s,%s'%(self.mywork,self.mymotto)		
		
if __name__=='__main__':
	myworld=MyWorld()
	if mystr=='��':
		myworld.person()
	elif mystr=='��':
		myworld.pig()
	elif mystr=='����':
		myworld.rooster()
	else:
		print '������˼��������û��¼��ö���'

		

	

	