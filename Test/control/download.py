# -*- coding:utf-8 -*-
import paramiko as miko
import tkFileDialog
#dir = tkFileDialog.askopenfilename() # 获取文件的绝对路径
# 设置路径
dir = tkFileDialog.askdirectory()

'''
t = miko.Transport(('192.168.6.6',22)) # 建立socket
key = miko.RSAKey.from_private_key_file(r'C:\Users\Tina\Desktop\id_rsa')
t.connect(username='root',pkey=key) # 和服务器建立连接
ftp = miko.SFTPClient.from_transport(t) # 创建ftp对象

local = r'C:\Users\Tina\Desktop\known_hosts'
remote = r'/root/.ssh/known_hosts'
try:
    ftp.get(remote,local)
except Exception ,e:
    print '下载失败',e
    exit()
finally:
    t.close()
'''