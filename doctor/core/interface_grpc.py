# --*--coding: utf-8 --*--
import copy
import json
import os
import grpc
import requests

from commonlib import utils, config
from commonlib.decorator import wrap_request_grpc, wrap_request
from commonlib.utils import log
from core.ret_grpc_utils import CommonRet as GrpcCommonRet
from core.ret_utils import CommonRet as HttpCommonRet


class BaseInterface(object):
    """ 基础接口类"""

    def __init__(self, service_name, method_name, stub, method_dict):
        self.origin_service_name = service_name
        self.origin_method_name = method_name
        self.origin_stub = stub
        self.origin_method_dict = method_dict
        self.origin_description = "暂无描述信息"
        self.origin_host = None
        self.origin_grpc_host = None
        self.origin_port = None
        self._pm_info = ""
        self._wrap_response_class = GrpcCommonRet
        self._is_print_log = True
        self._ext_info = None
        self._resp = None

    @property
    def stub(self):
        return self.origin_stub

    @property
    def service_name(self):
        return self.origin_service_name

    @property
    def method_name(self):
        return self.origin_method_name

    @property
    def method_dict(self):
        return self.origin_method_dict

    @property
    def description(self):
        """ 描述信息"""
        return self.origin_description

    @property
    def host(self):
        """ host名称，域名或ip"""
        return self.origin_host

    @property
    def grpc_host(self):
        """ host名称，域名或ip"""
        return self.origin_grpc_host

    @property
    def port(self):
        """ 端口号"""
        return self.origin_port

    @property
    def pm_info(self):
        return self._pm_info

    @property
    def print_status(self):
        """ 是否打印日志的开关"""
        return self._is_print_log

    @property
    def ext_info(self):
        """ 额外消息对象"""
        return self._ext_info

    @property
    def resp(self):
        """ 接口返回结果"""
        return self._resp


    def set_ext_info(self, ext_info):
        """ 设置额外消息对象"""
        self._ext_info = ext_info

    def set_print_log(self, flag=True):
        """ 设置该接口是否打印日志"""
        if flag:
            self._is_print_log = True
        else:
            self._is_print_log = False

    def set_wrap_response_class(self, resp_class):
        """ 设置请求的响应包装类"""
        self._wrap_response_class = resp_class

    def set_pm_info(self, service_name, method_name):
        """ 设置信息"""
        self._pm_info = "Collection:%s=>%s" % (service_name, method_name)

    def set_port(self, port=None):
        origin_port = self.origin_port
        self.origin_port = port
        log().debug("更新port:%s->%s" % (origin_port, port))

    def set_host(self, host):
        origin_host = self.origin_host
        if isinstance(host, str):
            if "://" in host:
                host = host.split("://")[1]
            if "/" in host:
                host = host.split("/")[0]
            if ":" in host:
                port = host.split(":")[1]
                self.set_port(port)
                host = host.split(":")[0]
            # else:
            #     self.set_port()
            self.origin_host = host
        else:
            raise Exception("set host失败. 请提供一个字符串")
        log().debug("更新host:%s->%s" % (origin_host, self.origin_host))

    def set_grpc_host(self, grpc_host):
        origin_host = self.origin_grpc_host
        self.origin_grpc_host = grpc_host
        log().debug("更新grpc host:%s->%s" % (origin_host, self.origin_grpc_host))

    def set_description(self, desc):
        self.origin_description = desc


