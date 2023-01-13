# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/7 20:33
@Author ： Riveryoyo
@IDE ：PyCharm

"""
import pytest

from common.YamlUtil import YamlUtil
from common.SendRequest import SendRequest


class TestUploadFile(object):
    @pytest.mark.smoke1
    @pytest.mark.parametrize('args', YamlUtil('yaml_data/test_upload_file.yaml').read_yaml())
    def test_upload_file(self, args):
        response = SendRequest(args).standard_yaml()
        print(response)
