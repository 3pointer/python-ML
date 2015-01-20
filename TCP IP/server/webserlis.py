#!/usr/bin/env python
# coding=utf-8

import socket
import time
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.41.37', 9999))
s.listen(5)
print 'Waiting for connection...'

def tcplink(sock, addr):
    print 'Accept net connection from %s:%s...' % addr
    sock.send('Wecome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit'or not data:
            break
        sock.send('Hello, %s' % data)
    sock.close()
    print 'connection from %s:%s Closed' % addr

while True:
    sock, addr = s.accept()
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()

