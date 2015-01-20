#!/usr/bin/env python
# coding=utf-8

f = open('/home/cxsys/lc/python/test/1.txt', 'r')
for line in f.readlines():
    print (line.strip())

