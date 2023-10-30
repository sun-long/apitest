 # --*--coding: utf-8 --*--
import json
import os
import time

import requests

from commonlib import config, utils, cmd_utils, system
from commonlib.decorator import wrap_request, wrap_curl_request
from core.ret_utils import CommonRet, CurlRet
from commonlib.utils import log


class BaseInterface(object):
    """ 基础接口类"""

    def __init__(self, item, values):
        self.item = item
        self.values = values
        self.origin_swagger_dir_name = "" # 测试目录名称
        self.origin_collection_name = "" # 测试集名称
        self.origin_interface_name = "" # 接口名称
        self.origin_name = self.item["operationId"] if 'operationId' in self.item else self.item['summary']
        self.origin_summary = self.item["summary"] if 'summary' in self.item else ""
        self.origin_title = self.item["collection_title"] if "collection_title" in self.item else ""
        self.origin_swagger_file = self.item["swagger_file_name"]
        self.origin_parameters = self.item["parameters"] if "parameters" in self.item else None
        self.origin_header = {}
        self.origin_url = ""
        self.origin_description = ""
        self.origin_host = "x.x.x.x"
        self.origin_path_prefix = ""
        self.origin_port = None
        self.origin_path = self.item["path"]
        self.origin_path_name = self.origin_path.split("/")[-1] if self.origin_path and len(self.origin_path.split("/")) > 0 else ""
        self.origin_path_version = self.origin_path.split("/")[-2] if self.origin_path and len(self.origin_path.split("/")) > 1 else ""
        self.origin_protocol = "http"
        self.origin_query = []
        self.origin_pathParams = []
        self.origin_body = None
        self.origin_formdata = None
        self.origin_responses = self.item["responses"] if "responses" in self.item else None
        self._pm_info = ""
        self._wrap_response_class = CommonRet
        self._is_print_log = True
        self.interface_type = 'http'
        self.parse_parameters()
        self.binary_file = None
        self.resp_obj = None
        self.body_dict = None
        self.stream_request = False

    @property
    def name(self):
        return self.origin_name

    @property
    def definitions(self):
        return self.values

    @property
    def path_action(self):
        return self.origin_path_name

    @property
    def path_version(self):
        return self.origin_path_version

    @property
    def collection_title(self):
        return self.origin_title

    @property
    def swagger_dir_name(self):
        return self.origin_swagger_dir_name

    @property
    def collection_name(self):
        return self.origin_collection_name

    @property
    def interface_name(self):
        return self.origin_interface_name

    @property
    def swagger_file(self):
        return self.origin_swagger_file


    @property
    def summary(self):
        return self.origin_summary

    @property
    def method(self):
        return self.item["method"]

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
    def protocol(self):
        return self.origin_protocol

    @property
    def path(self):
        self.fill_path()
        return self.origin_path

    @property
    def path_prefix(self):
        return self.origin_path_prefix

    @property
    def url(self):
        self.fill_path()
        if self.port:
            domain = "%s:%s" % (self.host, self.port)
        else:
            domain = self.host
        path = self.path
        if not path.startswith('/'):
            path = "/%s" % self.path
        path_prefix = self.path_prefix
        if path_prefix and not path_prefix.startswith('/'):
            path_prefix = "/%s" % self.path_prefix

        if 'X-Belt-Action' in self.headers or  'X-Sensenova-Action' in self.headers:  # belt项目方式
            return "%s://%s%s" % (self.protocol, domain, path_prefix)
        else:
            return "%s://%s%s%s" % (self.protocol, domain, path_prefix, path)

    @property
    def params(self):
        return self._get_params()

    @property
    def pm_info(self):
        return self._pm_info

    @property
    def print_status(self):
        """ 是否打印日志的开关"""
        return self._is_print_log

    @property
    def responses(self):
        return self._get_response()

    def _get_params(self):
        params = {}
        if not self.origin_query:
            return params
        for q in self.origin_query:
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

    def parse_parameters(self):
        """ 解析参数"""
        if not self.origin_parameters:
            return
        for info in self.origin_parameters:
            if 'in' not in info:
                continue
            if info['in'] == 'query':
                if not self.origin_query:
                    self.origin_query = []
                self.origin_query.append({
                    'key': info['name'],
                    'value': "",
                    'disabled': False,
                    'required': info['required'] if 'required' in info else None,
                    'type': info['type'] if 'type' in info else "undefined",
                })
            elif info['in'] == 'body':
                if '$ref' in info['schema']:
                    self.origin_body = self.init_body(info['schema']['$ref'])
                elif 'type' in info["schema"] and info["schema"]["type"] == "object" and "properties" in info["schema"]:
                    self.origin_body = self.init_body(info['schema'], is_ref=False)
            elif info['in'] == 'formData':
                if not self.origin_formdata:
                    self.origin_formdata = []
                if 'schema' in info and '$ref' in info['schema']:
                    formData_dict = self.init_body(info['schema']['$ref'])
                    for key, value in formData_dict.items():
                        self.origin_formdata.append({
                            'key': key,
                            'value': "",
                            # 'required': info['required'] if 'required' in info else None,
                            'type': "string",
                        })
                elif 'type' in info:
                    if info["type"] in ['string', 'file']:
                        self.origin_formdata.append({
                            'key': info["name"],
                            'value': "",
                            'type': info["type"],
                        })
                    else:
                        raise Exception("info:%s" % info)
                else:
                    raise Exception("info:%s" % info)
            elif info['in'] == 'path':
                if not self.origin_pathParams:
                    self.origin_pathParams = []

                self.origin_pathParams.append({
                    'key': info['name'],
                    'required': info['required'] if 'required' in info else None,
                    'disabled': False,
                    # 'value': 'undefined_%s' % info['name'],
                    'value': '{%s}' % info['name'],
                })

    def init_body(self, schema_address, is_ref=True):
        """ 初始化body"""
        def getDefinedObj(schema):
            """ 获取定义对象"""
            key = schema.split('#/definitions/')[-1]
            if key not in self.values:
                raise Exception('not found %s in definitions' % key)
            obj = self.values[key]
            return obj

        def get_body(schema_obj, ref=None):
            if not schema_obj:
                return
            if '$ref' in schema_obj:
                if "protobufValue" in schema_obj["$ref"]:
                    return "value"
                if schema_obj['$ref'] == ref:
                    return "killMe"
                else:
                    return get_body(getDefinedObj(schema_obj['$ref']), ref=schema_obj['$ref'])
            # print(schema_obj)
            if 'type' not in schema_obj or schema_obj['type'] == 'object':
                ret = {}
                if 'properties' in schema_obj:
                    for key, value in schema_obj['properties'].items():
                        ret.update({key: get_body(value, ref=ref)})
                if 'additionalProperties' in schema_obj and schema_obj["additionalProperties"]:
                    desc = get_body(schema_obj['additionalProperties'])
                    ret.update({
                        "additionalProp1": desc,
                        "additionalProp2": desc,
                        "additionalProp3": desc
                    })
                return ret
            elif schema_obj['type'] == 'string':
                ret = ""
                if 'enum' in schema_obj:
                    ret = "/".join(schema_obj['enum'])
                if 'default' in schema_obj:
                    ret = "[%s]%s" % (schema_obj['default'], ret)
                return ret
            elif schema_obj['type'] in ('number', 'integer'):
                return 0
            elif schema_obj['type'] == 'boolean':
                return False
            elif schema_obj['type'] == 'array':
                ret = []
                if "items" in schema_obj:
                    if "$ref" in schema_obj["items"]:
                        if schema_obj["items"]['$ref'] == ref:
                            r = "killMe"
                        else:
                            r = get_body(getDefinedObj(schema_obj["items"]['$ref']), ref=schema_obj["items"]['$ref'])
                        ret.append(r)
                return ret
            elif schema_obj['type'] == 'file':
                return ""
            else:
                raise Exception('undefined type %s' % schema_obj['type'])

        if is_ref:
            root_obj = getDefinedObj(schema_address)
        else:
            root_obj = schema_address
        body_dict = get_body(root_obj)
        return body_dict

    def _get_response(self):
        if not self.origin_responses:
            return
        ret = {}
        for status_code, resp in self.origin_responses.items():

            if 'schema' not in resp:
                info = ""
            elif 'allOf' in resp["schema"]:
                info = "Not Support allOf"
            elif 'type' in resp["schema"] and resp["schema"]["type"] == 'array':
                info = [self.init_body(resp["schema"]['items']['$ref']),]
            elif '$ref' in resp["schema"]:
                info = self.init_body(resp["schema"]['$ref'])
            else:
                info = ""
            ret.update({
                status_code: {
                    "description": resp["description"] if "description" in resp else "",
                    "info": info
                }
            })
        return ret
    def _get_path_variable(self):
        """ 获取路径中存在的变量"""
        path_dict = {}
        if not self.origin_pathParams:
            return path_dict
        for p in self.origin_pathParams:
            if "disabled" in p and p["disabled"] == True:
                continue
            path_dict[p["key"]] = p["value"]
        # log().info("params:%s" % params)
        return path_dict

    def fill_path(self):
        """ 填充path， 仅在调用接口的时候填充"""
        path_dict = self._get_path_variable()
        if path_dict:
            self.origin_path = self.origin_path.format(**path_dict)

    def set_print_log(self, flag=True):
        """ 设置该接口是否打印日志"""
        if flag:
            self._is_print_log = True
        else:
            self._is_print_log = False

    def set_wrap_response_class(self, resp_class):
        """ 设置请求的响应包装类"""
        self._wrap_response_class = resp_class

    def set_pm_info(self, collection_name, interface_name, resp_name=None, pm_env_name=None, swagger_dir_name=None):
        self._pm_info = "Collection:%s=>%s" % (collection_name, interface_name)
        self.origin_collection_name = collection_name
        self.origin_interface_name = interface_name
        if resp_name:
            self._pm_info += "=>%s" % resp_name
        if pm_env_name:
            self._pm_info += ", values:%s" % pm_env_name
        if swagger_dir_name:
            self.origin_swagger_dir_name = swagger_dir_name
            self._pm_info = "[%s]%s" % (swagger_dir_name, self._pm_info)

    def set_ext_info(self, ext_info):
        """ 设置额外消息对象"""
        self._ext_info = ext_info

    def set_binary_path(self, binary_path):
        if not binary_path.startswith("/"):
            binary_path = os.path.join(config.resource_path, "bin", binary_path)
        self.binary_file = binary_path

    def set_stream_request(self, stream=False):
        """ 设置接口是否未流式"""
        self.stream_request = stream

    def url_string(self):
        return self.url

    def set_headers(self, key, value=None):
        if value:
            self.origin_header[key] = value
        elif not value and key in self.origin_header:
            del self.origin_header[key]
        else:
            pass

    def set_protocol(self, protocol):
        self.origin_protocol = protocol

    def set_path_prefix(self, path_prefix):
        self.origin_path_prefix = path_prefix

    def set_host(self, host):
        origin_host = self.origin_host
        if not isinstance(host, str):
            if isinstance(host, dict) and "all" in host:
                host = host["all"]["host"]
            else:
                raise Exception('host must str. %s' % host)

        if "://" in host:
            protocol = host.split("://")[0]
            self.set_protocol(protocol)
            host = host.split("://")[1]
        if ":" in host:
            self.set_port(host.split(":")[1])
            host = host.split(":")[0]
        self.origin_host = host
        log().debug("更新host:%s->%s" % (origin_host, self.origin_host))

    def set_path(self, path):
        origin_path = self.origin_path
        self.origin_path = path
        log().debug("更新path:%s->%s" % (origin_path, self.origin_path))

    def set_path_param(self, key, value):
        """ 设置路径中的参数"""
        for i, param in enumerate(self.origin_pathParams):
            if param['key'] == key:
                origin_param = self.origin_pathParams[i]['value']
                self.origin_pathParams[i]['value'] = value
                log().debug("更新pathParam %s:%s->%s" % (key, origin_param, value))
                break


    def set_port(self, port):
        origin_port = self.origin_port
        self.origin_port = port
        log().debug("更新host:%s->%s" % (origin_port, self.origin_port ))

    def set_description(self, desc):
        if desc:
            self.item["description"] = desc


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
        """ 添加参数, 支持str 及list"""
        if isinstance(value, list):
            for v in value:
                self.origin_query.append({"key": key, "value": v})
        else:
            self.origin_query.append({"key": key, "value": value})

    def update_params(self, key, value):
        """ 更新参数, 同时更新同名参数"""
        """ value 支持 str , list"""
        if value is None:
            self.remove_params(key)
        else:
            # 删掉再添加
            self.remove_params(key)
            self.add_params(key, value)

            # self.origin_query = list(filter(lambda x: x["key"] != key, self.origin_query))
            # if isinstance(value, list):
            #     for v in value:
            #         self.origin_query.append({"key": key, "value": v, 'disabled': False})
            # else:
            #     self.origin_query.append({"key": key,"value": value, 'disabled': False})
            # old function
            # for i, query in enumerate(self.origin_query):
            #     if key == query["key"]:
            #         log().debug("更新param[key=%s]:%s->%s" % (key, query["value"], value, ))
            #         self.origin_query[i].update({"value": value, 'disabled': False})
            #         break

    def remove_params(self, key, value=None):
        del_list = []
        for i, query in enumerate(self.origin_query):
            if key == query["key"]:
                if value:
                    if value == query["value"]:
                        del_list.append(query)
                else:
                    del_list.append(query)
        for query in del_list:
            log().debug("删除param:%s" % query)
            self.origin_query.remove(query)
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
        self.fill_path()
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
        self.body_dict, self.files_dict = self._get_body()
        self.body_dict_log = None

    @property
    def body(self):
        return self.body_dict

    @property
    def body_log(self):
        req_message = ""
        try:
            if isinstance(self.body, dict):
                req_message = json.dumps(self.body, sort_keys=True, indent=2, ensure_ascii=False)
                req_message = ["%s..." % x[:100] if len(x) > 500 else x for idx, x in enumerate(req_message.split('\"'))]
                req_message = '\"'.join(req_message)
            elif self.body_dict_log and isinstance(self.body_dict_log, dict):
                req_message = json.dumps(self.body_dict_log, sort_keys=True, indent=2, ensure_ascii=False)
                req_message = ["%s..." % x[:100] if len(x) > 500 else x for idx, x in enumerate(req_message.split('\"'))]
                req_message = '\"'.join(req_message)
        except:
            pass
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
            result = self.origin_body
        elif self.origin_formdata:
            for fd in self.origin_formdata:
                if fd["type"] == "file":
                    files[fd["key"]] = fd["value"]
                else:
                    result[fd["key"]] = fd["value"]
        else:
            raise Exception("该方法暂不支持")
        return result, files

    def _get_upload_dict(self):
        _files = {}
        for param_name, file_path in self.files.items():
            log().info(os.path.exists(file_path))
            if not file_path.startswith("/") :
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
        from google.protobuf import json_format
        data = json_format.Parse(json.dumps(self.body), pb_obj)
        self.body_dict_log = self.body_dict
        self.body_dict = data.SerializeToString()
        self.origin_body["mode"] = 'formdata'


    @wrap_request()
    def request(self):
        self.fill_path()
        self._wrap_response_class = CommonRet
        if self.binary_file:
            _file = open(self.binary_file, 'rb')
            r = requests.post(self.url_string(), headers=self.headers, data=_file)
        elif self.origin_formdata or self.files:
            _files = []
            if self.files:
                _files = self.gen_upload_dict()
            r = requests.post(self.url_string(), data=self.body, headers=self.headers, files=_files, verify=False)
        elif self.origin_body or (not self.origin_formdata and not self.origin_body):
            r = requests.post(self.url_string(), json=self.body, headers=self.headers, verify=False, stream=self.stream_request)
        else:
            raise Exception("暂不支持的mode形式" )
        return r

    def _get_curl_cmd(self):
        """ 获取curl的cmd"""
        cmd = self.base_cmd % (self.method, self.url_string())
        if self.headers:
            for key, value in self.headers.items():
                cmd += self.base_header % (key, value)
        if self.origin_body or (not self.origin_formdata and not self.origin_body):
            cmd += self.base_header % ('Content-Type', 'application/json')
            if getattr(self, 'body'):
                cmd += self.base_body % json.dumps(self.body)
        elif self.origin_formdata:
            for key, value in self.body.items():
                cmd += self.base_formdata % (key, value)

        cmd += self.base_status_code

        return cmd

    @wrap_curl_request()
    def request_curl(self):
        """ 执行curl"""
        self.fill_path()
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
        self.fill_path()
        self._wrap_response_class = CommonRet

        if self.headers:
            r = requests.delete(self.url, params=self.params, headers=self.headers, verify=False)
        else:
            r = requests.delete(self.url, params=self.params, verify=False)
        return r

    @wrap_request()
    def requestbody(self):
        self.fill_path()
        self._wrap_response_class = CommonRet
        if self.origin_body or (not self.origin_formdata and not self.origin_body):
            if self.headers:
                r = requests.delete(self.url, json=self.body, headers=self.headers, verify=False)
            else:
                r = requests.delete(self.url, json=self.body, verify=False)
        elif self.origin_formdata:
            if self.headers:
                r = requests.delete(self.url, data=self.body, headers=self.headers, verify=False)
            else:
                r = requests.delete(self.url, data=self.body, verify=False)
        else:
            raise Exception("暂不支持的mode形式")
        return r


class PutInterface(PostInterface):
    """ Put接口"""

    def __init__(self, item, values):
        super(PutInterface, self).__init__(item, values)

    @wrap_request()
    def request(self):
        self.fill_path()
        self._wrap_response_class = CommonRet
        if self.origin_body or (not self.origin_formdata and not self.origin_body):
            if self.headers:
                r = requests.put(self.url, json=self.body, headers=self.headers, verify=False)
            else:
                r = requests.put(self.url, json=self.body, verify=False)
        elif self.origin_formdata:
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
            raise Exception("暂不支持的mode形式")
        return r


class PatchInterface(PostInterface):
    """ Put接口"""

    def __init__(self, item, values):
        super(PatchInterface, self).__init__(item, values)

    @wrap_request()
    def request(self):
        self.fill_path()
        self._wrap_response_class = CommonRet
        if self.origin_body or (not self.origin_formdata and not self.origin_body):
            if self.headers:
                r = requests.patch(self.url, json=self.body, headers=self.headers, verify=False)
            else:
                r = requests.patch(self.url, json=self.body, verify=False)
        elif self.origin_formdata:
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
            raise Exception("暂不支持的mode形式")
        return r




if __name__ == '__main__':
    pass