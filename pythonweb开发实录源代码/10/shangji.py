import pymssql
conn=pymssql.connect(host='.\SQLEXPRESS',user='sa',password='sa',database='UserDB')
cur=conn.cursor()
print '��ѡ��������һ��:\n(���) �����ݿ����������\t(ɾ��) ɾ�����ݿ��е�����\t(�޸�)�޸����ݵ�����\n(��ѯ) ��ѯ���ݵ�����'
check=raw_input('ѡ������Ҫ���еĲ���:')
if check=='���':
    print '------------��ӭ��ʹ��������ݵĹ���-------------'
    username=raw_input('�����������û�����')
    userpass=raw_input('�������������룺')
    useraddress=raw_input('���������ĵ�ַ��')
    userphone=raw_input('������������ϵ�绰��')
    sql="INSERT INTO tabUser(userName,userPass,userAddress,userPhone)VALUES(%s,%s,%s,%s)"
    param=(username,userpass,useraddress,userphone)
    n=cur.execute(sql,param)
    conn.commit()
    print '--------��ϲ�㣬��ӳɹ�-------'
    print '----------���֮�������-----'
    cur.execute('select * from tabUser')
    result=cur.fetchall()
    for resultItem in result:
        print resultItem
        
if check=='ɾ��':
    userid=raw_input('����������Ҫɾ���û��ı�ţ�')
    cur.execute('delete from tabUser where id='+userid)
    conn.commit()
    print '------------��ϲ�㣬ɾ���ɹ�------------'
    print '-----------ɾ��֮������ʾ������--------------'
    cur.execute('select * from tabUser')
    result=cur.fetchall()
    for resultItem in result:
        print resultItem
        
if check=='��ѯ':
    userid=raw_input('����������Ҫ��ѯ�û��ı�ţ�')
    cur.execute('select * from tabUser where id='+userid)
    print '------------��ϲ�㣬��ѯ������������ʾ------------'
    result=cur.fetchone()
    print '����ѯ�����ݱ��Ϊ��'+str(result[0])
    print '����ѯ����������Ϊ��'+str(result[1])
    print '����ѯ����������Ϊ��'+str(result[2])
    print '����ѯ�����ݵ�ַΪ��'+str(result[3])
    print '����ѯ�����ݵ绰Ϊ��'+str(result[4])
    
if check=='�޸�':    
    userid=raw_input('����������Ҫ�޸��û��ı�ţ�')
    username=raw_input('���������޸ĵ��û�����')
    userpass=raw_input('���������޸ĵ����룺')
    useraddress=raw_input('���������޸ĵĵ�ַ��')
    userphone=raw_input('���������޸ĵ���ϵ�绰��')
    sql='update tabUser set userName=%s,userPass=%s,userAddress=%s,userPhone=%s where id=%s'
    param=(username,userpass,useraddress,userphone,userid)
    cur.execute(sql,param)
    conn.commit()
    print '-----------����֮���������ʾ-------------'
    cur.execute('select * from tabUser')
    result=cur.fetchall()
    for resultItem in result:
        print resultItem
cur.close()
conn.close()
    
    
        
        
    

        
        
    
