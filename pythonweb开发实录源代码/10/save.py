import shelve
class Person:
    m = {}
    def __init__(self,title,content): 
        self.title = title 
        self.content = content 
    def say(self): 
        print '������ı�����:%s \t�������������:%s' % (self.content,self.content) 
temppath = 'MyGood' 
def init(): 
    m = {} 
    f = shelve.open(temppath,'w') 
    f["init"] = "--------------��ӭ��ʹ�����ܼ��±�---------------"
    f.close()     
init() 
print '��ѡ��������һ��:\n(add) ������ñ��������\t(del) ɾ�����õ�����\t(quit)�رռ��±�\n(show) չʾ���ñ��������'
while (True):    
    check=raw_input('ѡ������һ���Ĳ���:')
    if check == 'quit': 
        break 
    if check == 'add':
        print '-----------��ӭ��ʹ��������ӵĹ���------------'
        titleSave=raw_input('�������������ñ���ı���:')
        contentSave=raw_input('��������Ҫ���ñ��������:')
        f = shelve.open(temppath,'w') 
        f["title"] = titleSave
        f["content"] = contentSave        
        print '����ӵı����ǣ�'+f["title"],'����ӵ������ǣ�'+f["content"]        
    if check == 'del':
        print '-----------��ӭ��ʹ������ɾ���Ĺ���------------'
        titleDel=raw_input('����������ɾ������ļ�ֵ:')
        f = shelve.open(temppath,'w')
        if f.has_key(titleDel):
            del f[titleDel]   
        print 'ɾ���ɹ���'    
    if check == 'say':
        titleSave=raw_input('�������������ñ���ı���:')
        contentSave=raw_input('��������Ҫ���ñ��������:')                            
        Person(raw_input(titleSave,contentSave))
        Person(raw_input(titleSave,contentSave)).say() 
        print "��ϸ�����������û�б���Ŷ"         
    if check == 'show': 
        f = shelve.open(temppath,'w')        
        print '------------------�����������ñ��������------------------' 
        for key,value in f.iteritems(): 
            print key,value
        print '------------------ over ------------------' 
        f.close()

