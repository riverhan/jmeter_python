# -*- coding: UTF-8 -*-
# Author: hanerbin
# Date: 2022/11/24 16:03
import pytest

from common.SendRequest import SendRequest
from common.YamlUtil import YamlUtil


class TestGetToken(object):
    # @pytest.mark.smoke
    @pytest.mark.parametrize('args', YamlUtil('../yaml_data/get_token.yaml').read_yaml())
    def test_get_token(self, args):
        yamlutil = YamlUtil('../extract.yaml')
        url = args['request']['url']
        method = args['request']['method']
        if method == 'get':
            params = args['request']['params']
            r = SendRequest().send_all_request(method=method, url=url, params=params)
            token_data = {"access_token": r.json()['access_token']}
            yamlutil.write_yaml(token_data)
            print(r.json())
        else:
            data = args['request']['data']
            r = SendRequest().send_all_request(method=method, url=url, data=data)
            access_token = {'tenant_access_token': r.json()['tenant_access_token']}
            yamlutil.write_yaml(access_token)
            print(r.json())


if __name__ == '__main__':
    pytest.main()
