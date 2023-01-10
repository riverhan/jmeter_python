# -*- coding:utf-8 -*-
"""
# @Time : 2023/1/10 18:03
# @Author : Riveryoyo
"""
import os
import yaml


class DebugTalk(object):
    @staticmethod
    def read_yaml(key):
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'extract.yaml', 'r') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value[key]


if __name__ == '__main__':
    print(DebugTalk().read_yaml())
