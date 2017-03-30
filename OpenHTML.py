#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp932 -*-

import urllib2


class AccessPage(object):
    """docstring for AccessPage"""
    def __init__(self, url):
        super(AccessPage, self).__init__()
        self.html = self.getHTML(url)

    def getHTML(self, url):
        try:
            # set user
            user_agent = 'Mozilla/5.0'
            # user_agent = 'Chrome/41.0.2228.0'
            req = urllib2.Request(url)
            req.add_header("User-agent", user_agent)
            # access page
            return urllib2.urlopen(req)
        except:
            raise
