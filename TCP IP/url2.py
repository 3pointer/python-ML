#!/usr/bin/env python
# coding=utf-8

import urllib2
req = urllib2.Request('http://www.baidu.com')
reponse = urllib2.urlopen(req)
page = reponse.read()
print page
