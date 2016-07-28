#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 8023
# @Date:   2016-07-20 12:03:25
# @Last Modified by:   8023

import requests
import json
import re

class GetProxy(object):
    """docstring for GetProxy"""
    def __init__(self):
        #built-in regular
        self.SCHEME = r'(?P<scheme>https?|HTTPS?)'
        self.HOST = r'(?P<host>(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3})'
        self.PORT = r'(?P<port>\d{1,5})'
        self.MAXPAGE = r'(?P<maxpage>\d{1,6})'
        #requests headers
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        }

        #read json
        with open('Data.json', 'r') as f:
            self.data = json.load(f)

    def get_url(self, provider, html):
        l = []
        for x in re.finditer(self.data[provider]['re'].format(scheme = self.SCHEME, host = self.HOST, port = self.PORT), html, re.S):
            l.append({x.group('scheme').lower(): x.group('scheme').lower() + '://' + x.group('host') + ':' + x.group('port')})
        return (l)

    def get_html(self, provider, pattern, page):
        return requests.get(self.data[provider][pattern].format(page = page), headers = self.HEADERS).text

    def get_maxpage(self, provider, html):
        return int(re.search(self.data[provider]['maxpage'].format(maxpage = self.MAXPAGE), html, re.S).group('maxpage'))

if __name__ == '__main__':
    proxies = GetProxy()
    print(proxies.get_maxpage('xici', proxies.get_html('xici', 'cn_transparent', 1)))
    # print(proxies.get_url('kuai', proxies.get_html('kuai', 'cn_transparent', 1)))