class GrpcInterface(BaseInterface):
    """ grpc接口"""

    def __init__(self, service_name, method_name, stub, method, var_items):
        super(GrpcInterface, self).__init__(service_name, method_name, stub, method)
        self.body_dict = copy.deepcopy(method["input"]["json"])
        self.var_dict = copy.deepcopy(var_items["all_default"])
        self._grpc_req_func = self.method_dict["input"]["class"]
        self.body_dict_log = None  # 用于输出body
        self.interface_type = 'grpc'

    @property
    def body(self):
        return self.body_dict

    @property
    def body_log(self):
        req_message = None
        if isinstance(self.body, dict):
            req_message = json.dumps(self.body, sort_keys=True, indent=2, ensure_ascii=False)
            req_message = ["%s..." % x[:100] if len(x) > 500 else x for idx, x in enumerate(req_message.split('\"'))]
            req_message = '\"'.join(req_message)
        elif self.body_dict_log and isinstance(self.body_dict_log, dict):
            req_message = json.dumps(self.body_dict_log, sort_keys=True, indent=2, ensure_ascii=False)
            req_message = ["%s..." % x[:100] if len(x) > 500 else x for idx, x in enumerate(req_message.split('\"'))]
            req_message = '\"'.join(req_message)
        return req_message

    def get_default_message(self, message_name):
        """ 获取默认的message结构"""
        if message_name not in self.var_dict:
            raise Exception("message_name:%s 不存在" % message_name)
        return self.var_dict[message_name]

    def get_enum_message(self, message_name):
        """ 获取包含枚举的message结构"""
        # TODO
        pass

    def _get_channel(self):
        """ grpc: 获取channel"""
        return grpc.insecure_channel(self.grpc_host)

    def _get_stub_obj(self, channel):
        """ grpc：获取stub对象"""
        return self.stub(channel)

    def _modify_body_dict_field(self, field_name, field_value=None):
        """ 根据字段名称删除报文里的内容
            field_name demo:
                  "AK"
                  "deviceID"
                  "deviceShadowInfo.deviceShadow.AK"
                  "deviceShadowInfo.deviceShadow.deviceID"
                  "deviceShadowInfo.deviceShadow.version"
                  "deviceShadowInfo.subDeviceShadows.0.AK"
        """
        name_list = field_name.split(".")
        target = self.body_dict
        for name in name_list[:-1]:
            if name.isdigit():
                target = target[int(name)]
            else:
                target = target[name]
        if field_value is not None:
            if name_list[-1].isdigit():
                target[int(name_list[-1])] = field_value
            else:
                target[name_list[-1]] = field_value
        else:
            if name_list[-1].isdigit():
                del target[int(name_list[-1])]
            else:
                del target[name_list[-1]]

    def body_get(self, _path):
        """ 获取指定路径的数据"""
        current_list = []
        try:
            name_list = _path.split(".")
            target = self.body_dict
            for name in name_list[:-1]:
                current_list.append(name)
                if name.isdigit():
                    target = target[int(name)]
                else:
                    target = target[name]
            if name_list[-1].isdigit():
                current_list.append(name_list[-1])
                return target[int(name_list[-1])]
            else:
                return target[name_list[-1]]
        except:
            log().info("[Warning]body_get:path error:%s" % ".".join(current_list))
            return None

    def del_body(self, field_name):
        """ 删除报文中的某个字段"""
        self._modify_body_dict_field(field_name)
        log().info("删除%s 字段成功." % field_name)

    def update_body(self, field_name, field_value=None, escape=False, unescape=False, NoFieldNameCreate=False):
        """ 修改报文中的某个字段"""
        if not isinstance(field_name, str):
            raise Exception("field_name需要为报文中的字符串，如shadowMeta.meta")
        if field_value:
            if escape:
                field_value = utils.zhuanyi(field_value)
            if unescape:
                field_value = utils.dezhuanyi(field_value)
            self._modify_body_dict_field(field_name, field_value)
            log().debug("修改%s=>%s 成功." % (field_name, field_value))
        else:
            if escape:
                field_value = utils.zhuanyi(self.body_get(field_name))
            if unescape:
                field_value = utils.dezhuanyi(self.body_get(field_name))
            self._modify_body_dict_field(field_name, field_value)

    @wrap_request_grpc()
    def request(self):
        self._wrap_response_class = GrpcCommonRet
        if not self.host:
            raise Exception("未设置host.")
        channel = self._get_channel()
        stub_obj = self._get_stub_obj(channel)
        req_obj = self._grpc_req_func(**self.body)
        r = getattr(stub_obj, self.method_name)(req_obj)
        return r


