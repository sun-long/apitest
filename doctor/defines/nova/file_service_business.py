#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from commonlib import config
from defines.nova.api.file_service_swagger import FileSwaggerApi
import time
import os
"""
使用说明：


"""
def getFileStatusUntilReadyFunc(resp):
    """ 判断文件状态"""
    if resp.status_code == 200 and \
            resp.json_get("file.status") in ["INVALID", "VALID"]:
        return True
    else:
        return False

def getFileStatusUntilInvalidFunc(resp):
    """ 判断文件状态"""
    if resp.status_code == 200 and \
            resp.json_get("file.status") in ["INVALID"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("file.status") in ["VALID"]:
        raise Exception("file状态为%s!" % resp.json_get("file.status"))
    else:
        return False

def getFileStatusUntilValidFunc(resp):
    """ 判断文件状态"""
    if resp.status_code == 200 and \
            resp.json_get("file.status") in ["VALID"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("file.status") in ["INVALID"]:
        raise Exception("file状态为%s!" % resp.json_get("file.status"))
    else:
        return False


class FileSwaggerBusiness(FileSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(FileSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Sensenova-Signature"  # 默认token的key
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        time.sleep(1)

    @wait(timeout=180, interval=2, util_func=getFileStatusUntilInvalidFunc, raise_exception=True)
    def getFileStatusUntilInvalid(self, file_id):
        """ 查询文件状态为invalid"""
        return self.FileService_GetFileGetApi(file_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getFileStatusUntilValidFunc, raise_exception=True)
    def getFileStatusUntilValid(self, file_id):
        """ 查询文件状态为Valid"""
        return self.FileService_GetFileGetApi(file_id, print_log=False)

    @wait(timeout=1800, interval=2, util_func=getFileStatusUntilReadyFunc, raise_exception=True)
    def getFileStatusUntilReady(self, file_id):
        """ 查询文件状态为Valid 或 Invalid"""
        return self.FileService_GetFileGetApi(file_id, print_log=False)

    def createFile(self, file_name, description=None, scheme=None, is_delete=True, check_ready_status=True):
        """ 创建dataset,拥有cleanup功能"""
        file_path = os.path.join(config.nova_path, file_name)
        resp = self.uploadPostApi(file_path, description=description, scheme=scheme)
        assert resp.status_code == 200
        file_id = resp.json_get("id")
        # 添加clear up
        def clearUp():
            self.FileService_DeleteFileDeleteApi(file_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        # 校验状态
        status = None
        if check_ready_status:
            resp = self.getFileStatusUntilReady(file_id)
            status = resp.json_get("file.status")

        return file_id, status

    def createDatasetFile(self, file_name, description=None, is_delete=True, check_ready_status=True):
        """ 创建数据集文件"""
        return self.createFile(file_name, description=description, scheme="FINE_TUNE_1", is_delete=is_delete, check_ready_status=check_ready_status)

    def createKbsFile(self, file_name, description=None, is_delete=True):
        """ 创建知识库文件"""
        return self.createFile(file_name, description=description, scheme="KNOWLEDGE_BASE_1", is_delete=is_delete)

    def createImgFile(self, file_name, description=None, is_delete=True, check_ready_status=True):
        """ 创建数据集文件"""
        return self.createFile(file_name, description=description, scheme="FINE_TUNE_IMGEN_1", is_delete=is_delete, check_ready_status=check_ready_status)

    def createPdfFile(self, file_name, description=None, is_delete=True):
        """ 创建Pdf文件"""
        return self.createFile(file_name, description=description, scheme="KNOWLEDGE_BASE_PDF", is_delete=is_delete)
