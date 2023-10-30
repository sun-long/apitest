#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pytest_config.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/14 上午9:58   wangan      1.0         None
'''

class PytestConfigBase(object):
    """ pytest 项目通用配置基类"""

    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name


class ArgusConfig(PytestConfigBase):
    """ argus项目配置类"""

    def __init__(self):
        super(ArgusConfig, self).__init__()
        self._name = 'Argus'


