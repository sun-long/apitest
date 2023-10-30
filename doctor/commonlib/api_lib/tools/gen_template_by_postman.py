#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   gen_postman.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/9/3 下午1:58   wangan      1.0         None
'''
import copy
import json
import os
import re

from commonlib import utils, config
from core.ext_info import ExtFunctionInfo
from core.pm_utils import load_postman

class HtmlTemplate(object):
    """ html模板类"""
    def __init__(self, tmp_path):
        self.before_around = "$$%%"
        self.after_around = "%%$$"
        self._tmp_path = tmp_path
        self._template_text = self.read_tmp_file()

    @property
    def template_text(self):
        """ html字符串文本"""
        return self._template_text

    def read_tmp_file(self):
        """ 读取template文件"""
        try:
            with open(self._tmp_path, 'r') as f:
                template_text = f.read()
        except Exception as e:
            raise
        if not template_text:
            raise Exception("读取的文件为空.path:%s" % self._tmp_path)
        return template_text

    def replace(self, key, value=""):
        """ 替换模板中的key"""
        abs_key = "%s%s%s" % (self.before_around, key, self.after_around)
        # print("replace %s to '%s'" % (abs_key, value))
        return self.template_text.replace(abs_key, value)

class GenTemplatePostmanTool(object):
    def __init__(self, postman_dir, host=None):
        self.host = host
        self.postman_dir = postman_dir
        self.collections = None

    def init_collections(self):
        ef = ExtFunctionInfo()
        ef.isRequestOpened = True
        self.collections = load_postman(self.postman_dir)

    @staticmethod
    def save_file(data, file_name, save_dir):
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir)
        abs_path = os.path.join(save_dir, file_name)
        with open(abs_path, 'w') as f:
            f.write(data)
        return abs_path

    def filter_str(self, _str):
        """ 过滤字符串"""
        ret = _str
        if "." in _str:
            ret = _str.replace('.', '_')

        return ret

    def getSrvName(self, srv_name):
        split_list = '-.'
        is_word = True
        for splitChar in split_list:
            if splitChar in srv_name:
                srv_name = "".join([x[0].upper() + x[1:] for x in srv_name.split(splitChar)])
                is_word = False
        if is_word:
            srv_name = srv_name.capitalize()
        return srv_name

    def genApiTemplate(self, product_name):
        """ 生成Api模板"""
        with open(os.path.join(config.code_gen_path, 'swagger/api_template.tmp'), 'r') as f:
            template_all = f.read()
        with open(os.path.join(config.code_gen_path, 'swagger/api_template_func.tmp'), 'r') as f:
            template_func = f.read()
        template_all = template_all.replace('$$%%SWAGGER_DIR%%$$', self.postman_dir)
        for srv_name, srvInfo in self.collections.items.items():
            temp_all = copy.deepcopy(template_all)
            func_template = ""
            for method_name, methodInfo in srvInfo.items():
                # if methodInfo['operationId'] == 'AccountService_UpdateRole':
                #     i = 1
                intef = self.collections.interface(srv_name, method_name)

                temp_func_str = copy.deepcopy(template_func)

                desc_str = ""
                if 'summary' in methodInfo:
                    desc_str = methodInfo['summary'] if len(methodInfo['summary']) <=50 else "%s..." % methodInfo['summary'][:50]
                temp_func_str = temp_func_str.replace('$$%%SWAGGER_NAME%%$$', srv_name)
                temp_func_str = temp_func_str.replace('$$%%API_NAME%%$$', method_name)
                temp_func_str = temp_func_str.replace('$$%%TITLE%%$$', "path: [%s]%s" % (methodInfo['method'], methodInfo['path']))
                temp_func_str = temp_func_str.replace('$$%%DESC%%$$', desc_str)
                temp_func_str = temp_func_str.replace('$$%%FUNC_NAME%%$$', "%s%s" %(method_name, methodInfo['method'].capitalize()))

                param_str = ""
                param_list_str = ""
                param_code_str = ""
                full_path_code_str = ""
                param_name_list = []
                if '}' in methodInfo['path']:
                    pattern = re.compile(r'\{(.*?)\}')
                    full_param_list = pattern.findall(methodInfo['path'])
                    for full_param in full_param_list:
                        if full_param in param_name_list:
                            continue
                        param_list_str += ", %s" % full_param
                        full_path_code_str += "        intef.set_path_param(\"%s\", %s)\n" % (full_param, full_param)
                        param_name_list.append(full_param)
                if methodInfo['method'] in ['get', 'delete']:
                    if 'parameters' in methodInfo and methodInfo['parameters']:
                        for param_info in methodInfo['parameters']:
                            if param_info['in'] != 'query':
                                continue
                            description = param_info['description'] if 'description' in param_info else "null"
                            _type = param_info['type'] if 'type' in param_info else "undefined"
                            required = "*" if 'required' in param_info and param_info['required'] is True else ""
                            param_str += " " * 16 + '%s参数名称：%s　类型：%s　描述：%s\n' % (
                                required, param_info['name'], _type, description)
                            param_list_str += ", %s=None" % self.filter_str(param_info['name'])
                            param_code_str += "        intef.update_params(\"%s\", %s)\n" % (param_info['name'],
                                                                                             self.filter_str(param_info['name']))
                    if param_str.endswith('\n'):
                        param_str = param_str[:-2]
                    param_str = "params: \n%s" % param_str
                body_str = ""
                body_code_str = ""
                if methodInfo['method'] in ['post', 'put', 'patch']:
                    if intef.body:
                        if 'header' in intef.body:
                            intef.update_body('header')  # 移除header
                        for key, value in intef.body.items():
                            if key not in param_name_list:
                                param_list_str += ", %s=None" % key
                            body_code_str += "        intef.update_body(\"%s\", %s)\n" % (key, key)
                    body_str = json.dumps(intef.body, sort_keys=True, indent=4)
                    body_str = body_str.replace('\n' + ' ' * 4, '\n' + ' '* 20)
                    body_str = " " * 16 + body_str
                    if body_str.endswith('\n}'):
                        body_str = body_str[:-2] + '\n' + ' ' * 16 + '}'
                    body_str = "body: \n%s" % body_str

                resp_dict = intef.responses
                response_str = ""
                if resp_dict:
                    response_str = "resp:\n"
                    for status_code, info in resp_dict.items():
                        temp_str = json.dumps(info["info"], sort_keys=True, indent=4)
                        temp_str = temp_str.replace('\n' + ' ' * 4, '\n' + ' ' * 20)
                        temp_str = " " * 16 + temp_str
                        if temp_str.endswith('\n}'):
                            temp_str = temp_str[:-2] + '\n' + ' ' * 16 + '}'
                        response_str += " " * 16 + "%s(%s):\n%s\n" % (status_code, info["description"], temp_str)

                temp_func_str = temp_func_str.replace('$$%%STRUCTURE%%$$', param_str + body_str)
                temp_func_str = temp_func_str.replace('$$%%RESPONSE%%$$', response_str)
                temp_func_str = temp_func_str.replace('$$%%PARAM_LIST%%$$', param_list_str)
                temp_func_str = temp_func_str.replace('$$%%PARAM_CODE%%$$\n', param_code_str)
                temp_func_str = temp_func_str.replace('$$%%FULL_PATH_CODE%%$$\n', full_path_code_str)
                temp_func_str = temp_func_str.replace('$$%%BODY_CODE%%$$\n', body_code_str)

                func_template += temp_func_str
            temp_all = temp_all.replace('$$%%API_FUNCTION%%$$', func_template)
            # temp_all = temp_all.replace('$$%%SWAGGER_NAME%%$$', srv_name)
            temp_all = temp_all.replace('$$%%CLASS_NAME%%$$', self.getSrvName(srv_name))

            py_name = "%s_service_swagger.py" % self.getSrvName(srv_name).lower()
            save_dir = os.path.join(config.temp_template_path, self.swagger_dir, "defines/%s/api" % self.swagger_dir)
            abs_path = self.save_file(temp_all, py_name, save_dir)
            print("[%s]Api template gen success. Path:%s" % (py_name, abs_path))

    def genApiBusinessTemplate(self, product_name):
        """ 生成Api模板"""
        with open(os.path.join(config.code_gen_path, 'swagger/api_template_business.tmp'), 'r') as f:
            template_all = f.read()
        for srv_name, srvInfo in self.collections.items.items():
            temp_all = copy.deepcopy(template_all)
            # temp_all = temp_all.replace('$$%%SWAGGER_NAME%%$$', srv_name)
            import_str = "from defines.%s.api.%s_service_swagger import %sSwaggerApi\n" % (
                self.swagger_dir, self.getSrvName(srv_name).lower(), self.getSrvName(srv_name))

            temp_all = temp_all.replace('$$%%CLASS_NAME%%$$', self.getSrvName(srv_name))
            temp_all = temp_all.replace('$$%%API_IMPORT_LIST%%$$', import_str)

            py_name = "%s_service_business.py" % self.getSrvName(srv_name).lower()
            save_dir = os.path.join(config.temp_template_path, self.swagger_dir, "defines/%s" % self.swagger_dir)
            abs_path = self.save_file(temp_all, py_name, save_dir)
            print("[%s]Api template business gen success. Path:%s" % (py_name, abs_path))

    def genTestCaseTemplate(self, product_name):
        """ 生成Api模板"""
        # 接口测试模板
        with open(os.path.join(config.code_gen_path, 'swagger/testcase_template_api.tmp'), 'r') as f:
            template_api = f.read()
        with open(os.path.join(config.code_gen_path, 'swagger/testcase_template_api_func.tmp'), 'r') as f:
            template_api_func = f.read()

        # 参数测试模板
        with open(os.path.join(config.code_gen_path, 'swagger/testcase_template_param.tmp'), 'r') as f:
            template_param = f.read()
        with open(os.path.join(config.code_gen_path, 'swagger/testcase_template_param_func.tmp'), 'r') as f:
            template_param_func = f.read()

        # 场景测试模板
        # with open(os.path.join(config.code_gen_path, 'swagger/testcase_template_scenario_file.tmp'), 'r') as f:
        #     template_scenario_file = f.read()
        with open(os.path.join(config.code_gen_path, 'swagger/testcase_template_scenario_class.tmp'), 'r') as f:
            template_scenario_class = f.read()

        # scenario_class_all = ""
        for srv_name, srvInfo in self.collections.items.items():
            api_func_all = ""
            param_func_all = ""
            num = -1
            for method_name, methodInfo in srvInfo.items():
                num += 1
                # if methodInfo['operationId'] == 'AccountService_UpdateRole':
                #     i = 1
                intef = self.collections.interface(srv_name, method_name)

                desc_str = ""
                if 'summary' in methodInfo:
                    desc_str = methodInfo['summary'] if len(methodInfo['summary']) <=50 else "%s..." % methodInfo['summary'][:50]

                param_str = ""
                param_list_str = ""
                param_code_str = ""
                invalid_param_code_str = ""
                full_path_code_str = ""
                invalid_param_list_str = ""
                invalid_param_replace_str = ""
                param_name_list = []
                if '}' in methodInfo['path']:
                    pattern = re.compile(r'\{(.*?)\}')
                    full_param_list = pattern.findall(methodInfo['path'])
                    for full_param in full_param_list:
                        if full_param in param_name_list:
                            continue
                        param_list_str += ", %s" % full_param
                        full_path_code_str += " " * 8 + "%s = None\n" % full_param  # TODO 看看是否能加注视
                        param_name_list.append(full_param)
                if methodInfo['method'] in ['get', 'delete']:
                    if 'parameters' in methodInfo and methodInfo['parameters']:
                        for param_info in methodInfo['parameters']:
                            if param_info['in'] != 'query':
                                continue
                            description = param_info['description'] if 'description' in param_info else "null"
                            _type = param_info['type'] if 'type' in param_info else "undefined"
                            required = "*" if 'required' in param_info and param_info['required'] is True else ""
                            param_str += " " * 16 + '%s参数名称：%s　类型：%s　描述：%s\n' % (
                                required, param_info['name'], _type, description)
                            param_list_str += ", %s=%s" % (self.filter_str(param_info['name']), self.filter_str(param_info['name']))
                            param_code_str += " " * 8 + "%s = None\n" % self.filter_str(param_info['name'])
                            invalid_param_list_str += " " * 8 + "('%s', 'invalid%s'),\n" % (self.filter_str(param_info['name']),
                                                                                            self.filter_str(param_info['name']))
                            invalid_param_list_str += " " * 8 + "('%s', ''),\n" % self.filter_str(param_info['name'])
                            invalid_param_list_str += " " * 8 + "('%s', None),\n" % self.filter_str(param_info['name'])
                            invalid_param_replace_str += " " * 8 + "if invalidParam[0] == '%s':\n" % self.filter_str(param_info['name'])
                            invalid_param_replace_str += " " * 8 + "    %s = invalidParam[1]\n" % self.filter_str(param_info['name'])
                        invalid_param_code_str = "        intef.update_params(invalidParam[0], invalidParam[1])\n"

                    if param_str.endswith('\n'):
                        param_str = param_str[:-2]
                    param_str = "params: \n%s" % param_str
                body_str = ""
                body_code_str = ""
                invalid_body_code_str = ""
                if methodInfo['method'] in ['post', 'put', 'patch']:
                    if intef.body:
                        if 'header' in intef.body:
                            intef.update_body('header')
                        for key, value in intef.body.items():
                            if key not in param_name_list:
                                param_list_str += ", %s=%s" % (key, key)
                                body_code_str += " " * 8 + "%s = None\n" % key
                            invalid_param_list_str += " " * 8 + "('%s', 'invalid%s'),\n" % (key, key)
                            invalid_param_list_str += " " * 8 + "('%s', ''),\n" % key
                            invalid_param_list_str += " " * 8 + "('%s', None),\n" % key
                            invalid_param_replace_str += " " * 8 + "if invalidParam[0] == '%s':\n" % key
                            invalid_param_replace_str += " " * 8 + "    %s = invalidParam[1]\n" % key
                        invalid_body_code_str = "        intef.update_body(invalidParam[0], invalidParam[1])\n"

                    body_str = json.dumps(intef.body, sort_keys=True, indent=4)
                    body_str = body_str.replace('\n' + ' ' * 4, '\n' + ' '* 20)
                    body_str = " " * 16 + body_str
                    if body_str.endswith('\n}'):
                        body_str = body_str[:-2] + '\n' + ' ' * 16 + '}'
                    body_str = "body: \n%s" % body_str

                resp_dict = intef.responses
                response_str = ""
                if resp_dict:
                    response_str = "resp:\n"
                    for status_code, info in resp_dict.items():
                        temp_str = json.dumps(info["info"], sort_keys=True, indent=4)
                        temp_str = temp_str.replace('\n' + ' ' * 4, '\n' + ' ' * 20)
                        temp_str = " " * 16 + temp_str
                        if temp_str.endswith('\n}'):
                            temp_str = temp_str[:-2] + '\n' + ' ' * 16 + '}'
                        response_str += " " * 16 + "%s(%s):\n%s\n" % (status_code, info["description"], temp_str)

                if param_list_str:
                    param_list_str = param_list_str[2:]
                if invalid_param_list_str.endswith('\n'):
                    invalid_param_list_str = invalid_param_list_str[:-1]
                if invalid_param_replace_str.endswith('\n'):
                    invalid_param_replace_str = invalid_param_replace_str[:-1]

                # 替换api
                api_func_text = copy.deepcopy(template_api_func)
                api_func_text = api_func_text.replace('$$%%METHOD_NAME%%$$', method_name)
                api_func_text = api_func_text.replace('$$%%API_OBJ%%$$', "%sApi" % self.getSrvName(srv_name))
                api_func_text = api_func_text.replace('$$%%TEST_FUNC_DESC%%$$', desc_str)
                api_func_text = api_func_text.replace('$$%%API_FUNC%%$$', "%s%sApi" % (method_name, methodInfo['method'].capitalize()))
                api_func_text = api_func_text.replace('$$%%PARAM_LIST%%$$', param_list_str)
                api_func_text = api_func_text.replace('$$%%PARAM_CODE%%$$\n', full_path_code_str + param_code_str + body_code_str)
                # api_func_text = api_func_text.replace('$$%%INVALID_PARAM_LIST%%$$', invalid_param_list_str)
                # api_func_text = api_func_text.replace('$$%%INVALID_PARAM_REPLACE%%$$', invalid_param_replace_str)
                # api_func_text = api_func_text.replace('$$%%FULL_PATH_CODE%%$$\n', full_path_code_str)
                # api_func_text = api_func_text.replace('$$%%BODY_CODE%%$$\n', body_code_str)
                # api_func_text = api_func_text.replace('$$%%TEST_NUM%%$$', str(num).zfill(3))
                # api_func_text = api_func_text.replace('$$%%STRUCTURE%%$$', param_str + body_str)
                # api_func_text = api_func_text.replace('$$%%RESPONSE%%$$', response_str)
                api_func_all += api_func_text

                # 替换param
                param_func_text = copy.deepcopy(template_param_func)
                param_func_text = param_func_text.replace('$$%%METHOD_NAME%%$$', method_name)
                param_func_text = param_func_text.replace('$$%%API_OBJ%%$$', "%sApi" % self.getSrvName(srv_name))
                param_func_text = param_func_text.replace('$$%%TEST_FUNC_DESC%%$$', desc_str)
                param_func_text = param_func_text.replace('$$%%API_FUNC%%$$', "%s%sApi" % (method_name, methodInfo['method'].capitalize()))
                param_func_text = param_func_text.replace('$$%%PARAM_LIST%%$$', "%s, " % param_list_str if param_list_str else param_list_str)
                param_func_text = param_func_text.replace('$$%%PARAM_CODE%%$$\n', full_path_code_str + param_code_str + body_code_str)
                param_func_text = param_func_text.replace('$$%%INVALID_PARAM_LIST%%$$', invalid_param_list_str)
                param_func_text = param_func_text.replace('$$%%INVALID_PARAM_CODE%%$$', invalid_param_code_str)
                param_func_text = param_func_text.replace('$$%%INVALID_BODY_CODE%%$$', invalid_body_code_str)
                # param_func_text = param_func_text.replace('$$%%INVALID_PARAM_REPLACE%%$$', invalid_param_replace_str)
                param_func_text = param_func_text.replace('\n\n', '\n')
                param_func_all += param_func_text


            api_code_text = copy.deepcopy(template_api)
            api_code_text = api_code_text.replace('$$%%TEST_API_FUNCTION%%$$', api_func_all)
            api_code_text = api_code_text.replace('$$%%CLASS_DESC%%$$', srv_name)
            api_code_text = api_code_text.replace('$$%%CLASS_NAME%%$$', self.getSrvName(srv_name))

            param_code_text = copy.deepcopy(template_param)
            param_code_text = param_code_text.replace('$$%%TEST_API_FUNCTION%%$$', param_func_all)
            param_code_text = param_code_text.replace('$$%%CLASS_DESC%%$$', srv_name)
            param_code_text = param_code_text.replace('$$%%CLASS_NAME%%$$', self.getSrvName(srv_name))

            scenario_class_code_text = copy.deepcopy(template_scenario_class)
            scenario_class_code_text = scenario_class_code_text.replace('$$%%CLASS_NAME%%$$', self.getSrvName(srv_name))
            # scenario_class_all += scenario_class_code_text

            api_save_dir = os.path.join(config.temp_template_path, self.swagger_dir, "cases/test_%s" % self.swagger_dir, "api")
            param_save_dir = os.path.join(config.temp_template_path, self.swagger_dir, "cases/test_%s" % self.swagger_dir, "param")
            scenario_save_dir = os.path.join(config.temp_template_path, self.swagger_dir, "cases/test_%s" % self.swagger_dir, "scenario")

            api_name = "test_%s_api.py" % self.getSrvName(srv_name).lower()
            param_name = "test_%s_param.py" % self.getSrvName(srv_name).lower()
            scenario_name = "test_%s_scenario.py" % self.getSrvName(srv_name).lower()

            abs_api_path = self.save_file(api_code_text, api_name, api_save_dir)
            abs_param_path = self.save_file(param_code_text, param_name, param_save_dir)
            abs_scenario_path = self.save_file(scenario_class_code_text, scenario_name, scenario_save_dir)

            print("[%s]TestCase api template gen success. Path:%s" % (api_name, abs_api_path))
            print("[%s]TestCase param template gen success. Path:%s" % (param_name, abs_param_path))
            print("[%s]TestCase scenario template gen success. Path:%s" % (scenario_name, abs_scenario_path))

        # template_scenario_file = template_scenario_file.replace('$$%%TEST_CLASS_FUNCTION%%$$', scenario_class_all)
        # py_name = "test_%s_func.py" % self.swagger_dir
        # save_dir = os.path.join(config.temp_template_path, self.swagger_dir, "cases/test_%s" % self.swagger_dir)
        # abs_path = self.save_file(template_scenario_file, py_name, save_dir)
        # print("[%s]TestCase func template gen success. Path:%s" % (py_name, abs_path))

    def genConftestTemplate(self, product_name):
        """ 生成conftest模板"""
        with open(os.path.join(config.code_gen_path, 'swagger/conftest_template.tmp'), 'r') as f:
            template_all = f.read()
        with open(os.path.join(config.code_gen_path, 'swagger/conftest_template_func.tmp'), 'r') as f:
            template_func = f.read()

        temp_all = copy.deepcopy(template_all)
        func_template = ""
        import_str = ""
        for srv_name, srvInfo in self.collections.items.items():
            temp_func_str = copy.deepcopy(template_func)
            import_str += "from defines.%s.%s_service_business import %sSwaggerBusiness\n" % (
                self.swagger_dir, self.getSrvName(srv_name).lower(), self.getSrvName(srv_name))

            temp_func_str = temp_func_str.replace('$$%%API_OBJ%%$$', "%sApi" % self.getSrvName(srv_name))
            temp_func_str = temp_func_str.replace('$$%%API_NAME%%$$', "%sApi" % self.getSrvName(srv_name))
            temp_func_str = temp_func_str.replace('$$%%CLASS_NAME%%$$', "%s" % self.getSrvName(srv_name))
            func_template += temp_func_str
        temp_all = temp_all.replace('$$%%API_OBJ_FUNCTION%%$$', func_template)
        temp_all = temp_all.replace('$$%%API_IMPORT_LIST%%$$', import_str)

        py_name = "conftest.py"
        save_dir = os.path.join(config.temp_template_path, self.swagger_dir, "cases/test_%s" % self.swagger_dir)
        abs_path = self.save_file(temp_all, py_name, save_dir)
        print("[%s]Conftest template gen success. Path:%s" % (py_name, abs_path))

    def genSwagger(self, name, swagger_dir):
        ef = ExtFunctionInfo()
        ef.isRequestOpened = True
        collections = load_swagger(swagger_dir)
        collections.init(self, ext_info=ef)

        interface_list = []
        for srv_name, srvInfo in collections.items.items():
            for method_name, methodInfo in srvInfo.items():
                interface_list.append((srv_name, method_name))

        for srv_name, method_name in interface_list:
            intef = collections.interface(srv_name, method_name)
            if getattr(intef, 'request', None):
                ef.addRequest(intef)  # 将接口放到请求队列中
                # resp = intef.request()

        ef.genPostManFile(name)

    def getMethodNameLower(self, method_name, srv_name=None):
        """"""
        if len(method_name.split("_")) >= 2:
            srv_name = method_name.split("_")[0]
            m_name = method_name.split("_")[-1]
            srv_name = srv_name[0].lower() + srv_name[1:]
            m_name = m_name[0].lower() + m_name[1:]
            return "%s_%s" % (srv_name, m_name)
        else:
            if srv_name:
                srv_name = srv_name[0].lower() + srv_name[1:]
                m_name = method_name[0].lower() + method_name[1:]
                return "%s_%s" % (srv_name, m_name)
            else:
                return method_name[0].lower() + method_name[1:]

    def genNebulaDefineTemplate(self, product_name):
        """ 生成Api模板"""
        with open(os.path.join(config.code_gen_path, 'swagger/nebula_defines_template_func.tmp'), 'r') as f:
            template_func = f.read()
        for srv_name, srvInfo in self.collections.items.items():
            template_all = ""
            func_template = ""
            for method_name, methodInfo in srvInfo.items():
                temp_func_str = copy.deepcopy(template_func)
                # if methodInfo['operationId'] == 'AccountService_UpdateRole':
                #     i = 1
                intef = self.collections.interface(srv_name, method_name)
                desc_str = ""
                if 'summary' in methodInfo:
                    desc_str = methodInfo['summary'] if len(methodInfo['summary']) <=50 else "%s..." % methodInfo['summary'][:50]

                # temp_func_str = temp_func_str.replace('$$%%SWAGGER_NAME%%$$', srv_name)

                temp_func_str = temp_func_str.replace('$$%%FUNC_NAME%%$$', self.getMethodNameLower(method_name, srv_name=srv_name))
                temp_func_str = temp_func_str.replace('$$%%DESC%%$$', desc_str)
                if len(method_name.split("_")) > 1:
                    module_name = method_name.split("_")[0]
                else:
                    module_name = srv_name
                temp_func_str = temp_func_str.replace('$$%%MODULE_NAME%%$$', module_name)
                temp_func_str = temp_func_str.replace('$$%%METHOD_NAME%%$$', methodInfo['method'])
                param_str = ""
                param_list_str = ""
                param_code_str = ""
                param_dict = {}
                full_path_code_str = ""
                param_name_list = []
                if '}' in methodInfo['path']:
                    pattern = re.compile(r'\{(.*?)\}')
                    full_param_list = pattern.findall(methodInfo['path'])
                    for full_param in full_param_list:
                        if full_param in param_name_list:
                            continue
                        param_list_str += ", %s" % full_param
                        full_path_code_str += "        intef.set_path_param(\"%s\", %s)\n" % (full_param, full_param)
                        param_name_list.append(full_param)
                        intef.set_path_param(full_param, "%s")
                    intef.fill_path()

                if methodInfo['method'] in ['get', 'delete']:
                    if 'parameters' in methodInfo and methodInfo['parameters']:
                        for param_info in methodInfo['parameters']:
                            if param_info['in'] != 'query':
                                continue
                            description = param_info['description'] if 'description' in param_info else "null"
                            _type = param_info['type'] if 'type' in param_info else "undefined"
                            required = "*" if 'required' in param_info and param_info['required'] is True else ""
                            param_str += " " * 16 + '%s参数名称：%s　类型：%s　描述：%s\n' % (
                                required, param_info['name'], _type, description)
                            param_list_str += ", %s=None" % self.filter_str(param_info['name'])
                            param_code_str += "        intef.update_params(\"%s\", %s)\n" % (param_info['name'],
                                                                                             self.filter_str(param_info['name']))
                            param_dict[param_info['name']] = ""
                    if param_str.endswith('\n'):
                        param_str = param_str[:-2]
                    param_str = "params: \n%s" % param_str
                body_str = ""
                body_code_str = ""

                if methodInfo['method'] in ['post', 'put', 'patch']:
                    if intef.body:
                        if 'header' in intef.body:
                            intef.update_body('header')  # 移除header
                        for key, value in intef.body.items():
                            if key not in param_name_list:
                                param_list_str += ", %s=None" % key
                            body_code_str += "        intef.update_body(\"%s\", %s)\n" % (key, key)

                    body_str = json.dumps(intef.body, sort_keys=True, indent=4)
                    body_str = body_str.replace('\n' + ' ' * 4, '\n' + ' ' * 12)
                    # body_str = " " * 8 + body_str
                    if body_str.endswith('\n}'):
                        body_str = body_str[:-2] + '\n' + ' ' * 8 + '}'
                    # body_str = "body: \n%s" % body_str

                resp_dict = intef.responses
                response_str = ""
                if resp_dict:
                    response_str = "resp:\n"
                    for status_code, info in resp_dict.items():
                        temp_str = json.dumps(info["info"], sort_keys=True, indent=4)
                        temp_str = temp_str.replace('\n' + ' ' * 4, '\n' + ' ' * 20)
                        temp_str = " " * 16 + temp_str
                        if temp_str.endswith('\n}'):
                            temp_str = temp_str[:-2] + '\n' + ' ' * 16 + '}'
                        response_str += " " * 16 + "%s(%s):\n%s\n" % (status_code, info["description"], temp_str)

                param_dict_str = json.dumps(param_dict, sort_keys=True, indent=4)
                param_dict_str = param_dict_str.replace('\n' + ' ' * 4, '\n' + ' ' * 12)
                # param_dict_str = " " * 16 + param_dict_str
                if param_dict_str.endswith('\n}'):
                    param_dict_str = param_dict_str[:-2] + '\n' + ' ' * 8 + '}'
                body_str = "{}" if not body_str else body_str
                param_dict_str = "{}" if not param_dict_str else param_dict_str
                temp_func_str = temp_func_str.replace('$$%%DATA_DICT%%$$', body_str)
                temp_func_str = temp_func_str.replace('$$%%PARAMS_DICT%%$$', param_dict_str)
                temp_func_str = temp_func_str.replace('$$%%URL%%$$', intef.path)

                func_template += temp_func_str + "\n"
            # temp_all = temp_all.replace('$$%%API_FUNCTION%%$$', func_template)
            # temp_all = temp_all.replace('$$%%SWAGGER_NAME%%$$', srv_name)
            # temp_all = temp_all.replace('$$%%CLASS_NAME%%$$', srv_name.capitalize())

            py_name = "%s_define.py" % self.getSrvName(srv_name)
            save_dir = os.path.join(config.temp_template_path, self.swagger_dir, "defines")
            abs_path = self.save_file(func_template, py_name, save_dir)
            print("[%s]Api template gen success. Path:%s" % (py_name, abs_path))


    def genNebulaApiTemplate(self, product_name):
        """ 生成Api模板"""
        with open(os.path.join(config.code_gen_path, 'swagger/nebula_api_template.tmp'), 'r') as f:
            template_all = f.read()
        with open(os.path.join(config.code_gen_path, 'swagger/nebula_api_template_func.tmp'), 'r') as f:
            template_func = f.read()
        template_all = template_all.replace('$$%%SWAGGER_DIR%%$$', self.swagger_dir)
        for srv_name, srvInfo in self.collections.items.items():
            temp_all = copy.deepcopy(template_all)
            func_template = ""
            for method_name, methodInfo in srvInfo.items():
                # if methodInfo['operationId'] == 'AccountService_UpdateRole':
                #     i = 1
                intef = self.collections.interface(srv_name, method_name)

                temp_func_str = copy.deepcopy(template_func)

                desc_str = ""
                if 'summary' in methodInfo:
                    desc_str = methodInfo['summary'] if len(methodInfo['summary']) <=50 else "%s..." % methodInfo['summary'][:50]
                # temp_func_str = temp_func_str.replace('$$%%SWAGGER_NAME%%$$', srv_name)
                # temp_func_str = temp_func_str.replace('$$%%API_NAME%%$$', method_name)
                # temp_func_str = temp_func_str.replace('$$%%TITLE%%$$', "path: [%s]%s" % (methodInfo['method'], methodInfo['path']))
                temp_func_str = temp_func_str.replace('$$%%DESC%%$$', desc_str)
                temp_func_str = temp_func_str.replace('$$%%FUNC_NAME%%$$', self.getMethodNameLower(method_name, srv_name=srv_name))

                param_str = ""
                param_list_str = ""
                param_code_str = ""
                full_path_code_str = ""
                param_name_list = []
                if '}' in methodInfo['path']:
                    pattern = re.compile(r'\{(.*?)\}')
                    full_param_list = pattern.findall(methodInfo['path'])
                    for full_param in full_param_list:
                        if full_param in param_name_list:
                            continue
                        param_list_str += ", %s" % full_param
                        full_path_code_str += "%s," % full_param
                        param_name_list.append(full_param)
                if methodInfo['method'] in ['get', 'delete']:
                    if 'parameters' in methodInfo and methodInfo['parameters']:
                        for param_info in methodInfo['parameters']:
                            if param_info['in'] != 'query':
                                continue
                            description = param_info['description'] if 'description' in param_info else "null"
                            _type = param_info['type'] if 'type' in param_info else "undefined"
                            required = "*" if 'required' in param_info and param_info['required'] is True else ""
                            param_str += " " * 16 + '%s参数名称：%s　类型：%s　描述：%s\n' % (
                                required, param_info['name'], _type, description)
                            param_list_str += ", %s=None" % self.filter_str(param_info['name'])
                            param_code_str += "        param[\"params\"][\"%s\"] = %s\n" % (param_info['name'],
                                                                                          self.filter_str(param_info['name']))
                    if param_str.endswith('\n'):
                        param_str = param_str[:-2]
                    param_str = "params: \n%s" % param_str
                body_str = ""
                body_code_str = ""

                if methodInfo['method'] in ['post', 'put', 'patch']:
                    if intef.body:
                        if 'header' in intef.body:
                            intef.update_body('header')  # 移除header
                        for key, value in intef.body.items():
                            if key not in param_name_list:
                                param_list_str += ", %s=None" % key
                            body_code_str += "        param[\"data\"][\"%s\"] = %s\n" % (key, key)

                    body_str = json.dumps(intef.body, sort_keys=True, indent=4)
                    body_str = body_str.replace('\n' + ' ' * 4, '\n' + ' '* 20)
                    body_str = " " * 16 + body_str
                    if body_str.endswith('\n}'):
                        body_str = body_str[:-2] + '\n' + ' ' * 16 + '}'
                    body_str = "body: \n%s" % body_str

                resp_dict = intef.responses
                response_str = ""
                if resp_dict:
                    response_str = "resp:\n"
                    for status_code, info in resp_dict.items():
                        temp_str = json.dumps(info["info"], sort_keys=True, indent=4)
                        temp_str = temp_str.replace('\n' + ' ' * 4, '\n' + ' ' * 20)
                        temp_str = " " * 16 + temp_str
                        if temp_str.endswith('\n}'):
                            temp_str = temp_str[:-2] + '\n' + ' ' * 16 + '}'
                        response_str += " " * 16 + "%s(%s):\n%s\n" % (status_code, info["description"], temp_str)

                if full_path_code_str:
                    full_path_code_str = "        param[\"url\"] = param[\"url\"] %% (%s)\n" % full_path_code_str[:-1]
                temp_func_str = temp_func_str.replace('$$%%PATH_CODE%%$$\n', full_path_code_str)
                temp_func_str = temp_func_str.replace('$$%%PARAM_CODE%%$$\n', param_code_str)
                temp_func_str = temp_func_str.replace('$$%%BODY_CODE%%$$\n', body_code_str)
                temp_func_str = temp_func_str.replace('$$%%PARAM_FUNC_LIST%%$$', param_list_str)
                # temp_func_str = temp_func_str.replace('$$%%PARAM_LIST%%$$', param_list_str.lstrip(", "))

                # temp_func_str = temp_func_str.replace('$$%%STRUCTURE%%$$', param_str + body_str)
                # temp_func_str = temp_func_str.replace('$$%%RESPONSE%%$$', response_str)
                # temp_func_str = temp_func_str.replace('$$%%FULL_PATH_CODE%%$$\n', full_path_code_str)

                func_template += temp_func_str
            temp_all = temp_all.replace('$$%%API_FUNCTION%%$$', func_template)
            # temp_all = temp_all.replace('$$%%SWAGGER_NAME%%$$', srv_name)
            temp_all = temp_all.replace('$$%%CLASS_NAME%%$$', self.getSrvName(srv_name))

            py_name = "%s__init__.py" % self.getSrvName(srv_name)
            save_dir = os.path.join(config.temp_template_path, self.swagger_dir, "init/%s" % self.swagger_dir)
            abs_path = self.save_file(temp_all, py_name, save_dir)
            print("[%s]Nebula Api template gen success. Path:%s" % (py_name, abs_path))


if __name__ == '__main__':
    gts = GenTemplatePostmanTool('nebula_final')
    # gts.genSwagger("nebula", 'nebula')
    # gts = GenTemplateSwaggerTool('minos')
    gts.init_collections()
    gts.genApiTemplate('a')
    gts.genTestCaseTemplate('a')
    # gts.genConftestTemplate('a')

    # gts.genNebulaDefineTemplate("")
    # gts.genNebulaApiTemplate("")