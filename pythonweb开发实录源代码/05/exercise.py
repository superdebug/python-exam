people={
    'maxianglin':{
        'phone':'13587845896',
        'addr':'�����к�����'
    },
    'wanglili':{
        'phone':'13658475896',
        'addr':'����ʡ������'
    },
    'malingling':{
        'phone':'15784785842',
        'addr':'����ʡ֣����'
    }
}
labels={
    'phone':'�绰����',
    'addr':'��ͥסַ'
}
name=raw_input('�������û���:')
request=raw_input('Ҫ��ѯ���û�����ϵ�绰���Ǽ�ͥ��ַ����p����ϵ�绰  a����ͥסַ��')
if request == 'p':
    key='phone'
if request == 'a':
    key='addr'
if name in people:
    print '��Ҫ���ҵ�%s��%s��%s��'% (name,labels[key],people[name][key])
else:
    print '��������û����������������룡'
 

