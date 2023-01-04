# -*- coding: UTF-8 -*-
# Author: hanerbin
# Date: 2022/11/23 17:10

import pytest
import os
from common.YamlUtil import YamlUtil


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    pass
    # YamlUtil('../extract.yaml').clear_yaml()
