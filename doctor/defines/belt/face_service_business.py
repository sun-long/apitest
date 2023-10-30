#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
from commonlib import config
from commonlib.decorator import wait
from defines.belt.api.face_service_swagger import FaceSwaggerApi
from pytest_check import check
import random

"""
使用说明：


"""


class FaceSwaggerBusiness(FaceSwaggerApi):
    """ 业务类代码写在这里"""

    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(FaceSwaggerBusiness, self).__init__(
            host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(
                self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        if inte_obj.path == '/v1/face/detect_liveness':
            inte_obj.set_headers('X-Belt-Action', 'DetectLiveness')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/face/compare_image':
            inte_obj.set_headers('X-Belt-Action', 'CompareImage')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/face/add_person':  
            inte_obj.set_headers('X-Belt-Action', 'AddPerson')
            inte_obj.set_headers('X-Belt-Version', 'v1')  
        elif inte_obj.path == '/v1/face/add_person_face':  
            inte_obj.set_headers('X-Belt-Action', 'AddPersonFace')
            inte_obj.set_headers('X-Belt-Version', 'v1') 
        elif inte_obj.path == '/v1/face/create_person_db':  
            inte_obj.set_headers('X-Belt-Action', 'CreatePersonDB')
            inte_obj.set_headers('X-Belt-Version', 'v1') 
        elif inte_obj.path == '/v1/face/create_tag':  
            inte_obj.set_headers('X-Belt-Action', 'CreateTag')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/face/delete_person':  
            inte_obj.set_headers('X-Belt-Action', 'DeletePerson')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/face/delete_person_db':  
            inte_obj.set_headers('X-Belt-Action', 'DeletePersonDB')
            inte_obj.set_headers('X-Belt-Version', 'v1')  
        elif inte_obj.path == '/v1/face/delete_person_face':  
            inte_obj.set_headers('X-Belt-Action', 'DeletePersonFace')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/face/delete_tag':  
            inte_obj.set_headers('X-Belt-Action', 'DeleteTag')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/face/get_person':  
            inte_obj.set_headers('X-Belt-Action', 'GetPerson')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/face/list_person':  
            inte_obj.set_headers('X-Belt-Action', 'ListPerson')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/face/list_person_db':  
            inte_obj.set_headers('X-Belt-Action', 'ListPersonDB')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/face/list_tag':  
            inte_obj.set_headers('X-Belt-Action', 'ListTag')
            inte_obj.set_headers('X-Belt-Version', 'v1') 
        elif inte_obj.path == '/v1/face/search_person':  
            inte_obj.set_headers('X-Belt-Action', 'SearchPerson')
            inte_obj.set_headers('X-Belt-Version', 'v1') 
        elif inte_obj.path == '/v1/face/update_person':  
            inte_obj.set_headers('X-Belt-Action', 'UpdatePerson')
            inte_obj.set_headers('X-Belt-Version', 'v1') 
        elif inte_obj.path == '/v1/face/update_person_db':  
            inte_obj.set_headers('X-Belt-Action', 'UpdatePersonDB')
            inte_obj.set_headers('X-Belt-Version', 'v1')                                                                                               
        #qps limit 5/s
        time.sleep(0.2)    

    def idsImageToBase64(self, image_name):
        return self.imageToBase64(os.path.join(config.ids_image_path, image_name))

    def randomSelectOneImage(self, srcPath):
        """从srcPath中随机挑选一张图片"""
        fileNames=[]
        for root, dirs, files in os.walk(srcPath): 
            for file in files:
                if file.split('.')[-1] =="jpg":
                    fileName=os.path.join(root,file)
                fileNames.append(fileName)
        randomfile=random.choice(fileNames)
        return randomfile

    def transfromNameToId(self,tag_names,correlationBetweenNameAndId):
        """输入tags的名字，根据name和id的关联关系,输出tags对应的id
        param:tag_names:[t1,t2]
        param:correlationBetweenNameAndId:
                                    {"t1":"123",
                                     "t2":"156",
                                     "t3":"234"}
        param:return:tag_ids:["123","156"]
        """
        tag_ids=[]
        for tag_name in tag_names:
            for name ,id in correlationBetweenNameAndId.items():
                if tag_name==name:
                    tag_ids.append(id)
        return tag_ids


    def newDB(self):
        """创建用于测试的db库，如果存在则删掉，重新创建，返回创建的db_id"""
        name="test_db_search_person"
        description = "用于测试人员搜索创建的库"
        resp = self.FaceService_CreatePersonDBPostApi(name=name, description=description)
        if resp.status_code==200:
            db_id=resp.json_get("id")
            return db_id
        else:
            if "person db name already exists" in resp.resp_json["error"]["message"]:
                #找到test_db_search_person对应的db_id
                page_offset = 0
                page_limit = 100
                resp = self.FaceService_ListPersonDBGetApi(page_offset=page_offset, page_limit=page_limit)
                person_dbs=resp.json_get("person_dbs")
                exist_db_id=None
                for person_db in person_dbs:
                    if "test_db_search_person"==person_db["name"]:
                        exist_db_id=person_db["id"]
                if exist_db_id:
                    #删除库
                    self.FaceService_DeletePersonDBPostApi(id=exist_db_id)      
                #重新创建库
                name="test_db_search_person"
                description = "用于测试人员搜索创建的库"
                resp = self.FaceService_CreatePersonDBPostApi(name=name, description=description)
                if resp.status_code==200:
                    db_id=resp.json_get("id")
                    return db_id

    def compareImage(self, base_image=None, image=None, auto_rotate=False, min_quality_level=None, encrypt_info=None):
        """ 比较两个图片"""
        if base_image and not base_image.startswith("/"):
            base_image = self.idsImageToBase64(base_image)
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        if not min_quality_level:
            min_quality_level = "QUALITY_LEVEL_NONE"
        if not encrypt_info:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.FaceService_CompareImagePostApi(image=image, base_image=base_image, auto_rotate=auto_rotate,
                                                    min_quality_level=min_quality_level, encrypt_info=encrypt_info)
        return resp
    
    def clearDBs(self):
        """清理测试执行创建未删除的db"""
        resp = self.FaceService_ListPersonDBGetApi(page_offset=0, page_limit=10)
        if "total" in resp.json_get("page"):
            person_dbs=resp.json_get("person_dbs")
            total = resp.json_get("page.total")
        else:
            total = 0  
        
        while total>0:
  
            for db in person_dbs:
                self.FaceService_DeletePersonDBPostApi(id=db["id"])    
            #time.sleep(3)    
            resp = self.FaceService_ListPersonDBGetApi(page_offset=0, page_limit=10) 
            if "total" in resp.json_get("page"):
                person_dbs=resp.json_get("person_dbs")
                total = resp.json_get("page.total") 
            else:
                total = 0
                