#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook


def getBook():
    return DZone


class DZone(BaseFeedBook):
    title = 'Dzone'
    description = 'Recent posts on DZone.com'
    language = 'en'
    feed_encoding = "utf-8"
    page_encoding = "utf-8"
    keep_image = True
    fulltext_by_readability = True
    oldest_article = 2

    remove_classes = ["article-bumper"]

    feeds = [
        ('DZone Java Zone', 'http://feeds.dzone.com/java?format=xml'),
        ('DZone Web Dev Zone', 'http://feeds.dzone.com/webdev?format=xml'),
    ]
