#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook


def getBook():
    return DZone


class DZone(BaseFeedBook):
    title = 'Dzone_Java'
    description = 'Recent posts in Java on DZone.com'
    language = 'en-us'
    feed_encoding = "utf-8"
    page_encoding = "utf-8"
    max_articles_per_feed = '5'
    language = 'en-us'
    deliver_days = ['Thursday']
    feeds = [('DZone Java Zone', 'http://feeds.dzone.com/java?format=xml'),
             ('DZone Web Dev Zone', 'http://feeds.dzone.com/webdev?format=xml')
             ]
