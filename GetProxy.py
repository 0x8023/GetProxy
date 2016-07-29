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
        for x in re.finditer(self.data[provider]['re'].format(scheme = self.SCHEME, host = self.HOST, port = self.PORT), html, re.S):
            yield {x.group('scheme').lower(): x.group('scheme').lower() + '://' + x.group('host') + ':' + x.group('port')}

    def get_html(self, provider, pattern, page):
        return requests.get(self.data[provider][pattern].format(page = page), headers = self.HEADERS).text

    def get_maxpage(self, provider, pattern):
        return int(re.search(self.data[provider]['maxpage'].format(maxpage = self.MAXPAGE), self.get_html(provider, pattern, 1), re.S).group('maxpage'))

    def get_proxy(self, provider, pattern, quantity):
        num = 0
        for x in range(1, self.get_maxpage(provider, pattern)):
            for y in self.get_url(provider, self.get_html(provider, pattern, x)):
                if num < quantity: yield y
                else: return
                num += 1

if __name__ == '__main__':
    proxies = GetProxy()
    for x in proxies.get_proxy('xici', 'cn_transparent', 100):
        print(x)
