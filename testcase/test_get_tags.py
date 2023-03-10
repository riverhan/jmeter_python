# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/4 16:33
# @Author : Riveryoyo
"""

import pytest
from common.SendRequest import SendRequest
from common.YamlUtil import YamlUtil


class TestGetTags(object):
    @pytest.mark.smoke1
    @pytest.mark.parametrize('args', YamlUtil('yaml_data/get_tags.yaml').read_yaml())
    def test_get_tags(self, args):
        response = SendRequest(args).standard_yaml()
        print(response.text)
