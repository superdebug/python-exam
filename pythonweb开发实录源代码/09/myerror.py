import myindexerror
import myvalueerror
userList=['maxianglin','wanglili','malingling','fanxiaoxuan']
user_str=''
user_name=''
input_selectIndex=0
user_name=0
try:
    input_selectIndex=int(raw_input('������Ҫ��ѯ���û�����ţ�'))
    user_str=userList[input_selectIndex]
    input_selectName=raw_input('������Ҫ��ѯ���û�����')
    user_name=userList.index(input_selectName)
except IndexError,e:
    print '���ֵĴ�����Ϣ���Ϊ��',myindexerror.MyIndexError('1').value
except ValueError,e:
    print '���ֵĴ�����Ϣ���Ϊ��',myvalueerror.MyValueError('2').value
else:
    print '������ı��Ϊ'+str(input_selectIndex)+'���û�Ϊ��'+user_str
    print '��������û���'+input_selectName+'���б��ж�Ӧ������Ϊ��'+str(user_name)



