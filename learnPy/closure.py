#!/usr/bin/env python
# coding=utf-8

def addspam(fn):
    def new(*args):
        for value in args:
            print value
        return fn(*args)
    return new

@addspam
def useful(a, b):
    print a ** 2 + b ** 2

if __name__ == "__main__":
    useful(2, 3)
