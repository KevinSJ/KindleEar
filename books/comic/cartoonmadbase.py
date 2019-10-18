#!/usr/bin/env python
# -*- coding:utf-8 -*-
#http://www.cartoonmad.com网站的漫画的基类，简单提供几个信息实现一个子类即可推送特定的漫画
#Author: insert0003 <https://github.com/insert0003>
from bs4 import BeautifulSoup
from lib.urlopener import URLOpener
from lib.autodecoder import AutoDecoder
from books.base import BaseComicBook

class CartoonMadBaseBook(BaseComicBook):
    title               = u''
    description         = u''
    language            = ''
    feed_encoding       = ''
    page_encoding       = ''
    mastheadfile        = ''
    coverfile           = ''
    host                = 'https://www.cartoonmad.com'
    feeds               = [] #子类填充此列表[('name', mainurl),...]

    #获取漫画章节列表
    def getChapterList(self, url):
        decoder = AutoDecoder(isfeed=False)
        opener = URLOpener(self.host, timeout=60)
        chapterList = []

        if url.startswith( "http://" ):
            url = url.replace('http://', 'https://')

        result = opener.open(url)
        if result.status_code != 200 or not result.content:
            self.log.warn('fetch comic page failed: %s' % url)
            return chapterList

        content = self.AutoDecodeContent(result.content, decoder, self.feed_encoding, opener.realurl, result.headers)

        soup = BeautifulSoup(content, 'html.parser')
        allComicTable = soup.find_all('table', {'width': '800', 'align': 'center'})

        if (allComicTable is None):
            self.log.warn('allComicTable is not exist.')
            return chapterList

        for comicTable in allComicTable:
            comicVolumes = comicTable.find_all('a', {'target': '_blank'})
            if (comicVolumes is None):
                self.log.warn('comicVolumes is not exist.')
                return chapterList

            for volume in comicVolumes:
                href = self.urljoin(self.host, volume.get('href'))
                chapterList.append(href)

        return chapterList

    #获取漫画图片列表
    def getImgList(self, url):
        decoder = AutoDecoder(isfeed=False)
        opener = URLOpener(self.host, timeout=60)
        imgList = []

        result = opener.open(url)
        if result.status_code != 200 or not result.content:
            self.log.warn('fetch comic page failed: %s' % url)
            return imgList

        content = self.AutoDecodeContent(result.content, decoder, self.page_encoding, opener.realurl, result.headers)
        soup = BeautifulSoup(content, 'html.parser')
        sel = soup.find('select') #页码行，要提取所有的页面
        if (sel is None):
            self.log.warn('soup select is not exist.')
            return imgList

        ulist = sel.find_all('option') if sel else None
        if not ulist:
            self.log.warn('select option is not exist.')
            return imgList

        for ul in ulist:
            if ul.get('value') == None:
                ulist.remove(ul)

        firstPageTag = soup.find('img', {'oncontextmenu': 'return false'})
        firstPage = firstPageTag.get('src') if firstPageTag else None

        if firstPage != None:
            comicId, chapterId, length, imgType = self.getImgStr(firstPage)
            for index in range(len(ulist)):
                if imgType == "&":
                    # http://web3.cartoonmad.com/c529e4khw31/1733/049/001.jpg
                    imgUrl = "http://web3.cartoonmad.com/c529e4khw31/{}/{}/{}.jpg".format(comicId, chapterId, str(index+1).zfill(length))
                else:
                    # https://www.cartoonmad.com/home1/z2r17v3tr15/4295/186/001.jpg
                    imgUrl = "https://www.cartoonmad.com/home1/z2r17v3tr15/{}/{}/{}.jpg".format(comicId, chapterId, str(index+1).zfill(length))
                imgList.append(imgUrl)

        return imgList

    #获取漫画图片网址
    def getImgUrl(self, url):
        decoder = AutoDecoder(isfeed=False)
        opener = URLOpener(self.host, timeout=60)

        url = self.host + "/comic/" + url
        result = opener.open(url)
        if result.status_code != 200 or not result.content:
            self.log.warn('fetch comic page failed: %s' % url)
            return None

        content = self.AutoDecodeContent(result.content, decoder, self.page_encoding, opener.realurl, result.headers)
        soup = BeautifulSoup(content, 'html.parser')
        comicImgTag = soup.find('img', {'oncontextmenu': 'return false'})
        return comicImgTag.get('src') if comicImgTag else None

    #获取漫画图片格式
    def getImgStr(self, url):
        urls = url.split("/")
        comicId = urls[len(urls)-3]
        chapterId = urls[len(urls)-2]
        tail = urls[len(urls)-1]
        if "&" in tail:
            # comicpic.asp?file=/3583/001/001&rimg=1
            imgIndex = tail.split("&")[0]
            imgType = "&"
        else:
            # comicpic.asp?file=/3583/001/001
            imgIndex = tail
            imgType = ""
        return comicId, chapterId, len(imgIndex), imgType
