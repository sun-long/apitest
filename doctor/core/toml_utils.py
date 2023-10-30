#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   toml_utils.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/30 下午2:42   wangan      1.0         toml文件解析工具
'''
import os
import types

import toml

from commonlib.config import project_path
from commonlib.log_utils import log


def gen_config_obj(config_path):
    if config_path.startswith("/"):
        config_path = config_path
    else:
        config_path = os.path.join(project_path, "conf/%s.toml" % config_path)
    return gen_toml_object(toml.load(config_path))

def gen_extra_config_obj(config_path, extra_name):
    if config_path.startswith("/"):
        config_path = config_path
    else:
        config_path = os.path.join(project_path, "conf/%s/%s.toml" % (extra_name, config_path))
    return gen_toml_object(toml.load(config_path))


class Dict(dict):
    # # self.属性写入 等价于调用dict.__setitem__
    __setattr__ = dict.__setitem__
    # # self.属性读取 等价于调用dict.__setitem__
    __getattribute__ = dict.__getitem__

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    # # 等价于__setattr__ = dict.__setitem__
    # def __setattr__(self, key, value):
    #     dict.__setitem__(self, key, value)
    #
    # # 等价于__getattribute__ = dict.__getitem__ 或 __getattr__ = dict.__getitem__
    # def __getattribute__(self, item):
    #     return dict.__getitem__(self, item)


def gen_toml_object(dictObj, key_list=None, origin_inst=None):
    obj = dict_to_object(dictObj, key_list=key_list, origin_inst=origin_inst)
    def get(self, filed_link):
        info = eval('self.%s' % filed_link)
        log().info("[ConfigInfo]%s => %s" % (filed_link, info))
        if isinstance(info, dict):
            info["key"] = filed_link  # 添加键名
        return info
    obj.get = types.MethodType(get, obj)
    return obj


# 递归把dict转换成obj对象【兼容obj.属性和obj[属性]】
def dict_to_object(dictObj, key_list=None, origin_inst=None):
    if not isinstance(dictObj, dict):
        if origin_inst:
            origin_inst['_ext'][".".join(key_list)] = dictObj
        return dictObj
    inst = Dict()
    if not key_list:
        inst['_ext'] = {}
        inst['_extra'] = Dict()
        inst['_extra']['_keys'] = []
        key_list = []
        origin_inst = inst
    inst['_keys'] = []
    for k, v in dictObj.items():
        key_list.append(k)
        inst[k] = dict_to_object(v, key_list=key_list, origin_inst=origin_inst)
        if k == 'ConfigExtra':
            for extra_key in inst[k]["_keys"]:
                _list = inst[k][extra_key]
                if not _list:
                    continue
                origin_inst['_extra'][extra_key] = Dict()
                origin_inst['_extra'][extra_key]['_keys'] = []
                origin_inst['_extra']['_keys'].append(extra_key)
                for name in _list:
                    origin_inst['_extra'][extra_key][name] = gen_extra_config_obj(name, extra_key)
                    origin_inst['_extra'][extra_key]['_keys'].append(name)
        key_list.pop()
        inst['_keys'].append(k)

    return inst
