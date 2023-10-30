 # --*--coding: utf-8 --*--
import json
import os
import requests
from google.protobuf import json_format

from commonlib import config, utils, cmd_utils, system
from commonlib.decorator import wrap_request, wrap_curl_request
from core.interface import BaseCurl
from core.ret_utils import CommonRet, CurlRet
from commonlib.utils import log


class BaseInterface(object):
    """ 基础接口类"""

    def __init__(self, requestDataObj):
        self.origin_header = requestDataObj.headers
        self.origin_url = requestDataObj.url
        self.origin_method = requestDataObj.method
        self.origin_description = requestDataObj.desc
        self.origin_host = None
        self.origin_port = None
        self.origin_path = None
        self.origin_protocol = None
        # self.split_url()
        self.origin_params = None
        self.origin_body = None
        self.origin_formdata = None
        self._wrap_response_class = CommonRet
        self._pm_info = ""
        self._is_print_log = True

    @property
    def name(self):
        return "None"

    @property
    def method(self):
        return self.origin_method

    @property
    def headers(self):
        return self.origin_header

    @property
    def description(self):
        return self.origin_description

    @property
    def host(self):
        return self.origin_host

    @property
    def port(self):
        return self.origin_port

    @property
    def path(self):
        return self.origin_path

    @property
    def url(self):
        if self.port:
            domain = "%s:%s" % (self.host, self.port)
        else:
            domain = self.host
        return "%s://%s/%s" % (self.origin_protocol, domain, self.origin_path)

    @property
    def pm_info(self):
        return self._pm_info

    @property
    def print_status(self):
        """ 是否打印日志的开关"""
        return self._is_print_log

    def set_print_log(self, flag=True):
        """ 设置该接口是否打印日志"""
        if flag:
            self._is_print_log = True
        else:
            self._is_print_log = False

    def set_wrap_response_class(self, resp_class):
        """ 设置请求的响应包装类"""
        self._wrap_response_class = resp_class

    def set_pm_info(self, collection_name, interface_name, resp_name=None, pm_env_name=None):
        self._pm_info = "Collection:%s=>%s" % (collection_name, interface_name)
        if resp_name:
            self._pm_info += "=>%s" % resp_name
        if pm_env_name:
            self._pm_info += ", values:%s" % pm_env_name

    def url_string(self):
        return self.url

    def set_headers(self, key, value=None):
        if not self.origin_header:
            self.origin_header = {}
        if value:
            self.origin_header[key] = value
        else:
            if key in self.origin_header:
                del self.origin_header[key]

    def split_url(self):
        if not self.origin_url:
            return
        url_str = self.origin_url
        self.set_protocol(self.origin_url.split("://")[0])
        url_str = url_str.split("://")[1]
        self.set_host(url_str.split('/')[0])
        self.set_path("/".join(url_str.split('/')[1:]))

    def set_protocol(self, protocol):
        self.origin_protocol = protocol

    def set_host(self, host):
        origin_host = self.origin_host
        if "://" in host:
            protocol = host.split("://")[0]
            self.set_protocol(protocol)
            host = host.split("://")[1]
        if ":" in host:
            self.set_port(host.split(":")[1])
            host = host.split(":")[0]

        self.origin_host = host
        log().debug("更新host:%s->%s" % (origin_host, self.origin_host))

    def set_path(self, new_path):
        origin_path = self.origin_path
        if new_path.startswith('/'):
            new_path = new_path[1:]
        self.origin_path = new_path
        log().debug("更新path:%s->%s" % (origin_path, self.origin_path))

    def set_port(self, port):
        origin_port = self.origin_port
        self.origin_port = port
        log().debug("更新host:%s->%s" % (origin_port, self.origin_port))

    def set_description(self, desc):
        self.origin_description = desc


