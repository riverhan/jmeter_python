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
    @pytest.mark.parametrize('args', YamlUtil('yaml_data/create_tags.yaml').read_yaml())
    def test_create_tags(self, args):
        response = SendRequest(args).standard_yaml()
        print(response.json())
