# -*- coding:utf-8 -*-
import hashlib, MySQLdb, paramiko as miko,threading
m = hashlib.md5()
try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123', db='python', charset='utf8')
except Exception, e:
    print '连接出错', e
    exit()
cur = conn.cursor()

def insert(name,pwd):
    sql = 'insert into user(name,pwd) values("%s","%s")' % (name,pwd)
    cur.execute(sql)

threads = []
for i in range(10):
    t = threading.Thread(target=insert ,args=(str(i),str(i)))
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

conn.commit()