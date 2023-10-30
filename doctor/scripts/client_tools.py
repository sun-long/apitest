#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   grpc_tools.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/12/17 下午6:10   wangan      1.0         None
'''
from commonlib.api_lib.tools.client_tool import ClientTool
from commonlib.utils import dectry

dc_name = 'wangan'
dc_pwd = dectry('208_211_230_153_158_209_220_83_95_155_155_149_')

def download_package(uuid=None, target_dir=None):
    """ 生成message数据包
    :param uuid:
    :return:
    """
    ct = ClientTool(dc_name, dc_pwd)
    download_path = ct.download_package(uuid, target_dir)
    print("success.path:%s" % download_path)


def deploy_product(uuid=None, version=None, download_path=None, ip=None, port=None, username=None, password=None):
    ct = ClientTool(dc_name, dc_pwd)
    if not download_path:
        download_path = ct.download_package(uuid)
        print("success.path:%s" % download_path)
    port = int(port)
    ct.init_device(version, ip, port, username, password)
    ct.deploy_product(download_path,  ip, port, username, password)


def build_package(branch_name=None, config_name=None, description=None):
    ct = ClientTool(dc_name, dc_pwd)
    ct.build_package(branch_name, config_name, platform='linux', description=description)
    print('build_package,please wait finish.')


def config_list(branch_name=None):
    ct = ClientTool(dc_name, dc_pwd)
    config_dict = ct.config_list(branch_name)
    print('-' * 50)
    for name in config_dict.keys():
        print(name)

def branch_list(desc=None):
    ct = ClientTool(dc_name, dc_pwd)
    branches = ct.branch_list()
    print('-' * 50)
    for branch_info in branches:
        print("%s->%s" % (branch_info['name'], branch_info['cid']))


def batch_build_package(branch_name=None, env_type=None, update=None, description=None, test=None):
    env_type_all = ['staging', 'icloud']
    desc_dict = {
        'SenseRealty_x86': '地产-X86',
        'SenseRealtyDlc_x86': '地产-CPU',
        'SenseRealty_3559a': '地产-EC',
        'SenseSpace_3559a': '社区-EC',
        'SenseGo_3559a': '零售-EC',
    }
    if update:
        if update != 'update':
            raise Exception('update参数填写update是升级包' % update)

    if env_type not in env_type_all:
        raise Exception('env_type必须在%s中' % env_type)
    ct = ClientTool(dc_name, dc_pwd)
    config_dict = ct.config_list(branch_name)
    build_list = []
    for key in config_dict.keys():
        if env_type not in key:
            continue
        if update == "update" and update in key:
            build_list.append(key)
        elif not update and "update" not in key:
            build_list.append(key)

    for config_name in build_list:
        desc_name = "_".join(config_name.split('_')[:2])
        desc_str = "%s-%s" % (desc_dict[desc_name], env_type)
        if update == "update":
            desc_str = "%s-升级包" % desc_str
        if description:
            desc_str = "%s-%s" % (desc_str, description)
        if test:
            print('test:%s. desc=%s' % (config_name, desc_str))
        else:
            ct = ClientTool(dc_name, dc_pwd)
            ct.build_package(branch_name, config_name, platform='linux', description=desc_str)
            print('build_package %s success,please wait finish. desc=%s' % (config_name, desc_str))


def build_result(project_name=None, last_count=None):
    if not project_name:
        project_name = '365_SenseGoEdgeCube'
    ct = ClientTool(dc_name, dc_pwd)
    build_info_list = ct.build_results(project_name=project_name, last_count=int(last_count))
    for info in build_info_list:
        task = info['task']
        print('[%s]uuid:%s\n(%s)\n(%s)\n(%s)\n ' % (task['status'], task['uuid'], task['description'], task['payload']['options']['description'], task['created_at']))

if __name__ == '__main__':
    pass