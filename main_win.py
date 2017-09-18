#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import hashlib
import webbrowser
import pandas as pd
import urllib3
import requests
from bs4 import BeautifulSoup


class AccessPage(object):
    """docstring for AccessPage"""
    def __init__(self, url):
        super(AccessPage, self).__init__()
        self.html = self.getHTML(url)

    def getHTML(self, url):
        try:
            # set user
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            r = requests.get(url, headers=headers)
            # access page
            return r.content
        except:
            raise


def file_read(file_path):
    df = pd.read_csv(file_path, header=None)
    return df


def file_write(file_path, df):
    df.to_csv(file_path, header=False, index=False)
    return


def main():
    # init for browser
    browser = webbrowser.get('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" %s')

    # read dataset file
    f = 'dataset.csv'
    df = file_read(f)
    # check web site
    updateSites = []
    reg = []

    def _toMD5(text):
        return hashlib.md5(text).hexdigest()

    for i, row in df.iterrows():
        try:
            url = row[0]
            hash_ago = row[1]
        except:
            hash_ago = 0
        # print(url)

        # read html
        x = AccessPage(url)
        soup = BeautifulSoup(x.html, 'html.parser')
        html = soup.getText().encode('ascii', errors='backslashreplace')

        hash_now = _toMD5(html)
        if hash_now != hash_ago and hash_ago != 0:
            updateSites.append(url)
        reg.append([url, hash_now])
        df = pd.DataFrame(reg)
    
    # recode
    file_write(f, df)

    # view page
    for i in updateSites:
        print(i)
        browser.open(i)


if __name__ == "__main__":
    main()
