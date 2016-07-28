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
        self.port = r'(?P<port>\d*)'
        #requests headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        }

        #read json
        with open('Data.json', 'r') as f:
            self.data = json.load(f)

    def get_url(self, visibility = 'all', pattern = 'all'):
        url = []
        #都不介意
        if visibility == self.all and pattern == self.all:
            pass
        #不介意其中一项
        elif visibility == self.all or pattern == self.all:
            #如果不介意提供商
            if visibility == self.all:
                for x in self.data.values():
                    url += [x[pattern]['url']]
            #如果不介意国别和透明度
            elif pattern == self.all:
                for x in proxies.data[visibility].values():
                    url += [x['url']]
        #
        else:
            url += self.data[visibility][pattern]['url']
        print(url)

    def get_html(self):
        pass

    # def fetch_url(self):
    #     pass


if __name__ == '__main__':
    ss = r'(?P<scheme>https?|HTTPS?)'
    sh = r'(?P<host>(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3})'
    sp = r'(?P<port>\d*)'

    header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        }
    html = requests.get('http://www.kuaidaili.com/free/intr/', headers = header)

    with open('Data.json', 'r') as f:
        r = json.load(f)
        for x in re.finditer(r['kuai']['re'].format(scheme = ss, host = sh, port = sp), html.text, re.S):
            print(x.group('scheme').lower() + '://' + x.group('host') + ':' + x.group('port'))
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