#!/usr/bin/env python
# coding=utf-8

import csv
from numpy import *

def sdata():
    l = []
    cou = 0
    with open('test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            cou += 1
            l.append(line)
            if cou == 101:
                break
    return l

def wsdata(l):
    with open('test2.csv', 'wb') as file:
        lines = csv.writer(file)
        for i in l:
            lines.writerow(i)


def GetnewData():
    l = sdata()
    wsdata(l)

GetnewData()
