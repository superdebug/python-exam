import pymysql
'''
CREATE TABLE `tb1` (
url varchar(80)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into tb1 value ('孙悟空');
insert into tb1 value ('猪八戒');
insert into tb1 value ('abc');
'''



#打开数据库连接
conn = pymysql.connect(host='127.0.0.1',port=3306,
        user='root',passwd='123456',db='test1',charset='utf8')
#使用cursor()方法获取操作游标
cur = conn.cursor()

#使用SQL查询语句
cur.execute("use test1")
cur.execute("select * from tb1")

#print(cur.fetchone())
print(cur.fetchall())

