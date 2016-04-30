# -*- coding:utf-8 -*-
from socket import *

for i in range(1,100):
    try:
        ADDR = (('127.0.0.1',i))
        tcpSocket = socket(AF_INET,SOCK_STREAM)
        tcpSocket.connect(ADDR)
        tcpSocket.close()
        print i,'端口正常'
    except Exception as e:
        print i,'端口异常'