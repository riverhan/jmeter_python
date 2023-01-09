# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/4 17:31
# @Author : Riveryoyo
"""

import pytest
from common.SendRequest import SendRequest
from common.YamlUtil import YamlUtil


class TestCreateTage(object):
    @pytest.mark.smoke1
    @pytest.mark.parametrize('args', YamlUtil('yaml_data/create_tags.yaml').read_yaml())
    def test_create_tags(self, args):
        self.json = args['request']['data']
        self.params = {'access_token': YamlUtil('extract.yaml').read_yaml()['access_token']}
        response = SendRequest(args).standard_yaml(params=self.params)
        # if isinstance(response, int):
        #     print(response)
        # else:
        #     print(response)
        print(response)
