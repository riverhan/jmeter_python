import re

import jsonpath
import requests

from common.YamlUtil import YamlUtil


class SendRequest:

    def __init__(self, yam_args):
        self._standard = {'name', 'request', 'validate'}
        self._sess = requests.session()
        self._args = yam_args

    def standard_yaml(self, flag=1, **kwargs):
        if self._standard <= set(self._args.keys()):
            if set(self._args['request'].keys()).issuperset({'method', 'url'}):
                for k, v in self._args['request'].items():
                    if k == 'files':
                        for fk, fv in v.items():
                            v[fk] = open(fv, 'rb')
                self._extract_param(self._send_all_request(**self._args['request'], **kwargs))
                return self._send_all_request(**self._args['request'], **kwargs)
            else:
                print("YAML文件中必须包含'method'和'url'")
        else:
            print("YAML配置文件中缺少必要的标签")
            return flag == 0

    def _send_all_request(self, **kwargs):
        response = self._sess.request(**kwargs)
        return response

    def _extract_param(self, ret):
        if 'extract' in self._args.keys():
            for k, v in self._args['extract'].items():
                if "(.*?)" in v or "(.+?)" in v:
                    zz_value = re.findall(v, ret.text)
                    print(zz_value)
                    if len(zz_value) == 1:
                        YamlUtil('extract.yaml').write_yaml({k: zz_value[0]})
                    else:
                        YamlUtil('extract.yaml').write_yaml({k: zz_value})
                else:
                    json_value = jsonpath.jsonpath(ret.json(), v)
                    if json_value:
                        if len(json_value) == 1:
                            YamlUtil('extract.yaml').write_yaml({k: json_value[0]})
                            print(json_value)
                    else:
                        print('未提取到相关数据！！')


if __name__ == '__main__':
    # args = {'name': '上传文件', 'request': {'url': 'https://api.weixin.qq.com/cgi-bin/media/uploadimg', 'method':
    # 'post', 'files': {'media': '2023.jpg'}}, 'validate': None} params = { 'access_token':
    # '64_e9Q1amx7E0j4PDBk3wy5PBlhWNz9zmvRWU74WSqkX6xpO8QosJVD1WOdraJNgX_mMf2gfnxCMyKzFih_0YMm4kHXEQwjaRNF9itDw2xhb0n8gn68QY8-WNe-h1AATDbAFAFYI' } ya = SendRequest(args) a = ya.standard_yaml(files=args['request']['files'], params=params) print(a.json())
    pass
