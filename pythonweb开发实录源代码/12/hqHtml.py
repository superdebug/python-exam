import httplib
import urllib
rsw=raw_input('����������Ҫ�Ĳ�����ֱ�ӱ�����Դ��Z���������Դ��״̬�루H��')
if rsw=='H':
    print '--------���ǿ��Ի��URL��Դ��״̬�뷽ʽ------------'
    connection=httplib.HTTPConnection('localhost')
    connection.request('GET','/friend.html')
    re=connection.getresponse()    
    print re.status,re.reason
    print re.read()
    connection.close()
elif rsw=='Z':
    print '-------�ҿ���ִ�����صĲ���������Դ�F://dcy/�ļ��鿴Ŷ------'
    url = 'http://localhost/friend.html'
    path='F://dcy/friend.html'
    data = urllib.urlretrieve(url,path)
else:
    print 'ϵͳû��Ϊ��������Դ'
    