class HttpGrpcInterface(GrpcInterface):
    """ 支持http的 grpc接口"""
    def __init__(self, service_name, method_name, stub, method, var_items):
        super(HttpGrpcInterface, self).__init__(service_name, method_name, stub, method, var_items)
        self.origin_protocol = None
        self.origin_prefix_path = ""
        self.origin_header = {}
        self.origin_http_method_type = self._get_http_method_type()
        self.origin_http_path = self._get_http_path()
        self.interface_type = 'grpc,http'


    @property
    def name(self):
        return self.method_name

    @property
    def headers(self):
        """ header dict"""
        return self.origin_header

    @property
    def protocol(self):
        """ protocol http协议或 https协议"""
        return self.origin_protocol

    @property
    def method(self):
        """ http请求的方法类型 get post delete """
        return self.origin_http_method_type

    @property
    def path(self):
        """ http请求的路径"""
        return self.origin_http_path

    @property
    def port(self):
        """ http端口号"""
        return self.origin_port

    @property
    def prefix_path(self):
        """ http请求的路径的前缀"""
        return self.origin_prefix_path

    @property
    def url(self):
        """ http请求的完整url"""

        abs_path = "%s/%s" % (self.prefix_path, self.path)
        if abs_path.startswith("/"):
            abs_path = abs_path[1:]
        if self.port:
            _u = "%s://%s:%s/%s" % (self.protocol, self.host, self.port, abs_path)
        else:
            _u = "%s://%s/%s" % (self.protocol, self.host, abs_path)
        return _u

    def _get_http_method_type(self):
        """ 获取http method 类型"""
        if not self.method_dict["http_method"]:
            return
        return list(self.method_dict["http_method"]['[google.api.http]'].keys())[0]

    def _get_http_path(self):
        """ 获取http url path"""
        if not self.method_dict["http_method"]:
            return
        _path = self.method_dict["http_method"]['[google.api.http]'][self.method]
        if _path.startswith("/"):
            _path = _path[1:]
        return _path

    def fill_path(self):
        """ 填充path， 仅在调用接口的时候填充"""
        self.origin_http_path = self.origin_http_path.format(**self.body)

    def set_protocol(self, protocol='http'):
        origin_protocol = protocol
        self.origin_protocol = protocol
        log().debug("更新port:%s->%s" % (origin_protocol, protocol))

    def set_prefix_path(self, prefix):
        self.origin_prefix_path = prefix

    def set_host(self, host):
        origin_host = self.origin_host
        if isinstance(host, str):
            if "://" in host:
                protocol = host.split("://")[0]
                self.set_protocol(protocol)
                host = host.split("://")[1]
            else:
                self.set_protocol()
            if "/" in host:
                prefix_path = "/".join(host.split("/")[1:])
                self.set_prefix_path(prefix_path)
                host = host.split("/")[0]


            if ":" in host:
                port = host.split(":")[1]
                self.set_port(port)
                host = host.split(":")[0]
            else:
                self.set_port()
            self.origin_host = host
        else:
            raise Exception("set host失败. 请提供一个字符串")
        log().debug("更新host:%s->%s" % (origin_host, self.origin_host))

    def set_path(self, path, index=None):
        origin_path = self.origin_http_path
        if index is not None and isinstance(index, int) and index < len(origin_path.split("/")):
            _path_list = origin_path.split("/")
            _path_list[index] = path
            self.origin_http_path = "/".join(_path_list)
        elif isinstance(path, str):
            self.origin_http_path = path
        else:
            raise Exception("set path error. path:%s. index=%s" % (path, index))
        log().debug("更新path:%s->%s" % (origin_path, self.origin_http_path))

    def set_headers(self, key, value=None):
        """ 设置header"""
        header = self.origin_header
        if key in header:
            if value:
                header[key] = value
            else:
                del header[key]
        else:
            header[key] = value

    def _request_http(self):
        pass

    def request_http(self):
        self.fill_path()
        self._wrap_response_class = HttpCommonRet
        r = self._request_http()
        return r

