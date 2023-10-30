 # --*--coding: utf-8 --*--
import json
import os
import requests
from google.protobuf import json_format

from commonlib import config, utils, cmd_utils, system
from commonlib.decorator import wrap_request, wrap_curl_request
from core.ret_utils import CommonRet, CurlRet
from commonlib.utils import log


class BaseInterface(object):
    """ 基础接口类"""

    def __init__(self, item, values):
        self.item = item
        self.values = values
        self.origin_name = self.item["name"]
        self.origin_request = self.item["request"]
        self.origin_header = self.item["request"]["header"]
        self.origin_url = self.item["request"]["url"]
        if "description" not in self.item:
            self.item["description"] = "暂无描述信息"
        self.origin_description = self.item["description"]
        self.origin_host = self.item["request"]["url"]["host"]
        self.origin_port = self.item["request"]["url"]["port"] if "port" in self.item["request"]["url"] else None
        self.origin_path = self.item["request"]["url"]["path"]
        self.origin_protocol = self.item["request"]["url"]["protocol"]
        # self.origin_swagger_file = self.item["swagger_file_name"]
        self.origin_swagger_file = "nova"

        self.origin_grpc_host = None
        self._pm_info = ""
        self._wrap_response_class = CommonRet
        self._is_print_log = True
        self.interface_type = 'grpc,http'
        self.stream_request = False
        self.origin_swagger_dir_name = ""
        self.origin_collection_name = ""
        self.origin_interface_name = "" # 接口名称
        self.stream_request = False

    @property
    def interface_name(self):
        return self.origin_interface_name

    @property
    def collection_name(self):
        return self.origin_collection_name

    @property
    def swagger_file(self):
        return self.origin_swagger_file

    @property
    def swagger_dir_name(self):
        return self.origin_swagger_dir_name


    @property
    def name(self):
        return self.item["name"]

    @property
    def method(self):
        return self.item["request"]["method"]

    @property
    def headers(self):
        return self._get_headers()

    @property
    def description(self):
        return self.item["description"]

    @property
    def host(self):
        return self._get_host()

    @property
    def port(self):
        return self.item["request"]["url"]["port"] if "port" in self.item["request"]["url"] else None

    @property
    def path(self):
        return self._get_path()

    @property
    def url(self):
        if self.port:
            domain = "%s:%s" % (self.host, self.port)
        else:
            domain = self.host
        return "%s://%s/%s" % (self.item["request"]["url"]["protocol"], domain, self.path)

    @property
    def pm_info(self):
        return self._pm_info

    @property
    def print_status(self):
        """ 是否打印日志的开关"""
        return self._is_print_log

    def set_stream_request(self, stream=False):
        """ 设置接口是否未流式"""
        self.stream_request = stream

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

    def set_grpc_host(self, grpc_host):
        origin_host = self.origin_grpc_host
        self.origin_grpc_host = grpc_host
        log().debug("更新grpc host:%s->%s" % (origin_host, self.origin_grpc_host))


    def set_ext_info(self, ext_info):
        """ 设置额外消息对象"""
        self._ext_info = ext_info

    def url_string(self):
        return self.url

    def _get_host(self):
        return ".".join(self.item["request"]["url"]["host"])

    def _get_path(self):
        return "/".join(self.item["request"]["url"]["path"])

    def set_headers(self, key, value=None, type=None):
        header = self.item["request"]["header"]
        for i, h in enumerate(header):
            if key == h['key']:
                if value:
                    header[i]["value"] = value
                if type:
                    header[i]["type"] = type
                if "disabled" in h:
                    header[i]["disabled"] = False
                if not value:
                    del header[i]
                return
        else:
            if value is not None:
                if type:
                    header.append({"key": key, "value": value, "type": type})
                else:
                    header.append({"key": key, "value": value})

    def set_protocol(self, protocol):
        self.item["request"]["url"]["protocol"] = protocol

    def set_host(self, host, index=None):
        origin_host = ".".join(self.item["request"]["url"]["host"])
        if index and isinstance(index, int) and index < len(self.item["request"]["url"]["host"]):
            self.item["request"]["url"]["host"][index] = host
        elif isinstance(host, list):
            self.item["request"]["url"]["host"] = host
        elif isinstance(host, str):
            if "://" in host:
                protocol = host.split("://")[0]
                self.set_protocol(protocol)
                host = host.split("://")[1]
            if ":" in host:
                self.set_port(host.split(":")[1])
                host = host.split(":")[0]
            self.item["request"]["url"]["host"] = host.split(".")
        else:
            raise Exception("set host失败")
        log().debug("更新host:%s->%s" % (origin_host, ".".join(self.item["request"]["url"]["host"])))

    def set_path(self, path, index=None):
        origin_path = ".".join(self.item["request"]["url"]["path"])
        if index and isinstance(index, int) and index < len(self.item["request"]["url"]["path"]):
            self.item["request"]["url"]["path"][index] = path
        elif isinstance(path, list):
            self.item["request"]["url"]["path"] = path
        elif isinstance(path, str):
            self.item["request"]["url"]["path"] = path.split("/")
        else:
            pass
        log().debug("更新path:%s->%s" % (origin_path, ".".join(self.item["request"]["url"]["path"])))

    def set_port(self, port):
        origin_port = self.item["request"]["url"]["port"] if "port" in self.item["request"]["url"] else "None"
        self.item["request"]["url"]["port"] = port
        log().debug("更新host:%s->%s" % (origin_port, self.item["request"]["url"]["port"]))

    def set_description(self, desc):
        self.item["description"] = desc

    def _get_headers(self):
        headers = {}
        if "header" in self.item["request"] and self.item["request"]["header"]:
            for h in self.item["request"]["header"]:
                if "disabled" in h:
                    if not h["disabled"]:
                        headers[h["key"]] = h["value"]
                else:
                    headers[h["key"]] = h["value"]
        return headers


