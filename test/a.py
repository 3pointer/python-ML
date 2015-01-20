#!/usr/bin/env python
# coding=utf-8

f = open('/home/cxsys/lc/python/test/1.txt', 'w')

for i in range(100):
    f.writelines(str(i)+'\n');
