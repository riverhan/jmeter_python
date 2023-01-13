# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/13 17:50
# @Author : Riveryoyo
"""
import pytest
from common.YamlUtil import YamlUtil
from common.SendRequest import SendRequest


class TestLogin(object):
    @pytest.mark.smoke
    @pytest.mark.parametrize('args', YamlUtil('yaml_data/shop_yaml/login.yaml').read_yaml())
    def test_login(self, args):
        response = SendRequest(args).standard_yaml()
        print(response.json())
        print(response.status_code)