class BaseCurl(object):

    def __init__(self):
        """ 初始化"""
        self.client_info = None
        self._cmd_str = None

    @property
    def cmd_str(self):
        """ 完整CMD"""
        return self._cmd_str

    @property
    def base_cmd(self):
        """ 基础cmd"""
        return "curl --location --request %s '%s' "

    @property
    def base_header(self):
        """ 基础header"""
        return " --header '%s: %s' "

    @property
    def base_status_code(self):
        return " -w '**@@**http_code:%{http_code}' "

    @property
    def base_body(self):
        # return """ --data-raw '%s' """
        return """ --data '%s' """

    @property
    def base_formdata(self):
        return " -F '%s=%s' "

    def set_client(self, ip, port=22, username='root', password='root'):
        """ 设置client"""
        self.client_info = {
            "ip": ip,
            "port": port,
            "username": username,
            "password": password,
        }
        log().debug("client设置成功,%s" % self.client_info)

    def _exec_curl(self, cmd):
        """ 执行curl"""
        self._cmd_str = cmd
        log().info("cmd:%s" % cmd)
        if self.client_info:
            # if not cmd_utils.ping_ip(self.client_info["ip"]):
            #     raise Exception("%s ping不通" % self.client_info["ip"])
            ret, output, err = cmd_utils.ssh_cmd(cmd,
                                                 self.client_info["ip"],
                                                 port=self.client_info["port"],
                                                 username=self.client_info["username"],
                                                 password=self.client_info["password"])
        else:
            ret, output, err = system.ci_system(cmd, logger=None, loglevel='info',
                                                prompt='curl', output=True)
        return ret, output, err


