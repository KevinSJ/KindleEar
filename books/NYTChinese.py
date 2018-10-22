#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook


def getBook():
    return NYTChinese


class NYTChinese(BaseFeedBook):
    title = u'纽约时报中文网'
    description = u'纽约时报中文网。'
    language = 'zh-cn'
    feed_encoding = "utf-8"
    page_encoding = "utf-8"
    oldest_article = 2
    keep_image = True
    fulltext_by_readability = True
    fulltext_by_instapaper = False

    feeds = [
        (u'纽约时报中文网', 'https://cn.nytimes.com/rss/'),
    ]