class GetInterface(BaseInterface, BaseCurl):
    """ GET接口"""

    def __init__(self, requestDataObj):
        BaseInterface.__init__(self, requestDataObj)
        BaseCurl.__init__(self)
        self.origin_params = requestDataObj.params
        if self.origin_params is None:
            self.origin_params = {}

    @property
    def params(self):
        return self.origin_params

    def url_string(self):
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

    def add_params(self, key, value):
        if key in self.params and isinstance(self.params[key], list):
            self.params[key].append(value)
        elif key in self.params:
            self.params[key] = [self.params[key], value]
        else:
            self.params[key] = value

    def update_params(self, key, value):
        """更新指定key的value"""
        self.params[key] = value

    def remove_params(self, key):
        if key in self.params:
            del self.params[key]

    def _get_curl_cmd(self):
        """ 获取curl的cmd"""
        cmd = self.base_cmd % (self.method, self.url_string())
        if self.headers:
            for key, value in self.headers.items():
                cmd += self.base_header % (key, value)
        cmd += self.base_status_code
        return cmd

    @wrap_request()
    def request(self, ret_class=None):
        if ret_class:
            self._wrap_response_class = ret_class
        else:
            self._wrap_response_class = CommonRet
        if self.headers:
            r = requests.get(self.url, params=self.params, headers=self.headers)
        else:
            r = requests.get(self.url, params=self.params)
        return r

    @wrap_curl_request()
    def request_curl(self):
        """ 执行curl"""
        self._wrap_response_class = CurlRet
        cmd = self._get_curl_cmd()
        ret, output, err = self._exec_curl(cmd)
        return ret, output, err


class PostInterface(BaseInterface, BaseCurl):
    """ POST接口"""

    def __init__(self, requestDataObj):
        BaseInterface.__init__(self, requestDataObj)
        BaseCurl.__init__(self)
        self.origin_body = requestDataObj.body
        self.origin_formdata = requestDataObj.formdata
        self.mode = None
        self.body_dict, self.files_dict = self._get_body()
        self.body_dict_log = None

    @property
    def body(self):
        return self.body_dict

    @property
    def formdata(self):
        return self.origin_formdata

    @property
    def body_log(self):
        req_message = None
        if isinstance(self.body, dict):
            req_message = json.dumps(self.body, sort_keys=True, indent=2)
            req_message = ["%s..." % x[:100] if len(x) > 500 else x for idx, x in enumerate(req_message.split('\"'))]
            req_message = '\"'.join(req_message)
        elif self.body_dict_log and isinstance(self.body_dict_log, dict):
            req_message = json.dumps(self.body_dict_log, sort_keys=True, indent=2)
            req_message = ["%s..." % x[:100] if len(x) > 500 else x for idx, x in enumerate(req_message.split('\"'))]
            req_message = '\"'.join(req_message)
        return req_message

    @property
    def files(self):
        return self.files_dict

    def _get_body(self):
        result = {}
        files = {}
        if not self.origin_body and not self.origin_formdata:
            return result, files
        if self.origin_body:
            self.mode = 'raw'
        elif self.origin_formdata:
            self.mode = 'formdata'

        if self.mode == 'raw':
            result  = self.origin_body
        elif self.mode == 'formdata':
            for fd in self.origin_formdata:
                if fd["type"] == "text":
                    result[fd["key"]] = fd["value"]
                elif fd["type"] == "file":
                    files[fd["key"]] = fd["src"]
        else:
            raise Exception("该方法暂不支持")
        return result, files

    def _get_upload_dict(self):
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

    def gen_upload_dict(self):
        _files = {}
        path_dict = self._get_upload_dict()
        for name, _path in path_dict.items():
            _files[name] = open(_path, "rb")
        return _files

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
        name_list = _path.split(".")
        target = self.body_dict
        for name in name_list[:-1]:
            if name.isdigit():
                target = target[int(name)]
            else:
                target = target[name]
        if name_list[-1].isdigit():
            return target[int(name_list[-1])]
        else:
            return target[name_list[-1]]

    def del_body(self, field_name):
        """ 删除报文中的某个字段"""
        self._modify_body_dict_field(field_name)
        log().info("删除%s 字段成功." % field_name)

    def update_body(self, field_name, field_value=None, escape=False, unescape=False):
        """ 修改报文中的某个字段"""
        if not isinstance(field_name, str):
            raise Exception("field_name需要为报文中的字符串，如shadowMeta.meta")
        if field_value is not None:
            if escape:
                field_value = utils.zhuanyi(field_value)
            if unescape:
                field_value = utils.dezhuanyi(field_value)
            self._modify_body_dict_field(field_name, field_value)
            if field_value and isinstance(field_value, str) and len(field_value) > 50:
                log().debug("修改%s=>%s... 成功." % (field_name, field_value[:50]))
            else:
                log().debug("修改%s=>%s 成功." % (field_name, field_value))
        else:
            if escape:
                field_value = utils.zhuanyi(self.body_get(field_name))
            if unescape:
                field_value = utils.dezhuanyi(self.body_get(field_name))
            self._modify_body_dict_field(field_name, field_value)

    def body_to_pb(self, pb_obj):
        """ body转pb序列化"""
        data = json_format.Parse(json.dumps(self.body), pb_obj)
        self.body_dict_log = self.body_dict
        self.body_dict = data.SerializeToString()
        self.mode = 'formdata'


    @wrap_request()
    def request(self):
        self._wrap_response_class = CommonRet
        if self.mode == 'raw':
            if self.headers:
                r = requests.post(self.url, json=self.body, headers=self.headers)
            else:
                r = requests.post(self.url, json=self.body)
        elif self.mode == 'formdata':
            if self.headers:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.post(self.url, data=self.body, headers=self.headers, files=_files)
                else:
                    r = requests.post(self.url, data=self.body, headers=self.headers)
            else:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.post(self.url, data=self.body, headers=self.headers, files=_files)
                else:
                    r = requests.post(self.url, data=self.body)
        else:
            raise Exception("暂不支持的mode形式: %s" % self.mode)
        return r

    def _get_curl_cmd(self):
        """ 获取curl的cmd"""
        cmd = self.base_cmd % (self.method, self.url_string())
        if self.headers:
            for key, value in self.headers.items():
                cmd += self.base_header % (key, value)

        if self.mode == 'raw':
            cmd += self.base_header % ('Content-Type', 'application/json')
            if getattr(self, 'body'):
                cmd += self.base_body % json.dumps(self.body)
        elif self.mode == 'formdata':
            for key, value in self.body.items():
                cmd += self.base_formdata % (key, value)

        cmd += self.base_status_code

        log().info("cmd:%s" % cmd)
        return cmd

    @wrap_curl_request()
    def request_curl(self):
        """ 执行curl"""
        self._wrap_response_class = CurlRet
        cmd = self._get_curl_cmd()
        ret, output, err = self._exec_curl(cmd)
        return ret, output, err


