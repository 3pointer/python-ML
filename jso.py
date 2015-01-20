#!/usr/bin/env python
# coding=utf-8

import json
d = dict(name='Bob', age=20, score=80)
json_str = json.dumps(d)


if __name__ == '__main__':
    print json_str
