class Animal(object):
    def __init__(self):
        pass
    def Eat(self):
        pass

class Chicken(Animal):
    def __init__(self):
        super(Chicken, self).__init__()
    def Eat(self):
        print '��ֻ���Ѿ�������'

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
    def Eat(self):
        print '�⹷���Ѿ�������'

#ʵ��һ�����õķ���,����Ҳ������ʵ�ְ�
class Person(object):
    def __init__(self,name):
        self.name = name
        print '�ҵ����ֽУ�%s'%self.name
    def Feed(self, ped):
        ped.Eat()


if __name__ == '__main__':
    Kobe = Person('Kobe')#��������ȡ�����ְ�
    pedChicken = Chicken()#����һ��С������
    pedDog = Dog()#����һ��С������
    #Kobe.Feed(pedChicken)#Feed�������ݴ���Ĳ�����ͬ����
    Kobe.Feed(pedDog)
