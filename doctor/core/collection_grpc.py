#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   collection.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/26 上午9:48   wangan      1.0         测试集合类
'''
import datetime
import json
import os
import re

from google.protobuf import json_format

from commonlib import config
from commonlib.config import project_path, grpc_req_path
from commonlib.log_utils import log
from core import interface_grpc


class CollectionsGrpc(object):
    """ 测试接口集合"""
    def __init__(self, items, pb2_module, pb2_grpc_module, var_items, _dir):
        """ grpc 测试集"""
        self.collection_name = _dir.split("/")[-1]
        self.origin_items = items
        self.origin_var_items = var_items
        self.pb2_module = pb2_module
        self.pb2_grpc_module = pb2_grpc_module
        self.items = self._gen_items()
        self.var_items = self._gen_var_items()
        self._test_obj = None  # 测试对象
        self._custom_func_name = None  # 自定义方法名称
        self._conf = None  # 配置文件集合，用于填充配置

    def init(self, test_obj, custom_func_name=None, conf=None, ext_info=None):
        self._test_obj = test_obj
        self._custom_func_name = custom_func_name
        self._conf = conf
        self._ext_info = ext_info

    @classmethod
    def travel_message(cls, fields, out, default_enum_type=False, default_list_num=1):
        """ 生成dict结构"""
        for field in fields:
            name = field.name
            if hasattr(field, 'message_type') and field.message_type:
                if isinstance(field.default_value, list):
                    out[name] = []
                    for x in range(default_list_num):
                        temp = {}
                        cls.travel_message(field.message_type.fields, temp, default_enum_type, default_list_num)
                        out[name].append(temp)
                else:
                    out[name] = {}
                    cls.travel_message(field.message_type.fields, out[name], default_enum_type, default_list_num)
                    # 打开注释， 即可生成http接口的json
                    # if "value" in out[name] and len(out[name].keys()) == 1:
                    #     out[name] = out[name]["value"]
            else:
                if hasattr(field, 'enum_type') and field.enum_type:
                    values = [_type.name for _type in field.enum_type.values]
                    if default_enum_type:
                        # out.update({name: values[0]}) # 枚举值
                        out.update({name: field.default_value})  # 默认值
                    else:
                        out.update({name: "/".join(values)})
                else:
                    if isinstance(field.default_value, bytes):
                        out.update({name: field.default_value.decode()})
                    else:
                        out.update({name: field.default_value})

    def save_message(self, name="", save_dir=None):
        if not save_dir:
            save_dir = os.path.join(config.temp_path, 'pb_info', "%s_%s" % (name, self.get_time_str()))
        os.makedirs(save_dir)
        self.save_req_json(save_dir)
        self.save_var_json(save_dir)
        self.save_service_info_json(save_dir)

    def save_service_info_json(self, _dir):
        """ 保存基本信息"""
        _dict = {}
        for service_name, service in self.items.items():
            if "methods" not in service or not service["methods"]:
                continue
            _dict[service_name] = {}
            for method_name, method in service["methods"].items():
                try:
                    desc = getattr(service['servicer'], method_name).__doc__
                except:
                    desc = ""
                _dict[service_name].update({
                    method_name: {
                        'desc': desc,
                        'input': method["input"]["name"],
                        'output': method["output"]["name"],
                    }})
                if 'http_method' in method and '[google.api.http]' in method['http_method']:
                    _dict[service_name][method_name].update({'method': method['http_method']['[google.api.http]']})

        data = json.dumps(_dict, cls=MyEncoder, sort_keys=True, indent=2, ensure_ascii=False)
        self.write_file(os.path.join(_dir, "service_info.json"), data)

    def save_req_json(self, _dir):
        """ 保存req数据"""
        req_dir = os.path.join(_dir, 'req')
        res_dir = os.path.join(_dir, 'res')
        for service_name, service in self.items.items():
            if "methods" not in service or not service["methods"]:
                continue
            req_default_dir = os.path.join(req_dir, service_name, 'default')
            req_enum_dir = os.path.join(req_dir, service_name, 'enum')
            res_default_dir = os.path.join(res_dir, service_name, 'default')
            res_enum_dir = os.path.join(res_dir, service_name, 'enum')
            os.makedirs(req_default_dir)
            os.makedirs(req_enum_dir)
            os.makedirs(res_default_dir)
            os.makedirs(res_enum_dir)
            for method_name, method in service["methods"].items():
                data = json.dumps(method["input"]["json"], cls=MyEncoder, sort_keys=True, indent=2)
                self.write_file(os.path.join(req_default_dir, "%s.json" % method["input"]["name"]), data)
                data = json.dumps(method["input"]["json_with_enum"], cls=MyEncoder, sort_keys=True, indent=2)
                self.write_file(os.path.join(req_enum_dir, "%s.json" % method["input"]["name"]), data)

                data = json.dumps(method["output"]["json"], cls=MyEncoder, sort_keys=True, indent=2)
                self.write_file(os.path.join(res_default_dir, "%s.json" % method["output"]["name"]), data)
                data = json.dumps(method["output"]["json_with_enum"], cls=MyEncoder, sort_keys=True, indent=2)
                self.write_file(os.path.join(res_enum_dir, "%s.json" % method["output"]["name"]), data)

    def save_var_json(self, _dir):
        """ 保存req数据"""
        var_dir = os.path.join(_dir, 'var')
        for pb_name, pb_dict in self.var_items['file'].items():
            default_dir = os.path.join(var_dir, pb_name, 'default')
            enum_dir = os.path.join(var_dir, pb_name, 'enum')
            os.makedirs(default_dir)
            os.makedirs(enum_dir)
            for name, _dict in pb_dict.items():
                data = json.dumps(_dict['default_json'], cls=MyEncoder, sort_keys=True, indent=2)
                self.write_file(os.path.join(default_dir, "%s.json" % name), data)
                data = json.dumps(_dict['enum_json'], cls=MyEncoder, sort_keys=True, indent=2)
                self.write_file(os.path.join(enum_dir, "%s.json" % name), data)

    @staticmethod
    def get_time_str():
        return datetime.datetime.now().strftime('%Y%m%d%-H%M%S')

    @staticmethod
    def write_file(path, context, delete=True):
        # if not path.startswith("/"):
        #     path = os.path.join(project_path, path)
        if os.path.isfile(path) and delete:
            os.remove(path)
        with open(path, 'w') as f:
            f.write(context)
        print("文件写入成功.path:%s" % path)

    @staticmethod
    def read_json(path):
        with open(path, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict

    def _gen_items(self):
        _dict = {}
        for key, value in self.origin_items.items():
            for service_name,  service_descriptor in value['pb'].items():
                pb = service_descriptor
                stub = value['pb_grpc']['%sStub' % service_name]
                servicer = value['pb_grpc_servicer']['%sServicer' % service_name]
                module = value['module_obj']
                methods = {}
                for m in service_descriptor.methods:
                    input_json, output_json = {}, {}
                    input_json_enum, output_json_enum = {}, {}
                    self.travel_message(m.input_type.fields, input_json, default_enum_type=True)
                    self.travel_message(m.output_type.fields, output_json, default_enum_type=True)
                    self.travel_message(m.input_type.fields, input_json_enum)
                    self.travel_message(m.output_type.fields, output_json_enum)

                    # http使用的method
                    http_method_json = json_format.MessageToJson(m.GetOptions()) if m.GetOptions() else None
                    http_method = json.loads(http_method_json)
                    methods.update({
                        m.name: {
                            'input': {
                                'name': m.input_type.name,
                                'full_name': m.input_type.full_name,
                                'type': m.input_type,
                                'json': input_json,
                                'json_with_enum': input_json_enum,
                                'class': getattr(module, m.input_type.name)
                            },
                            'output': {
                                'name': m.output_type.name,
                                'full_name': m.output_type.full_name,
                                'type': m.output_type,
                                'json': output_json,
                                'json_with_enum': output_json_enum
                            },
                            'http_method': http_method
                        }
                    })

                _dict[service_name] = {'pb': pb,
                                       'stub': stub,
                                       'servicer': servicer,
                                       'methods': methods
                                       }

        return _dict

    def _gen_var_items(self):
        _dict = {
            'all_default': {},
            'all_enum': {},
            'file': {},
        }
        for key, value in self.origin_var_items.items():
            _dict['file'][key] = {}
            for name, _type in value.items():
                default_json, enum_json = {}, {}
                self.travel_message(_type.DESCRIPTOR.fields, default_json, default_enum_type=True)
                self.travel_message(_type.DESCRIPTOR.fields, enum_json)
                _dict['all_default'].update({name: default_json})
                _dict['all_enum'].update({name: enum_json})
                _dict["file"][key].update({
                    name: {
                        'type': _type,
                        'default_json': default_json,
                        'enum_json': enum_json,
                    }
                })
        return _dict

    @staticmethod
    def _select_interface(method):
        """ 选择接口class"""
        if not method["http_method"]:
            return interface_grpc.GrpcInterface
        method_name = list(method["http_method"]['[google.api.http]'].keys())[0]
        if method_name.lower() == "get":
            return interface_grpc.GetGrpcInterface
        elif method_name.lower() == "post":
            return interface_grpc.PostGrpcInterface
        elif method_name.lower() == "put":
            return interface_grpc.PutGrpcInterface
        elif method_name.lower() == "delete":
            return interface_grpc.DeleteGrpcInterface
        else:
            raise Exception("未支持的method name: %s" % method_name)

    def interface(self, service_name, method_name, req_name=None, req_data=None):
        if service_name not in self.items:
            raise Exception("测试集中不包含%s" % service_name)
        if method_name not in self.items[service_name]["methods"]:
            raise Exception("%s测试集中不包含接口%s" % (service_name, method_name))
        method = self.items[service_name]["methods"][method_name]
        stub = self.items[service_name]['stub']
        obj = self._select_interface(method)(service_name, method_name, stub, method, self.var_items)
        obj.set_pm_info(service_name, method_name)
        obj.set_ext_info(self._ext_info)
        if req_name:
            req_path = os.path.join(grpc_req_path, self.collection_name, service_name, "%s.json" % req_name)
            if not os.path.isfile(req_path):
                raise Exception("请求json文件未找到，请检查路径：%s" % req_name)
            req_json = self.read_json(req_path)
            obj.body_dict = self.format_conf_variables(self._conf, req_json)
            log().debug("请求报文已替换.源文件:%s" % req_path)
        elif req_data:
            obj.body_dict = self.format_conf_variables(self._conf, req_data)
            log().debug("请求报文已替换.")
        self.call_init_interface(obj)
        return obj

    def format_conf_variables(self, conf_obj, json_dict):
        """ 替换配置变量"""
        if conf_obj and json_dict:
            json_str = json.dumps(json_dict)
            for key, value in conf_obj._ext.items():
                json_str = re.sub(r"\$\(%s\)" % key, str(value), json_str, count=0, flags=0)
            json_dict = json.loads(json_str)
        return json_dict

    def call_init_interface(self, inte_obj):
        """ 调用初始化接口方法, 对接口对象进行初始化,如有包含自定义方法的话，默认的init_interface就不生效了"""
        if self._custom_func_name:
            if hasattr(self._test_obj, self._custom_func_name):
                log().debug("接口初始化开始：")
                _func = getattr(self._test_obj, self._custom_func_name)
                _func(inte_obj)
            return

        if hasattr(self._test_obj, 'init_interface'):
            log().debug("接口初始化开始：")
            self._test_obj.init_interface(inte_obj)


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)
