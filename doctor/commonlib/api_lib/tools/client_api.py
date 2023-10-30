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
from commonlib.api_lib.client.task import ClientTask

from commonlib.log_utils import log
from core.pm_utils import load_postman
collections = load_postman("argus/console/")


class ClientApi(object):
    """ 端api调用"""

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

    def get_value(self, key, data, global_data=None, default=None):
        """ 从yaml文件中获取指定key的值"""
        if key in data:
            return data[key]
        if global_data and key in global_data:
            return global_data[key]
        return default

    def client_doing(self, yaml_path):
        """　端操作"""
        action_support_list = ['ClearTask', 'CreateTask', 'SetDNS', 'BindStore']
        result = utils.read_post_data_yaml(yaml_path)
        if self.config_obj:
            result = collections.format_conf_variables(self.config_obj, result)

        result = utils.dict_to_object(result)
        process_list = result['Process']
        client_dict = result['Clients']
        subdevice_dict = result['SubDevices']
        global_dict = result['Global']
        capability_dict = result['Capability']
        appCapability_dict = result['AppCapability']
        for p in process_list:
            action_name = p['action'].strip()
            if action_name not in action_support_list:
                log().info('action:%s暂不支持.skip该步骤' % p['action'])
                continue
            clients = self.get_value('client', p, global_data=global_dict)
            client_list = []
            if clients:
                client_list = [x.strip() for x in clients.split(',') if x and x.strip() in client_dict]
                if len(client_list) == 0:
                    log().info('client_name可能填写有误或不存在：%s' % p['client'])
                    continue

            if action_name == 'ClearTask':
                for client_name in client_list:
                    client_info = client_dict[client_name]
                    clientApi = ClientTask(self.config_obj.Clients.Service, client_info=client_info)
                    clientApi.destroy_all_task()

            if action_name == 'CreateTask':
                for client_name in client_list:
                    client_info = client_dict[client_name]
                    clientApi = ClientTask(self.config_obj.Clients.Service, client_info=client_info)

                    task_type = self.get_value('task_type', p, global_data=global_dict, default='None').strip()
                    if task_type not in ['RTSP', 'FILE', 'DLC']:
                        log().info('task_type:%s暂不支持.skip该步骤' % p['task_type'])
                        continue

                    task_title = None
                    if 'task_title' in p and p['task_title']:
                        task_title = p['task_title'].strip()

                    capability_list, appCapability_list = [], []
                    capability = self.get_value('capability', p, global_data=global_dict)
                    if capability:
                        capability_list = [capability_dict[x.strip()] for x in capability.split(',') if x and x.strip() in capability_dict]

                    appCapability = self.get_value('appCapability', p, global_data=global_dict)
                    if appCapability:
                        appCapability_list = [appCapability_dict[x.strip()] for x in appCapability.split(',') if x and x.strip() in appCapability_dict]

                    if task_type == 'RTSP':
                        camera = self.get_value('camera', p, global_data=global_dict, default='None').strip()
                        if camera not in subdevice_dict:
                            log().info('camera:%s暂不支持.skip该步骤' % p)
                            continue
                        camera_info = subdevice_dict[camera]
                        task_id = clientApi.createTask(camera_info, camera_name=task_title, capability=capability_list,
                                                       application_capability=appCapability_list)
                    elif task_type == 'FILE':
                        file_path = self.get_value('file_path', p, global_data=global_dict)

                        task_id = clientApi.createFileTask(file_path, camera_name=task_title, capability=capability_list,
                                                           application_capability=appCapability_list)
                    elif task_type == 'DLC':
                        log().info('暂时不支持')
                        continue
                    else:
                        raise Exception('task_type error:%s' % task_type)

                    if task_id:
                        status = self.get_value('status', p, global_data=global_dict, default='stop').strip()
                        if status == 'run':
                            clientApi.start_task(task_id)
                            time_utils.sleep(5)

            if action_name == 'SetDns':
                for client_name in client_list:
                    client_info = client_dict[client_name]
                    clientApi = ClientTask(self.config_obj.Clients.Service, client_info=client_info)

                    dns1 = self.get_value('dns1', p, global_data=global_dict, default='10.4.192.27').strip()
                    dns2 = self.get_value('dns2', p, global_data=global_dict, default='10.8.8.8').strip()
                    clientApi.set_dns([
                        {"address": dns1},
                        {"address": dns2},
                    ])
                    clientApi.cmd_restart_all_service()

            if action_name == 'BindStore':
                store_id = self.get_value('store_id', p, global_data=global_dict, default=None).strip()
                if not store_id:
                    log().info('store_id:%s暂不支持.skip该步骤' % p)
                    continue
                store_id_list = [x.strip() for x in store_id.split(',') if x and x.strip()]

                for idx, client_name in enumerate(client_list):
                    client_info = client_dict[client_name]
                    clientApi = ClientTask(self.config_obj.Clients.Service, client_info=client_info)

                    resp = clientApi.status()
                    device_id = resp.json_get('info.device_id')

                    if idx < len(store_id_list):
                        store_id = store_id_list[idx]
                    else:
                        store_id = store_id_list[-1]
                    resp = clientApi.bind_store(device_id, store_id)
                    assert resp.status_code == 200



if __name__ == '__main__':
    ca = ClientApi()
    ca.set_config_obj_by_type('dev')
    ca.client_doing('task_demo')