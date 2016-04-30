# -*- coding:utf-8 -*-
from socket import *

ADDR = ('127.0.0.1',8888)
tcpSocket = socket(AF_INET,SOCK_STREAM)
tcpSocket.connect(ADDR)

while True:
    data = raw_input('>>')
    if data == '':
        break
    tcpSocket.send(data) # 给服务器发送数据
    data = tcpSocket.recv(1024)  # 接受客户端数据
    if data:  # 如果服务器发回数据则输出
        print data
    else:
        break
tcpSocket.close()