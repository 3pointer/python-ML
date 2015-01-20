#!/usr/bin/env python
# coding=utf-8

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('192.168.41.37', 9999))

print 'Bind UDP in 9999...'
while True:
    data, addr = s.recvfrom(1024)
    print 'Received from %s:%s.' % addr
    s.sendto('Hello, %s!' % data, addr)
    
