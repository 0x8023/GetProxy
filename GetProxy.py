#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 8023
# @Date:   2016-07-20 12:03:25
# @Last Modified by:   8023

import requests
import json

class GetProxy(object):
    """docstring for GetProxy"""
    def __init__(self):
        self.all = 'all'

        self.ca = 'cn_anonymous'
        self.ct = 'cn_transparent'
        self.ia = 'intl_anonymous'
        self.it = 'intl_transparent'
        #requests headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        }
        #read json
        with open('Data.json', 'r') as f:
            self.data = json.load(f)

    def get_url(self, visibility = 'all', pattern = 'all'):
        url = []
        if visibility == self.all: #如果不介意提供商
            for x in self.data.values():
                url += [x[pattern]['url']]

        if pattern == self.all: #如果不介意国别和透明度
            for x in proxies.data[visibility].values():
                url += [x['url']]

        # url += self.data[visibility][pattern]['url']
        print(url)

    def get_html(self):
        pass

    # def fetch_url(self):
    #     pass


if __name__ == '__main__':
    # r = requests.get('http://www.xicidaili.com/nn/')
    # print(r.text)
    proxies = GetProxy();
    proxies.get_url(pattern = proxies.ca);

        # print(v)
        # v[cn_anonymous]
    # for k in proxies.data:

    #     print(k)

    # print(proxies.data)



    # 获取最大页面()
    # 循环获取html代码
    # 正则匹配()
    # 输出list