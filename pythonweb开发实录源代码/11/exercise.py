import sys,os  
import urllib  
def downloadPydev(a,b,c):  
    """  
        call back function  
        a,�����ص����ݿ�  
        b,���ݿ�Ĵ�С  
        c,Զ���ļ��Ĵ�С  
    """ 
    print "�������أ������ĵȴ�����" 
    prec=100.0*a*b/c  
    if 100 < prec:  
        prec=100 
        print "%.2f%%"%(prec,)    
def main(argv):  
    """  
        main  
    """ 
    print "��ʼ���ء���" 
    urllib.urlretrieve("http://cdnetworks-kr-1.dl.sourceforge.net/project/pydev/pydev/Pydev%201.6.5/Pydev%201.6.5.zip"\

                       ,"tmp/python.pydev.zip"\

                       ,downloadPydev)  
    print "������ɡ���"         
if __name__=="__main__":  
    main(sys.argv[1:]) 

