#!/usr/bin/env python
# coding=utf-8


import time, uuid, functools, threading, logging

class Dict(dict):
    def __init__(self, names = (), values = (), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    
    def __setattr__(self, key, value):
        self[key] = value

