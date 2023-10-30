#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ext_info.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/11 上午10:03   wangan      1.0         None
'''
import json
import os

from pytest_check import check

from commonlib import config, utils, time_utils
from commonlib.log_utils import log


class ExtFunctionInfo(object):
    """ function级别 测试数据处理类"""

    _static_variable_dict = {}  # 全局变脸存储
    _static_variable_list = []  # 全局变脸存储

    def __init__(self):
        self.before_list = []  # 前置作业列表
        self.after_list = []  # 后置作业列表
        self.isAfterOpened = True  # 后置任务列表开关
        self.isBeforeOpened = True  # 后置任务列表开关
        self.isRequestOpened = True  # 保存postman文件开关
        self.variable_dict = {}  # 公用变量字典空间
        self.variable_list = []  # 公用变量列表空间
        self.request_list = []  # 接口执行列表

    @property
    def static_variable_dict(self):
        return ExtFunctionInfo._static_variable_dict

    @property
    def static_variable_list(self):
        return ExtFunctionInfo._static_variable_list

    def addRequest(self, inte_obj):
        self.request_list.append(inte_obj)

    def extendRequest(self, request_list):
        self.request_list.extend(request_list)

    def addAfterFunc(self, func):
        #这步是吧deletedb那个方法加入到self.after_list
        self.after_list.append(func)

    def addBeforeFunc(self, func):
        self.before_list.append(func)

    def doAfter(self):
        if not self.isAfterOpened:
            log().info('isAfterOpened is False, not do.')
            return
        log().info('start exec do after func')
        self.after_list.reverse()
        for func in self.after_list:
            try:
                func()
            except Exception as e:
                with check: assert None, 'exec After %s Failed, ERROR:%s' % (func.__name__, e)

    def doBefore(self):
        if not self.isBeforeOpened:
            log().warning('isBeforeOpened is False, not do.')
            return
        for func in self.before_list:
            try:
                func()
            except Exception as e:
                with check: assert None, 'exec Before %s Failed, ERROR:%s' % (func.__name__, e)

    def _genPmHeader(self, inte_obj):
        header_list = []
        headers = inte_obj.headers
        if not headers:
            return header_list
        for key, value in headers.items():
            header_list.append({
                "key": key,
                "value": value,
                "type": "text",
                "disabled": False

            })
        return header_list

    def _genPmPath(self, inte_obj):
        path = []
        # if getattr(inte_obj, 'prefix_path', None):
        #     path.extend(inte_obj.prefix_path.split('/'))
        # if getattr(inte_obj, 'path', None):
        #     path.extend(inte_obj.path.split('/'))
        domain = "%s://%s" % (inte_obj.origin_protocol, inte_obj.host)
        temp = inte_obj.url.split(domain)[-1]
        if temp:
            path.extend(temp.split('/'))
        path = [x for x in path if x]
        return path

    def _genPmQuery(self, inte_obj):
        query = []
        if not getattr(inte_obj, 'params', None):
            return query
        for key, value in inte_obj.params.items():
            value_list = value if isinstance(value, list) else [value]
            for v in value_list:
                query.append({
                    "key": key,
                    "value": v,
                    "disabled": False
                })
        return query

    def _genPmUrl(self, inte_obj):
        path = self._genPmPath(inte_obj)
        query = self._genPmQuery(inte_obj)
        url_info = {
            "raw": inte_obj.url_string(),
            "protocol": inte_obj.origin_protocol,
            "host": inte_obj.host.split("."),
            "path": path
        }
        if query:
            url_info.update({"query": query})
        if inte_obj.port:
            url_info.update({"port": inte_obj.port})
        return url_info

    def _genPmRaw(self, inte_obj):
        raw = None
        if getattr(inte_obj, 'body', None):
            raw = json.dumps(inte_obj.body, sort_keys=True, indent=2)
        return raw

    def _genPmBody(self, inte_obj):
        body_info = {}
        raw = self._genPmRaw(inte_obj)
        if raw:
            body_info = {
                "mode": "raw",  # TODO
                "raw": raw,
                "options": {
                    "raw": {
                        "language": "json"
                    }
                }
            }
        return body_info

    def genRequestInfo(self, inte_obj, idx=None):
        # name = inte_obj.name
        collection_title = inte_obj.collection_title
        name = inte_obj.summary
        resp_status = None
        # if collection_title:
        #     name = "%s-%s" % (collection_title, name)
        method = inte_obj.method
        header = self._genPmHeader(inte_obj)
        url = self._genPmUrl(inte_obj)
        body = self._genPmBody(inte_obj)
        req_info = {
            "name": "",
            "request": {
                "method": method,
                "url": url,
                "description": inte_obj.description
            },
            "response": []
        }
        if inte_obj.resp_obj:
            resp_status = inte_obj.resp_obj.status_code
            resp_headers = []
            for key, value in inte_obj.resp_obj.origin_resp.headers.items():
                resp_headers.append({
                    "key": key,
                    "value": value,
                })
            resp_info = {
                "name": "response",
                "originalRequest": {
                    "method": method,
                    "url": url,
                },
                "status": inte_obj.resp_obj.reason,
                "code": inte_obj.resp_obj.status_code,
                "_postman_previewlanguage": "json",
                "header": resp_headers,
                "cookie": [],
                "body": inte_obj.resp_obj.origin_resp.text
            }
            if header:
                resp_info['originalRequest'].update({"header": header})
            if body and inte_obj.method not in ['get', 'delete']:
                resp_info['originalRequest'].update({"body": body})
            req_info["response"].append(resp_info)

        if header:
            req_info['request'].update({"header": header})
        if body and inte_obj.method not in ['get', 'delete']:
            req_info['request'].update({"body": body})

        if resp_status:
            name = "[%s]%s" % (resp_status, name)
        if idx is not None:
            name = "[Step_%s]%s" % (idx + 1, name)
        req_info['name'] = name
        return req_info

    def genPostManFile(self, pm_name):
        """ 生成3级目录"""
        pm_name = "%s_%s" % (pm_name, time_utils.get_time_str())
        if not self.isRequestOpened:
            return
        pm_dict = {
            'info': {
                "_postman_id": "0d061f8e-9b09-4c06-9d2f-7162f6ab8e14",
                "name": pm_name,
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            },
            "item": [],
        }
        try:
            res = {}
            for idx, inte_obj in enumerate(self.request_list):
                level1_dir_name = inte_obj.item["swagger_file_name"]
                if level1_dir_name not in res:
                    res[level1_dir_name] = {}
                if "tags" in inte_obj.item and len(inte_obj.item["tags"]) > 0:
                    level2_dir_name = inte_obj.item["tags"][0]
                else:
                    level2_dir_name = "noTag"
                if level2_dir_name not in res[level1_dir_name]:
                    res[level1_dir_name][level2_dir_name] = []

                req_info = self.genRequestInfo(inte_obj, idx=idx)
                res[level1_dir_name][level2_dir_name].append(req_info)

            for level1_dir_name, level1_info in res.items():
                level1_item = {
                    "name": level1_dir_name,
                    "item": []
                }
                for level2_dir_name, level2_list in level1_info.items():
                    level2_item = {
                        "name": level2_dir_name,
                        "item": level2_list
                    }
                    level1_item["item"].append(level2_item)
                pm_dict['item'].append(level1_item)

            utils.write_request_file(pm_name, pm_dict)
        except Exception as e:
            log().warning('genPMFile failed1. %s' % e)
            raise

    def genPostManFileOld(self, pm_name, pm_dir=None):
        """ 单级目录"""
        pm_dict = {
            'info': {
                "_postman_id": "0d061f8e-9b09-4c06-9d2f-7162f6ab8e14",
                "name": pm_name,
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            },
            "item": [],
        }
        try:
            for idx, inte_obj in enumerate(self.request_list):
                req_info = self.genRequestInfo(inte_obj, idx=idx)
                pm_dict['item'].append(req_info)

            # utils.write_request_file(pm_name, pm_dict) # 写入到temp目录下
            if pm_dir:
                utils.write_request_file_in_result(pm_name, pm_dict, pm_dir)
        except Exception as e:
            log().warning('genPMFile failed2. %s' % e)

    def interfaceCov(self, cov_path,test_mark):
        """ 接口覆盖率统计"""
        swagger_dict = {}
        for inte_obj in self.request_list:
            swagger_dir_name = inte_obj.swagger_dir_name
            collection_name = inte_obj.collection_name
            interface_name = inte_obj.interface_name
            if swagger_dir_name not in swagger_dict:
                swagger_dict[swagger_dir_name] = {}
            if collection_name not in swagger_dict[swagger_dir_name]:
                swagger_dict[swagger_dir_name][collection_name] = {
                    "keys": [],
                    "data": {}
                }
            if interface_name not in swagger_dict[swagger_dir_name][collection_name]["keys"]:
                swagger_dict[swagger_dir_name][collection_name]["keys"].append(interface_name)
                swagger_dict[swagger_dir_name][collection_name]["data"][interface_name] = {
                    "count": 0,
                    "requests": []
                }
            swagger_dict[swagger_dir_name][collection_name]["data"][interface_name]["count"] += 1
            swagger_dict[swagger_dir_name][collection_name]["data"][interface_name]["requests"].append(inte_obj)
        # TODO 统计接口调用次数，暂时不需要
        # for swagger_dir_name, swagger_info in swagger_dict.items():
        #     for collection_name, collection_info in swagger_info.items():
        #         i = 1

        interface_dict = {}
        for swagger_name in swagger_dict.keys():
            swagger_dir = os.path.join(config.swagger_path, swagger_name)
            interface_list = self.readInterfaceList(swagger_dir,test_mark)
            interface_dict[swagger_name] = interface_list

        # 计算覆盖率
        res_list = []
        res_list.append("接口覆盖率统计:")
        for swagger_name, swagger_info in interface_dict.items():
            log().info("swagger:%s" % swagger_name)
            total_keys_count, exec_keys_count = 0, 0
            for collection_name, collection_info in swagger_info.items():
                total_keys = collection_info["keys"]
                diff_key_list = total_keys
                total_keys_count += len(total_keys)
                if swagger_name not in swagger_dict or collection_name not in swagger_dict[swagger_name]:
                    res_list.append("[%s][%s]cov:%s(%s/%s)" % (swagger_name, collection_name, 0, 0, len(total_keys)))
                else:
                    exec_keys = swagger_dict[swagger_name][collection_name]["keys"]
                    exec_keys_count += len(exec_keys)
                    # TODO 未校验执行的接口是否在所有接口中
                    res_list.append("[%s][%s]cov:%.2f%%(%s/%s)" % (swagger_name, collection_name,
                                                        len(exec_keys)/len(total_keys)*100.0,
                                                        len(exec_keys), len(total_keys)))
                    diff_key_list = [key for key in total_keys if key not in exec_keys]
                for key in diff_key_list:
                    data_info = interface_dict[swagger_name][collection_name]["data"][key]
                    res_list.append("-->[%s]%s" % (data_info["method"], data_info["path"]))
            if total_keys_count == 0:
                res_list.append("[Warning]total_keys_count is zero")
            else:
                res_list.append("Total Cov:%.2f(%s/%s)" % (exec_keys_count / total_keys_count*100.0,
                                                  exec_keys_count, total_keys_count))

        res_str = "\n".join(res_list)
        utils.write_cov_file(cov_path, res_str)

    def readInterfaceList(self, swagger_dir,test_mark):
        mark_map_file = os.path.join(swagger_dir, "mark_map.csv")
        module_list = []
        if os.path.exists(mark_map_file) and test_mark:
            mark_map_list = utils.read_csv(mark_map_file)
            for mark_map in mark_map_list:
                if mark_map[0] == test_mark:
                    module_list.append(mark_map[1])
            log().info('module_list: %s' % module_list)
                    
        interface_list_file = os.path.join(swagger_dir, "interface_list.csv")
        interface_map = {}
        if os.path.exists(interface_list_file):
            interface_list = utils.read_csv(interface_list_file)
            for info in interface_list:
                if not info:
                    continue
                if info[0].startswith("#"):
                    continue
                level1_name = info[0]

                # by wangan add os.path.exists(mark_map_file)
                if os.path.exists(mark_map_file) and test_mark and level1_name not in module_list:
                    continue

                if level1_name not in interface_map:
                    interface_map[level1_name] = {
                        "keys": [],
                        "data": {}
                    }
                level2_name = info[1]
                if level2_name not in interface_map[level1_name]:
                    interface_map[level1_name]["data"][level2_name] = {
                        "method": info[2],
                        "path": info[3]
                    }
                    interface_map[level1_name]["keys"].append(level2_name)
        return interface_map

class ParamsDict(object):
    def __init__(self, _params, lib):
        """ 参数化格式类型
            TODO add displayName
            组合可以自动组合，也可以手动组合
            支持加tag
            如果没有找到的话，取default对应的值，如果没有default　取none
        """
        self._params = _params
        self._targetVersion = None
        self._lib = lib

    @property
    def affixLib(self):
        return self._lib

    def set_targetVersion(self, version):
        self._targetVersion = version

    @staticmethod
    def normalize(affix_group):
        if not affix_group:
            return 'common'
        _group = []
        if isinstance(affix_group, list):
            for affix in affix_group:
                name_list = affix.split('_')
                if len(name_list) != 2:
                    raise Exception('词缀名称错误:%s' % affix)
                _group.append("%s%s" % (name_list[1].capitalize(), name_list[0].capitalize()))
            return "_".join(_group)

        if isinstance(affix_group, dict):
            for key, value in affix_group.items():
                if not value:
                    _group.append("%s(%s)" % (key, "common"))
                    continue
                temp_group = []
                for affix in value:
                    name_list = affix.split('_')
                    if len(name_list) != 2:
                        raise Exception('词缀名称错误:%s' % affix)
                    temp_group.append("%s%s" % (name_list[1].capitalize(), name_list[0].capitalize()))
                _group.append("%s(%s)" % (key, "_".join(temp_group)))
            return "_".join(_group)

    @staticmethod
    def genParams(affix_list, affix_lib):
        if not affix_list:
            return ParamsDict({}, affix_lib)
        if isinstance(affix_list, list):
            affix_dict = {}
            for affix in affix_list:
                k1, k2 = affix.split('_')
                for info in affix_lib[k1]:
                    if info['key'] == k2:
                        affix_info = info
                        break
                else:
                    raise Exception('Not Found affix: %s' % affix)
                affix_dict[k1] = affix_info
            return ParamsDict(affix_dict, affix_lib)

        if isinstance(affix_list, dict):
            result = {}
            for key, value in affix_list.items():
                if isinstance(value, list):
                    affix_dict = {}
                    for affix in value:
                        k1, k2 = affix.split('_')
                        for info in affix_lib[k1]:
                            if info['key'] == k2:
                                affix_info = info
                                break
                        else:
                            raise Exception('Not Found affix: %s' % affix)
                        affix_dict[k1] = affix_info
                    result[key] = ParamsDict(affix_dict, affix_lib)
                else:
                    result[key] = ParamsDict({}, affix_lib)
            return result

    def get(self, key):
        if key in self._params:
            return self._params[key]

    def get_version(self, key):
        version = None
        try:
            info = self.get(key)
            if info:
                version = info['version']
            else:
                version = self.affixLib[key][0]['version']
        except:
            pass
        return version

    def get_value(self, key, default='$$None$$'):
        value = None
        info = self.get(key)
        if info:
            value = info['value']
        elif default != '$$None$$':
            value = default
        else:
            try:
                value = self.affixLib[key][0]['value']
            except:
                pass
        return value

    def get_key(self, key):
        value = None
        info = self.get(key)
        if info:
            value = info['key']
        else:
            try:
                value = self.affixLib[key][0]['key']
            except:
                pass
        return value



    def check_version(self, key, targetVersion=None):
        """ field => cloud  target => client"""
        if not targetVersion:
            targetVersion = self._targetVersion
        fieldVersion = self.get_version(key)
        if not fieldVersion or not targetVersion:
            return True
        fieldVersion_list = fieldVersion.split('.')
        targetVersion_list = targetVersion.split('.')
        for x in range(3):
            if int(targetVersion_list[x]) == int(fieldVersion_list[x]):
                continue
            if int(targetVersion_list[x]) > int(fieldVersion_list[x]):
                return True
            if int(targetVersion_list[x]) < int(fieldVersion_list[x]):
                return False
        else:
            return True

    def skip_if_version(self):
        is_skip = False
        for key, value in self._params.items():
            if not self.check_version(key):
                is_skip = True
                log().info("[%s]version:%s, targetVersion:%s" % (key, self.get_version(key), self._targetVersion))
        return is_skip



class ParamsDictDemo(object):
    def __init__(self, _params, lib):
        """ 参数化格式类型
            TODO add displayName
            组合可以自动组合，也可以手动组合
            支持加tag
            如果没有找到的话，取default对应的值，如果没有default　取none
        """
        self._params = _params
        self._targetVersion = None
        self._lib = lib

    @property
    def affixLib(self):
        return self._lib

    def set_targetVersion(self, version):
        self._targetVersion = version

    @staticmethod
    def normalize(affix_group):
        if not affix_group:
            return 'common'
        _group = []
        if isinstance(affix_group, list):
            for affix in affix_group:
                name_list = affix.split('_')
                if len(name_list) != 2:
                    raise Exception('词缀名称错误:%s' % affix)
                _group.append("%s%s" % (name_list[1].capitalize(), name_list[0].capitalize()))
            return "_".join(_group)

        if isinstance(affix_group, dict):
            for key, value in affix_group.items():
                if not value:
                    _group.append("%s(%s)" % (key, "common"))
                    continue
                temp_group = []
                for affix in value:
                    name_list = affix.split('_')
                    if len(name_list) != 2:
                        raise Exception('词缀名称错误:%s' % affix)
                    temp_group.append("%s%s" % (name_list[1].capitalize(), name_list[0].capitalize()))
                _group.append("%s(%s)" % (key, "_".join(temp_group)))
            return "_".join(_group)

    @staticmethod
    def genParams(affix_list, affix_lib):
        if not affix_list:
            return ParamsDict({}, affix_lib)
        if isinstance(affix_list, list):
            affix_dict = {}
            for affix in affix_list:
                k1, k2 = affix.split('_')
                for info in affix_lib[k1]:
                    if info['key'] == k2:
                        affix_info = info
                        break
                else:
                    raise Exception('Not Found affix: %s' % affix)
                affix_dict[k1] = affix_info
            return ParamsDict(affix_dict, affix_lib)

        if isinstance(affix_list, dict):
            result = {}
            for key, value in affix_list.items():
                if isinstance(value, list):
                    affix_dict = {}
                    for affix in value:
                        k1, k2 = affix.split('_')
                        for info in affix_lib[k1]:
                            if info['key'] == k2:
                                affix_info = info
                                break
                        else:
                            raise Exception('Not Found affix: %s' % affix)
                        affix_dict[k1] = affix_info
                    result[key] = ParamsDict(affix_dict, affix_lib)
                else:
                    result[key] = ParamsDict({}, affix_lib)
            return result



    def get(self, key):
        if key in self._params:
            return self._params[key]

    def get_version(self, key):
        version = None
        try:
            info = self.get(key)
            if info:
                version = info['version']
            else:
                version = self.affixLib[key][0]['version']
        except:
            pass
        return version

    def get_value(self, key, default='$$None$$'):
        value = None
        info = self.get(key)
        if info:
            value = info['value']
        elif default != '$$None$$':
            value = default
        else:
            try:
                value = self.affixLib[key][0]['value']
            except:
                pass
        return value

    def check_version(self, key, targetVersion=None):
        """ field => cloud  target => client"""
        if not targetVersion:
            targetVersion = self._targetVersion
        fieldVersion = self.get_version(key)
        if not fieldVersion or not targetVersion:
            return True
        fieldVersion_list = fieldVersion.split('.')
        targetVersion_list = targetVersion.split('.')
        for x in range(3):
            if int(targetVersion_list[x]) == int(fieldVersion_list[x]):
                continue
            if int(targetVersion_list[x]) > int(fieldVersion_list[x]):
                return True
            if int(targetVersion_list[x]) < int(fieldVersion_list[x]):
                return False
        else:
            return True

    def skip_if_version(self):
        is_skip = False
        for key, value in self._params.items():
            if not self.check_version(key):
                is_skip = True
                log().info("[%s]version:%s, targetVersion:%s" % (key, self.get_version(key), self._targetVersion))
        return is_skip

