#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   dbproxy.py
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/11/3 下午5:07   wangan      1.0         None
'''
import base64
import os
import time

from commonlib.api_lib.base_api import BaseApi
from commonlib.log_utils import log
from core.pm_utils import load_postman
from core.ret_utils import RespRet

collections = load_postman("common/prometheus/")


class PrometheusApi(BaseApi):
    def __init__(self, host):
        self.host = host
        collections.init(self)

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        inte_obj.set_host(self.host)
        inte_obj.set_wrap_response_class(RespRet)

    def GetStaticFeatureProxyDbSize(self, sfd_name):
        """ 查询SFD使用量 查询当前最新"""
        prometheus = collections.interface('prometheus', '查询SFD使用量')
        query = 'sum(static_feature_proxy_db_size{service="%s"}) by (service)' % sfd_name
        prometheus.update_params('query', query)
        resp = prometheus.request()
        self.log_resp_info(resp)
        if resp.json["status"] != 'success':
            raise Exception("查询SFD失败")
        return resp.json_get("data.result.0.value")[1]

if __name__ == '__main__':
    host = 'http://prometheus-argus-staging.sensetime.com'
    pts = PrometheusApi(host)
    res = pts.GetStaticFeatureProxyDbSize('argus-sfd-sg-sfd-proxy-headless')
    print(res)