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
        self.scheme = r'(?P<scheme>https?|HTTPS?)'
        self.host = r'(?P<host>(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3})'
        self.port = r'(?P<port>\d{1,5})'
        self.maxpage = r'(?P<maxpage>\d{1,6})'
        #requests headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        }

        #read json
        with open('Data.json', 'r') as f:
            self.data = json.load(f)

    # def get_proxies(self, num, provider, pattern):
    #     l = []
    #     for x in get_html(provider, pattern):
    #         for y in get_url(x, provider):
    #             l += y
    #             if len(l) >= num:
    #                 return l

    def get_url(self, provider, pattern, html):
        for x in re.finditer(r[provider]['re'].format(scheme = self.scheme, host = self.host, port = self.port), html, re.S):
            print(x.group('scheme').lower() + '://' + x.group('host') + ':' + x.group('port'))

    def get_html(self, provider, pattern, page):
        return requests.get(self.data[provider][pattern].format(page), headers = self.headers).text

    def get_maxpage(self, provider, html):
        return int(re.search(self.data[provider]['maxpage'].format(maxpage = self.maxpage), html, re.S).group('maxpage'))

if __name__ == '__main__':
    proxies = GetProxy()
    print(proxies.get_maxpage('kuai', proxies.get_html('kuai', 'cn_transparent', 1)))

    # print(html.text)

    # proxies = GetProxy();
    # proxies.get_url(pattern = proxies.ca);


        # print(v)
        # v[cn_anonymous]
    # for k in proxies.data:

    #     print(k)

    # print(proxies.data)



    # 获取最大页面()
    # 循环获取html代码
    # 正则匹配()
    # 输出list