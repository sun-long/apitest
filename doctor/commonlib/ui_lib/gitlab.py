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


class GitLab(BaseUI):
    def __init__(self, username, password, driverversion, zone="sz"):
        """ gitlab sz"""
        if zone == "sz":
            self.login_url = "https://gitlab.sz.sensetime.com/"
        elif zone == "bj":
            self.login_url = "https://gitlab.bj.sensetime.com/"
        else:
            raise Exception("invalid zone:%s" % zone)
        self.login_username = username
        self.login_password = password
        super(GitLab, self).__init__(driverversion)
        self._login()
        self._set_cookies()
        self._set_token()
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
        self.driver.find_element_by_id("username").send_keys(self.login_username)
        self.driver.find_element_by_id("password").send_keys(self.login_password)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(1)

    def downloadApi(self, url, save_path=None):
        # url = 'https://gitlab.sz.sensetime.com/belt/crd/ras-protocols/ras-device/-/raw/cx_dms/gen/swagger/service.swagger.json'
        res = requests.get(url, cookies=self.cookies, allow_redirects=False)

        if not save_path:
            save_path = 'service.swagger.json'
        with open(save_path, "wb") as code:
            code.write(res.content)
        return save_path





if __name__ == '__main__':
    gh = GitLab("", "")
    download_path = gh.downloadApi('')
    i = 1


