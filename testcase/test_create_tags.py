# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/4 17:31
# @Author : Riveryoyo
"""
import pytest
from common.SendRequest import SendRequest
from common.YamlUtil import YamlUtil


class TestCreateTage(object):
    @pytest.mark.smoke
    @pytest.mark.parametrize('args', YamlUtil('../yaml_data/create_tags.yaml').read_yaml())
    def test_create_tags(self, args):
        self.url = args['request']['url']
        self.method = args['request']['method']
        self.data = args['request']['data']
        print(self.data)
        self.params = {'access_token': YamlUtil('../extract.yaml').read_yaml()['access_token']}
        r = SendRequest.send_all_request(method=self.method, url=self.url, params=self.params, json=self.data)
        print(r.json())
