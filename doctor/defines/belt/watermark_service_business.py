#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.watermark_service_swagger import WatermarkSwaggerApi
import os
from commonlib import config
import base64

"""
使用说明：


"""


class WatermarkSwaggerBusiness(WatermarkSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(WatermarkSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        if inte_obj.path == '/v1/watermark/sign_image':
            inte_obj.set_headers('X-Belt-Action', 'SignImage')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/watermark/verify_image':
            inte_obj.set_headers('X-Belt-Action', 'VerifyImage')
            inte_obj.set_headers('X-Belt-Version', 'v1')
    def idsImageToBase64(self, image_name):
        return self.imageToBase64(os.path.join(config.ids_image_path, image_name))
    def idsBase64ToImage(self,base64_data,path):
        img=base64.b64decode(base64_data)
        with open(path, "wb") as f:
            f.write(img)
