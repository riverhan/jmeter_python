# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/4 16:33
# @Author : Riveryoyo
"""

import pytest
from common.SendRequest import SendRequest
from common.YamlUtil import YamlUtil


class TestGetTags(object):
    @pytest.mark.smoke
    @pytest.mark.parametrize('args', YamlUtil('yaml_data/get_tags.yaml').read_yaml())
    def test_get_tags(self, args):
        params = {'access_token': YamlUtil('extract.yaml').read_yaml()['access_token']}
        print(params)
        response = SendRequest(args).standard_yaml(params=params)
        print(response.text)
