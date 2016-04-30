# -*- coding:utf-8 -*-
#数据库连接类
import MySQLdb as db
class Mydb:
    def __init__(self,host,pwd,user,base): #类的初始化机制
        try:
            self.conn = db.connect(host=host, passwd=pwd, user=user, db=base, charset='utf8')
        except Exception as e:
            self.error(e)
            exit()
        self.cur = self.conn.cursor() # 创建数据库操作指针
    def error(self,e,sql=None): # 报错机制
        if sql:
            print '异常啦：',sql,e
        else:
            print '异常啦：',e
    def zhixing(self,sql): # 数据库的执行机制
        try:
            row = self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.error(sql,e)
        return row
    def select(self,sql):
        self.zhixing(sql)
        return self.cur.fetchall()
    def close(self):
        self.cur.close()
        self.conn.close()
mydb = Mydb('localhost','123','root','python')

if __name__ == '__main__':
    # sql = 'insert into user(name,pwd) value("%s","%s")' % ('凯撒大帝','123')
    #sql = 'delete from user where id>67'
    #sql = 'update user set name="路人甲" where name="路人姨"'
    sql = 'select * from user'
    row = mydb.select(sql)
    for item in row:
        for v in item:
            print v,
        print '\n'
    mydb.close()