class GetGrpcInterface(HttpGrpcInterface):
    """ grpc:GET接口"""

    def __init__(self, service_name, method_name, stub, method, var_items):
        super(GetGrpcInterface, self).__init__(service_name, method_name, stub, method, var_items)

    @property
    def params(self):
        return self._get_params()

    def url_string(self):
        self.fill_path()
        param_list = []
        for key, value in self.params.items():
            if isinstance(value, list):
                for v in value:
                    param_list.append("%s=%s" % (key, v))
            else:
                param_list.append("%s=%s" % (key, value))
        if param_list:
            return self.url + "?" + "&".join(param_list)
        return self.url

    def _get_params(self):
        params = {}
        for key, value in self.body.items():
            if isinstance(value, dict):
                # TODO 第一版 暂时不支持多级的情况
                continue
            params[key] = value
        return params

    def add_params(self, key, value):
        if key in self.body:
            if isinstance(self.body[key], dict):
                raise Exception("不支持修改多级参数")
            if isinstance(self.body[key], list):
                self.body[key].append(value)
            else:
                origin_value = self.body[key]
                self.body[key] = [origin_value, value]
        else:
            self.body[key] = value
        # log().info("添加param[key=%s]:%s" % (key, value,))

    def update_params(self, key, value):
        """只更新第一个同名参数，如果有多个同名参数的情况下，请先清除再添加"""
        self.body.update({key: value})

    def remove_params(self, key, value=None):
        if key in self.body:
            if isinstance(self.body[key], list):
                if value in self.body[key]:
                    self.body[key].remove(value)
            else:
                del self.body[key]

    @wrap_request()
    def _request_http(self):
        if self.headers:
            r = requests.get(self.url, params=self.params, headers=self.headers, verify=False)
        else:
            r = requests.get(self.url, params=self.params, verify=False)
        return r


class PostGrpcInterface(HttpGrpcInterface):
    """ POST接口"""

    def __init__(self, service_name, method_name, stub, method, var_items):
        super(PostGrpcInterface, self).__init__(service_name, method_name, stub, method, var_items)
        self.files_dict = {}

    @property
    def files(self):
        return self.files_dict

    def _get_upload_dict(self):
        """ TODO 当使用的时候 需要修改"""
        _files = {}
        for param_name, file_path in self.files.items():
            log().info(os.path.exists(file_path))
            if not file_path.startswith("/"):
                _path = os.path.join(config.resource_path, "images", file_path)
            elif not os.path.exists(file_path):
                log().info("lalalla不存在")
                file_name = os.path.basename(file_path)
                _path = utils.find_file(file_name, os.path.join(config.resource_path, "images"))
                if not _path:
                    raise Exception("待上传文件未找到. 原始path:%s" % file_path)
            else:
                _path = file_path
            _files[param_name] = _path
        return _files

    def url_string(self):
        self.fill_path()
        return self.url

    def gen_upload_dict(self):
        _files = {}
        path_dict = self._get_upload_dict()
        for name, _path in path_dict.items():
            _files[name] = open(_path, "rb")
        return _files

    @wrap_request()
    def _request_http(self):
        """ 暂不支持上传文件 TODO"""
        if self.headers:
            r = requests.post(self.url, json=self.body, headers=self.headers, verify=False)
        else:
            r = requests.post(self.url, json=self.body, verify=False)
        return r

class DeleteGrpcInterface(GetGrpcInterface):
    """ Delete接口 备注，delete暂时不支持body， 可以使用类似get的方式"""

    def __init__(self, service_name, method_name, stub, method, var_items):
        super(DeleteGrpcInterface, self).__init__(service_name, method_name, stub, method, var_items)

    @wrap_request()
    def _request_http(self):
        if self.headers:
            r = requests.delete(self.url, params=self.params, headers=self.headers, verify=False)
        else:
            r = requests.delete(self.url, params=self.params, verify=False)
        return r

class PutGrpcInterface(PostGrpcInterface):
    """ Put接口"""

    def __init__(self, service_name, method_name, stub, method, var_items):
        super(PutGrpcInterface, self).__init__(service_name, method_name, stub, method, var_items)

    @wrap_request()
    def _request_http(self):
        if self.headers:
            r = requests.put(self.url, json=self.body, headers=self.headers, verify=False)
        else:
            r = requests.put(self.url, json=self.body, verify=False)
        return r




if __name__ == '__main__':
    pass