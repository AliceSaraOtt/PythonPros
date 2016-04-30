# -*- coding: utf-8 -*-
import paramiko as miko

ssh = miko.SSHClient()
key = miko.RSAKey.from_private_key_file('C:\Users\Tina\Desktop\id_rsa')
ssh.set_missing_host_key_policy(miko.AutoAddPolicy())  # 连接不在kown_hosts 文件中的

try:
    #ssh.connect('192.168.6.129', 22, 'root','123456')
    ssh.connect('192.168.6.129', 22, 'root',pkey=key)
except Exception as e:
    print '暂时无法连接',e

dir = ''
while True:
    command = raw_input('>>')
    if command == 'quit':
        break
    elif command.find('cd') == 0:
        dir = command + ';'
    stdin, stdout, stderr = ssh.exec_command(dir + command)
    for line in stdout.readlines():
        print line,
