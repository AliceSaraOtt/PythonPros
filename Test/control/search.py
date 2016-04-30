# -*- coding:utf-8 -*-
import MySQLdb as db,time,sys
reload(sys)
sys.setdefaultencoding('utf8')
try:
    conn = db.connect(host='127.0.0.1', passwd='123', user='root', db='python', charset='utf8')
    cur = conn.cursor()
except Exception ,e:
    print '连接错误',e
red = ['\033[1;31;m','\033[0m']
while True:
    pattern = raw_input('查询：')
    if pattern == '':
        continue
    sql = 'select ename,age,sex,income from employee where concat(ename,age,sex,income) like "%%%s%%"' % pattern
    cur.execute(sql)
    res = cur.fetchall()
    print '%d条记录' % len(res)
    if len(res):
        for row in res:
            for v in row:
                print str(v).replace(pattern,pattern.join(red)),
            print '\n'
    c = raw_input('是否继续查询 y/n：')
    if c == 'n': # 退出系统
        for i in range(3,0,-1):
            print '%d秒后退出'.join(red) % i
            time.sleep(1)
        break
cur.close()
conn.close()