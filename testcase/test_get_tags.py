# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/4 16:33
# @Author : Riveryoyo
"""
import os
import sys

import pytest
from common.SendRequest import SendRequest
from common.YamlUtil import YamlUtil
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)


class TestGetTags(object):
    @pytest.mark.usermanage
    @pytest.mark.parametrize('args', YamlUtil('yaml_data/get_tags.yaml').read_yaml())
    def test_get_tags(self, args):
        self.url = args['request']['url']
        self.method = args['request']['method']
        params = {'access_token': YamlUtil('../extract.yaml').read_yaml()['access_token']}
        print(params)
        r = SendRequest.send_all_request(method=self.method, url=self.url, params=params)
        print(r.json())
