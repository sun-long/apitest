#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gen_postman.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/9/3 下午1:58   wangan      1.0         None
'''
import json
import os
import shutil
import sys

from commonlib import config, utils, sign_utils, time_utils, cmd_utils
from commonlib.log_utils import log
from commonlib.ui_lib.confluence import Confluence
from commonlib.ui_lib.gitlab import GitLab
from core.ext_info import ExtFunctionInfo
from core.swagger_utils import load_swagger


class GenPostManTool(object):
    def __init__(self, host=None):
        self.host = host

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """

        if self.host:
            host = self.host
            try:
                if isinstance(host, dict):
                    host = host[inte_obj.swagger_file]
                    if isinstance(host, dict):
                        tag = inte_obj.item["tags"][0]
                        if tag not in host and "all" in host:
                            host = host["all"]["host"] + host["all"]["prefix"]
                        elif tag in host:
                            host = host[tag]["host"] + host[tag]["prefix"]
                        else:
                            host = "http://invalid_host/"
                else:
                    host = json.loads(self.host)[inte_obj.swagger_file]
            except:
                pass
                # raise
            inte_obj.set_host(host)
        # inte_obj.set_headers('Authorization', "Bearer {{token}}")

    def readHostMap(self, swagger_dir):
        host_map_file = os.path.join(swagger_dir, "host_map.csv")
        host_map = {}
        if os.path.exists(host_map_file):
            host_map_list = utils.read_csv(host_map_file)
            for info in host_map_list:
                if not info:
                    continue
                if info[0].startswith("#"):
                    continue
                level1_name = info[0]
                if level1_name not in host_map:
                    host_map[level1_name] = {}
                level2_name = info[1]
                if level2_name not in host_map[level1_name]:
                    host_map[level1_name][level2_name] = {
                        "host": info[2],
                        "prefix": info[3] if len(info) > 3 else ""
                    }
        return host_map

    def genSwagger(self, name, swagger_dir, file=None):
        swagger_dir = os.path.join(config.swagger_path, swagger_dir)
        self.host = self.readHostMap(swagger_dir)
        ef = ExtFunctionInfo()
        ef.isRequestOpened = True
        collections = load_swagger(swagger_dir)
        collections.init(self, ext_info=ef)

        interface_list = []
        for srv_name, srvInfo in collections.items.items():
            for method_name, methodInfo in srvInfo.items():
                interface_list.append((srv_name, method_name))
                summary = methodInfo["summary"] if "summary" in methodInfo else ""
                summary = summary.replace("\n", " ")
                print("%s|%s|%s|%s|%s|%s" % (srv_name, method_name.split("_")[0], method_name.split("_")[-1], methodInfo["method"], summary, methodInfo["path"]))

        for srv_name, method_name in interface_list:
            intef = collections.interface(srv_name, method_name)
            intef.set_headers("authorization", "Bearer {{token}}")
            # intef.set_headers("X-Belt-Action", "action_name")
            # intef.set_headers("X-Belt-Version", "v1")
            # intef.set_headers("X-Belt-Token", "{{userToken}}")
            # intef.set_headers("X-Belt-Signature", "{{akToken}}")
            if getattr(intef, 'request', None):
                ef.addRequest(intef)  # 将接口放到请求队列中
                # resp = intef.request()

        ef.genPostManFile(name)

    def listSwaggerPath(self, swagger_dir, name_list=None):
        swagger_dir = os.path.join(config.swagger_path, swagger_dir)
        self.host = self.readHostMap(swagger_dir)
        ef = ExtFunctionInfo()
        ef.isRequestOpened = True
        collections = load_swagger(swagger_dir)
        collections.init(self, ext_info=ef)

        if name_list and isinstance(name_list, str):
            name_list = [name_list]

        print("\nList:")
        for srv_name, srvInfo in collections.items.items():
            if name_list and srv_name not in name_list:
                continue
            print("")
            for method_name, methodInfo in srvInfo.items():
                # print("[%s]%s" % (methodInfo["method"], methodInfo["path"]))
                print("%s,%s,%s,%s" % (srv_name, method_name, methodInfo["method"], methodInfo["path"]))

    def updateRemoteSwagger(self, swagger_dir, driverversion=None, swagger_file=None, username=None, password=None):
        """ 更新远程swagger"""
        swagger_dir = os.path.join(config.swagger_path, swagger_dir)
        remote_swagger_file = os.path.join(swagger_dir, "remote_swagger.csv")
        if not os.path.exists(remote_swagger_file):
            print("%s Not Found. exit!")
            sys.exit(0)

        remote_list = utils.read_csv(remote_swagger_file)
        gh,bj_gh, cf = None, None, None
        for line in remote_list:
            if not line :
                continue
            if line[0].strip().startswith("#"):
                continue
            name = line[0]
            if swagger_file and swagger_file != name:
                continue
            url = line[1]
            origin_path = os.path.join(swagger_dir, "%s.json" % name)
            cookie_path = os.path.join(swagger_dir, "cookie")
            old_exist = False
            if os.path.exists(origin_path):
                old_exist = True
            cookie = None
            if os.path.exists(cookie_path):
                with open(cookie_path, "r") as f:
                    cookie = f.read()
            import platform
            plat = platform.system().lower()
            if plat == 'windows':
                temp_path = "d:/temp/%s.json" % name
            else:
                temp_path = "/tmp/%s.json" % name

            if 'gitlab.sz' in url:
                if not gh:
                    gh = GitLab(username, password, driverversion)
                gh.downloadApi(url, save_path=temp_path)
            elif 'gitlab.bj' in url:
                if not bj_gh:
                    bj_gh = GitLab(username, password, driverversion, zone="bj")
                bj_gh.downloadApi(url, save_path=temp_path)
            elif 'confluence' in url:
                if not cf:
                    cf = Confluence(username,
                                    password,
                                    driverversion)
                cf.downloadApi(url, save_path=temp_path)
            else:
                utils.download_file(url, temp_path, cookie=cookie)
            try:
                data = utils.read_temp_json(temp_path)
            except:
                print("Error read %s" % temp_path)
                raise
            if "openapi" in data and data["openapi"].startswith('3'):
                temp_version2_path = "/tmp/%s_v2.json" % name
                cmd_utils.exec_cmd("api-spec-converter --from=openapi_3 --to=swagger_2 --syntax=json %s > %s" % (temp_path, temp_version2_path))
                temp_path = temp_version2_path
                # TODO
            new_md5 = sign_utils.getMd5ByFile(temp_path)
            if old_exist:
                old_md5 = sign_utils.getMd5ByFile(origin_path)
                if old_md5 == new_md5:
                    print("%s:md5一致,没有更新.SKIP" % name)
                    continue
                else:
                    bak_dir = os.path.join(swagger_dir, "bak")
                    if not os.path.exists(bak_dir):
                        os.makedirs(bak_dir)
                    bak_path = os.path.join(bak_dir, "%s.json_bak_%s" % (name, time_utils.get_time_str()))
                    shutil.move(origin_path, bak_path)
                    print("%s:md5不一致,有新的更新.备份现有文件到%s" % (name, bak_path))
            else:
                print("%s:本地文件不存在,等待更新." % name)
            shutil.move(temp_path, origin_path)
            print("%s:更新成功." % name)

if __name__ == '__main__':
    # GenPostManTool("http://{{host}}").genSwagger("nebula", "nebula_ap")
    # GenPostManTool().updateRemoteSwagger("belt")
    GenPostManTool().listSwaggerPath("belt")
