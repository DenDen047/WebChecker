#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import commands
import pandas as pd
from BeautifulSoup import BeautifulSoup

from OpenHTML import AccessPage


def file_read(file_path):
    df = pd.read_csv(file_path, header=None)
    return df


def file_write(file_path, df):
    df.to_csv(file_path, header=False, index=False)
    return


def main():
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
        print url

        # read html
        x = AccessPage(url)
        soup = BeautifulSoup(x.html)
        soup = soup.body
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
        print i
        commands.getoutput('open ' + i)


if __name__ == "__main__":
    main()