class GetInterface(BaseInterface, BaseCurl):
    """ GET接口"""

    def __init__(self, item, values):
        BaseInterface.__init__(self, item, values)
        BaseCurl.__init__(self)
        if "query" not in self.item["request"]["url"]:
            self.item["request"]["url"]["query"] = []
        self.origin_query = self.item["request"]["url"]["query"]

    @property
    def params(self):
        return self._get_params()

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

    def _get_params(self):
        params = {}
        if "query" not in self.item["request"]["url"]:
            return params
        for q in self.item["request"]["url"]["query"]:
            if "disabled" in q and q["disabled"] == True:
                continue
            if q["key"] in params:
                if isinstance(params[q["key"]], list):
                    params[q["key"]].append(q["value"])
                else:
                    temp = params[q["key"]]
                    params[q["key"]] = [temp, q["value"]]
            else:
                params[q["key"]] = q["value"]
        # log().info("params:%s" % params)
        return params

    def add_params(self, key, value):
        self.item["request"]["url"]["query"].append({"key": key, "value": value})
        # log().info("添加param[key=%s]:%s" % (key, value,))
        # log().info("new query:%s" % self.item["request"]["url"]["query"])

    def update_params(self, key, value):
        """只更新第一个同名参数，如果有多个同名参数的情况下，请先清除再添加"""
        querys = self.item["request"]["url"]["query"]
        for i, query in enumerate(querys):
            if key == query["key"]:
                log().debug("更新param[key=%s]:%s->%s" % (key, query["value"], value, ))
                querys[i].update({"value": value, 'disabled': False})
                break

    def remove_params(self, key, value=None):
        del_list = []
        querys = self.item["request"]["url"]["query"]
        for i, query in enumerate(querys):
            if key == query["key"]:
                if value:
                    if value == query["value"]:
                        del_list.append(query)
                else:
                    del_list.append(query)
        for query in del_list:
            log().debug("删除param:%s" % query)
            querys.remove(query)
        # log().info("query:%s" % self.item["request"]["url"]["query"])

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
            r = requests.get(self.url, params=self.params, headers=self.headers, verify=False)
        else:
            r = requests.get(self.url, params=self.params, verify=False)
        return r

    @wrap_curl_request()
    def request_curl(self):
        """ 执行curl"""
        self._wrap_response_class = CurlRet
        cmd = self._get_curl_cmd()
        ret, output, err = self._exec_curl(cmd)
        return ret, output, err


class PostInterface(GetInterface):
    """ POST接口"""

    def __init__(self, item, values):
        BaseInterface.__init__(self, item, values)
        # BaseCurl.__init__(self)
        if 'body' in self.item["request"]:
            self.origin_body = self.item["request"]["body"]
        else:
            self.origin_body = None
        self.binary_file = None
        self.body_dict, self.files_dict = self._get_body()
        self.body_dict_log = None

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

    @property
    def files(self):
        return self.files_dict

    def set_binary_path(self, binary_path):
        if not binary_path.startswith("/"):
            binary_path = os.path.join(config.resource_path, "bin", binary_path)
        self.binary_file = binary_path

    def _get_body(self):
        result = {}
        files = {}
        if 'body' not in self.item["request"]:
            return result, files
        if 'body' not in self.item["request"]:
            return result, files
        if 'mode' not in self.item["request"]["body"]:
            return result, files
        body_dict = self.item["request"]["body"]
        mode = body_dict["mode"]
        if mode == 'raw':
            if not body_dict['raw']:
                return result, files
            result = json.loads(body_dict['raw'])
        elif mode == 'formdata':
            for fd in body_dict["formdata"]:
                if fd["type"] == "text":
                    result[fd["key"]] = fd["value"]
                elif fd["type"] == "file":
                    files[fd["key"]] = fd["src"]
        elif mode == 'file':
            files['path'] = None
            files['path'] = None
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
                if name_list[-1] in target:
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
        self.origin_body["mode"] = 'formdata'


    @wrap_request()
    def request(self):
        self._wrap_response_class = CommonRet
        mode = self.origin_body["mode"]
        if mode == 'raw':
            if self.headers:
                r = requests.post(self.url_string(), json=self.body, headers=self.headers, verify=False,stream=self.stream_request)
            else:
                r = requests.post(self.url_string(), json=self.body, verify=False,stream=self.stream_request)
        elif mode == 'formdata':
            if self.headers:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.post(self.url_string(), data=self.body, headers=self.headers, files=_files, verify=False)
                else:
                    r = requests.post(self.url_string(), data=self.body, headers=self.headers, verify=False)
            else:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.post(self.url_string(), data=self.body, headers=self.headers, files=_files, verify=False)
                else:
                    r = requests.post(self.url_string(), data=self.body, verify=False)
        elif mode == 'file':
            if not os.path.exists(self.binary_file):
                raise Exception("upload file is not exist,path=%s" % self.binary_file)
            _file = open(self.binary_file, 'rb')
            if self.headers:
                r = requests.post(self.url_string(), headers=self.headers, data=_file)
            else:
                r = requests.post(self.url_string(), data=_file)
        else:
            raise Exception("暂不支持的mode形式: %s" % mode)
        return r

    def _get_curl_cmd(self):
        """ 获取curl的cmd"""
        cmd = self.base_cmd % (self.method, self.url_string())
        if self.headers:
            for key, value in self.headers.items():
                cmd += self.base_header % (key, value)
        if self.origin_body and 'mode' in self.origin_body:
            mode = self.origin_body["mode"]
            if mode == 'raw':
                cmd += self.base_header % ('Content-Type', 'application/json')
                if getattr(self, 'body'):
                    cmd += self.base_body % json.dumps(self.body)
            elif mode == 'formdata':
                for key, value in self.body.items():
                    cmd += self.base_formdata % (key, value)

        cmd += self.base_status_code

        return cmd

    @wrap_curl_request()
    def request_curl(self):
        """ 执行curl"""
        self._wrap_response_class = CurlRet
        cmd = self._get_curl_cmd()
        ret, output, err = self._exec_curl(cmd)
        return ret, output, err


