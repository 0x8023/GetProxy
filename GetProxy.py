#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 8023
# @Date:   2016-07-20 12:03:25
# @Last Modified by:   8023

import requests

class GetProxy(object):
    """docstring for GetProxy"""
    def __init__(self, arg):
        self.all = 1

        self.anonymous = 2
        self.transparent = 3

        self.cn = 2
        self.intl = 3

        self.ca = {'kuai' : }
        self.ct = {'kuai' : }
        self.ia = {'kuai' : }
        self.it = {'kuai' : }

        self.visibility = {'kuai' : 'http://www.kuaidaili.com/free/',
                           'xici' : 'http://www.xicidaili.com/'}

        # super(GetProxy, self).__init__()
        # self.arg = arg

    def get_html(self, providers = self.all, country = self.all, visibility = self.all):
        pass

    def fetch_url():
        pass

    def


if __name__ == '__main__':
    r = requests.get('http://www.baidu.com')
    print(r.text)
    # print('dui')