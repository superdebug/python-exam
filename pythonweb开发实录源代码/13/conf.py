import xml.dom.minidom
#��xml�ļ���ȡ���ݿ����õ���
class CDBConfig:
  def __init__(self,ConfigFilePath):                #ConfigFilePath�������ļ���·��
    self.__ConfigFilePath=ConfigFilePath
    CDBConfig.DBConnects={}                        #CDBConfig.DBConnects��CDBConfig��ľ�̬�ֵ��Ա������������ݿ���ʴ�    
    self.ConfigXMLFile()                                    #��XML�ļ��ж�ȡ���ݿ�������Ϣ
  #���������������ֵ����������ӵķ���
  def AddConnect(self,key,server="(localhost)",database="master",user="sa",password="",dbtype="SQLServer"):
    if dbtype=="SQLServer" :
      self.__sconn = "server=" + server + ";database=" + database + ";uid=" + user +";pwd=" + password;
      CDBConfig.DBConnects[key]=self.__sconn
      #�����ȡXML�ļ��ķ���
  def ConfigXMLFile(self):
    self.__key = ""
    self.__server = ""
    self.__database = ""
    self.__user = ""
    self.__password = ""
    self.__xmlFile=open(self.__ConfigFilePath,'r')                        #ֻ���������ļ�
    self.__dom=xml.dom.minidom.parse(self.__xmlFile)                #����xml
    self.__xmlFile.close()                                                                    #�ر��ļ�
    self.__connect_elements=self.__dom.getElementsByTagName("DBConnection")       #ȡ�����е�DBConnection��
    for connect_element in self.__connect_elements:                    #ÿ��DBConnection�ڶ���һ�����Ӵ�
        self.__key      = connect_element.getAttribute("Key")
        self.__server   = connect_element.getAttribute("Server")
        self.__database = connect_element.getAttribute("Database")
        self.__user     = connect_element.getAttribute("User")
        self.__password = connect_element.getAttribute("Password")
        self.AddConnect(self.__key,self.__server,self.__database,self.__user,self.__password,dbtype="SQLServer")
        print '---------keyΪ',self.__key,'��DBConnection----------'
        print self.__key
        print self.__server
        print self.__database
        print self.__user
        print self.__password 
if __name__=="__main__":                           
    myconns=CDBConfig("connection.xml")
    for key in CDBConfig.DBConnects.keys():#��ÿһ��keyִ��
      print '-------------��ӡÿ�����ݿ������--------------'
      print key+'\t'                                               #��ÿ�����ݿ����Ӷ���ӡ����


