import socket , select
s=socket.socket()
host=socket.gethostname()
port=1234
s.bind((host,port))
fdmap={s.fileno():s}
s.listen(5)
p=select.poll()       #����Polling����
p.register(s)         #ע��Socket����
while True:
    events=p.poll()   #��ȡ׼���õ��ļ�����
    for fd,event in events :
        if fd is fdmap:
            c,addr=s.accept()
            print '��ȡ�������ԣ�',addr
            p.register(c)
            fdmap[c.fileno()]=c      #��������Socket
        elif event & select.POLLIN:
            data=fdmap[fd].recv(1024)
            if not data:          #û������
                print fdmap[fd].getpeername(),'disconnected'
                p.unregister(fd)
                del fdmap[fd]
        else:
            print data
           
