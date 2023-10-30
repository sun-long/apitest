#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.authiam_service_swagger import AuthiamSwaggerApi
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log
import os

"""
使用说明：


"""


class AuthiamSwaggerBusiness(AuthiamSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(AuthiamSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "Authorization" # 默认token的key
        self.TOKEN_VALUE = "Bearer %s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        if inte_obj.path == '/v1/login':
            inte_obj.set_headers('X-Belt-Action', '')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/captcha':
            inte_obj.set_headers('X-Belt-Action', '')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        else:
            inte_obj.set_headers('X-Belt-Action', inte_obj.path_action)
            inte_obj.set_headers('X-Belt-Version', inte_obj.path_version)

    def get_captcha(self, showImage=False, print_log=True):
        """ 获取验证码"""
        resp = self.captchaGetApi(width=300, height=300, print_log=print_log)
        assert resp.status_code == 200
        captcha_id = resp.json_get("id")
        if showImage:
            data = resp.json_get("data")
            data = data.split("data:image/png;base64,")[-1]
            img_path = os.path.join(config.temp_path, "captcha.png")
            utils.base64ToFile(img_path, data)
            from PIL import Image
            img = Image.open(img_path)
            img.show()
        return captcha_id

    def login_with_phone(self, phone, password, captcha_id, digits, source=None):
        """ 手机号登录"""
        captcha = {
            "digits": digits,
            "id": captcha_id
        }
        client_id = None
        expires_after = 36000
        email = None
        verification_code = None
        username = None
        password = sign_utils.getMd5(password)
        resp = self.loginPostApi(captcha=captcha, client_id=client_id, expires_after=expires_after, email=email,
                                       phone=phone, verification_code=verification_code,source=source,
                                       username=username, password=password)
        return resp

    def login_with_user(self, username, password, captcha_id, digits):
        """ 用户名密码登录"""
        captcha = {
            "digits": digits,
            "id": captcha_id
        }
        client_id = None
        expires_after = 36000
        email = None
        verification_code = None
        username = username
        password = sign_utils.getMd5(password)
        resp = self.loginPostApi(captcha=captcha, client_id=client_id, expires_after=expires_after, email=email,
                                       phone=None, verification_code=verification_code,
                                       username=username, password=password)
        return resp

