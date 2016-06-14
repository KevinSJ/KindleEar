#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseFeedBook


def getBook():
    return CodingHorror


class CodingHorror(BaseFeedBook):
    title = 'Coding Horror'
    description = 'Programming and human factors'
    language = 'en'
    feed_encoding = "utf-8"
    page_encoding = "utf-8"
    oldest_article = 2
    keep_image = True
    fulltext_by_readability = False

    feeds = [
        ('Coding Horror', 'http://feeds.feedburner.com/codinghorror?format=xml', True),
    ]
