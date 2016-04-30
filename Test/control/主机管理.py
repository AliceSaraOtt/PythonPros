# -*- coding:utf-8 -*-
import hashlib, MySQLdb, paramiko as miko
m = hashlib.md5()
try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123', db='python', charset='utf8')
except Exception, e:
    print '连接出错', e
    exit()
cur = conn.cursor()

# 注册
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
            sql = 'insert into user(name,pwd) value("%s","%s")' % (uname, pwd)
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
# 登陆
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
        if len(row) > 0:  # 用户存在
            if row[0][3] >= 3:
                print '3次密码错误，账号锁定，请到银行持身份证解锁'
                break
            if row[0][2] == pwd:
                print '登陆成功'
                return True
            else:
                c = row[0][3] + 1
                sql = 'update user set c="%d" where name="%s"' % (c, uname)
                cur.execute(sql)
                conn.commit()
                print '密码错误'
                continue
        else:
            print '用户名不存在'
            continue

# 获取主机
def getHost():
    sql = 'select ip from host'
    cur.execute(sql)
    res = cur.fetchall()
    while True:
        for k, v in enumerate(res):  # 显示主机列表
            print k, '\t', v[0]
        ip_i = raw_input('选择主机')
        if ip_i == 'quit':
            return
        ip_i = int(ip_i)
        ip = res[ip_i][0]
        conHost(ip)

# 连接主机
def conHost(ip):
    ssh = miko.SSHClient()
    ssh.set_missing_host_key_policy(miko.AutoAddPolicy())
    key = miko.RSAKey.from_private_key_file(r'C:\Users\Tina\Desktop\id_rsa')
    try:
        ssh.connect(ip, 22, 'root', pkey=key)
    except Exception, e:
        print '无法连接', e
        return
    while True:
        command = raw_input('>>')
        if command == 'quit':
            return
        stdin, stdout, stderr = ssh.exec_command(command)
        for line in stdout.readlines():
            print line,

# 清空主机
def clear():
    sql = 'delete from host'
    cur.execute(sql)
    conn.commit()

if __name__ == '__main__':
    while True:
        print'''
        1.用户注册
        2.用户登陆
        3.退出系统
        4.清空数据
        '''
        c = raw_input('请选择：')
        if c == '1':
            reg()
        elif c == '2':
            if login():
                getHost()
        elif c == '3':
            break
        elif c == '4':
            clear()
    cur.close()  # 关闭数据库
    conn.close()
