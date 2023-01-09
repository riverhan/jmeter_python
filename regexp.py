# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/9 23:35
@Author ： Riveryoyo
@IDE ：PyCharm

"""
import re

regexp = r"\${(.*?)\((.*?)\)}"
a = '${read_yaml(token1)}'
b = re.findall(regexp, a)
print(b)
