#!/usr/bin/env python
# coding=utf-8

import random

def qsort(l, left, right):
    if (left > right):
        return
    low = left
    high = right
    x = l[left]
    while(low < high):
        while(low < high and x < l[high]):
            high -= 1
        if low < high:
            l[low] = l[high]
            low += 1
        while(low < high and x > l[low]):
            low += 1
        if low < high:
            l[high] = l[low]
            high -= 1

    l[low] = x
    qsort(l, left, low - 1)
    qsort(l, low + 1, right)

def qsort2(l, left, right):
    if (left > right):
        return
    low = left
    high = right
    x = l[left]
    while(low < high):
        while(low < high and x <= l[high]):
            high -= 1
        l[low] = l[high]
        while(low < high and x >= l[low]):
            low += 1
        l[high] = l[low]

    l[low] = x
    qsort(l, left, low - 1)
    qsort(l, low + 1, right)

if __name__ == '__main__':
    x = []
    for i in range(20):
        x.append(random.randint(1, 1000))

    print x
    qsort2(x, 0, len(x) - 1)
    print x

