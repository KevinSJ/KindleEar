#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook


def getBook():
    return xkcd


class xkcd(BaseFeedBook):
    title = 'xkcd'
    description = 'A webcomic of romance,sarcasm, math, and language.'
    language = 'en'
    feed_encoding = 'utf-8'
    page_encoding = 'utf-8'
    oldest_article = 2
    fulltext_by_readablity = True
    fulltext_by_instapaper = False

    feeds = [
        ('xkcd', 'http://xkcd.com/rss.xml'),
    ]
