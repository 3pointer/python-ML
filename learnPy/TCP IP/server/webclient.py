#!/usr/bin/env python
# coding=utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.41.37', 9999))

print s.recv(1024)
for data in ['MIC', 'TYra', 'DPo']:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
