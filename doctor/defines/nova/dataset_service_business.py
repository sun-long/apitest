#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
from commonlib import utils
from commonlib.decorator import wait
from defines.nova.api.dataset_service_swagger import DatasetSwaggerApi


"""
使用说明：


"""


def getdatasetTaskUntilFileValidFunc(resp):
    """ 判断dataset运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("dataset.files.0.status") in ["VALID",]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("dataset.files.0.status") in ["INVALID"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("dataset.files.0.status"))
    else:
        return False

def getdatasetTaskUntilFileINVALIDFunc(resp):
    """ 判断dataset运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("dataset.files.0.status") in ["INVALID"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("dataset.files.0.status") in ["VALID"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("dataset.files.0.status"))
    else:
        return False

def getdatasetTaskUntilDatasetREADYFunc(resp):
    """ 判断dataset运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("dataset.status") in ["READY"]:
        return True
    else:
        return False


def getImgDatasetTaskUntilDatasetREADYFunc(resp):
    """ 判断dataset运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("dataset.status") in ["READY"]:
        return True
    else:
        return False

class DatasetSwaggerBusiness(DatasetSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(DatasetSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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

    @wait(timeout=180, interval=2, util_func=getdatasetTaskUntilFileValidFunc, raise_exception=True)
    def getdatasetTaskUntilFileUPLOADED(self, dataset_id):
        """ 查询dataset任务直到文件上传完成"""
        return self.NovaFinetunesDatasetService_GetNovaFinetunesDatasetGetApi(dataset_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getdatasetTaskUntilFileINVALIDFunc, raise_exception=True)
    def getdatasetTaskUntilFileINVALID(self, dataset_id):
        """ 查询dataset任务直到文件INVALID"""
        return self.NovaFinetunesDatasetService_GetNovaFinetunesDatasetGetApi(dataset_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getdatasetTaskUntilDatasetREADYFunc, raise_exception=True)
    def getdatasetTaskUntilDatasetREADY(self, dataset_id):
        """ 查询dataset任务直到任务ready"""
        return self.NovaFinetunesDatasetService_GetNovaFinetunesDatasetGetApi(dataset_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getImgDatasetTaskUntilDatasetREADYFunc, raise_exception=True)
    def getImgDatasetTaskUntilDatasetREADY(self, dataset_id):
        """ 查询dataset任务直到任务ready"""
        return self.NovaFinetunesDatasetService_GetImgenFinetuneDatasetGetApi(dataset_id, print_log=False)

    def createDataSets(self, file_path, description=None, is_delete=True):
        """ 创建dataset,拥有cleanup功能"""
        resp = self.NovaFinetunesDatasetService_CreateNovaFinetunesDatasetPostApi(description=description)
        assert resp.status_code == 200
        dataset_id = resp.json_get("dataset.id")

        resp = self.NovaFinetunesDatasetService_AddFileToNovaFinetunesDatasetPostApi(dataset_id, description="auto")
        assert resp.status_code == 200
        url = resp.json_get("url")
        file_id = resp.json_get("id")

        utils.upload_file(url, file_path)

        # 7. 根据datasetid查询dataset,文件上传成功
        self.getdatasetTaskUntilFileUPLOADED(dataset_id)
        # 7. 根据datasetid查询dataset,任务ready
        self.getdatasetTaskUntilDatasetREADY(dataset_id)
        # 添加clear up
        def clearUp():
            self.NovaFinetunesDatasetService_DeleteNovaFinetunesDatasetDeleteApi(dataset_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        return dataset_id

    def createDataSetsWithFiles(self, files, description=None, is_delete=True, wait_ready=True):
        """ 创建dataset,拥有cleanup功能"""
        resp = self.NovaFinetunesDatasetService_CreateNovaFinetunesDatasetPostApi(description=description, files=files)
        assert resp.status_code == 200
        dataset_id = resp.json_get("dataset.id")

        # 添加clear up
        def clearUp():
            self.NovaFinetunesDatasetService_DeleteNovaFinetunesDatasetDeleteApi(dataset_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)
        if wait_ready:
            self.getdatasetTaskUntilDatasetREADY(dataset_id)
        return dataset_id

    def createImgDataSetsWithFiles(self, files, description=None, is_delete=True):
        """ 创建dataset,拥有cleanup功能"""
        resp = self.NovaFinetunesDatasetService_CreateImgenFinetuneDatasetPostApi(description=description, files=files)
        assert resp.status_code == 200
        dataset_id = resp.json_get("dataset.id")

        # 添加clear up
        def clearUp():
            self.NovaFinetunesDatasetService_DeleteImgenFinetuneDatasetDeleteApi(dataset_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)
        return dataset_id

    def NovaFinetunesDatasetService_DownloadFileFromNovaFinetunesDatasetGetApi(self, id, file_id, loginToken=None):
        """ 下载数据集"""
        time.sleep(2)
        import requests
        if loginToken:
            token = loginToken
        else:
            token = self.token
        url = "%s/v1/llm/fine-tune/datasets/%s/files/%s" % (self.host, id, file_id)
        payload = {}
        headers = {
            'Authorization': 'Bearer %s' % token
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
