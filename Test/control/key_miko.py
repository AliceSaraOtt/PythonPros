# -*- coding: utf-8 -*-
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pkey_file = r'C:\Users\Tina\Desktop\id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)
ssh.connect('192.168.6.8', 22, 'root', pkey=key)
while True:
    command = raw_input('>>')
    if command == 'quit':
        break
    stdin, stdout, stderr = ssh.exec_command(command)
    for line in stdout.readlines():
        print line,
ssh.close()
