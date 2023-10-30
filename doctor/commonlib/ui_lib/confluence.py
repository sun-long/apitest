#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hikvision.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/12/2 下午4:46   wangan      1.0         None
'''
import os
import re
import time

import requests

from commonlib.ui_lib.base_ui import BaseUI


class Confluence(BaseUI):
    def __init__(self, username, password, driverversion):
        """ 海康摄像头管理平台"""
        self.login_url = "https://confluence.sensetime.com/"
        self.login_username = username
        self.login_password = password
        super(Confluence, self).__init__(driverversion)
        self._login()
        self._set_cookies()
        # self._set_token()
        self.quit()
        i = 1

    @property
    def cookies(self):
        return self._cookies

    @property
    def authenticity_token(self):
        return self._token

    def _set_cookies(self):
        cookies_dict = {}
        for cookie in self.driver.get_cookies():
            cookies_dict.update({cookie['name']: cookie['value']})
        self._cookies = cookies_dict

    def _set_token(self):
        self._token = self.driver.find_element_by_xpath("//meta[@name='csrf-token']").get_attribute('content')

    def _login(self):
        """ 登录"""
        time.sleep(1)
        self.driver.get(self.login_url)
        self.driver.find_element_by_id("os_username").send_keys(self.login_username)
        self.driver.find_element_by_id("os_password").send_keys(self.login_password)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(1)

    def downloadApi(self, url, save_path=None):
        res = requests.get(url, cookies=self.cookies, allow_redirects=False)

        if not save_path:
            save_path = 'service.swagger.json'
        with open(save_path, "wb") as code:
            code.write(res.content)
        return save_path





if __name__ == '__main__':
    gh = Confluence("wangan", "liuting@")
    download_path = gh.downloadApi('')
    i = 1


