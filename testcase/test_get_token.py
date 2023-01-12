# -*- coding: UTF-8 -*-
# Author: hanerbin
# Date: 2022/11/24 16:03
import pytest

from common.SendRequest import SendRequest
from common.YamlUtil import YamlUtil


class TestGetToken(object):
    @pytest.mark.smoke
    @pytest.mark.parametrize('args', YamlUtil('yaml_data/get_token.yaml').read_yaml())
    def test_get_token(self, args):
        response = SendRequest(args).standard_yaml()
        print(response.text)


if __name__ == '__main__':
    pytest.main()
