#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
import re

class Spider:

    def __init__(self):
        self.siteUrl = 'http://mm.taobao.com/json/request_top_list.htm'

    def getPage(self, pageIndex):
        url = self.siteUrl + "?page=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        reponse = urllib2.urlopen(request)
        return reponse.read().decode('gbk')

    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        for i in items:
            print i[0], i[1], i[2], i[3], i[4]

spider = Spider()
spider.getContents(1)