class DeleteInterface(PostInterface):
    """ Delete接口 备注，delete暂时不支持body， 可以使用类似get的方式"""

    def __init__(self, item, values):
        # GetInterface.__init__(self, item, values)
        PostInterface.__init__(self, item, values)

    @wrap_request()
    def request(self):
        self._wrap_response_class = CommonRet

        if self.headers:
            r = requests.delete(self.url, params=self.params, headers=self.headers, verify=False)
        else:
            r = requests.delete(self.url, params=self.params, verify=False)
        return r

    @wrap_request()
    def requestbody(self):
        self._wrap_response_class = CommonRet
        mode = self.origin_body["mode"]
        if mode == 'raw':
            if self.headers:
                r = requests.delete(self.url, json=self.body, headers=self.headers, verify=False)
            else:
                r = requests.delete(self.url, json=self.body, verify=False)
        elif mode == 'formdata':
            if self.headers:
                r = requests.delete(self.url, data=self.body, headers=self.headers, verify=False)
            else:
                r = requests.delete(self.url, data=self.body, verify=False)
        else:
            raise Exception("暂不支持的mode形式: %s" % mode)
        return r


class PutInterface(PostInterface):
    """ Put接口"""

    def __init__(self, item, values):
        super(PutInterface, self).__init__(item, values)

    @wrap_request()
    def request(self):
        self._wrap_response_class = CommonRet
        mode = self.origin_body["mode"]
        if mode == 'raw':
            if self.headers:
                r = requests.put(self.url, json=self.body, headers=self.headers, verify=False)
            else:
                r = requests.put(self.url, json=self.body, verify=False)
        elif mode == 'formdata':
            if self.headers:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.put(self.url, data=self.body, headers=self.headers, files=_files, verify=False)
                else:
                    r = requests.put(self.url, data=self.body, headers=self.headers, verify=False)
            else:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.put(self.url, data=self.body, headers=self.headers, files=_files, verify=False)
                else:
                    r = requests.put(self.url, data=self.body, verify=False)
        else:
            raise Exception("暂不支持的mode形式: %s" % mode)
        return r


class PatchInterface(PutInterface):
    """ Put接口"""

    def __init__(self, item, values):
        super(PatchInterface, self).__init__(item, values)

    @wrap_request()
    def request(self):
        self._wrap_response_class = CommonRet
        mode = self.origin_body["mode"]
        if mode == 'raw':
            if self.headers:
                r = requests.patch(self.url, json=self.body, headers=self.headers, verify=False)
            else:
                r = requests.patch(self.url, json=self.body, verify=False)
        elif mode == 'formdata':
            if self.headers:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.patch(self.url, data=self.body, headers=self.headers, files=_files, verify=False)
                else:
                    r = requests.patch(self.url, data=self.body, headers=self.headers, verify=False)
            else:
                if self.files:
                    _files = self.gen_upload_dict()
                    r = requests.patch(self.url, data=self.body, headers=self.headers, files=_files, verify=False)
                else:
                    r = requests.patch(self.url, data=self.body, verify=False)
        else:
            raise Exception("暂不支持的mode形式: %s" % mode)
        return r


if __name__ == '__main__':
    pass