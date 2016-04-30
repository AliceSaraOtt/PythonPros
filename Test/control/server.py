# -*- coding:utf-8 -*-
from socket import *

ADDR = ('127.0.0.1',8888)
tcpSocket = socket(AF_INET,SOCK_STREAM)
tcpSocket.bind(ADDR)
tcpSocket.listen(1)

while True:
    print '等待连接'
    cliSocket ,addr = tcpSocket.accept() # 接受一个客户端的连接
    print addr ,'已连接'
    while True:
        data = cliSocket.recv(1024) # 1kb
        if data:
            cliSocket.send('来自星星的' + data)
        else:
            break

