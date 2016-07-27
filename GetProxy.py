#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 8023
# @Date:   2016-07-20 12:03:25
# @Last Modified by:   8023

import requests
import json

class GetProxy(object):
    """docstring for GetProxy"""
    def __init__(self, arg):
        self.all = 'all'
        self.ca = 'cn_anonymous'
        self.ct = 'cn_transparent'
        self.ia = 'intl_anonymous'
        self.it = 'intl_transparent'

        # super(GetProxy, self).__init__()
        # self.arg = arg

    # def get_html(self, providers = self.all, country = self.all, visibility = self.all):
    #     pass

    # def fetch_url(self):
    #     pass


if __name__ == '__main__':
    # r = requests.get('http://www.baidu.com')
    # print(r.text)object

    with open('Data.db', 'r') as f:
        data = json.load(f)