#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   grpc_tools.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/12/17 下午6:10   wangan      1.0         None
'''

from commonlib import time_utils
from commonlib.api_lib.tools.gen_postman import GenPostManTool
from commonlib.api_lib.tools.gen_template import GenTemplateSwaggerTool


def gen_swagger(host=None, name=None, sdir=None, file=None):
    """ 生成swagger
    :param product_name:
    :return:
    """
    if not name:
        name = "postman_by_swagger_%s" % time_utils.get_time_str()
    if not host:
        host = "127.0.0.1"
    GenPostManTool(host=host).genSwagger(name, sdir, file=file)


def list_swagger(sdir=None):
    """ 列出swagger path"""
    GenPostManTool(host="127.0.0.1").listSwaggerPath(sdir)


def update_swagger_json(sdir=None, chromeversion=None, file=None, username=None, password=None):
    """　更新swagger json"""
    """ 适用于从远程地址获取swagger.json文档的情况,使用前需要在swagger目录下创建remote_swagger.csv文件
        文件格式:　名字,地址
    """
    if not chromeversion:
        chromeversion = "110"
    GenPostManTool().updateRemoteSwagger(sdir, driverversion=chromeversion, swagger_file=file,  username=username,
                                         password=password)


def gen_api_template(swagger_path=None):
    """ 生成api文件的模板"""
    gts = GenTemplateSwaggerTool(swagger_path)
    gts.init_collections()
    gts.genApiTemplate('')


def gen_case_template(swagger_path=None):
    """ 生成case文件的模板"""
    gts = GenTemplateSwaggerTool(swagger_path)
    gts.init_collections()
    gts.genTestCaseTemplate('')


def gen_conftest_template(swagger_path=None):
    """ 生成conftest文件的模板"""
    gts = GenTemplateSwaggerTool(swagger_path)
    gts.init_collections()
    gts.genConftestTemplate('')


def gen_all_template(swagger_path=None):
    """ 生成conftest文件的模板"""
    gts = GenTemplateSwaggerTool(swagger_path)
    gts.init_collections()
    gts.genApiTemplate('')
    gts.genApiBusinessTemplate('')
    gts.genTestCaseTemplate('')
    gts.genConftestTemplate('')

def gen_nebula_template(swagger_path=None):
    """ 生成nebula文件的模板"""
    gts = GenTemplateSwaggerTool(swagger_path)
    gts.init_collections()
    gts.genNebulaApiTemplate('')
    gts.genNebulaDefineTemplate('')



if __name__ == '__main__':
    gen_swagger(name='belt', sdir='belt')
    # gen_all_template('belt')