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
import csv
import time
import datetime
import pytz
import urllib3
urllib3.disable_warnings()
import requests

from commonlib.ui_lib.base_ui import BaseUI
from commonlib import time_utils

class Kibana(BaseUI):
    def __init__(self, username, password, host, driverversion="116"):
        """ gitlab sz"""
        self.login_url = "%s/login#?_g=()" % host
        self.api_url = host
        self.login_username = username
        self.login_password = password
        super(Kibana, self).__init__(driverversion)
        self._login()
        self._set_cookies()
        self.quit()

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
        self.driver.find_element_by_name("username").send_keys(self.login_username)
        self.driver.find_element_by_name("password").send_keys(self.login_password)
        self.driver.find_element_by_xpath("//*[@id='reactLoginRoot']/div//form/button").click()
        time.sleep(1)

    def msearchApi(self, query_list, gte, lte, current_time):
        current_time = current_time * 1000
        url = "%s/elasticsearch/_msearch?rest_total_hits_as_int=true&ignore_throttled=true" % self.api_url

        querys = ""
        for query in query_list:
            querys += "{\"multi_match\":{\"type\":\"phrase\",\"query\":\"%s\",\"lenient\":true}}," % query
        if querys:
            querys = querys[:-1]
        payload = "{\"index\":\"logging_*\",\"ignore_unavailable\":true,\"preference\":%s}\n{\"timeout\":\"30000ms\",\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"fixed_interval\":\"3h\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[{\"field\":\"@timestamp\",\"format\":\"date_time\"}],\"query\":{\"bool\":{\"must\":[],\"filter\":[{\"bool\":{\"filter\":[%s]}},{\"range\":{\"@timestamp\":{\"format\":\"strict_date_optional_time\",\"gte\":\"%s\",\"lte\":\"%s\"}}}],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647}}\n" % (current_time, querys, gte, lte)

        # payload = "{\"index\":\"logging_*\",\"ignore_unavailable\":true,\"preference\":%s}\n{\"timeout\":\"30000ms\",\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"fixed_interval\":\"3h\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[{\"field\":\"@timestamp\",\"format\":\"date_time\"}],\"query\":{\"bool\":{\"must\":[],\"filter\":[{\"bool\":{\"filter\":[{\"multi_match\":{\"type\":\"phrase\",\"query\":\"%s\",\"lenient\":true}},{\"multi_match\":{\"type\":\"phrase\",\"query\":\"%s\",\"lenient\":true}}]}},{\"range\":{\"@timestamp\":{\"format\":\"strict_date_optional_time\",\"gte\":\"%s\",\"lte\":\"%s\"}}}],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647}}\n" % (current_time, query_list[0], query_list[1], gte,lte)
        # payload = "{\"index\":\"logging*\",\"ignore_unavailable\":true,\"preference\":1693978929737}\n{\"timeout\":\"30000ms\",\"version\":true,\"size\":500,\"sort\":[{\"@timestamp\":{\"order\":\"desc\",\"unmapped_type\":\"boolean\"}}],\"_source\":{\"excludes\":[]},\"aggs\":{\"2\":{\"date_histogram\":{\"field\":\"@timestamp\",\"fixed_interval\":\"3h\",\"time_zone\":\"Asia/Shanghai\",\"min_doc_count\":1}}},\"stored_fields\":[\"*\"],\"script_fields\":{},\"docvalue_fields\":[{\"field\":\"@timestamp\",\"format\":\"date_time\"}],\"query\":{\"bool\":{\"must\":[],\"filter\":[{\"bool\":{\"filter\":[{\"multi_match\":{\"type\":\"phrase\",\"query\":\"7ea07d90-30d2-4013-86fb-9517c6064f23\",\"lenient\":true}},{\"multi_match\":{\"type\":\"phrase\",\"query\":\"GetRoutedModel\",\"lenient\":true}}]}},{\"range\":{\"@timestamp\":{\"format\":\"strict_date_optional_time\",\"gte\":\"2023-08-30T06:07:22.714Z\",\"lte\":\"2023-09-06T06:07:22.714Z\"}}}],\"should\":[],\"must_not\":[]}},\"highlight\":{\"pre_tags\":[\"@kibana-highlighted-field@\"],\"post_tags\":[\"@/kibana-highlighted-field@\"],\"fields\":{\"*\":{}},\"fragment_size\":2147483647}}"

        headers = {
            'kbn-version': '7.4.2',
            'content-type': 'application/x-ndjson',
            'Connection': 'keep-alive'
        }
        response = requests.request("POST", url, cookies=self.cookies, headers=headers, data=payload, verify=False)
        #print(response.status_code)
        #print(response.text)
        return response


def to_utc_time_str(time_str):
    tz = pytz.timezone('Asia/Shanghai')
    utc_tz = pytz.utc
    dt_start= datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')  
    utc_start = dt_start.replace(tzinfo=tz).astimezone(utc_tz)
    utc_start = utc_start+ datetime.timedelta(minutes =6)
    utc_time_str = utc_start.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    return utc_time_str

def time_shift(utctime_str,add_min):
    dt = datetime.datetime.strptime(utctime_str,'%Y-%m-%dT%H:%M:%S.%fZ')
    new_dt = dt + datetime.timedelta(minutes =add_min)
    return new_dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    
def search(start,end,min_step):
    gte = to_utc_time_str(start)
    end =  to_utc_time_str(end)
    model_list = ["nova-ptc-yue-oral-xl-v1-4-1-0825","nova-ptc-yue-xl-v1-4-1-0825","nova-ptc-xl-v2-internal-test"]
    current_time = time_utils.get_timestamp()
    query1 = "utilize_model_name"
    result = {}
    results = []
    with open(f"result/weight.csv","w", newline='') as csvfile:
        header = ['begin','end','nova-ptc-yue-oral-xl-v1-4-1-0825','nova-ptc-yue-xl-v1-4-1-0825','nova-ptc-xl-v2-internal-test','sum']
        writer = csv.DictWriter(csvfile,fieldnames=header)
        writer.writeheader()
        for i  in range(0, 12):
            result['begin']=gte
            lte = time_shift(gte,min_step)
            result['end']=lte
        
            sum = 0
            for model in model_list:
                query2 = model
                resp = kibanaObj.msearchApi(query1,query2, gte, lte, current_time)
                info = resp.json()
                hits = info["responses"][0]["hits"]["total"]
                result[model]= hits
                sum = sum+hits
            result['sum'] = sum   
            writer.writerow(result)
            print(result)
            results.append(result)
            gte = lte
    
if __name__ == '__main__':
    # kibanaObj = Kibana("llmreadonly", "mGXV5v@sxzXNe&s3", 116)
    # kibanaObj = Kibana("llm", "sensenova", 116)
    # start = "2023-09-07 18:30:00"
    # end = "2023-09-08 06:30:00"
    # search(start,end,60)

    kibanaObj = Kibana("llm", "sensenova", "https://kibana.stage.sensenova.cn", driverversion="116")
    query1 = "28c520b4-69a1-4796-ba4c-a3b133725078"
    query2 = "backends"
    gte = "2023-09-18T08:00:08.728Z"
    lte = "2023-09-19T08:00:08.728Z"
    current_time = time_utils.get_timestamp()
    resp = kibanaObj.msearchApi([query1, query2], gte, lte, current_time)
    i = 1
  

            
            

