#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from commonlib import utils
from defines.belt.api.argusdb_service_swagger import ArgusdbSwaggerApi


"""
使用说明：


"""


class ArgusdbSwaggerBusiness(ArgusdbSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(ArgusdbSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息
        self.configMap = utils.readConfigMap("argus.yaml", "http://db-proxy.argus:20000")

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        # self.set_interface_prefix_path(inte_obj)
        self.set_belt_defines(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

    def CreateStreamGroup(self, ak=None, bind_groups=None, expired_time=None,
                          group_mold=None, group_name=None, group_size=None,
                          group_tag=None, merge_cb_url=None,save_image_option=None,
                          pedes_cb_url=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None,
                          is_delete=True):
        """ 动态库创建 """
        resp =  self.DB_CreateStreamGroupPostApi(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                                group_mold=group_mold, group_name=group_name,
                                                group_size=group_size, group_tag=group_tag,save_image_option=save_image_option,
                                                merge_cb_url=merge_cb_url, pedes_cb_url=pedes_cb_url, loginToken=loginToken,
                                                sendRequest=sendRequest, print_log=print_log, interface_desc=interface_desc)
        # 添加clear up
        def clearUp():
            if resp.status_code == 200 and resp.json_get("error_code") == 0:
                group_id = resp.json_get("group_id")
                self.DB_DeleteStreamGroupPostApi(ak=ak, group_id=group_id, loginToken=loginToken)


        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        return resp

    def CreateStaticGroup(self, ak=None, group_mold=None, group_name=None,
                          group_size=None, group_tag=None, pedes_cb_url=None,
                          loginToken=None, sendRequest=True,save_image_option=None,
                          print_log=True, interface_desc=None, is_delete=True):
       """ 静态库创建 """
       resp = self.DB_CreateStaticGroupPostApi(ak=ak, group_name=group_name, group_mold=group_mold,save_image_option=save_image_option,
                                               group_tag=group_tag, group_size=group_size, pedes_cb_url=pedes_cb_url,
                                               loginToken=loginToken, sendRequest=sendRequest, print_log=print_log,
                                               interface_desc=interface_desc)
       # 添加clear up
       def clearUp():
           if sendRequest and resp.status_code == 200 and resp.json_get("error_code") == 0:
               group_id = resp.json_get("group_id")
               self.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id, loginToken=loginToken)

       if self.ext_info and is_delete:
           self.ext_info.addAfterFunc(clearUp)

       return resp

    def CreatePersonPostFromFile(self, file_path, ak=None, bounding=None, group_id=None, image=None, override=None,
                                 person_id=None, loginToken=None, sendRequest=True, print_log=True,
                                 interface_desc=None):
        """ 上传文件, 创建人员"""
        intef = self.DB_CreatePersonPostApi(ak=ak, bounding=bounding, group_id=group_id, image=image,
                                           override=override, person_id=person_id,
                                           loginToken=loginToken, sendRequest=False, print_log=print_log,
                                           interface_desc=interface_desc)
        intef.files["file"] = file_path
        return intef.request() if sendRequest else intef

    def SearchImagePostFromFile(self, file_path, ak=None, bounding=None, group_id=None, image=None,
                                threshold=None, top_k=None, loginToken=None, sendRequest=True,
                                print_log=True, interface_desc=None):
        """ 上传文件， 搜索图片"""
        intef = self.DB_SearchImagePostApi(ak=ak, bounding=bounding, group_id=group_id, image=image,
                                threshold=threshold, top_k=top_k, loginToken=loginToken, sendRequest=False,
                                print_log=print_log, interface_desc=interface_desc)
        intef.files["file"] = file_path
        return intef.request() if sendRequest else intef

    def UpdatePersonPostFromFile(self, file_path, ak=None, group_id=None, image=None, person_id=None, loginToken=None,
                                 sendRequest=True, print_log=True, interface_desc=None):
        """ 上传文件， 更新人员"""
        intef = self.DB_UpdatePersonPostApi(ak=ak, group_id=group_id, image=image, person_id=person_id, loginToken=loginToken,
                                 sendRequest=False, print_log=print_log, interface_desc=interface_desc)
        intef.files["file"] = file_path
        return intef.request() if sendRequest else intef

    def SearchImageMultiFaceFromFile(self, file_path, ak=None, bounding=None, group_id=None, image=None,
                                     threshold=None, top_k=None, loginToken=None, sendRequest=True,
                                     print_log=True, interface_desc=None):
        """ 上传文件， 搜索多脸"""
        intef = self.DB_SearchImageMultiFacePostApi(ak=ak, bounding=bounding, group_id=group_id, image=image,
                                     threshold=threshold, top_k=top_k, loginToken=loginToken, sendRequest=False,
                                     print_log=print_log, interface_desc=interface_desc)

        intef.files["file"] = file_path
        return intef.request() if sendRequest else intef