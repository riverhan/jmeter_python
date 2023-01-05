# -*- coding: UTF-8 -*-
# Author: hanerbin
# Date: 2022/11/24 16:03
import os
import sys

import pytest

from common.SendRequest import SendRequest
from common.YamlUtil import YamlUtil


class TestGetToken(object):
    @pytest.mark.smoke
    @pytest.mark.parametrize('args', YamlUtil('yaml_data/get_token.yaml').read_yaml())
    def test_get_token(self, args):
        yamlutil = YamlUtil('extract.yaml')
        params = args['request']['params']
        r = SendRequest(args).send_all_request(params=params)
        token_data = {"access_token": r.json()['access_token']}
        yamlutil.write_yaml(token_data)


if __name__ == '__main__':
    pytest.main()
