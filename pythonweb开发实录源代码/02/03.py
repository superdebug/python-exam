class Myclass:   #�����е�ÿ�����ʵ�����ĸ��д������Сд
    __username=''   #˽������ǰ����ʹ�������»���Ϊǰ׺
    def __init__ (self,username):
        self.__username=username   #self�൱��Java�����е�this�ؼ��֣���ʾ����
    def getUserName (self):      #������������ĸСд�����ÿ�����ʵ�����ĸҪ��д
        return self.__username
if __name__ == "__main__":
    myclass = MyClass('admin')      #��������Сд��ĸ
    print myclass.getUserName()