class DeleteInterface(GetInterface, PostInterface):
    """ Delete接口 备注，delete暂时不支持body， 可以使用类似get的方式"""

    def __init__(self, requestDataObj):
        GetInterface.__init__(self, requestDataObj)
        PostInterface.__init__(self, requestDataObj)

    @wrap_request()
    def request(self):
        self._wrap_response_class = CommonRet

        if self.headers:
            r = requests.delete(self.url, params=self.params, headers=self.headers)
        else:
            r = requests.delete(self.url, params=self.params)
        return r

    @wrap_request()
    def requestbody(self):
        self._wrap_response_class = CommonRet
        if self.mode == 'raw':
            if self.headers:
                r = requests.delete(self.url, json=self.body, headers=self.headers)
            else:
                r = requests.delete(self.url, json=self.body)
        elif self.mode == 'formdata':
            if self.headers:
                r = requests.delete(self.url, data=self.body, headers=self.headers)
            else:
                r = requests.delete(self.url, data=self.body)
        else:
            raise Exception("暂不支持的mode形式: %s" % self.mode)
        return r


class PutInterface(PostInterface):
    """ Put接口"""

    def __init__(self, requestDataObj):
        super(PutInterface, self).__init__(requestDataObj)

    @wrap_request()
    def request(self):
        self._wrap_response_class = CommonRet
        if self.mode == 'raw':
            if self.headers:
                r = requests.put(self.url, json=self.body, headers=self.headers)
            else:
                r = requests.put(self.url, json=self.body)
        elif self.mode == 'formdata':
            if self.headers:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.put(self.url, data=self.body, headers=self.headers, files=_files)
                else:
                    r = requests.put(self.url, data=self.body, headers=self.headers)
            else:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.put(self.url, data=self.body, headers=self.headers, files=_files)
                else:
                    r = requests.put(self.url, data=self.body)
        else:
            raise Exception("暂不支持的mode形式: %s" % self.mode)
        return r





if __name__ == '__main__':
    pass