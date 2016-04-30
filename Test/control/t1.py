# -*- coding:utf-8 -*-
from time import sleep,ctime

def fun1():
    sleep(5)
def fun2():
    sleep(3)

if '__main__' == __name__:
    print ctime()
    fun1()
    fun2()
    print ctime()
