from SocketServer import TCPServer , ThreadingMixIn , StreamRequestHandler
class Server(ThreadingMixIn , TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handle (self):
        addr=self.request.getpeername()
        print '��ȡ���������ԣ�',addr
        self.wfile.write('ʹ��Thead��ʽʵ�ֶ�����')
if __name__=='__main__':    
    server=Server(('localhost',1234),Handler)
    server.serve_forever()

