def fruitFun (fruitList):
    checked = ['�㽶','����','����'] 
    for e in fruitList: 
        if e not in checked: 
            checked.append(e)
    print '-------------��ӭʹ��ˮ����Ϣ����ϵͳ--------------'
    print '����ˮ����'
    checked.sort(reverse=True)
    for item in checked :
        print item
    return checked
fruits = ['ƻ��','�㽶','����','����','����','ƻ��','�㽶','����']
addFruit = raw_input('��������Ҫ��ӵ�ˮ����')
fruits.append(addFruit)
fruitList = fruitFun(fruits)
selectFruit= raw_input('������Ҫ���ҵ�ˮ�����ƣ�')
print '��Ҫ���ҵ�ˮ������Ϊ��'+selectFruit+'����ˮ�����б��е�λ��Ϊ��'+str(fruitList.index(selectFruit)+1)+'��'


