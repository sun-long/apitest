#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time
from commonlib import config, utils
from commonlib.decorator import wait
from defines.nova.api.kbs_service_swagger import KbsSwaggerApi
from commonlib.log_utils import log


"""
使用说明：


"""

def getKbsTaskUntilFileVALIDFunc(resp):
    """ 判断kbs文件状态"""
    if resp.status_code == 200 and \
            resp.json_get("knowledge_base.files.0.status") in ["VALID"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["INVALID"]:
        raise Exception("kbs文件状态为%s!" % resp.json_get("knowledge_base.status"))
    else:
        return False

def getKbsTaskUntilFileINVALIDFunc(resp):
    """ 判断kbs文件状态"""
    if resp.status_code == 200 and \
            resp.json_get("knowledge_base.files.0.status") in ["INVALID"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["VALID"]:
        raise Exception("kbs任务状态为%s!" % resp.json_get("knowledge_base.status"))
    else:
        return False

def getKbsTaskUntilFileUploadedFunc(resp):
    """ 判断serving运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("knowledge_base.files.0.status") in ["UPLOADED", "INVALID", "VALID"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["INVALID"]:
        raise Exception("kbs任务状态为%s!" % resp.json_get("knowledge_base.status"))
    else:
        return False

def getKbsTaskUntilReadyFunc(resp):
    """ 判断serving运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["AVAILABLE", "UNAVAILABLE"]:
        return True
    else:
        return False

def getKbsTaskUntilLoadingFunc(resp):
    """ 判断serving运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["LOADING"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["UNAVAILABLE", "AVAILABLE"]:
        raise Exception("kbs任务状态为%s!" % resp.json_get("knowledge_base.status"))
    else:
        return False

def getKbsTaskUntilAVAILABLEFunc(resp):
    """ 判断serving运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["AVAILABLE",]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["UNAVAILABLE"]:
        raise Exception("kbs任务状态为%s!" % resp.json_get("knowledge_base.status"))
    else:
        return False

def getKbsTaskUntilUNAVAILABLEFunc(resp):
    """ 判断serving运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["UNAVAILABLE"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("knowledge_base.status") in ["AVAILABLE"]:
        raise Exception("kbs任务状态为%s!" % resp.json_get("knowledge_base.status"))
    else:
        return False

class KbsSwaggerBusiness(KbsSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(KbsSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Sensenova-Signature" # 默认token的key
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        # 限流1qps    
        time.sleep(1)        

    @wait(timeout=180, interval=2, util_func=getKbsTaskUntilFileUploadedFunc, raise_exception=True)
    def getKbsTaskUntilFileUploaded(self, kbs_id):
        """ 查询kbs任务直到文件uploaded"""
        return self.KnowledgeBaseService_GetKnowledgeBaseByIDGetApi(kbs_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getKbsTaskUntilFileINVALIDFunc, raise_exception=True)
    def getKbsTaskUntilFileINVALID(self, kbs_id):
        """ 查询kbs任务直到文件uploaded"""
        return self.KnowledgeBaseService_GetKnowledgeBaseByIDGetApi(kbs_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getKbsTaskUntilFileVALIDFunc, raise_exception=True)
    def getKbsTaskUntilFileVALID(self, kbs_id):
        """ 查询kbs任务直到文件valid"""
        return self.KnowledgeBaseService_GetKnowledgeBaseByIDGetApi(kbs_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getKbsTaskUntilReadyFunc, raise_exception=True)
    def getKbsTaskUntilReady(self, kbs_id):
        """ 查询kbs任务直到任务终态"""
        return self.KnowledgeBaseService_GetKnowledgeBaseByIDGetApi(kbs_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getKbsTaskUntilAVAILABLEFunc, raise_exception=True)
    def getKbsTaskUntilAVAILABLE(self, kbs_id):
        """ 查询kbs任务直到任务available"""
        return self.KnowledgeBaseService_GetKnowledgeBaseByIDGetApi(kbs_id, print_log=False)

    @wait(timeout=180, interval=0.5, util_func=getKbsTaskUntilLoadingFunc, raise_exception=True)
    def getKbsTaskUntilLoading(self, kbs_id):
        """ 查询kbs任务直到任务loading"""
        return self.KnowledgeBaseService_GetKnowledgeBaseByIDGetApi(kbs_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getKbsTaskUntilUNAVAILABLEFunc, raise_exception=True)
    def getKbsTaskUntilUNAVAILABLE(self, kbs_id):
        """ 查询Kbs任务直到任务unavailable"""
        return self.KnowledgeBaseService_GetKnowledgeBaseByIDGetApi(kbs_id, print_log=False)

    def createKbs(self, file_name, description=None, is_delete=True, wait_available=True):
        """ 创建知识库"""
        # 1. 创建知识库
        resp = self.KnowledgeBaseService_CreateKnowledgeBasePostApi(description=description)
        create_resp = resp
        assert resp.status_code == 200
        kbs_id = resp.json_get("data.id")

        # 4. 给知识库添加文件
        resp = self.KnowledgeBaseService_CreateKnowledgeBaseFilesPostApi(kbs_id, description=description)
        assert resp.status_code == 200
        file_id = resp.json_get("id")
        url = resp.json_get("url")

        # 6. （手动）上传文件
        file_path = os.path.join(config.nova_path, file_name)
        utils.upload_file(url, file_path)

        if wait_available:
            self.getKbsTaskUntilFileUploaded(kbs_id)
            self.getKbsTaskUntilAVAILABLE(kbs_id)

        # 添加clear up
        def clearUp():
            self.KnowledgeBaseService_DeleteKnowledgeBaseDeleteApi(kbs_id)

        if self.ext_info and is_delete and kbs_id:
            self.ext_info.addAfterFunc(clearUp)

        return create_resp

    def createKbsWithFiles(self, files, description=None, is_delete=True, wait_available=True, wait_unavailable=False):
        """ 创建知识库-通过文件"""
        # 1. 创建知识库
        resp = self.KnowledgeBaseService_CreateKnowledgeBasePostApi(description=description, files=files)
        assert resp.status_code == 200
        kbs_id = resp.json_get("knowledge_base.id")

        # 添加clear up
        def clearUp():
            self.KnowledgeBaseService_DeleteKnowledgeBaseDeleteApi(kbs_id)

        if self.ext_info and is_delete and kbs_id:
            self.ext_info.addAfterFunc(clearUp)
        self.getKbsTaskUntilReady(kbs_id)

        return kbs_id

    def KnowledgeBaseService_DownloadKnowledgeBaseFilesGetApi(self, knowledge_base_id, file_id, loginToken=None,
                                                                  sendRequest=True, print_log=True,
                                                                  interface_desc=None):
        """  获取知识库文件的下载地址 该接口参数校验通过后，会以 HTTP 302 方式返回下载链接 """
        """  path: [get]/v1/llm/knowledge-bases/{knowledge_base_id}/files/{file_id} API """
        time.sleep(1)
        import requests
        if loginToken:
            token = loginToken
        else:
            token = self.token
        url = "%s/v1/llm/knowledge-bases/%s/files/%s" % (self.host, knowledge_base_id, file_id)
        payload = {}
        headers = {
            'Authorization': 'Bearer %s' % token
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response



