#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   client_tool.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/2/26 下午4:49   wangan      1.0         None
'''
import os

from commonlib import cmd_utils
from commonlib.ui_lib.devcenter import DevCenter


class ClientTool(object):
    """ 客户端操作工具"""

    def __init__(self, dc_name, dc_pwd):
        """ init """
        self.dc_obj = None
        self.init_dc_obj(dc_name, dc_pwd)

    def init_dc_obj(self, dc_name, dc_pwd):
        self.dc_obj = DevCenter(dc_name, dc_pwd)

    def download_package(self, uuid, target_dir=None):
        """ 下载安装包"""
        download_path = self.dc_obj.downloadApi(uuid, target_dir)
        print('download success.path:%s' % download_path)
        return download_path

    def get_build_commit(self, release_name):
        """获取commit"""
        info = self.dc_obj.referenceApi()
        branch_list = info['branches']
        for branch_dict in branch_list:
            if release_name == branch_dict['name']:
                return branch_dict['cid']
        return None

    def build_package(self, branch_name, config_name, platform='linux', description=None):
        reference_info = self.dc_obj.referenceApi()
        branches = reference_info["branches"]
        for branch_info in branches:
            if branch_info['name'] == branch_name:
                target_branch = branch_info
                break
        else:
            raise Exception('未找到指定branch.%s' % branch_name)
        commit_id = target_branch['cid']
        info = self.dc_obj.commitApi(commit_id)
        build_info = info['branches'][0]
        print('Commit:%s' % build_info['cid'])
        print('Author:%s' % build_info['author'])
        print('Message:%s' % build_info['message']['title'])
        config_dict = build_info['autorelease_config']['config']
        if config_name not in config_dict:
            raise Exception('未找到指定config.%s' % config_name)
        if not description:
            raise Exception('未添加描述信息')
        data = {
            'branch': branch_name,
            'cid': build_info['cid'],
            'config': config_name,
            'platform': 'linux',
            'description': description,
        }
        self.dc_obj.buildApi(data)

    def config_list(self, branch_name):
        reference_info = self.dc_obj.referenceApi()
        branches = reference_info["branches"]
        for branch_info in branches:
            if branch_info['name'] == branch_name:
                target_branch = branch_info
                break
        else:
            raise Exception('未找到指定branch.%s' % branch_name)
        commit_id = target_branch['cid']
        info = self.dc_obj.commitApi(commit_id)
        build_info = info['branches'][0]
        print('Commit:%s' % build_info['cid'])
        print('Author:%s' % build_info['author'])
        print('Message:%s' % build_info['message']['title'])
        config_dict = build_info['autorelease_config']['config']
        return config_dict

    def branch_list(self):
        reference_info = self.dc_obj.referenceApi()
        branches = reference_info["branches"]
        return branches

    def init_device(self, version, ip, port, username, password):
        if username == 'root':
            client_root_dir = '/root/emmc'
        elif username == 'sensetime':
            client_root_dir = '/home/sensetime'
        else:
            raise Exception('端username error:%s' % username)
        cmd = 'cd %s;rm -rf *%s*;rm -rf sensego' % (client_root_dir, version)
        ret, output, err = cmd_utils.ssh_cmd(cmd, ip, port=port, username=username, password=password)
        print('[OK]%s' % cmd)
        cmd = 'sv stop /etc/service/*'
        ret, output, err = cmd_utils.ssh_cmd(cmd, ip, port=port, username=username, password=password)
        print('[OK]%s' % cmd)
        cmd = 'supervisorctl stop all'
        ret, output, err = cmd_utils.ssh_cmd(cmd, ip, port=port, username=username, password=password)
        print('[OK]%s' % cmd)
        print('[OK]client init finish.')

    def build_results(self, project_name='365_SenseGoEdgeCube', last_count=20):
        result_list = self.dc_obj.buildResults(project_name)
        result_list.reverse()
        result_list = result_list[:last_count]
        build_info_list = []
        for result in result_list:
            res = self.dc_obj.buildReport(result['report_link'])
            build_info_list.append(res)
        return build_info_list

    def deploy_product(self, download_path, ip, port, username, password):
        if username == 'root':
            client_root_dir = '/root/emmc'
        elif username == 'sensetime':
            client_root_dir = '/home/sensetime'
        else:
            raise Exception('端username error:%s' % username)
        file_name = download_path.split('/')[-1]
        target_path = os.path.join(client_root_dir, file_name)
        cmd_utils.scp_dir(download_path, target_path, ip, port, username, password)
        cmd = 'cd %s;tar -zxvf %s' % (client_root_dir, file_name)
        ret, output, err = cmd_utils.ssh_cmd(cmd, ip, port=port, username=username, password=password)
        print('[OK]%s' % cmd)

        install_dir = os.path.join(client_root_dir, output.decode().split('\n')[0].split('/')[0])

        # if username == 'root':
        #     cmd = 'cd %s;./install_all.sh &' % install_dir
        # elif username == 'sensetime':
        #     cmd = 'cd %s;echo %s|sudo -S ./install_all.sh &' % (install_dir, password)
        # else:
        #     raise Exception('端username error:%s' % username)
        # ret, output, err = cmd_utils.ssh_cmd(cmd, ip, port=port, username=username, password=password)
        # print('[OK]%s' % cmd)

        i = 1

if __name__ == '__main__':
    dc_name ='wangan'
    dc_pwd = 'liuting0216#'
    ct = ClientTool(dc_name, dc_pwd)
    # ct.build_package('release/5.1.2', 'SenseRealty_x86_icloud')
    ct.build_results()
    # version = '5.1.2'
    # ip = '10.4.10.29'
    # port = 22
    # username = 'root'
    # password = 'T2mksense1'
    # uuid = '60d454a27c6d4a02ab9c80be19faef65'

    # ip = '10.4.10.40'
    # port = 22
    # username = 'root'
    # password = 'T2mksense1'
    # uuid = 'd866d3ce68aa4e0db2dcc0c96dd2beea'

    # ip = '10.4.10.69'
    # port = 22
    # username = 'root'
    # password = 'T2mksense1'
    # uuid = 'd866d3ce68aa4e0db2dcc0c96dd2beea'
    #
    # ct.init_device(version, ip, port, username, password)
    # download_path = ct.download_package(uuid)
    # ct.deploy_product(download_path,  ip, port, username, password)