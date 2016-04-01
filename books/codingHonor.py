#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook


def getBook():
    return CodingHonor


class CodingHonor(BaseFeedBook):
    title = 'Coding Horror'
    description = 'Programming and human factors'
    language = 'en-us'
    feed_encoding = "utf-8"
    page_encoding = "utf-8"
    max_articles_per_feed = '15'
    language = 'en-us'
    deliver_days = ['Thursday']
    feeds = [('CODING HORROR', 'http://feeds.feedburner.com/codinghorror?format=xml', True),
             ]
