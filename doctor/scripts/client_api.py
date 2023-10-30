#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   grpc_tools.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/12/17 下午6:10   wangan      1.0         None
'''
from commonlib.api_lib.tools.client_api import ClientApi


def client_run(yaml_path=None):
    """ 端执行命令
    :param yaml_path:
    :return:
    """
    ca = ClientApi()
    ca.set_config_obj_by_type('dev')
    ca.client_doing(yaml_path)

if __name__ == '__main__':
    pass