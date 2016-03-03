import asyncore,socket

class AsyncGet(asyncore.dispatcher):
    def __init__(self,host):
        asyncore.dispatcher.__init__(self)
        self.host=host
        #����Socket����
        self.create_socket(socket.AF_INET, \
                            socket.SOCK_STREAM)
        self.connect((host,80))                        #���ӷ�����
        self.request='GET /index.html HTTP/1.0\r\n\r\n' #����index.htmlҳ��
        self.outf=None
        print '�����index.html���ԣ�',host

    def handle_connect(self):
        print '���ӣ�',self.host

    def handle_read(self):
        if not self.outf:
            print '���ڴ������ӣ���',self.host
        self.outf=open('%s.txt'%self.host,'wb')   #����������Ϣд����±���
        data=self.recv(8192)                #��ȡ���������͹�������Ϣ
        if data:
            self.outf.write(data)           #д����±���

    def writeable(self):
        return len(self.request)>0

    def handle_write(self):
        num_sent=self.send(self.request)       #���Ϳͻ�������
        
    def handle_close(self):
        asyncore.dispatcher.close(self)
        print 'Socket����ر��ڣ�',self.host
        if self.outf:
            self.outf.close()
if __name__=='__main__':
    AsyncGet('www.python.org')
    asyncore.loop()
