def abstract():
    raise NotImplementedError("�Բ��𣬲�����ʵ��������")
class MyClothStore:
	#���÷�װ������Ƴ�ʼ��
	def __init__(self):  
		self.fname = 'SIMILE'
		print self.fname	
		if self.__class__ is MyClothStore:
			abstract()	
class MyGrilCloth(MyClothStore):
	def __init__ (self):		
		self.clothname='������˽��'
		print self.fname
class MyBoyCloth(MyClothStore):
	def __init__ (self):
		self.clothname='̫��˼����'
		print self.clothname
class BoyCloth(MyClothStore,MyBoyCloth):
	def __init__ (self,AdultName,AdultMake,AdultPrice,AdultWash):
		print '�����װ����ȫ�����ܵ������ǣ�'
		MyClothStore.__init__(self)		
		print '�����װ�������ǣ�'
		MyBoyCloth.__init__(self)	
		self.AdultName=AdultName
		print '����·���������:%s'%self.AdultName
		self.AdultMake=AdultMake
		print '����·���������:%s'%self.AdultMake
		self.AdultPrice=AdultPrice
		print '����·��ļ۸���:%s'%self.AdultPrice
		self.AdultWash=AdultWash
		print '����·�ֻ�ܱ���:%s'%self.AdultWash		
class AdultCloth(MyClothStore,MyGrilCloth):
	def __init__ (self,AdultName,AdultMake,AdultPrice,AdultWash):
		print '��Ůʿ��װ��ȫ�����ܵ������ǣ�'
		MyClothStore.__init__(self)		
		print '��Ůʿ��װ�������ǣ�'
		MyGrilCloth.__init__(self)	
		self.AdultName=AdultName
		print '����·���������:%s'%self.AdultName
		self.AdultMake=AdultMake
		print '����·���������:%s'%self.AdultMake
		self.AdultPrice=AdultPrice
		print '����·��ļ۸���:%s'%self.AdultPrice
		self.AdultWash=AdultWash
		print '����·�ֻ�ܱ���:%s'%self.AdultWash
if __name__=='__main__':
	 adultcloth=AdultCloth('dcy','guochan','1500RMB','��ϴ')
	 adultcloth=BoyCloth('taikesi','guochan','2500RMB','��ϴ')
