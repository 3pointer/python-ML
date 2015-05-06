#!/usr/bin/env python
# coding=utf-8

import time
import sys

def produce(l):
    i = 0
    while 1:
        if i < 5:
            l.append(i)
            yield i
            i += 1
            time.sleep(1)
        else:
            return

def consume(l):
    p = produce(l)
    while 1:
        try:
            p.next()
            print l.pop()
        except StopIteration:
            sys.exit(0)

l = []
consume(l)
