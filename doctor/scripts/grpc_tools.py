#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   grpc_tools.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/12/17 下午6:10   wangan      1.0         None
'''
from commonlib.api_lib.tools.post_data_tool import PostDataTool
from core.proto_utils import load_proto


def gen_message(product_name=None):
    """ 生成message数据包
    :param product_name:
    :return:
    """
    collections = load_proto(product_name)
    collections.save_message(product_name)
    print("success.")

def post_data(yaml_path=None, config=None, ak=None, sk=None, device_id=None, host=None, static_id=None, stream_id=None):
    """ 推送数据 """
    pdt = PostDataTool()
    if not config:
        config = 'dev'
    pdt.set_config_obj_by_type(config)
    pdt.post_data_from_yaml(yaml_path, ak=ak, sk=sk, device_id=device_id,
                            host=host, static_id=static_id, stream_id=stream_id)


if __name__ == '__main__':
    post_data('demo', config='dev')