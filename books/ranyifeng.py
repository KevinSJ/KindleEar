#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook


def getBook():
    return ranyifeng


class ranyifeng(BaseFeedBook):
    title = u'阮一峰的网络日志'
    description = ''
    language = 'zh-cn'
    feed_encoding = 'utf-8'
    page_encoding = 'utf-8'
    oldest_article = 2
    fulltext_by_readablity = True
    fulltext_by_instapaper = False

    feeds = [
        ('ranyifeng', 'http://feeds.feedburner.com/ruanyifeng/?format=xml'),
    ]