# -*- coding:utf-8 -*-
from db import *
while True:
    print '''
        1.查
        2.增
        3.删
        4.退
        '''
    c = int(raw_input('请选择：'))
    if c == 1:
        sql = 'select server,ip from host'
        res = mydb.select(sql)
        for item in res:
            for v in item:
                print v,
            print '\n'
    elif c == 2:
        hname = raw_input('主机名：')
        ip = raw_input('IP：')
        sql = 'insert into host(server,ip) value("%s","%s")' % (hname,ip)
        row = mydb.zhixing(sql)
        if row == 1:
            print '增加成功'
            continue
    elif c == 3:
        hname = raw_input('主机名：')
        sql = 'delete from host where ip="%s"' % hname
        row = mydb.zhixing(sql)
        if row > 0:
            print '删除成功'
            continue
    elif c == 4:
        break
