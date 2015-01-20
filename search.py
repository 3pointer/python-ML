#!/usr/bin/env python
# coding=utf-8

import os
def search(dis, string):
    for x in os.listdir(dis):
        if os.path.isdir(os.path.join(dis, x)):
            search(os.path.join(dis,x),string)
        elif x.find(string) >= 0: #不用os.path.join, 为什么不行？
            print x, ':', os.path.join(dis, x)

search('/home/cxsys/lc/python/', '.py')
