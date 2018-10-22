#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook


def getBook():
    return blogs 


class blogs(BaseFeedBook):
    title = u'博客合集'
    description = u'一些有用的博客合集'
    language = 'zh-cn'
    feed_encoding = 'utf-8'
    page_encoding = 'utf-8'
    oldest_article = 5
    fulltext_by_readablity = True
    fulltext_by_instapaper = False

    feeds = [
        ('ranyifeng', 'http://feeds.feedburner.com/ruanyifeng/?format=xml'),
        ('lilydjwg', 'https://blog.lilydjwg.me/feed'),
        ('2newcentury', 'http://2newcenturynet.blogspot.com/feeds/posts/default'),
        (u'找一個推理的地方', 'https://linerak.wordpress.com/feed/'),
        ('phoniexlzx', 'https://blog.phoenixlzx.com/atom.xml'),
        ('bambooom', 'http://bambooom.github.io/feed.xml'),
        ('changchen', 'https://changchen.me/atom.xml'),
    ]
