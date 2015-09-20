#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Pool
from time import sleep

def f(x):
    for i in range(10):
        print '%s---%s' % (i, x)
        sleep(1)


def main():
    pool = Pool(processes=3)
    for i in range(11, 20):
        result = pool.apply(f, (i,))
    pool.close()
    pool.join()
    if result.successful():
        print 'successful'

if __name__ == '__main__':
    main()
