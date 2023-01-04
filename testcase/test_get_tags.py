# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/4 16:33
# @Author : Riveryoyo
"""
import pytest
from common.SendRequest import SendRequest
from common.YamlUtil import YamlUtil


class TestGetTags(object):
    @pytest.mark.parametrize('args', YamlUtil('../yaml_data/get_tags.yaml').read_yaml())
    def test_get_tags(self, args):
        self.url = args['request']['url']
        self.method = args['request']['method']
        params = {'access_token': YamlUtil('../extract.yaml').read_yaml()['access_token']}
        print(params)
        r = SendRequest.send_all_request(method=self.method, url=self.url, params=params)
        print(r.json())
