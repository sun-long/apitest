#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   post_data.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/1/19 上午9:43   wangan      1.0         None
'''
import os
import time

import toml

from commonlib import utils, config, time_utils, sign_utils

from commonlib.log_utils import log
from core.pm_utils import load_postman
from commonlib.api_lib.argus.landfill import LandFill
from commonlib.api_lib.argus.dbproxy import DbProxyApi
collections = load_postman("argus/console/")


class PostDataTool(object):
    """ 端推送数据工具"""

    def __init__(self, config_obj=None):
        self.config_obj = config_obj

    def set_config_obj_by_type(self, config_type):
        """ 根据配置名称，设置配置对象"""
        if config_type.startswith("/"):
            config_path = config_type
        else:
            config_path = os.path.join(config.project_path, "conf/%s.toml" % config_type)
        self.config_obj = utils.dict_to_object(toml.load(config_path))

    def set_config_obj(self, config_obj):
        """ 设置配置对象"""
        self.config_obj = config_obj

    def get_value(self, key, data, default=None):
        """ 从yaml文件中获取指定key的值"""
        if key not in data or not data[key]:
            return default
        else:
            return data[key]

    def post_data_from_yaml(self, yaml_path, ak=None, sk=None, host=None, device_id=None, static_id=None, stream_id=None):
        """ 推送数据"""
        support_type = ['face', 'body', 'facebody', 'static',
                        'facev2', 'bodyv2', 'facebodyv2', 'staticsmall']
        result = utils.read_post_data_yaml(yaml_path)
        if self.config_obj:
            result = collections.format_conf_variables(self.config_obj, result)

        info = result["info"]
        data = result["data"] if "data" in result else None
        env = info["default"]

        reason_list = []

        if not host:
            host = env["service"]
        if not ak:
            ak = env["ak"]
        if not sk:
            sk = env["sk"] if "sk" in env else None
        if not device_id:
            device_id = env["device_id"] if "device_id" in env else None

        db_proxy_service = host
        if 'db_proxy_service' in env:
            db_proxy_service = env['db_proxy_service']

        db_proxy_ak = ak
        if 'db_proxy_ak' in env:
            db_proxy_ak = env['db_proxy_ak']

        domain_service = host
        if 'domain_service' in env:
            domain_service = env['domain_service']

        domain_ak = ak
        if 'domain_ak' in env:
            domain_ak = env['domain_ak']


        landfill = LandFill(host, ak, sk, config_obj=self.config_obj)

        # 创建静态库
        if static_id:
            pass
        elif 'static_id' in env:
            static_id = env['static_id']
        else:
            dbapi = DbProxyApi(db_proxy_service, db_proxy_ak)
            static_name = 'static_%s' % time_utils.get_now_timestamp()
            resp = dbapi.AddStaticGroup(static_name)
            static_id = resp.resp_json['group_id']
            time.sleep(1)
        # 创建动态库
        if stream_id:
            pass
        elif 'stream_id' in env:
            stream_id = env['stream_id']
        else:
            group_id_list = []
            for x in range(20):
                dbapi = DbProxyApi(db_proxy_service, db_proxy_ak)
                stream_name = 'stream_%s_%s' % (time_utils.get_now_timestamp(), x)
                callback_dict = None
                if 'callback' in env:
                    callback_dict = env['callback']
                # callback_dict = {'pedes_cb_url': 'http://echo.argus-staging:8080'}
                resp = dbapi.AddStreamGroup(stream_name, [static_id], callback_dict=callback_dict)
                stream_id = resp.resp_json['group_id']
                group_id_list.append(stream_id)
            log().info('group_id_list:%s' % group_id_list)
            time.sleep(60)
        log().info('static_id=%s' % static_id)
        log().info('stream_id=%s' % stream_id)

        # 绑定动态库
        if device_id:
            landfill_t = LandFill(domain_service, domain_ak, sk, config_obj=self.config_obj)
            resp = landfill_t.bind_deviceId(device_id, stream_id, stream_id)
            if resp.status_code == 200:
                log().info("绑定device id成功")
            else:
                raise Exception('绑定device_id失败')
        if not data:
            log().info('finish.exit')
            return
        for d in data:
            if 'type' not in d or d['type'].lower() not in support_type:
                reason_list.append('type error.')
                continue
            post_type = d['type'].lower()

            if 'path' not in d or not d['path']:
                reason_list.append('path is null')
                continue

            if 'timestamp' not in d or not d['timestamp']:
                ts = time_utils.get_now_timestamp()
            else:
                ts = time_utils.get_timestamp(d['timestamp'])
            desc = self.get_value('desc', d, default='no desc')
            delay = self.get_value('delay', d, default=1)

            if 'bg_image_upload' not in d or not d['bg_image_upload'] or d['bg_image_upload'] in [0, 'false', 'False']:
                bg_image_upload = False
            else:
                bg_image_upload = True

            if post_type == 'face':
                resp = landfill.Pedestrian_face(stream_id, d['path'], ts, desc=desc)
                if resp.status_code == 200 and 'request_id' in resp.json:
                    reason_list.append("post success.request_id=%s" % resp.json["request_id"])
                else:
                    reason_list.append('post failed. %s' % d['path'])
            elif post_type == 'body':
                resp = landfill.Pedestrian_body(stream_id, d['path'], ts, desc=desc)
                if resp.status_code == 200 and 'request_id' in resp.json:
                    reason_list.append("post success.request_id=%s" % resp.json["request_id"])
                else:
                    reason_list.append('post failed. %s' % d['path'])
            elif post_type == 'static':
                if 'pid' not in d or not d['pid']:
                    # pid = sign_utils.getUuid(32)
                    pid = None
                else:
                    pid = d['pid']
                if 'override' in d and d['override'] is True:
                    override = "1"
                else:
                    override = None
                dbapi = DbProxyApi(db_proxy_service, db_proxy_ak)
                resp = dbapi.AddPerson(d['path'], static_id, pid, desc=desc, override=override)
                if resp.status_code == 200 and 'request_id' in resp.json:
                    reason_list.append("post success.request_id=%s" % resp.json["request_id"])
                else:
                    reason_list.append('post failed. %s' % d['path'])
            elif post_type == 'staticsmall':
                """ 动态库的静态小库推送"""
                if 'pid' not in d or not d['pid']:
                    # pid = sign_utils.getUuid(32)
                    pid = None
                else:
                    pid = d['pid']
                dbapi = DbProxyApi(db_proxy_service, db_proxy_ak)
                resp = dbapi.AddPerson(d['path'], stream_id, pid, desc=desc)
                if resp.status_code == 200 and 'request_id' in resp.json:
                    reason_list.append("post success.request_id=%s" % resp.json["request_id"])
                else:
                    reason_list.append('post failed. %s' % d['path'])
            elif post_type == 'facev2':
                resp = landfill.Pedestrian_face_v2(d['path'], ts, device_id=device_id, desc=desc,
                                                   bg_image_upload=bg_image_upload)
                if resp.status_code == 200 and 'request_id' in resp.json:
                    reason_list.append("post success.request_id=%s" % resp.json["request_id"])
                else:
                    reason_list.append('post failed. %s' % d['path'])
            elif post_type == 'bodyv2':
                resp = landfill.Pedestrian_body_v2(d['path'], ts, device_id=device_id, desc=desc,
                                                   bg_image_upload=bg_image_upload)
                if resp.status_code == 200 and 'request_id' in resp.json:
                    reason_list.append("post success.request_id=%s" % resp.json["request_id"])
                else:
                    reason_list.append('post failed. %s' % d['path'])
            elif post_type == 'facebodyv2':
                resp = landfill.Pedestrian_facebody_v2(d['path'], ts, device_id=device_id, desc=desc,
                                                   bg_image_upload=bg_image_upload)
                if resp.status_code == 200 and 'request_id' in resp.json:
                    reason_list.append("post success.request_id=%s" % resp.json["request_id"])
                else:
                    reason_list.append('post failed. %s' % d['path'])
            time.sleep(delay)
        log().info('reason list：')
        for reason in reason_list:
            log().info('%s' % reason)

if __name__ == '__main__':
    pdt = PostDataTool()
    pdt.set_config_obj_by_type('dev')
    pdt.post_data_from_yaml('nosaveimg')