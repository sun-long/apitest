#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hikvision.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/12/2 下午4:46   wangan      1.0         None
'''
import time

from commonlib.ui_lib.base_ui import BaseUI


class HikVision(BaseUI):
    def __init__(self, ip, username, password):
        """ 海康摄像头管理平台"""
        self.login_url = "http://%s/doc/page/config.asp" % ip
        # self.login_url = "http://www.baidu.com"
        self.login_username = username
        self.login_password = password

        super(HikVision, self).__init__()

    def login(self):
        """ 登录"""
        time.sleep(1)
        self.driver.get(self.login_url)
        self.driver.find_element_by_id("username").send_keys(self.login_username)
        self.driver.find_element_by_id("password").send_keys(self.login_password)
        self.driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(1)

    def get_select_text(self, elem_select, ):
        """ 获取select text"""
        select_value = elem_select.get_attribute('value')  # 获取Select选中的值
        options_list = elem_select.find_elements_by_tag_name('option')
        for elem_option in options_list:
            if str(elem_option.get_attribute('value')) == str(select_value):
                return str(elem_option.text)
        else:
            return None

    def collect_compressConfig_info(self):
        """ 收集config信息"""
        compressConfig = {
        }
        video_check_map = {
            "videoCode": {
                "ng-model": "oVideoParams.videoEncoding",
                "name": "视频编码",
                "map": {
                    'H.264': 'H264',
                    'H.265': 'H265',
                    'MJPEG': None,
                }
            },
            "videoFrameRate": {
                "ng-model": "oVideoParams.frameRate",
                "name": "视频帧率",
                "map": {
                    '1/16': 'R_1d16',
                    '1/8': 'R_1d8',
                    '1/4': 'R_1d4',
                    '1/2': 'R_1d2',
                    '1': 'R_1',
                    '2': 'R_2',
                    '4': 'R_4',
                    '6': 'R_6',
                    '8': 'R_8',
                    '10': 'R_10',
                    '12': 'R_12',
                    '15': 'R_15',
                    '16': 'R_16',
                    '18': 'R_18',
                    '20': 'R_20',
                    '22': 'R_22',
                    '25': 'R_25',
                }
            },
            "videoResolution": {
                "ng-model": "oVideoParams.resolution",
                "name": "分辨率",
                "map": {
                    '1280*720P': 'VR_1280_720P',
                    '1920*1080P': 'VR_1920_1080P',
                    '2560*1440': 'VR_1920_1080P',
                    '2688*1520': 'VR_2688_1520',
                    '640*480': 'VR_640_480',
                    '704*576': 'VR_704_576',
                }
            },
            "videoType": {
                "ng-model": "oVideoParams.videoType",
                "name": "视频类型",
                "map": {
                    '视频流': 'VIDEO',
                    '复合流': 'COMPLEX',
                }
            },
        }
        audio_check_map = {
            "audioCode": {
                "ng-model": "oVideoParams.videoType",
                "name": "视频编码",
            },
        }
        self.driver.find_element_by_name("videoAudio").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('li[module="video"]').click()
        elem_select = self.driver.find_element_by_css_selector('select[ng-model="oVideoParams.streamType"]')
        options_list = elem_select.find_elements_by_tag_name('option')
        stream_info = {}
        stream_dict = {
            '主码流（定时）': 'mainStream',
            '子码流': 'subStream',
            '第三码流': 'thirdStream',
        }
        for option in options_list:
            stream_name = option.text
            if stream_name not in stream_dict:
                continue
            print("Stream is: " + option.text)
            option.click()
            time.sleep(2)
            stream_info[stream_dict[stream_name]] = {}

            for key, value in video_check_map.items():
                css_selector = 'select[ng-model=\"%s\"]' % value['ng-model']

                elem_select = self.driver.find_element_by_css_selector(css_selector)
                text = self.get_select_text(elem_select)
                if text not in value['map']:
                    continue
                stream_info[stream_dict[stream_name]][key] = value['map'][text]

                # video_check_map[key]['value'] = value['map'][text]
                # options_list = elem_select.find_elements_by_tag_name('option')
                # print("Key is: " + key)
                # for indx, option in enumerate(options_list):
                #     # print("Value is: " + option.get_attribute("value"))
                #     print("Text is:" + option.text)


        i = 1




if __name__ == '__main__':
    hv = HikVision("10.4.10.15", 'admin', 'ADMIN1234')
    hv.login()
    hv.collect_compressConfig_info()