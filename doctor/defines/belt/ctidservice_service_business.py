#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
from commonlib import config
from pytest_check import check
import random

from commonlib.decorator import wait
from defines.belt.api.ctidservice_service_swagger import CtidServiceSwaggerApi

"""
ʹ��˵����


"""


class CtidServiceSwaggerBusiness(CtidServiceSwaggerApi):
    """ ҵ�������д������"""

    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(CtidServiceSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "Authorization"  # Ĭ��token��key
        self.TOKEN_VALUE = "Bearer %s"  # tokenĬ����Ϣ

    def init_interface(self, inte_obj):
        """��ʼ���ӿں�������Ҫͳһ��ʼ���Ĳ���д������
        inte_obj:�ǽӿڵĶ��󣬱�����Ҫͳһ��ʼ��host��inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

    def ctidImageToBase64(self, image_name):
        return self.imageToBase64(os.path.join(config.ids_image_path, image_name))
