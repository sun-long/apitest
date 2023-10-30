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


class DevCenter(BaseUI):
    def __init__(self, username, password):
        """ 海康摄像头管理平台"""
        self.login_url = "http://devcenter.bj.sensetime.com/users/sign_in"
        self.login_username = username
        self.login_password = password
        super(DevCenter, self).__init__()
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
        self.driver.find_element_by_id("user_username").send_keys(self.login_username)
        self.driver.find_element_by_id("user_password").send_keys(self.login_password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)

    def downloadApi(self, uuid, target_dir=None):
        url = 'http://devcenter.bj.sensetime.com/builds/download/%s' % uuid
        res = requests.get(url, cookies=self.cookies, allow_redirects=False)
        location = res.headers['location']
        params = location.split('?')[-1].split('&')
        file_name = None
        for param in params:
            if param.split('=')[0] == "filename":
                file_name = param.split('=')[1]
                break
        if not file_name:
            raise Exception('not found filename')

        if target_dir:
            file_name = os.path.join(target_dir, file_name)

        set_cookie = res.headers['Set-Cookie']
        headers = {
            "cookie": set_cookie}
        res = requests.get(location, headers=headers)
        with open(file_name, "wb") as code:
            code.write(res.content)
        return file_name

    def referenceApi(self):
        url = 'http://devcenter.bj.sensetime.com/products/365.json'
        res = requests.get(url, cookies=self.cookies, allow_redirects=False)
        if res.status_code != 200:
            raise Exception('ERROR! url=%s' % url)
        return res.json()

    def commitApi(self, commit_id):
        url = 'http://devcenter.bj.sensetime.com/products/365/commit_info/%s.json' % commit_id
        res = requests.get(url, cookies=self.cookies, allow_redirects=False)
        if res.status_code != 200:
            raise Exception('ERROR! url=%s' % url)
        return res.json()

    def buildApi(self, data):
        """ build"""
        url = 'http://devcenter.bj.sensetime.com/products/365/builds'
        # data = {
        #     'branch': 'release/5.1.1',
        #     'cid': 'a5fddb5479f228538fee97a1a64e779819ea7029',
        #     'config': 'SenseRealty_x86_icloud',
        #     'platform': 'linux',
        #     'description': 'test-wangan_1',
        #     'authenticity_token': self.authenticity_token,
        # }
        data.update({'authenticity_token': self.authenticity_token,})
        print("build info:")
        print(data)
        r = requests.post(url, data=data, cookies=self.cookies, allow_redirects=False)
        if r.status_code != 302:
            raise Exception('build error')

    def buildResults(self, project_name='365_SenseGoEdgeCube'):
        url = 'http://devcenter.bj.sensetime.com/products/%s/builds/results' % project_name
        res = requests.get(url, cookies=self.cookies, allow_redirects=False)
        if res.status_code != 200:
            raise Exception('ERROR! url=%s' % url)
        html = res.text

        exp1 = re.compile("(?isu)<tr[^>]*>(.*?)</tr>")
        exp2 = re.compile("(?isu)<td[^>]*>(.*?)</td>")
        exp3 = re.compile(r'href="(.*?)"')
        exp4 = re.compile("<span[^>]*>(.*?)</span>")
        result_list = []
        for row in exp1.findall(html):
            res = exp2.findall(row)
            if not res:
                continue
            result_list.append({
                'report_link':  exp3.findall(res[0])[0],
                # 'c_time': res[1].strip(),
                # 'status': exp4.findall(res[3])[0]
            })

        return result_list

    def buildReport(self, report_link):
        """ report信息"""
        url = 'http://devcenter.bj.sensetime.com%s' % report_link
        res = requests.get(url, cookies=self.cookies, allow_redirects=False)
        if res.status_code != 200:
            raise Exception('ERROR! url=%s' % url)
        report_info = res.json()
        return report_info

if __name__ == '__main__':
    dc = DevCenter("username", 'password')
    uuid = '30a2c64ee37b471ab9f6d2fe14a699c1'
    download_path = dc.downloadApi(uuid)
    # print('download success.path:%s' % download_path)
    # dc.buildApi()
    dc.buildResults()


