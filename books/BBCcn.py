#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook


def getBook():
    return BBCcn


class BBCcn(BaseFeedBook):
    title = u'BBC中文'
    description = u''
    language = 'zh-cn'
    feed_encoding = "utf-8"
    page_encoding = "utf-8"
    oldest_article = 2
    fulltext_by_readability = True
    fulltext_by_instapaper = False

    feeds = [
        (u'新闻主页', 'http://www.bbc.com/zhongwen/simp/index.xml'),
    ]
