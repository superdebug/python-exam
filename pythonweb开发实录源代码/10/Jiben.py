import sqlite3				#����sqlite3ģ��
conn=sqlite3.connect('userDB.db')	#�������ݿ�userDB�����userDB�����ڣ��򴴽����ݿ�userDB
cur=conn.cursor()
print '---------δ����֮ǰ������-----------'
conn.execute("create table if not exists address(id integer primary key autoincrement,name varchar(128),address varchar(128))")		#���address�����ڣ��򴴽���address
conn.execute("insert into address(name,address)values('dcy','zhengzhou')")	#���һ�����ݵ���address
cur.execute("select * from address")
res=cur.fetchall()				#�����α����cur��fetchall()�������ر�address�е���������
print "address:",res				#��������

for line in res:					#��������
	for f in line:
		print f	

conn.execute("delete from address where id=12")
conn.execute("delete from address where id=17")
conn.execute("delete from address where id=30")
conn.execute("delete from address where id=30")
strUpdate=raw_input('��ѡ����Ҫ�޸�ĳ�����ݵı�ţ�')
strId=raw_input('��ѡ����Ҫɾ��ĳ�����ݵı�ţ�')

conn.execute("update address set name='maxianglin' where id="+strUpdate)

conn.execute("delete from address where id="+strId)
conn.commit()					#�ֶ��ύ
print '-------------����֮�������----------------'
cur.execute("select * from address")	#�����α����cur��execute������ѯ��address�е�����
res=cur.fetchall()				#�����α����cur��fetchall()�������ر�address�е���������
print "address:",res				#��������

for line in res:					#��������
	for f in line:
		print f	
cur.close()						#�ر��α����cur
conn.close()						#�ر����ݿ����Ӷ���conn
