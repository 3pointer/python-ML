#!/usr/bin/env python
# coding=utf-8

import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid == 0:
    print 'I am child (%s), my parent is %s.' %(os.getpid(), os.getppid())
else:
    print 'I am parent Process (%s).' %(os.getpid())

