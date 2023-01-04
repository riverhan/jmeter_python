# -*- coding: UTF-8 -*-
# Author: hanerbin
# Date: 2022/11/24 18:52
import yaml
import os


class YamlUtil(object):
    def __init__(self, yaml_file):
        """
        通过__init__方法把yaml文件传入到这个类
        :param yaml_file:
        """
        self.yaml_file = yaml_file

    def read_yaml(self):
        """
        yaml.load():对yaml文件进行反序列化
        """
        with open(self.yaml_file, 'r', encoding="UTF-8") as f:
            value = yaml.safe_load(stream=f)
            # return yaml.load(f, Loader=yaml.FullLoader)
            return value

    def write_yaml(self, data):
        with open(self.yaml_file, encoding='utf-8', mode='a+') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def clear_yaml(self):
        with open(self.yaml_file, encoding='utf-8', mode='w') as f:
            f.truncate()


if __name__ == '__main__':
    yamlutil = YamlUtil('../extract.yaml')
    print(yamlutil.read_yaml())
