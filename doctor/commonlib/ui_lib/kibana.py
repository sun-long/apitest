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


class Kibana(BaseUI):
    def __init__(self, username, password, driverversion):
        """ gitlab sz"""
        self.login_url = "http://kibana.sensegalaxy-test.sensetime.com/login#?_g=()"
        self.login_username = username
        self.login_password = password
        super(Kibana, self).__init__(driverversion)
        self._login()
        self._set_cookies()
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

    def _login(self):
        """ 登录"""
        time.sleep(1)
        self.driver.get(self.login_url)
        self.driver.find_element_by_id("sg.username").send_keys(self.login_username)
        self.driver.find_element_by_id("sg.password").send_keys(self.login_password)
        self.driver.find_element_by_id("sg.login").click()
        time.sleep(1)

    def msearchApi(self, request_id, gte, lte, current_time):
        gte = gte * 1000
        lte = lte * 1000
        current_time = current_time * 1000
        url = "http://kibana.sensegalaxy-test.sensetime.com/elasticsearch/_msearch?rest_total_hits_as_int=true&ignore_throttled=true"
        # payload = "{\"index\":\"galaxy_adaptor_cp_dev\",\"ignore_unavailable\":true,\"preference\":%s}\n{\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"interval\":\"3h\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[{\"field\":\"@timestamp\",\"format\":\"date_time\"}],\"query\":{\"bool\":{\"must\":[{\"query_string\":{\"query\":\"\\\"%s\\\"\",\"analyze_wildcard\":true,\"default_field\":\"*\"}},{\"range\":{\"@timestamp\":{\"gte\":%s,\"lte\":%s,\"format\":\"epoch_millis\"}}}],\"filter\":[],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647},\"timeout\":\"30000ms\"}\n" % (lte, request_id, gte, lte)
        # payload = "{\"index\":\"galaxy_adaptor_cp_dev\",\"ignore_unavailable\":true,\"preference\":1682239461200}\n{\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"interval\":\"3h\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[{\"field\":\"@timestamp\",\"format\":\"date_time\"}],\"query\":{\"bool\":{\"must\":[{\"query_string\":{\"query\":\"\\\"c66bbb3a-4264-44dd-8f2e-f92b151bb755\\\"\",\"analyze_wildcard\":true,\"default_field\":\"*\"}},{\"range\":{\"@timestamp\":{\"gte\":1681574400000,\"lte\":1682265600000,\"format\":\"epoch_millis\"}}}],\"filter\":[],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647},\"timeout\":\"30000ms\"}\n"
        payload = "{\"index\":\"galaxy_adaptor_cp_test\",\"ignore_unavailable\":true,\"preference\":%s}\n{\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"interval\":\"3h\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[{\"field\":\"@timestamp\",\"format\":\"date_time\"}],\"query\":{\"bool\":{\"must\":[{\"query_string\":{\"query\":\"\\\"%s\\\"\",\"analyze_wildcard\":true,\"default_field\":\"*\"}},{\"range\":{\"@timestamp\":{\"gte\":%s,\"lte\":%s,\"format\":\"epoch_millis\"}}}],\"filter\":[],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647},\"timeout\":\"30000ms\"}\n" % (current_time, request_id, gte, lte)
        headers = {
            'kbn-version': '6.8.2',
            'content-type': 'application/x-ndjson',
            'Connection': 'keep-alive'
        }
        response = requests.request("POST", url, cookies=self.cookies, headers=headers, data=payload)
        return response



if __name__ == '__main__':
    ki = Kibana("admin", "c5h7ziki", 110)
    resp = ki.msearchApi("c66bbb3a-4264-44dd-8f2e-f92b151bb755",1681969784669,1681984184669)
    i = 1


