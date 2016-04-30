# -*- coding: utf-8 -*-
import paramiko

t = paramiko.Transport(('192.168.6.129', 22))
t.connect(username='root', password='123456')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r'/root/.ssh/authorized_keys'
localpath = r'C:\Users\Tina\Desktop\authorized_keys'
sftp.put(localpath, remotepath)
t.close()



# rsa 无密码
'''
key = paramiko.RSAKey.from_private_key_file(r'C:\Users\Tina\Desktop\id_rsa')
t = paramiko.Transport(('192.168.6.8', 22))
t.connect(username='root', pkey=key)
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r'/root/.ssh/miko.py'
localpath = r'C:\Users\Tina\Desktop\miko.py'
sftp.put(localpath, remotepath)
t.close()
'''