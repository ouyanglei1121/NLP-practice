#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: ouyang lei time:2019/8/5

from __future__ import division
import nltk, re, pprint
import urllib.request
url = 'http://www.gu tenberg.org/files/2554/2554.txt'
proxies = {'http': 'http://www.someproxy.com:3128'}
raw = urllib.request.urlopen(url, proxies=proxies).read()
print(len(raw))

