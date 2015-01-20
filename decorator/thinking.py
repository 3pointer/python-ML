#!/usr/bin/env python
# coding=utf-8

import functools

def log(text):
    if isinstance(text, str):
        def decorater(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'begin call %s():' % func.__name__
                func(*args, **kw)
                print 'end call %s():' % func.__name__
            return wrapper
        return decorater
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print 'begin call %s():' % text.__name__
            text(*args, **kw)
            print 'end call %s():' % text.__name__
        return wrapper
@log
def f():
    print '呵呵呵'

@log('execute')
def fun():
    print 'ssdsadsad'


if __name__ == '__main__':
    f()
    print '______________________-'
    fun()

