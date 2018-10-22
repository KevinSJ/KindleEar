#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Wallstreetcn

class Wallstreetcn(BaseFeedBook):
    title                 = u'华尔街见闻'
    description           = u''
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 2
    fulltext_by_readability = True
    fulltext_by_instapaper = False

    feeds = [
            (u'华尔街见闻', 'https://dedicated.wallstreetcn.com/rss.xml'),
            ]
