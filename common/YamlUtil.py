import os

import yaml


class YamlUtils(object):
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self):
        with open(self.yaml, mode='r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(stream=f)
            return yaml_data

    def write_yaml(self, data):
        with open(self.yaml, mode='w', encoding='utf-8') as f:
            yaml.dump(data, stream=f, allow_unicode=True, encoding='utf-8')

    def clear_yaml(self):
        with open(self.yaml, mode='w', encoding='utf-8') as f:
            f.truncate()


if __name__ == '__main__':
    pass
