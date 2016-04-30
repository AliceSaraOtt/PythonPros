# -*- coding:utf-8 -*-
import hashlib,MySQLdb
m = hashlib.md5()
try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123', db='python', charset='utf8')
except Exception ,e:
    print '连接出错',e
    exit()
cur = conn.cursor()

def reg():
    while True:
        uname = raw_input('账户名：')
        pwd = raw_input('密码：')
        if uname == '' or pwd == '':
            print '用户名或密码不能为空'
            continue
        sql = 'select name from user where name="%s"' % uname
        row = cur.execute(sql)
        if row == 0:
            m.update(pwd)
            pwd = m.hexdigest()
            sql = 'insert into user(name,pwd) value("%s","%s")' % (uname,pwd)
            row = cur.execute(sql)
            if row:
                print '注册成功'
                conn.commit()
                return 1
            else:
                print '暂时无法注册，请重新注册'
        else:
            print '用户名已经存在'
            continue

def login():
    while True:
        print '请登录'
        uname = raw_input('用户名：')
        pwd = raw_input('密码：')
        m = hashlib.md5()
        m.update(pwd)
        pwd = m.hexdigest()
        if uname == '' or pwd == '':
            print '用户名或密码不能为空'
            continue
        sql = 'select * from user where name="%s"' % (uname)
        cur.execute(sql)
        row = cur.fetchall()
        if len(row) > 0: # 用户存在
            if row[0][3] >= 3:
                print '3次密码错误，账号锁定，请到银行持身份证解锁'
                break
            if row[0][2] == pwd:
                print '登陆成功'
                break
            else:
                c = row[0][3] + 1
                sql = 'update user set c="%d" where name="%s"' % (c,uname)
                cur.execute(sql)
                conn.commit()
                print '密码错误'
                continue
        else:
            print '用户名不存在'
            continue
if __name__ == '__main__':
    if reg():
        login()
    cur.close()
    conn.close()