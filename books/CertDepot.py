#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook


def getBook():
    return CertDepot


class CertDepot(BaseFeedBook):
    title = 'CertDepot'
    description = ''
    language = ''
    feed_encoding = 'utf-8'
    page_encoding = 'utf-8'
    oldest_article = 2
    fulltext_by_readablity = True
    fulltext_by_instapaper = False

    feeds = [
        ('CertDepot', 'http://feeds.feedburner.com/Certdepot?format=xml'),
    ]
