#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from pytest_check import check
from PIL import Image
class TestArgusPersonScenario(object):
    """ Argusrrs scenario test"""

    @pytest.fixture(scope="class", autouse=True)
    def init_func(self, config_obj):
        # 初始化测试集
        # 所有test运行前运行一次，接收外部参数env_obj，初始化测试环境
        log().info("==========%s测试开始==========" % self.__class__.__name__)

    def teardown_class(self):
        # 所有test运行完后运行一次
        log().info("==========%s测试结束==========\n" % self.__name__)
        log().info("clear tasks finish")

    def setup_method(self, method):
        # 每个测试用例执行之前做操作
        log().info("用例%s开始" % method.__name__)

    def teardown_method(self, method):
        # 每个测试用例执行之后做操作
        log().info("用例%s结束" % method.__name__)


    def test_scenario_person_000_personCreate(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ 测试api接口添加会员"""
        """
        1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        2. 测试api接口添加会员,传参image/override，期望添加成功 (上传文件)
        3. 测试api接口添加会员,传参file/override,期望添加成功 (base64)
        4. 测试search图片，期望接口返回成功 (上传文件)
        5. 测试search图片，期望接口返回成功 (base64)
        6. 删除person
        """
        # 1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        # formdata python不支持传空file
        # ak = config_obj.Argus.ak
        # personID = "cyf"
        # override = "0"
        # image = ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/cyf/cyf1.jpg"))
        # resp = ArgusdbApi.DB_CreatePersonPostApi(ak=ak, group_id=staticGroup, person_id=personID, override=override, image=image)
        # assert resp.status_code == 200
        # assert resp.json_get("error_code") == 0
        # assert resp.json_get("error_msg") == "OK"
        # assert resp.json_get("person_id") == personID
        # time_utils.sleep(2)
        #
        # resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=staticGroup, person_id=personID)
        # assert resp.status_code == 200
        # assert resp.json_get("error_code") == 0
        # assert resp.json_get("error_msg") == "OK"
        # assert len(resp.json_get("list")) == 1
        # assert resp.json_get("list.0.person_id") == personID
        # assert resp.json_get("list.0.image")

        # 2. 测试api接口添加会员,传参image/override，期望添加成功 (上传文件)
        ak = config_obj.Argus.ak
        personID = "cyf"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf2.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID, override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 3. 测试api接口添加会员,传参file/override,期望添加成功
        ak = config_obj.Argus.ak
        personID = "cyf"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf3.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 4. 测试search图片，期望接口返回成功
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf3.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold="0.9", top_k="5")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == personID
        assert resp.json_get("list.0.score") >= 0.999

        # 5. 测试search图片，期望接口返回成功 (base64)
        # image = ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/cyf/cyf3.jpg"))
        # resp = ArgusdbApi.DB_SearchImagePostApi(ak=ak, group_id=staticGroup, image=image, threshold=0.9, top_k=5)
        # assert resp.status_code == 200
        # assert resp.json_get("error_code") == 0
        # assert resp.json_get("error_msg") == "OK"
        # assert len(resp.json_get("list")) == 1
        # assert resp.json_get("list.0.person_id") == personID
        # assert resp.json_get("list.0.score") >= 0.999

        # 6. 删除person
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak,group_id=staticGroup, person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak', 404,5, "NOT_FOUND: group not found"),
        ('ak', '', 400, 3, "INVALID_ARGUMENT: invalid parameter, ak is required"),
        ('ak', None, 400, 3, "INVALID_ARGUMENT: invalid parameter, ak is required"),
        ('group_id', 'invalidgroup_id', 404,5, "NOT_FOUND: group not found"),
        ('group_id', '',400,3,"INVALID_ARGUMENT: invalid parameter, group_id is required"),
        ('group_id', None,400,3,"INVALID_ARGUMENT: invalid parameter, group_id is required"),
    ])
    def test_scenario_person_001_CreatePersonInvalidParam(self, invalidParam, config_obj, ArgusdbApi, staticGroup, streamGroup):
        """  测试api接口添加会员,ak或者group为空，ak和group对应关系不正确，期望添加失败"""
        ak = config_obj.Argus.ak
        personID = "cyf10"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        intef = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        intef = intef.request()
        assert intef.status_code == invalidParam[2]
        assert intef.json_get("error_code") == invalidParam[3]
        assert intef.json_get("error_msg") == invalidParam[4]

    def test_scenario_person_002_personUpdate(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ 测试api接口更新会员"""
        """
        1. 测试api接口添加会员,不传personid，传参image，期望添加成功
        2. 测试api接口修改会员,存在personid，修改file，或者image，期望修改成功
        3. 测试api接口修改会员,不存在personid，期望修改失败
        4. 测试api接口修改会员,存在personid，ak或者staticGroup为空，或者关系不正确，期望修改失败，错误提醒
        5. 删除person
        """
        # 1. 测试api接口添加会员,不传personid，传参image，期望添加成功
        ak = config_obj.Argus.ak
        personID = None
        override = "0"
        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id")
        personID = resp.json_get("person_id")
        time_utils.sleep(2)

        resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=staticGroup, person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == personID
        assert resp.json_get("list.0.image")

        # 2. 测试api接口修改会员,存在personid，修改file，或者image，期望修改成功
        # image = ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/zxq/xueqi2.jpg"))
        # resp = ArgusdbApi.DB_UpdatePersonPostApi(ak=ak, group_id=staticGroup, image=image, person_id=personID)
        # assert resp.status_code == 200
        # assert resp.json_get("error_code") == 0
        # assert resp.json_get("error_msg") == "OK"

        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi3.jpg")
        resp = ArgusdbApi.UpdatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        # 3. 测试api接口修改会员,不存在personid，期望修改失败
        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi3.jpg")
        resp = ArgusdbApi.UpdatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id="invalidID")
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: person query err: not found"

        # 4.测试api接口修改会员,存在personid，ak或者staticGroup为空，或者关系不正确，期望修改失败，错误提醒
        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi3.jpg")
        resp = ArgusdbApi.UpdatePersonPostFromFile(file_path, ak="", group_id=staticGroup, person_id=personID)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, ak is required"

        resp = ArgusdbApi.UpdatePersonPostFromFile(file_path, ak=ak, group_id="", person_id=personID)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, group_id is required"

        resp = ArgusdbApi.UpdatePersonPostFromFile(file_path, ak="invaildAk", group_id=staticGroup, person_id=personID)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

        resp = ArgusdbApi.UpdatePersonPostFromFile(file_path, ak=ak, group_id="invalidGroup", person_id=personID)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

        # 5. 删除person
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak,group_id=staticGroup, person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_person_003_personGet(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ 测试api接口添加会员,传参personid，传参file,期望添加成功"""
        """
        1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        2. 测试pesonGetone功能，ak和group正确，personid存在，期望成功
        3. 测试pesonGetone功能,personID不存在，获取失败
        4. 测试pesonGetone功能,ak，group为空，或者关系不对应，获取失败
        5. 删除person
        """
        # 1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        ak = config_obj.Argus.ak
        personID = "cyf0003"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 2. 测试pesonGetone功能，ak和group正确，personid存在，期望成功
        resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=streamGroup, person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == personID
        assert resp.json_get("list.0.image")

        # 3. 测试pesonGetone功能,personID不存在，获取失败
        resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=streamGroup, person_id="invaildPersonID")
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: person not found"

        # 4.测试pesonGetone功能,ak，group为空，或者关系不对应，获取失败
        resp = ArgusdbApi.DB_GetPersonGetApi(ak="invalidAk", group_id=streamGroup, person_id=personID)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

        resp = ArgusdbApi.DB_GetPersonGetApi(ak="", group_id=streamGroup, person_id=personID)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, ak is required"

        resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id="", person_id=personID)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, group_id is required"

        resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=streamGroup, person_id="")
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, person_id is required"

        resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id="invaildGroupID", person_id=personID)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

        # 5. 删除person
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak,group_id=streamGroup, person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_person_004_searchImage(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ 测试api接口添加会员,传参personid，传参file,期望添加成功"""
        """
        1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        2. 测试search图片，期望接口返回成功
        3. 测试search图片，topk不传（期望有默认值3），期望接口返回成功
        4. 测试search图片，不存在，期望接口返回成功为空
        5. 测试search图片，topk不在（3-10）直接，期望接口报错
        6. 测试search图片，ak或者staticGroup为空或者关系不存在，期望接口返回失败
        7. 删除person
        """
        ak = config_obj.Argus.ak
        personID = "cyf1"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf2"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf2.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf3"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf3.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf4"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf4.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 2. 测试search图片，期望接口返回成功
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold=0.9, top_k=5)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 4
        assert resp.json_get("list.0.person_id") == "cyf1"
        assert resp.json_get("list.0.score") >= 0.999

        # 3. 测试search图片，topk不传（期望有默认值3），期望接口返回成功
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold="0.9", top_k=None)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 3
        assert resp.json_get("list.0.person_id") == "cyf1"
        assert resp.json_get("list.0.score") >= 0.999

        # 4. 测试search图片，不存在，期望接口返回成功为空
        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold="0.9", top_k="5")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0

        # 5. 测试search图片，topk不在（3-10）直接，期望接口报错
        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold="0.9", top_k="2")
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: topk must between 3 to 20"

        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold="0.9", top_k="21")
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: topk must between 3 to 20"

        # 6. 测试search图片，ak或者staticGroup为空或者关系不存在，期望接口返回失败
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak="", group_id=staticGroup, threshold="0.9", top_k="5")
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, ak is required"

        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id="", threshold="0.9", top_k="5")
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, group_id is required"

        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak="invaildAK", group_id=staticGroup, threshold="0.9", top_k="5")
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id="invaildGroupID", threshold="0.9", top_k="5")
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") ==  "NOT_FOUND: group not found"

        # 7. 删除person
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak,group_id=staticGroup, person_id="cyf1")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak,group_id=staticGroup, person_id="cyf2")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak,group_id=staticGroup, person_id="cyf3")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak,group_id=staticGroup, person_id="cyf4")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_person_004_searchFeature(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ 测试api搜索feature,传参personid，传参file,期望添加成功"""
        """
        1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        2. 测试searchfeature，期望接口返回成功
        3. 测试searchfeature，topk不传（期望有默认值），期望接口返回成功
        4. 测试searchfeature，不存在，期望接口返回成功为空
        5. 测试searchfeature，topk不在（3-5）范围内，期望接口返回错误提示
        6. 测试searchfeature，ak或者streamGroup为空或者关系不存在，期望接口返回失败
        7. 测试searchfeature，group的版本和特征版本不一致（特征24503，group是24902），期望接口返回失败，及参数错误的提示
        8. 删除person
        """
        # 1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        ak = config_obj.Argus.ak
        personID = "cyf1"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf2"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf2.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf3"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf3.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf4"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf4.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 2. 测试searchfeature，期望接口返回成功
        feature = "U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpMVBxcGOLuDhv9YTSHWZltkJHI4QqW3YqmykY8MFYidmu7g5xQKjOFMGZQkaogMCoHUgtsXhPblVX8vSSEOh1GieXjvG7Xxu7m61cirXyRLv2KHdi66VZnQ0WoqddSpvbfXTf+3i1jHjs3PKSPFP0GJ2Xza2eWmsiQwYbK+K9nrw8KM86C5Ch+E1mJW6XfeaImrYdjRjhqRHPAFmjzk22MpRYoiJaks2QhNBjy6TUZWj+xcPBTg2wYrPddtI53zm0fJQ3Wtc4hZTqat/oJrTNled5kJ7NoXqP967l+re3Wt3igFcMHHsUhvvTz8Ie1CudEtasM14ut7D02HyKGuTXifUfztOKCFXUQ76vXjC470LsSoCbEM9t6b/nOq7hN3OSyZrYTuvRh4S+G0ypE/F9AEeUAUaBFYmgPS0tVNexccveZ75NXNFXCwfMd0eeG3hKzSIOVaKF2lGZAw1ck+95mpx0g7jLczri0JLttchXFzZge3VCWxB4J9bKDuYQps46Clhm6FMLApeyGoKT4Dd8nq5OAtqBkc2c1o1VTSc+xXATGRRBSTXI+8DijjNktMQTUoSKbZ59JYYeej7wHFVdGF5Xtz8R16T8/VWWNxrpu3Z/Z24KP1+oQhe8O1vIQF31rDlWh3SxZHMjKI2bMjkBijq39EMOrvOHQ9ttJh+P0r0VpzgQezrm7V1KtJ/SmKeG1Q2h+X2nvZ7zL6x2zRVF7//KN2+TRZ2T6be8e02GpY4UG2g6wbq9wARFG1L1TAaj/czCk3Ts4vv02c8gML0I1UD5PNuOYXSQDcCcnTrfgaNibl6tH9EgB77hYqCFQRcfNfpHgJXGITyUPPKhmx3D+gIHCitc46eLijmsuwdcJqU0xHj6dQrufgFuVmltskunVbVoIg1k9EdJxYqalSYyu2dviz/3WmEoACZYNITnBt79DoFzNvK3dQiPBKhvH0kcKKE8bHM3E32Oa9BXDBdK7ZrnZJSFAOizJoA9QqTCSgzrTaDdufO5FkGBi09k4hzJgow7D4T5cANHOh/AoDZNjJNZngoYkXbA0rVQXYraXLU09JI0UFVf6Ho4Ya9x1/EQgtftK+Je4HM8YtkUdTh7EicT81jgYgGrAJVtPOCAVw1BGadBAL61dMjIMrPLKEy/5XdOwTYVFIyI5Zg5Y9HE471qlCYWOPLQh4HPxDXGiyBOA76GWdSeciM/KKhYSBwMvUXK0I+MYsPKgjTuuuvQqgQSO1uiKSDi+S9Va1NwfyjmkKj+9f9oaQoDdgtCT8Y1nxpTgBa4gQEzCguTtWBqADPVM00hNK5YlU2yyNwBW+ROCNPke5ctQF/ovcOmWCnEGcldlde4rq6Pq/oSi3w1Pw=="
        #24503 feature = "U09GMbdfAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAA/WLF7qsHh10JN/ua8T33ka5HOO7OFD7h5ciIuFyZtdbf0equC0bIcl4J3zKeIQCy4vWrcE5voxAsR51N7TkKqiV+CAOnLAYlql4Q63fXghUzhw3WZ+E5O7tyqA40OmWOSbiXM6DRBwcfyxR7jYObpbjsKX6Mvjo90R3K/l9MX/YzQq0bwoJbntxAK/2BUODX4oH24tqgxYmpUQAwGlrQChEF+WItd0vtTbhruLUCg18afeNMXbJQhO4RfVYUCwt7TWUlHX3J5xCkdCmDytUnD10IB6u+I5oXAiyRvBp96cnXPsqAS6Z45hEgYWIKuPvcFI0J84FDlOTo+BdvCEULNX89xYGbtZq7s7pPb4Y8cijGF0u/Jv+JxSU/ctBev8D65vEkVNgbKAvdutOaahDlIzTCtKhaw9oX+b+yI3j9/eVsiGqxDQ7tXu7mZamdmIwmTwtCK/dHyzxe/k4EYlVXBjk9xI3w1OnhfwHlMjPuk/E9W4XLXKnjzG2ULwScZhCpmKk6OBU5whKOg7DaFaqOwY3K1SU8kd8Y0Y/2GIC/yhmmrCBZa5PFo3fj1zwHWYE7Fqy57uryuUf0HHwk+ILrGaWlaGry8cjjMSOrgQ9Xxxff5XaAwn0tPAD3HCrjN4yztrrJ9U8RZ0NpuaxGUKsvbVKxMODosa9fcdm4+IgjjlanmLOeKPCSrvSKWCtZaVd74QyoXUrd7BrU/ewZyttX0jO59Rp5/DsYCNlKQs1Xx63CmtnD/yH/A+jjLJ9QAvdCgL3/f6loeeNTodhjsQSlF13kdzTs3iJbTRd6hbDwwXH0paPqFBQldX56Vnc8kPk40S7wD8NjRsPT0sJCpWFY/utVrUasXh7yTIJgIDV1jG61L2Tq2WCDi/aTH7KnuCxQZf+n+gfyuz1Ph6rMIdUE3vOgTMEmCgCdAw4ZO6q0/ga3pFIcb3WXbrfxYQB5mN6JCfdiG1EpkHaqNm8Kx2zF3Y04tYXzewoVPdtZ/FxGET44U5hSOMxnd1c+GMV+gtyxJU3KkJhOtFEJcGPyAxLXD00itYh7cFizHuaDs/up86X76UB6LbF3m31ec7AEjUrwXPEDzaeT7VS8PyArC0HWIJtnIbHdfDcPam4apqlmdm9VXudaNHwkIogfnma4nx2lRm44CgpVDKdazgnqxgRoWCwv+FbP5JimYbZYlpmPqeW+8FsEk+AkZSm6hFgEDKtNkU0p9q63r6rUT17ecxGiJcV544GgBPrn6px8Eto3PZJdg1btjgcjMcM3t5yG7MAktEiXyRUInIrG98raLVuq0iYSixQW4X4EZ7hwBgCzB06fBKGZmU0mu01r7to3yB1WGzOOsPa4kRo0l1Hd1Vgb0v2WKnPj7/vKrZsyNoWsE5w=="

        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, group_id=streamGroup, feature=feature, threshold=0.9, top_k=5)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 4
        assert resp.json_get("list.0.person_id") == "cyf4"
        assert resp.json_get("list.0.score") >= 0.999

        # 3. 测试searchfeature，topk不传（期望有默认值），期望接口返回成功
        feature = "U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpMVBxcGOLuDhv9YTSHWZltkJHI4QqW3YqmykY8MFYidmu7g5xQKjOFMGZQkaogMCoHUgtsXhPblVX8vSSEOh1GieXjvG7Xxu7m61cirXyRLv2KHdi66VZnQ0WoqddSpvbfXTf+3i1jHjs3PKSPFP0GJ2Xza2eWmsiQwYbK+K9nrw8KM86C5Ch+E1mJW6XfeaImrYdjRjhqRHPAFmjzk22MpRYoiJaks2QhNBjy6TUZWj+xcPBTg2wYrPddtI53zm0fJQ3Wtc4hZTqat/oJrTNled5kJ7NoXqP967l+re3Wt3igFcMHHsUhvvTz8Ie1CudEtasM14ut7D02HyKGuTXifUfztOKCFXUQ76vXjC470LsSoCbEM9t6b/nOq7hN3OSyZrYTuvRh4S+G0ypE/F9AEeUAUaBFYmgPS0tVNexccveZ75NXNFXCwfMd0eeG3hKzSIOVaKF2lGZAw1ck+95mpx0g7jLczri0JLttchXFzZge3VCWxB4J9bKDuYQps46Clhm6FMLApeyGoKT4Dd8nq5OAtqBkc2c1o1VTSc+xXATGRRBSTXI+8DijjNktMQTUoSKbZ59JYYeej7wHFVdGF5Xtz8R16T8/VWWNxrpu3Z/Z24KP1+oQhe8O1vIQF31rDlWh3SxZHMjKI2bMjkBijq39EMOrvOHQ9ttJh+P0r0VpzgQezrm7V1KtJ/SmKeG1Q2h+X2nvZ7zL6x2zRVF7//KN2+TRZ2T6be8e02GpY4UG2g6wbq9wARFG1L1TAaj/czCk3Ts4vv02c8gML0I1UD5PNuOYXSQDcCcnTrfgaNibl6tH9EgB77hYqCFQRcfNfpHgJXGITyUPPKhmx3D+gIHCitc46eLijmsuwdcJqU0xHj6dQrufgFuVmltskunVbVoIg1k9EdJxYqalSYyu2dviz/3WmEoACZYNITnBt79DoFzNvK3dQiPBKhvH0kcKKE8bHM3E32Oa9BXDBdK7ZrnZJSFAOizJoA9QqTCSgzrTaDdufO5FkGBi09k4hzJgow7D4T5cANHOh/AoDZNjJNZngoYkXbA0rVQXYraXLU09JI0UFVf6Ho4Ya9x1/EQgtftK+Je4HM8YtkUdTh7EicT81jgYgGrAJVtPOCAVw1BGadBAL61dMjIMrPLKEy/5XdOwTYVFIyI5Zg5Y9HE471qlCYWOPLQh4HPxDXGiyBOA76GWdSeciM/KKhYSBwMvUXK0I+MYsPKgjTuuuvQqgQSO1uiKSDi+S9Va1NwfyjmkKj+9f9oaQoDdgtCT8Y1nxpTgBa4gQEzCguTtWBqADPVM00hNK5YlU2yyNwBW+ROCNPke5ctQF/ovcOmWCnEGcldlde4rq6Pq/oSi3w1Pw=="
        # 24503 feature = "U09GMbdfAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAA/WLF7qsHh10JN/ua8T33ka5HOO7OFD7h5ciIuFyZtdbf0equC0bIcl4J3zKeIQCy4vWrcE5voxAsR51N7TkKqiV+CAOnLAYlql4Q63fXghUzhw3WZ+E5O7tyqA40OmWOSbiXM6DRBwcfyxR7jYObpbjsKX6Mvjo90R3K/l9MX/YzQq0bwoJbntxAK/2BUODX4oH24tqgxYmpUQAwGlrQChEF+WItd0vtTbhruLUCg18afeNMXbJQhO4RfVYUCwt7TWUlHX3J5xCkdCmDytUnD10IB6u+I5oXAiyRvBp96cnXPsqAS6Z45hEgYWIKuPvcFI0J84FDlOTo+BdvCEULNX89xYGbtZq7s7pPb4Y8cijGF0u/Jv+JxSU/ctBev8D65vEkVNgbKAvdutOaahDlIzTCtKhaw9oX+b+yI3j9/eVsiGqxDQ7tXu7mZamdmIwmTwtCK/dHyzxe/k4EYlVXBjk9xI3w1OnhfwHlMjPuk/E9W4XLXKnjzG2ULwScZhCpmKk6OBU5whKOg7DaFaqOwY3K1SU8kd8Y0Y/2GIC/yhmmrCBZa5PFo3fj1zwHWYE7Fqy57uryuUf0HHwk+ILrGaWlaGry8cjjMSOrgQ9Xxxff5XaAwn0tPAD3HCrjN4yztrrJ9U8RZ0NpuaxGUKsvbVKxMODosa9fcdm4+IgjjlanmLOeKPCSrvSKWCtZaVd74QyoXUrd7BrU/ewZyttX0jO59Rp5/DsYCNlKQs1Xx63CmtnD/yH/A+jjLJ9QAvdCgL3/f6loeeNTodhjsQSlF13kdzTs3iJbTRd6hbDwwXH0paPqFBQldX56Vnc8kPk40S7wD8NjRsPT0sJCpWFY/utVrUasXh7yTIJgIDV1jG61L2Tq2WCDi/aTH7KnuCxQZf+n+gfyuz1Ph6rMIdUE3vOgTMEmCgCdAw4ZO6q0/ga3pFIcb3WXbrfxYQB5mN6JCfdiG1EpkHaqNm8Kx2zF3Y04tYXzewoVPdtZ/FxGET44U5hSOMxnd1c+GMV+gtyxJU3KkJhOtFEJcGPyAxLXD00itYh7cFizHuaDs/up86X76UB6LbF3m31ec7AEjUrwXPEDzaeT7VS8PyArC0HWIJtnIbHdfDcPam4apqlmdm9VXudaNHwkIogfnma4nx2lRm44CgpVDKdazgnqxgRoWCwv+FbP5JimYbZYlpmPqeW+8FsEk+AkZSm6hFgEDKtNkU0p9q63r6rUT17ecxGiJcV544GgBPrn6px8Eto3PZJdg1btjgcjMcM3t5yG7MAktEiXyRUInIrG98raLVuq0iYSixQW4X4EZ7hwBgCzB06fBKGZmU0mu01r7to3yB1WGzOOsPa4kRo0l1Hd1Vgb0v2WKnPj7/vKrZsyNoWsE5w=="
        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, group_id=streamGroup, feature=feature, threshold=0.9, top_k=None)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 3
        assert resp.json_get("list.0.person_id") == "cyf4"
        assert resp.json_get("list.0.score") >= 0.999

        # 4. 测试searchfeature，不存在，期望接口返回成功为空
        feature = "U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpKhrghR8cOLJuZNOLF7BQbmrq4nMFn3qJSkByDhFm+/KIWkrpcV2lAJAvgAEwV6EqF/AJcPIvCJHemoKDXkQOAv1S+WnkM2TqwW/S2MwGtrtCGsXq5CrWy5mBuEhqXCUMYb55bWsNYMoToH3pc/d4XxAEaffpbcDyFtq4Lh+8CZPHgL5LVc7PhOiZ6JWKLtt9C1jjRJZUdBocLqX8OiAY0fjiU/Q4p5gx/EbmbCuYk0rCaP0TXFyXVdy/ZkzOoHZ6wNQ1aGc28c3ZkcFhrpZmfHjTsGXz95raDT1zoLCzWoSzCyqpYow6WcK9vlfFWYz+6bcYBYHN3tMQ1PLTqQ4OgyjGKHRdqenN1M9HL8O1nLoY1KnM1ixzCBYkGO5acTTwtbzYaavxy5OfjnTzJ5mGun/YO18N/rP7IRw3ZGpNj2EdKcUNerUa7iyuAbUGhN/88eH8aRuzWr7sSPdm+G/dNgoO0Hd7WuyLlY2IM3i/WlN5LRWXGZkSoZxDo4bwRJXETgb6tmCCMEuskmzKnGdLV19slAYIqpalmp5vu9Kj6sZiBcgGAG7BjEVv+G5QLN5x+WTK0X2lMdtUHOEak0P+7HOpDvra3FKvu/wn+SeUN+4Bb7AnuKAA0G3KfhCPL8ixd1J8I3d2wkPUtJJ9L9l7KknctvOufvOH2Z6LgciUI4AoUqRzw7jY+14LkzvoGGaTeJ9330CiM6k5cWJyVPtIJsQWlvDTb7F1HyORZgM1rI/Hdomv6JYUxswBDu915nil7hzL2nBcbbhtGVXVQe0P+XIlKAXnedQwaGXiDSg0ULmicEB43zcehxEUQclhqBumMb1xT57/XdVfkxcE2/XP9s+wDy+OnfaS35Y+hYSXDq+w1Fl6Ft1WU/zpFDlcbYKJohQNeQEVgzAExLhf1ovQumw+eJ+XHCWZ2N5+SCyGH9PxnsVe98jrlmBZ5D3CdqpSlfsEh/IQEbwcBBRAI5wRoGg0QvWyXbmaeOrpAswOJhdOxpHVgWA0CNRviSCMehKy8wErnv4dEeIf5ivtQ8DyM+yd5kquJ0+WDwbJS7FKpGRqdisbIHORD13Lm7yXKHh/ANqdt8s4f9us1MjwNzn/nj8/v82bOgwjHBWNu6tmlX5E6S0UaxvXttOzSCwP7TUHVJKAVIc2w8q/IeAhPPGPgliuFnHgLluu2SsduR8PtK1Vi0f/VpfPQC1ErUlZQVUqTCgPj4Q5aPNwaNG3FBuQn7Ik4lHGG7AwciCNo1pejCexhT6Wg9jT53SkFT/L5eqAZrtbYVdkaG2EC/IrOne2DgyGQUBg3G12vfViKlX+y4s4ZCgaF8IeuCzon56cJNYbK1aPp87eqiO+NkefZzQBGA=="
        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, group_id=streamGroup, feature=feature, threshold=0.9, top_k=5)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0

        # 5. 测试searchfeature，topk不在（3-5）范围内，期望接口返回错误提示
        feature = "U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpKhrghR8cOLJuZNOLF7BQbmrq4nMFn3qJSkByDhFm+/KIWkrpcV2lAJAvgAEwV6EqF/AJcPIvCJHemoKDXkQOAv1S+WnkM2TqwW/S2MwGtrtCGsXq5CrWy5mBuEhqXCUMYb55bWsNYMoToH3pc/d4XxAEaffpbcDyFtq4Lh+8CZPHgL5LVc7PhOiZ6JWKLtt9C1jjRJZUdBocLqX8OiAY0fjiU/Q4p5gx/EbmbCuYk0rCaP0TXFyXVdy/ZkzOoHZ6wNQ1aGc28c3ZkcFhrpZmfHjTsGXz95raDT1zoLCzWoSzCyqpYow6WcK9vlfFWYz+6bcYBYHN3tMQ1PLTqQ4OgyjGKHRdqenN1M9HL8O1nLoY1KnM1ixzCBYkGO5acTTwtbzYaavxy5OfjnTzJ5mGun/YO18N/rP7IRw3ZGpNj2EdKcUNerUa7iyuAbUGhN/88eH8aRuzWr7sSPdm+G/dNgoO0Hd7WuyLlY2IM3i/WlN5LRWXGZkSoZxDo4bwRJXETgb6tmCCMEuskmzKnGdLV19slAYIqpalmp5vu9Kj6sZiBcgGAG7BjEVv+G5QLN5x+WTK0X2lMdtUHOEak0P+7HOpDvra3FKvu/wn+SeUN+4Bb7AnuKAA0G3KfhCPL8ixd1J8I3d2wkPUtJJ9L9l7KknctvOufvOH2Z6LgciUI4AoUqRzw7jY+14LkzvoGGaTeJ9330CiM6k5cWJyVPtIJsQWlvDTb7F1HyORZgM1rI/Hdomv6JYUxswBDu915nil7hzL2nBcbbhtGVXVQe0P+XIlKAXnedQwaGXiDSg0ULmicEB43zcehxEUQclhqBumMb1xT57/XdVfkxcE2/XP9s+wDy+OnfaS35Y+hYSXDq+w1Fl6Ft1WU/zpFDlcbYKJohQNeQEVgzAExLhf1ovQumw+eJ+XHCWZ2N5+SCyGH9PxnsVe98jrlmBZ5D3CdqpSlfsEh/IQEbwcBBRAI5wRoGg0QvWyXbmaeOrpAswOJhdOxpHVgWA0CNRviSCMehKy8wErnv4dEeIf5ivtQ8DyM+yd5kquJ0+WDwbJS7FKpGRqdisbIHORD13Lm7yXKHh/ANqdt8s4f9us1MjwNzn/nj8/v82bOgwjHBWNu6tmlX5E6S0UaxvXttOzSCwP7TUHVJKAVIc2w8q/IeAhPPGPgliuFnHgLluu2SsduR8PtK1Vi0f/VpfPQC1ErUlZQVUqTCgPj4Q5aPNwaNG3FBuQn7Ik4lHGG7AwciCNo1pejCexhT6Wg9jT53SkFT/L5eqAZrtbYVdkaG2EC/IrOne2DgyGQUBg3G12vfViKlX+y4s4ZCgaF8IeuCzon56cJNYbK1aPp87eqiO+NkefZzQBGA=="
        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, group_id=streamGroup, feature=feature, threshold=0.9, top_k=2)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: topk must between 3 to 20"

        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, group_id=streamGroup, feature=feature, threshold=0.9, top_k=21)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: topk must between 3 to 20"

        # 6. 测试searchfeature，ak或者streamGroup为空或者关系不存在，期望接口返回失败
        feature = "U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpMVBxcGOLuDhv9YTSHWZltkJHI4QqW3YqmykY8MFYidmu7g5xQKjOFMGZQkaogMCoHUgtsXhPblVX8vSSEOh1GieXjvG7Xxu7m61cirXyRLv2KHdi66VZnQ0WoqddSpvbfXTf+3i1jHjs3PKSPFP0GJ2Xza2eWmsiQwYbK+K9nrw8KM86C5Ch+E1mJW6XfeaImrYdjRjhqRHPAFmjzk22MpRYoiJaks2QhNBjy6TUZWj+xcPBTg2wYrPddtI53zm0fJQ3Wtc4hZTqat/oJrTNled5kJ7NoXqP967l+re3Wt3igFcMHHsUhvvTz8Ie1CudEtasM14ut7D02HyKGuTXifUfztOKCFXUQ76vXjC470LsSoCbEM9t6b/nOq7hN3OSyZrYTuvRh4S+G0ypE/F9AEeUAUaBFYmgPS0tVNexccveZ75NXNFXCwfMd0eeG3hKzSIOVaKF2lGZAw1ck+95mpx0g7jLczri0JLttchXFzZge3VCWxB4J9bKDuYQps46Clhm6FMLApeyGoKT4Dd8nq5OAtqBkc2c1o1VTSc+xXATGRRBSTXI+8DijjNktMQTUoSKbZ59JYYeej7wHFVdGF5Xtz8R16T8/VWWNxrpu3Z/Z24KP1+oQhe8O1vIQF31rDlWh3SxZHMjKI2bMjkBijq39EMOrvOHQ9ttJh+P0r0VpzgQezrm7V1KtJ/SmKeG1Q2h+X2nvZ7zL6x2zRVF7//KN2+TRZ2T6be8e02GpY4UG2g6wbq9wARFG1L1TAaj/czCk3Ts4vv02c8gML0I1UD5PNuOYXSQDcCcnTrfgaNibl6tH9EgB77hYqCFQRcfNfpHgJXGITyUPPKhmx3D+gIHCitc46eLijmsuwdcJqU0xHj6dQrufgFuVmltskunVbVoIg1k9EdJxYqalSYyu2dviz/3WmEoACZYNITnBt79DoFzNvK3dQiPBKhvH0kcKKE8bHM3E32Oa9BXDBdK7ZrnZJSFAOizJoA9QqTCSgzrTaDdufO5FkGBi09k4hzJgow7D4T5cANHOh/AoDZNjJNZngoYkXbA0rVQXYraXLU09JI0UFVf6Ho4Ya9x1/EQgtftK+Je4HM8YtkUdTh7EicT81jgYgGrAJVtPOCAVw1BGadBAL61dMjIMrPLKEy/5XdOwTYVFIyI5Zg5Y9HE471qlCYWOPLQh4HPxDXGiyBOA76GWdSeciM/KKhYSBwMvUXK0I+MYsPKgjTuuuvQqgQSO1uiKSDi+S9Va1NwfyjmkKj+9f9oaQoDdgtCT8Y1nxpTgBa4gQEzCguTtWBqADPVM00hNK5YlU2yyNwBW+ROCNPke5ctQF/ovcOmWCnEGcldlde4rq6Pq/oSi3w1Pw=="
        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak="", group_id=streamGroup, feature=feature, threshold=0.9, top_k=5)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, ak is required"

        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, group_id="", feature=feature, threshold=0.9, top_k=5)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") ==  "INVALID_ARGUMENT: invalid parameter, group_id is required"

        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, group_id=streamGroup, feature="", threshold=0.9, top_k=5)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") =="INVALID_ARGUMENT: invalid parameter, feature is required"

        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak="invalidAK", group_id=streamGroup, feature=feature, threshold=0.9, top_k=5)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, group_id="invalidGroup", feature=feature, threshold=0.9, top_k=5)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

        # 7. 测试searchfeature，group的版本和特征版本不一致（特征24503，group是24902），期望接口返回失败，及参数错误的提示
        feature = "U09GMbdfAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAADxgPbu0gbTP4oW3PFyr7qnDqefmkMzT4Zg7l+qOwXUc/W6/TeOIbkBDiAxxnKs9qth4t2qzGDWuI7kEKfAD/HizirkKEU0JIgLQSbL5kbq0TWNPnd0KAnIRWehSfckUFK3sJ9NuZmhcftqg76FeFOVZcXjne7IzvTOKOxn5xi264/DdwUz0DD3iKNCo1rDdJX5phB0R4uwwUBO/CDiHBjgqzWQhAwwEGjeCE8+MjquPA2N8Nz2qMe/ThPMwTozF9Hd5lr7v2HnCzRz34JK6pfno67n82+NviirMCS+DkBAr5eckWcvYXDKJ7VzAmdH+eeKQAONNzmPmzsZb0HPPZQ9x0XQ3vsLHbL8ZJYjgIN0tBbdORSAqfNiIhclpZCH2CfqqGw6eOaY/QsO+PeSbY3O62HvTfYeE2ix2FRcS8sRUv4qgWYUwyGxQROd9711JIid+LiNTpmHiZggMPe4XL3F9Xi81j+3MG33FtTgGyo0TDXfLohpbuRvDKrlDn5jqfp9wviwKG38VHpnt3dA/PToIEV9C6TOV6QLNYcUTUFIU7le7N5aPYI8cWvE1e0jG4joGpTH6Qo8FFou1BN80jSod9gTjW5Xsq55ZSOjsYZc1hlhC7Du8KoEo7aQTECcg4ai/Iggk0Plc4Y8vfyBNj/fPsbf255nJ+ALiCCQkn07F5zWhkZPU2W3Y8TYO45P2DRnSdOC6CXS1DFFSMgdTbZguLY3Ksoc5Zj9xCJEBa1ygnYdJokK71BbV628c1fmh4wadJKrip3KhK3NLfPEBQJjbnVsOMId8VGTm7IeS/IP261odCun31ymK1J/tnSviQD+gsZNZtz2ydI6Nx575B0DVro2SfObRScLUowYIwp/x7MXMHN5iXWTDOmzyzFrdxumXCqsMtJTY2pytUM0mdOlwyBXCI1ziCknBXtze7gMDWNexRyQ4aeRwOPKb8jSTNQeP3VszAfCKSBFzHQ9RCoKaeam6gBwhifkuR621iyEmmBB/4P8aZcbzS862h2oQ+JTcEK4IV2uHHsKYzYyzHOr4ZdrgC+ZcytV/P04iIF/6tNEGIBlOuP8F+rQ713q2AdZroZFm6gJV+B89oTKIKM+5QGr2Qr7o6lAJrheWQzYqwCQAyN5NcphnPKOx1tMRAiNuWTZDOrPYgx+CK0QLlxfxf5h/9DN6oPJBDU8rfnbIb6eQzdcwbPnxXPYSZwcHaxTcv69J3h5dTxQRPDupMWe5eHVDmlXkV5UN+HEgsraxyZEPBKYiA+tEfLrxfuE8N6iI0PBEgsSwbpN/CsU6sQz1PgdtSQAkyu4E19y6pxC/agEmQbs7El48b+Amfo1ELZzdO7jzYV4h0rDKpxLH/BPv7dTc3EIKDvJvo1VLNqYtQ=="
        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, group_id=streamGroup, feature=feature, threshold=0.9, top_k=5)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert "feature’s version and group's version are not equal" in resp.json_get("error_msg")

        # 8. 删除person
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf1")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf2")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf3")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf4")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_person_005_personDelete(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ person Create"""
        """
        1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        2. 测试pesondelete功能,期望删除成功
        3. 测试pesondelete功能,ak，group为空，或者关系不对应，获取失败
        """
        # 1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        ak = config_obj.Argus.ak
        personID = "cyf005"
        override = "0"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=staticGroup,person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak',404,5,"NOT_FOUND: group not found"),
        ('ak', '', 400,3, "INVALID_ARGUMENT: invalid parameter, ak is required"),
        ('ak', None, 400,3, "INVALID_ARGUMENT: invalid parameter, ak is required"),
        ('group_id', 'invalidgroup_id', 404,5,"NOT_FOUND: group not found"),
        ('group_id', '', 400,3,"INVALID_ARGUMENT: invalid parameter, group_id is required"),
        ('group_id', None, 400,3,"INVALID_ARGUMENT: invalid parameter, group_id is required"),
        ('person_id', 'invalidperson_id', 404,5,"NOT_FOUND: person query err, not found"),
        # ('person_id', ''),
        # ('person_id', None),
    ])
    def test_scenario_person_006_DeletePersonInvalidParam(self, invalidParam, config_obj, ArgusdbApi,staticGroup, streamGroup):
        """  DB API """
        ak = config_obj.Argus.ak
        group_id = staticGroup
        person_id = "cyf1111"
        intef = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=group_id, person_id=person_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code == invalidParam[2]
        assert resp.json_get("error_code") ==invalidParam[3]
        assert resp.json_get("error_msg") == invalidParam[4]

    def test_scenario_person_007_PersonAddMutilFace(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ PersonAddMutilFace"""
        """
        1.先添加静态库人员，personadd, 图中两张图片，期望添加的是largeface：诗涵
        2.测试search图片，期望接口返回成功
        3.测试pesondelete功能,期望删除成功
        """
        # 1. 测试api接口添加会员,传参personid，传参file,期望添加成功
        ak = config_obj.Argus.ak
        personID = "twoface"
        override = "0"
        file_path = os.path.join(config.goimage_path, "twoface.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 2.测试search图片，期望接口返回成功
        file_path = os.path.join(config.goimage_path, "face/wsh/shihan2.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold="0.9", top_k="5")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == "twoface"
        assert resp.json_get("list.0.score") >= 0.9 and resp.json_get("list.0.score") <= 0.99

        # 3.测试pesondelete功能,期望删除成功
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=staticGroup, person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_person_008_PersonGetList(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ PersonGetList"""
        """
        1. 先添加静态库人员，personadd
        2. 测试personlist功能，总2条数据，limit：0(会取默认10)，offset：0，reversed：0，获取成功，两条
        3. 测试personlist功能，总2条数据，limit：1，offset：0，reversed：1，获取成功，1条
        4. 测试personlist功能，总2条数据，limit：1，offset：1，reversed：0，获取成功，1条
        5. 测试personlist功能，总2条数据，limit：1，offset：2，reversed：0，获取成功，0条
        6. 测试personlist功能，limit，offset，reversed参数不正确，获取失败
        7. 测试pesonGetlist功能,ak或者groupID不正确，获取失败
        8. 测试pesondelete功能,期望删除成功
        """
        ak = config_obj.Argus.ak
        personID = "cyf0081"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        ak = config_obj.Argus.ak
        personID = "cyf0082"
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf2.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id=staticGroup)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        with check: assert resp.json_get("total") == 2
        with check: assert len(resp.json_get("list")) == 2
        with check: assert resp.json_get("list.0.person_id") == "cyf0081"
        with check: assert resp.json_get("list.1.person_id") == "cyf0082"
        with check: assert resp.json_get("list.0.image")
        with check: assert resp.json_get("list.1.image")

        # 3.测试personlist功能，总2条数据，limit：1，offset：0，reversed：1，获取成功，1条
        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id=staticGroup, limit=1,reversed=1, offset=0)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        with check: assert resp.json_get("total") == 2
        with check: assert len(resp.json_get("list")) == 1
        with check: assert resp.json_get("list.0.person_id") == "cyf0082"
        with check: assert resp.json_get("list.0.image")

        # 4. 测试personlist功能，总2条数据，limit：1，offset：1，reversed：0，获取成功，1条
        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id=staticGroup, limit=1, reversed=0, offset=1)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        with check: assert resp.json_get("total") == 2
        with check: assert len(resp.json_get("list")) == 1
        with check: assert resp.json_get("list.0.person_id") == "cyf0082"
        with check: assert resp.json_get("list.0.image")

        # 5. 测试personlist功能，总2条数据，limit：1，offset：2，reversed：0，获取成功，0条
        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id=staticGroup, limit=1, reversed=0, offset=2)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        with check: assert resp.json_get("total") == 2

        # 6. 测试personlist功能，limit，offset，reversed参数不正确，获取失败
        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id=staticGroup, limit=201, reversed=0, offset=1)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: limit is invalid"

        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id=staticGroup, limit=200, reversed=0, offset=-1)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: offset is invalid"

        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id=staticGroup, limit=200, reversed=2, offset=1)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: json bind error"

        # 7.测试pesonGetlist功能,ak或者groupID不正确，获取失败
        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id="invalidGroupID", limit=1, reversed=0, offset=1)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: get group err, not found"

        resp = ArgusdbApi.DB_ListPersonGetApi(ak="invalidAK", group_id=staticGroup, limit=1, reversed=0, offset=1)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: get group err, not found"

        resp = ArgusdbApi.DB_ListPersonGetApi(ak="", group_id=staticGroup, limit=1, reversed=0, offset=1)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: json bind error"

        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id="", limit=1, reversed=0, offset=1)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: json bind error"

        # 8.测试pesondelete功能,期望删除成功
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=staticGroup, person_id="cyf0081")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=staticGroup, person_id="cyf0082")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_person_009_AddPersonWithBound_1(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ AddPersonWithBound"""
        """
        1. 测试api添加会员,带bound参数，twoface,传大框，期望添加的是大脸人员wsh，期望返回正确
        """
        ak = config_obj.Argus.ak
        personID = "twofacebig" # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "twoface.jpg")
        img = Image.open(file_path)
        width = img.width
        height = img.height
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": width, "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override, bounding=bounding)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        file_path = os.path.join(config.goimage_path, "face/wsh/shihan3.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=streamGroup, threshold=0.9, top_k=None)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == "twofacebig"
        assert resp.json_get("list.0.score") >= 0.9

        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=streamGroup, threshold=0.9, top_k=None)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup,person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    # bug
    def test_scenario_person_009_AddPersonWithBound_2(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ AddPersonWithBound"""
        """
        2. 测试api添加会员,带bound参数，twoface,传左边框，期望添加的是左边人员cyf，期望返回正确
        """
        # 2.测试api添加会员,带bound参数，twoface,传左边框，期望添加的是左边人员cyf，期望返回正确
        ak = config_obj.Argus.ak
        personID = "twofacecyf"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "twoface.jpg")
        img = Image.open(file_path)
        width = img.width
        height = img.height
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x":int(width/2) , "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override, bounding=bounding)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold=0.9, top_k=None)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == personID
        assert resp.json_get("list.0.score") >= 0.9

        file_path = os.path.join(config.goimage_path, "face/wsh/shihan3.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold=0.9, top_k=None)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=staticGroup,person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_person_009_AddPersonWithBound_3(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ AddPersonWithBound"""
        """
        1. 测试api添加会员,带bound参数，twoface,传大框，期望添加的是大脸人员wsh，期望返回正确
        2. 测试api添加会员,带bound参数，twoface,传左边框，期望添加的是左边人员cyf，期望返回正确
        3. 测试api添加会员,带bound参数，twoface,传右边框，期望添加的是shihan，期望返回正确
        4. 测试api添加会员,带bound参数，bound内无人脸，期望返回错误提示
        """
        # 3.测试api添加会员,带bound参数，twoface,传右边框，期望添加的是shihan，期望返回正确
        ak = config_obj.Argus.ak
        personID = "twofacecyf"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "twoface.jpg")
        img = Image.open(file_path)
        width = img.width
        height = img.height
        bounding = {
            "vertices": [
                {"x": int(width / 2), "y": 1},
                {"x": width, "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID,
                                                   override=override, bounding=bounding)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        file_path = os.path.join(config.goimage_path, "face/wsh/shihan3.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold=0.9, top_k=None)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == "twofacecyf"
        assert resp.json_get("list.0.score") >= 0.9

        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, threshold=0.9, top_k=None)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=staticGroup, person_id=personID)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
    # bug
    def test_scenario_person_009_AddPersonWithBound_4(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ AddPersonWithBound"""
        """
        1. 测试api添加会员,带bound参数，twoface,传大框，期望添加的是大脸人员wsh，期望返回正确
        2. 测试api添加会员,带bound参数，twoface,传左边框，期望添加的是左边人员cyf，期望返回正确
        3. 测试api添加会员,带bound参数，twoface,传右边框，期望添加的是shihan，期望返回正确
        4. 测试api添加会员,带bound参数，bound内无人脸，期望返回错误提示
        """
        # 4. 测试api添加会员,带bound参数，bound内无人脸，期望返回错误提示
        ak = config_obj.Argus.ak
        personID = "zxq"  # 1440 * 1080
        override = "1"
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": 2, "y": 2}
            ]
        }
        bounding = json.dumps(bounding)
        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override, bounding=bounding)
        assert resp.status_code == 500
        assert resp.json_get("error_code") == 2
        assert resp.json_get("error_msg") == "INTERNAL: get feature failed, msg overlap failed: no face"

    def test_scenario_person_009_BatchSearchFeature(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ BatchSearchFeature"""
        """
        1. 测试api接口添加会员,steamgroup里添加cyf1,cyf2,cyf3,cyf4,cyf5和zxq,期望添加成功
        2. 测试batchsearchfeature,cyf1,zxq1，topk为5或者不传（默认应该3），搜索streamgroup（存在cyf1-5,zxq1）和staticgroup（无特征），期望接口返回成功
        3. 测试searchfeature,ak或group不存在,或者为空，期望接口返回失败
        4. 测试searchfeature,feature为空或者feature版本不对,或者configs为空，期望接口返回失败
        5. 测试searchfeature,feature超出范围（1），期望接口返回失败
        6. 测试searchfeature,groups超出范围（10），期望接口返回失败
        7. 测试searchfeature,topk为空或者超出范围（3-5），期望接口返回失败
        """
        ak = config_obj.Argus.ak
        personID = "cyf1"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf2"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf2.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf3"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf3.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf4"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf4.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf5"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf5.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "zxq"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 2.测试batchsearchfeature,cyf1,zxq1，topk为5或者不传（默认应该3），搜索streamgroup（存在cyf1-5,zxq1）和staticgroup（无特征），期望接口返回成功
        # cyf的feature
        features = ["U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAhGZu+3IHiqNvqkJXp+A4JI9FOUZUJEG+hlZr8y1s7GQ08Z4FH6nC8Hqgt+zVi8C/RM+/XC1NyvWWw81jv9O8+VRTQJ6Iv4wpQaempW9V+HbcjSc7F0HrunoHsYuKUsHYrhJLUvuJ1O4dp9PzcR6XI5y8ND6IKcdg9W0L+XH77YI1wO+onoHaCx6Fn1jkCC9YozNmYMtOM8bM1DQgl70w3CyHGzxq3RBAEE6idwJmdXDZUwFMjQEXvoHjvaqJ4AcY6CaQOsRKLZQa4UZx2k4Y9EV6AZVtkknDdMav4zIkvtSE7Xy+qGWMPHIl+ognhaMl1X35UpWCApyIagclDwO2uJHH8R8fgNwBCphVOSnhQLPqdMFCWqzPfLeVkp9kyIYOABSgq9ij+4i0WJPEu3ILUB2Uh7Y1dkN4yoBA1oDMUBPJeggRwWZgLDZHV07fZF+5dlMmXAFIEg0RSbboDYZENdz0ITQgU+wbq9AcKsn5m8gPL4rsKnT1x/PVPmH89zzjV5rR/Kjt+5y2oCfWmI62/OYlSwj+mfYpiEyHdRht7ckRlhFeZfToVIIQP/mo7UxsGp2jnD5ahV/f5Wi8z2G5cvQ5QKGSddEAVPsq2A72Pf9ocbH2e9egQ8RhI1M9jYGJITFHqbifjAPaWFYIs/d0t8TGUGY4ipB6ytQsM8eex11PPM9BvhwD5BQrVQzLCWNn72p+kHJ2gKOeL04bQ0bukoBv505+jqFO0uyXiNSQU5KuG0QUNwtH5amdbdGq+8XC8rDrUMRSyDLPbZavgpD7IdDp5pQfOBUYALGHy3zjgsrLU++pS8pN4QYK9Ou6SkODjUx4sPaEEOkzMp3xYTx5gvK5K0fngil/dpq1qpNW1y5VCWDl3RPMuZETaN4TMzOEeF+c2gm0GiMHZKqf9M+qCNzGGMquZXhtggxAlbaZfYgjoqq4HkXuuiP+3HPNDBgqtIkiqLfArYZd3ycuZ+fLnw89alhb+XO5P+UFdBk3XK+cbOMd9/bSpoRjIBA/k4LhUbJl9uRgN+Au4bFE8cMbdt422wNxw84ZRBg94vryesdbJnxPFJI+Rvht7oIPv3Q23gqbJwA2KvL+DsqRANXbOs9VrvsJhDqrzjjK87++KtARebks1aOlVaSKU4dP4on3YpXBhaSr/vKKjnQkF/Exu4sePBKvgetztP0tY3GaWFE+uYsA9bqQqWUJAE4qQHM3FaJbNGsVSZNyZ4P1HyGCtCJgwFFR2ToA4uhK4aFKgZkz9e+5o2cbvOQUhOMxnwMe+hht70Pr6xkEqCJYAqPCCVoveiQUJ8vgiGDiqHjNTReBkVEnQHynYoO0yYdrFNsi+aflmAOzlo8kaF88ARO66chXIUEj/D+g988bBEber2Q=="]
        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
                "top_k": 5
            },
            {
                "group_id": staticGroup,
                "threshold": 0.9,
                "top_k": 5
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("results")) == 2
        assert resp.json_get("results.0.code") == 0
        assert len(resp.json_get("results.0.feature_results")) == 1
        assert len(resp.json_get("results.0.feature_results.0.list")) == 5
        assert resp.json_get("results.0.feature_results.0.list.0.feature_id")
        assert resp.json_get("results.0.feature_results.0.list.0.person_id") == "cyf1"
        assert resp.json_get("results.0.feature_results.0.list.0.score") >= 0.999

        assert len(resp.json_get("results.1.feature_results")) == 1
        assert not resp.json_get("results.1.feature_results.0.list")

        # cyf的feature 不填topk
        features = ["U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAhGZu+3IHiqNvqkJXp+A4JI9FOUZUJEG+hlZr8y1s7GQ08Z4FH6nC8Hqgt+zVi8C/RM+/XC1NyvWWw81jv9O8+VRTQJ6Iv4wpQaempW9V+HbcjSc7F0HrunoHsYuKUsHYrhJLUvuJ1O4dp9PzcR6XI5y8ND6IKcdg9W0L+XH77YI1wO+onoHaCx6Fn1jkCC9YozNmYMtOM8bM1DQgl70w3CyHGzxq3RBAEE6idwJmdXDZUwFMjQEXvoHjvaqJ4AcY6CaQOsRKLZQa4UZx2k4Y9EV6AZVtkknDdMav4zIkvtSE7Xy+qGWMPHIl+ognhaMl1X35UpWCApyIagclDwO2uJHH8R8fgNwBCphVOSnhQLPqdMFCWqzPfLeVkp9kyIYOABSgq9ij+4i0WJPEu3ILUB2Uh7Y1dkN4yoBA1oDMUBPJeggRwWZgLDZHV07fZF+5dlMmXAFIEg0RSbboDYZENdz0ITQgU+wbq9AcKsn5m8gPL4rsKnT1x/PVPmH89zzjV5rR/Kjt+5y2oCfWmI62/OYlSwj+mfYpiEyHdRht7ckRlhFeZfToVIIQP/mo7UxsGp2jnD5ahV/f5Wi8z2G5cvQ5QKGSddEAVPsq2A72Pf9ocbH2e9egQ8RhI1M9jYGJITFHqbifjAPaWFYIs/d0t8TGUGY4ipB6ytQsM8eex11PPM9BvhwD5BQrVQzLCWNn72p+kHJ2gKOeL04bQ0bukoBv505+jqFO0uyXiNSQU5KuG0QUNwtH5amdbdGq+8XC8rDrUMRSyDLPbZavgpD7IdDp5pQfOBUYALGHy3zjgsrLU++pS8pN4QYK9Ou6SkODjUx4sPaEEOkzMp3xYTx5gvK5K0fngil/dpq1qpNW1y5VCWDl3RPMuZETaN4TMzOEeF+c2gm0GiMHZKqf9M+qCNzGGMquZXhtggxAlbaZfYgjoqq4HkXuuiP+3HPNDBgqtIkiqLfArYZd3ycuZ+fLnw89alhb+XO5P+UFdBk3XK+cbOMd9/bSpoRjIBA/k4LhUbJl9uRgN+Au4bFE8cMbdt422wNxw84ZRBg94vryesdbJnxPFJI+Rvht7oIPv3Q23gqbJwA2KvL+DsqRANXbOs9VrvsJhDqrzjjK87++KtARebks1aOlVaSKU4dP4on3YpXBhaSr/vKKjnQkF/Exu4sePBKvgetztP0tY3GaWFE+uYsA9bqQqWUJAE4qQHM3FaJbNGsVSZNyZ4P1HyGCtCJgwFFR2ToA4uhK4aFKgZkz9e+5o2cbvOQUhOMxnwMe+hht70Pr6xkEqCJYAqPCCVoveiQUJ8vgiGDiqHjNTReBkVEnQHynYoO0yYdrFNsi+aflmAOzlo8kaF88ARO66chXIUEj/D+g988bBEber2Q=="]
        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
            },
            {
                "group_id": staticGroup,
                "threshold": 0.9,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("results")) == 2
        assert resp.json_get("results.0.code") == 0
        assert len(resp.json_get("results.0.feature_results")) == 1
        assert len(resp.json_get("results.0.feature_results.0.list")) == 3  # top_k 默认3
        assert resp.json_get("results.0.feature_results.0.list.0.feature_id")
        assert resp.json_get("results.0.feature_results.0.list.0.person_id") == "cyf1"
        assert resp.json_get("results.0.feature_results.0.list.0.score") >= 0.999

        assert len(resp.json_get("results.1.feature_results")) == 1
        assert not resp.json_get("results.1.feature_results.0.list")

        # xueqi的feature
        features = ["U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAhGZu+3IHiqNvqkJXp+A4J4YZrEDXK+aEjR93KURiyNUzA3HIdYPJHaAminGiFoOj7+38pfJIU5GRjXHHTg+cuPhUBRhvOH0lQYekWBUB3lveLpn6yV3GWkmMjmlkeeu3rsAlplS2GzENGHdmLUfkFnSwpKGyZMd4oCoEvcjUFYc6F3zMC13DsA09JNO161poA7CuPi94upoAA1fc0C0r0XoAB5NlY4gXQdZirxmWPICwVfwbxvuma8qW9a3Xi/FaSglEc8mRxAR2ewNC8JBGHLVi4HWxwe242rfauI3Pq5PFV0pUVV/SffROL74D40iVjMj61y2V8RLVW0z9NzOlmaa8hcnZ2HIqsSlyRSN/84skKl0CZxteoC/2b7ecQftSd+bLDui1aDjdyeBxJ/+03R/h4Um+ksUTOiT2s2CHWe0AhoklfueaQ6IMsjD3EJqEif/R5jFF3pNQRGdtVPQ7tRBQZcuTgoRSk+JX9UwQ8pMAEz6aRZBp8pcZkhlAHdei6GgJTy/RIKT/7ctVKK0UmCyOVANfTXwRwVqWmKE767aN0ESLFw1f7xWNsp4QAtsSxZPHUTV6WEg03aMY2riCMNw2Mf7kRBaMqT/0BZoFW9fsF4eesFq80pKsVEuduSdZ6XRm7ysmyEiu61z8jgol/uiFfet2GvQ6ZrEDSLtAzPTa1q9gCG3VkMDw4bJQndC+hVER8BjfYGqY0ZREVV8g67Qy2Y9UdP/boLbhfMgDSeuJutW/6C8K4SuXn8WYkjsVWEZsCpEVzWZiFrPm5eUp5uzVE/fLAfoyamMuS6c7q+8pio8ve75BMs3rqxFRCPypdTg327gSgTm23FpQjxysSWCjVGn0BhQzTmeUgt+zi6maTykbtGGwBpF/A9juSTDv5RD6opWdKdutZwmIydNrXnV7KRfEUi4m5VuDOunUMEI18OOivpjBRa0mWOf4qNkmrqDZ2EhSvBmePbJEp4uDsX2uuI9KmbvpK/73Eq3mBDmKpiqHe4H4JJcNu0FFJiyoJSYDA+foMmChKj+m/Tb4lfgw50Xk5JyCUPmxDnzWdp39V8pp/SVcONUqFhuDvi4xWE58iV3BW4+xKZPGmiwhrWpkp9XctiXjyRrJMV0oHCpLug0cgnyV7CTYE4thgedCKJ1lIAtWY8ok039ZAhPyXCTOkdSVU2yEuvgwLGRPhnN2VKdHaQZ9P4Y85iArcKgayCMzNVIesLaz9fX1BwDBPOBnmoHsuL8mRBT9yw88xCqY3HqitE//IdKzMPkRbWgrKvooP4Fb9DKEAmDA+XTfKGJ7RqOv+0p3JexHqT0M2DUtmvJNYkUtyizLwUUkggJRKOgD7oC3RqdU2uu7DnZT8mBIirDccCUee/oiiLX97gw=="]
        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
            },
            {
                "group_id": staticGroup,
                "threshold": 0.9,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("results")) == 2
        assert resp.json_get("results.0.code") == 0
        assert len(resp.json_get("results.0.feature_results")) == 1
        assert len(resp.json_get("results.0.feature_results.0.list")) == 1  # top_k 默认3
        assert resp.json_get("results.0.feature_results.0.list.0.feature_id")
        assert resp.json_get("results.0.feature_results.0.list.0.person_id") == "zxq"
        assert resp.json_get("results.0.feature_results.0.list.0.score") >= 0.999

        assert len(resp.json_get("results.1.feature_results")) == 1
        assert not resp.json_get("results.1.feature_results.0.list")

        # 3. 测试searchfeature,ak或group不存在,或者为空，期望接口返回失败
        features = ["U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpMVBxcGOLuDhv9YTSHWZltkJHI4QqW3YqmykY8MFYidmu7g5xQKjOFMGZQkaogMCoHUgtsXhPblVX8vSSEOh1GieXjvG7Xxu7m61cirXyRLv2KHdi66VZnQ0WoqddSpvbfXTf+3i1jHjs3PKSPFP0GJ2Xza2eWmsiQwYbK+K9nrw8KM86C5Ch+E1mJW6XfeaImrYdjRjhqRHPAFmjzk22MpRYoiJaks2QhNBjy6TUZWj+xcPBTg2wYrPddtI53zm0fJQ3Wtc4hZTqat/oJrTNled5kJ7NoXqP967l+re3Wt3igFcMHHsUhvvTz8Ie1CudEtasM14ut7D02HyKGuTXifUfztOKCFXUQ76vXjC470LsSoCbEM9t6b/nOq7hN3OSyZrYTuvRh4S+G0ypE/F9AEeUAUaBFYmgPS0tVNexccveZ75NXNFXCwfMd0eeG3hKzSIOVaKF2lGZAw1ck+95mpx0g7jLczri0JLttchXFzZge3VCWxB4J9bKDuYQps46Clhm6FMLApeyGoKT4Dd8nq5OAtqBkc2c1o1VTSc+xXATGRRBSTXI+8DijjNktMQTUoSKbZ59JYYeej7wHFVdGF5Xtz8R16T8/VWWNxrpu3Z/Z24KP1+oQhe8O1vIQF31rDlWh3SxZHMjKI2bMjkBijq39EMOrvOHQ9ttJh+P0r0VpzgQezrm7V1KtJ/SmKeG1Q2h+X2nvZ7zL6x2zRVF7//KN2+TRZ2T6be8e02GpY4UG2g6wbq9wARFG1L1TAaj/czCk3Ts4vv02c8gML0I1UD5PNuOYXSQDcCcnTrfgaNibl6tH9EgB77hYqCFQRcfNfpHgJXGITyUPPKhmx3D+gIHCitc46eLijmsuwdcJqU0xHj6dQrufgFuVmltskunVbVoIg1k9EdJxYqalSYyu2dviz/3WmEoACZYNITnBt79DoFzNvK3dQiPBKhvH0kcKKE8bHM3E32Oa9BXDBdK7ZrnZJSFAOizJoA9QqTCSgzrTaDdufO5FkGBi09k4hzJgow7D4T5cANHOh/AoDZNjJNZngoYkXbA0rVQXYraXLU09JI0UFVf6Ho4Ya9x1/EQgtftK+Je4HM8YtkUdTh7EicT81jgYgGrAJVtPOCAVw1BGadBAL61dMjIMrPLKEy/5XdOwTYVFIyI5Zg5Y9HE471qlCYWOPLQh4HPxDXGiyBOA76GWdSeciM/KKhYSBwMvUXK0I+MYsPKgjTuuuvQqgQSO1uiKSDi+S9Va1NwfyjmkKj+9f9oaQoDdgtCT8Y1nxpTgBa4gQEzCguTtWBqADPVM00hNK5YlU2yyNwBW+ROCNPke5ctQF/ovcOmWCnEGcldlde4rq6Pq/oSi3w1Pw=="]
        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
                "top_k": 5,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak="invalidAk", features=features, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("results")) == 1
        assert resp.json_get("results.0.code") == 0
        assert "NOT_FOUND" in resp.json_get("results.0.feature_results.0.msg")

        search_configs = [
            {
                "group_id": "InvalidstreamGroup",
                "threshold": 0.9,
                "top_k": 5,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 1
        assert resp.json_get("results.0.code") == 0
        assert "NOT_FOUND" in resp.json_get("results.0.feature_results.0.msg")

        search_configs = [
            {
                "group_id": "",
                "threshold": 0.9,
                "top_k": 5,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert "INVALID_ARGUMENT" in resp.json_get("error_msg")

        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
                "top_k": 5,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak="", features=features, search_configs=search_configs)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert "INVALID_ARGUMENT" in resp.json_get("error_msg")

        # 4. 测试searchfeature,feature为空或者feature版本不对,或者configs为空，期望接口返回失败
        features = []
        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
                "top_k": 5,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: features is reuired"

        features = ["123456"]
        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
                "top_k": 5,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("results")) == 1
        assert resp.json_get("results.0.feature_results.0.code") == -1
        assert "feature base64 decode failed" in resp.json_get("results.0.feature_results.0.msg")

        features = ["U09GMbdfAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAKFC3QdRdNLLxjzyxSMcwdV3l/sjiHPP+XjL/E3R+pjk6gQa5iSVz49oOZFgu8kuDaYx6tPwJCI3uD7QrEPguInz+F7+JHlhk5Qp4KOHQFNG0XSyWUFGQEhNNSgs9NqMkjmPNDulyDl3e4HpdCoPusU9bFBVzUx2n4xFZO29grj5IpuZsB1ccBPAPqUGyvtZ5+PZL57Jm7t8mJQx+0K1v9XPcqIzcZEn4E2tJ/6u/Aa6WwYyADbeVVFNFsJXgeSYCXiD4i0rQdJqquO3JMSl776z7e7xlvqXZoyCNpCGM6IL0tYJlYuA3ceeJ3Yn5FpHRlAjLsxNhg3+0+BAzrgCPxyoluitZM8nOYZ4VMKrWbVd6OP4i1CLJdrihvwoBmNQJly5tJfRPfyVpFnD5XjPw8dPeml7/x5Ip5RdORf9mOQd4dWi4LKqJQbe6EpzX6BYUKAlQ+kNI9JjPtGV/eWvwF4OIyFoWLTcsBQjnlwLs+05eZfPMKqr5AxDixrCvWotNm1nWDmB6cPR8IDjCWJ6QO/0dNPaMNbIHv62zD2IfZR+Ke/BLaL62KlS/sKCLBa/a0RmTo4+DdcP567g4YCw12iojLVa+7HHusm0YUCt1oo5R8bKvAFRr2UVYB5Y4RZGBo9HnwXVd1MSRDG2xhTRgUppfKY2SO/y3m9Fhxx11h2S4it1DtOvz/3F7qMvhp1m5XQ/gEbLF4rxld64IaLtksTlR6hSXLZatpWHaYzBD6sQnJupLKni+VgOPXCGmb0mUkodumKaEUGkBaY23plNmwSMUtvOXj3EJeFdmbksVH9Rt+vCoPnpO6z8ZaX3iL32KaUFayUXKGunEcBgHwbMnVQl/QzB8STgZeA9WD/1rAJrSMcJ2PTxc95m0DWUO6LR/L0A1hr7t3RGnQSgz8TMjH6yrSfEZ0j5fp4Ge0aXopiMNrRXMiyfM/xW508b1kYCu7WJ8WBhFSZq9P87asJBVKAkSmAsE5Rd6mqM3MTzrceOOKJRXo5WO6HaJx9thdgzZYThtDLg6j7DcCv4m6v9A0GZzMYBicNdmS1Pyh889c7fxlvAqdMyr5c3i0wt2LUAw09+6VslTlFrf7lL8iz1FsRQJwfVrk0X2JiFt4CLMXFsf9ofTYgC4c7sWYMolxXLDbWzt1QQP7myOlBPJNret96uGIM9DSjdsYgfAj+D5Fh0tfoGkjigEIjvFLEaXHr14W6HzGP6uvb4vxMrmhawaLuHxvaBr3AZaWq8LI/F5wvu3cevgjo97wio5jtsTILoE6/554okCG49LXn+yk8WvbqOPHeMQloWQgHKe879oT3a7miNv8YLSODk4KA+/Yt++BaN1DQ7lgM7R/5sttvbxcO+V+eKaO0aRCGJ09ekE6LA=="]
        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
                "top_k": 5,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("results")) == 1
        assert resp.json_get("results.0.feature_results.0.code") == -1
        assert "feature’s version and group's version are not equal" in resp.json_get("results.0.feature_results.0.msg")

        features = ["U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpMVBxcGOLuDhv9YTSHWZltkJHI4QqW3YqmykY8MFYidmu7g5xQKjOFMGZQkaogMCoHUgtsXhPblVX8vSSEOh1GieXjvG7Xxu7m61cirXyRLv2KHdi66VZnQ0WoqddSpvbfXTf+3i1jHjs3PKSPFP0GJ2Xza2eWmsiQwYbK+K9nrw8KM86C5Ch+E1mJW6XfeaImrYdjRjhqRHPAFmjzk22MpRYoiJaks2QhNBjy6TUZWj+xcPBTg2wYrPddtI53zm0fJQ3Wtc4hZTqat/oJrTNled5kJ7NoXqP967l+re3Wt3igFcMHHsUhvvTz8Ie1CudEtasM14ut7D02HyKGuTXifUfztOKCFXUQ76vXjC470LsSoCbEM9t6b/nOq7hN3OSyZrYTuvRh4S+G0ypE/F9AEeUAUaBFYmgPS0tVNexccveZ75NXNFXCwfMd0eeG3hKzSIOVaKF2lGZAw1ck+95mpx0g7jLczri0JLttchXFzZge3VCWxB4J9bKDuYQps46Clhm6FMLApeyGoKT4Dd8nq5OAtqBkc2c1o1VTSc+xXATGRRBSTXI+8DijjNktMQTUoSKbZ59JYYeej7wHFVdGF5Xtz8R16T8/VWWNxrpu3Z/Z24KP1+oQhe8O1vIQF31rDlWh3SxZHMjKI2bMjkBijq39EMOrvOHQ9ttJh+P0r0VpzgQezrm7V1KtJ/SmKeG1Q2h+X2nvZ7zL6x2zRVF7//KN2+TRZ2T6be8e02GpY4UG2g6wbq9wARFG1L1TAaj/czCk3Ts4vv02c8gML0I1UD5PNuOYXSQDcCcnTrfgaNibl6tH9EgB77hYqCFQRcfNfpHgJXGITyUPPKhmx3D+gIHCitc46eLijmsuwdcJqU0xHj6dQrufgFuVmltskunVbVoIg1k9EdJxYqalSYyu2dviz/3WmEoACZYNITnBt79DoFzNvK3dQiPBKhvH0kcKKE8bHM3E32Oa9BXDBdK7ZrnZJSFAOizJoA9QqTCSgzrTaDdufO5FkGBi09k4hzJgow7D4T5cANHOh/AoDZNjJNZngoYkXbA0rVQXYraXLU09JI0UFVf6Ho4Ya9x1/EQgtftK+Je4HM8YtkUdTh7EicT81jgYgGrAJVtPOCAVw1BGadBAL61dMjIMrPLKEy/5XdOwTYVFIyI5Zg5Y9HE471qlCYWOPLQh4HPxDXGiyBOA76GWdSeciM/KKhYSBwMvUXK0I+MYsPKgjTuuuvQqgQSO1uiKSDi+S9Va1NwfyjmkKj+9f9oaQoDdgtCT8Y1nxpTgBa4gQEzCguTtWBqADPVM00hNK5YlU2yyNwBW+ROCNPke5ctQF/ovcOmWCnEGcldlde4rq6Pq/oSi3w1Pw=="]
        search_configs = []
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: search_configs is reuired"

        # 5 测试searchfeature,feature超出范围（1），期望接口返回失败
        features = [
            "U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpMVBxcGOLuDhv9YTSHWZltkJHI4QqW3YqmykY8MFYidmu7g5xQKjOFMGZQkaogMCoHUgtsXhPblVX8vSSEOh1GieXjvG7Xxu7m61cirXyRLv2KHdi66VZnQ0WoqddSpvbfXTf+3i1jHjs3PKSPFP0GJ2Xza2eWmsiQwYbK+K9nrw8KM86C5Ch+E1mJW6XfeaImrYdjRjhqRHPAFmjzk22MpRYoiJaks2QhNBjy6TUZWj+xcPBTg2wYrPddtI53zm0fJQ3Wtc4hZTqat/oJrTNled5kJ7NoXqP967l+re3Wt3igFcMHHsUhvvTz8Ie1CudEtasM14ut7D02HyKGuTXifUfztOKCFXUQ76vXjC470LsSoCbEM9t6b/nOq7hN3OSyZrYTuvRh4S+G0ypE/F9AEeUAUaBFYmgPS0tVNexccveZ75NXNFXCwfMd0eeG3hKzSIOVaKF2lGZAw1ck+95mpx0g7jLczri0JLttchXFzZge3VCWxB4J9bKDuYQps46Clhm6FMLApeyGoKT4Dd8nq5OAtqBkc2c1o1VTSc+xXATGRRBSTXI+8DijjNktMQTUoSKbZ59JYYeej7wHFVdGF5Xtz8R16T8/VWWNxrpu3Z/Z24KP1+oQhe8O1vIQF31rDlWh3SxZHMjKI2bMjkBijq39EMOrvOHQ9ttJh+P0r0VpzgQezrm7V1KtJ/SmKeG1Q2h+X2nvZ7zL6x2zRVF7//KN2+TRZ2T6be8e02GpY4UG2g6wbq9wARFG1L1TAaj/czCk3Ts4vv02c8gML0I1UD5PNuOYXSQDcCcnTrfgaNibl6tH9EgB77hYqCFQRcfNfpHgJXGITyUPPKhmx3D+gIHCitc46eLijmsuwdcJqU0xHj6dQrufgFuVmltskunVbVoIg1k9EdJxYqalSYyu2dviz/3WmEoACZYNITnBt79DoFzNvK3dQiPBKhvH0kcKKE8bHM3E32Oa9BXDBdK7ZrnZJSFAOizJoA9QqTCSgzrTaDdufO5FkGBi09k4hzJgow7D4T5cANHOh/AoDZNjJNZngoYkXbA0rVQXYraXLU09JI0UFVf6Ho4Ya9x1/EQgtftK+Je4HM8YtkUdTh7EicT81jgYgGrAJVtPOCAVw1BGadBAL61dMjIMrPLKEy/5XdOwTYVFIyI5Zg5Y9HE471qlCYWOPLQh4HPxDXGiyBOA76GWdSeciM/KKhYSBwMvUXK0I+MYsPKgjTuuuvQqgQSO1uiKSDi+S9Va1NwfyjmkKj+9f9oaQoDdgtCT8Y1nxpTgBa4gQEzCguTtWBqADPVM00hNK5YlU2yyNwBW+ROCNPke5ctQF/ovcOmWCnEGcldlde4rq6Pq/oSi3w1Pw==",
            "U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpMVBxcGOLuDhv9YTSHWZltkJHI4QqW3YqmykY8MFYidmu7g5xQKjOFMGZQkaogMCoHUgtsXhPblVX8vSSEOh1GieXjvG7Xxu7m61cirXyRLv2KHdi66VZnQ0WoqddSpvbfXTf+3i1jHjs3PKSPFP0GJ2Xza2eWmsiQwYbK+K9nrw8KM86C5Ch+E1mJW6XfeaImrYdjRjhqRHPAFmjzk22MpRYoiJaks2QhNBjy6TUZWj+xcPBTg2wYrPddtI53zm0fJQ3Wtc4hZTqat/oJrTNled5kJ7NoXqP967l+re3Wt3igFcMHHsUhvvTz8Ie1CudEtasM14ut7D02HyKGuTXifUfztOKCFXUQ76vXjC470LsSoCbEM9t6b/nOq7hN3OSyZrYTuvRh4S+G0ypE/F9AEeUAUaBFYmgPS0tVNexccveZ75NXNFXCwfMd0eeG3hKzSIOVaKF2lGZAw1ck+95mpx0g7jLczri0JLttchXFzZge3VCWxB4J9bKDuYQps46Clhm6FMLApeyGoKT4Dd8nq5OAtqBkc2c1o1VTSc+xXATGRRBSTXI+8DijjNktMQTUoSKbZ59JYYeej7wHFVdGF5Xtz8R16T8/VWWNxrpu3Z/Z24KP1+oQhe8O1vIQF31rDlWh3SxZHMjKI2bMjkBijq39EMOrvOHQ9ttJh+P0r0VpzgQezrm7V1KtJ/SmKeG1Q2h+X2nvZ7zL6x2zRVF7//KN2+TRZ2T6be8e02GpY4UG2g6wbq9wARFG1L1TAaj/czCk3Ts4vv02c8gML0I1UD5PNuOYXSQDcCcnTrfgaNibl6tH9EgB77hYqCFQRcfNfpHgJXGITyUPPKhmx3D+gIHCitc46eLijmsuwdcJqU0xHj6dQrufgFuVmltskunVbVoIg1k9EdJxYqalSYyu2dviz/3WmEoACZYNITnBt79DoFzNvK3dQiPBKhvH0kcKKE8bHM3E32Oa9BXDBdK7ZrnZJSFAOizJoA9QqTCSgzrTaDdufO5FkGBi09k4hzJgow7D4T5cANHOh/AoDZNjJNZngoYkXbA0rVQXYraXLU09JI0UFVf6Ho4Ya9x1/EQgtftK+Je4HM8YtkUdTh7EicT81jgYgGrAJVtPOCAVw1BGadBAL61dMjIMrPLKEy/5XdOwTYVFIyI5Zg5Y9HE471qlCYWOPLQh4HPxDXGiyBOA76GWdSeciM/KKhYSBwMvUXK0I+MYsPKgjTuuuvQqgQSO1uiKSDi+S9Va1NwfyjmkKj+9f9oaQoDdgtCT8Y1nxpTgBa4gQEzCguTtWBqADPVM00hNK5YlU2yyNwBW+ROCNPke5ctQF/ovcOmWCnEGcldlde4rq6Pq/oSi3w1Pw=="
        ]
        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
                "top_k": 5,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: features' length must be 1"

        # 6. 测试searchfeature,groups超出范围（10），期望接口返回失败
        features = [
            "U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpMVBxcGOLuDhv9YTSHWZltkJHI4QqW3YqmykY8MFYidmu7g5xQKjOFMGZQkaogMCoHUgtsXhPblVX8vSSEOh1GieXjvG7Xxu7m61cirXyRLv2KHdi66VZnQ0WoqddSpvbfXTf+3i1jHjs3PKSPFP0GJ2Xza2eWmsiQwYbK+K9nrw8KM86C5Ch+E1mJW6XfeaImrYdjRjhqRHPAFmjzk22MpRYoiJaks2QhNBjy6TUZWj+xcPBTg2wYrPddtI53zm0fJQ3Wtc4hZTqat/oJrTNled5kJ7NoXqP967l+re3Wt3igFcMHHsUhvvTz8Ie1CudEtasM14ut7D02HyKGuTXifUfztOKCFXUQ76vXjC470LsSoCbEM9t6b/nOq7hN3OSyZrYTuvRh4S+G0ypE/F9AEeUAUaBFYmgPS0tVNexccveZ75NXNFXCwfMd0eeG3hKzSIOVaKF2lGZAw1ck+95mpx0g7jLczri0JLttchXFzZge3VCWxB4J9bKDuYQps46Clhm6FMLApeyGoKT4Dd8nq5OAtqBkc2c1o1VTSc+xXATGRRBSTXI+8DijjNktMQTUoSKbZ59JYYeej7wHFVdGF5Xtz8R16T8/VWWNxrpu3Z/Z24KP1+oQhe8O1vIQF31rDlWh3SxZHMjKI2bMjkBijq39EMOrvOHQ9ttJh+P0r0VpzgQezrm7V1KtJ/SmKeG1Q2h+X2nvZ7zL6x2zRVF7//KN2+TRZ2T6be8e02GpY4UG2g6wbq9wARFG1L1TAaj/czCk3Ts4vv02c8gML0I1UD5PNuOYXSQDcCcnTrfgaNibl6tH9EgB77hYqCFQRcfNfpHgJXGITyUPPKhmx3D+gIHCitc46eLijmsuwdcJqU0xHj6dQrufgFuVmltskunVbVoIg1k9EdJxYqalSYyu2dviz/3WmEoACZYNITnBt79DoFzNvK3dQiPBKhvH0kcKKE8bHM3E32Oa9BXDBdK7ZrnZJSFAOizJoA9QqTCSgzrTaDdufO5FkGBi09k4hzJgow7D4T5cANHOh/AoDZNjJNZngoYkXbA0rVQXYraXLU09JI0UFVf6Ho4Ya9x1/EQgtftK+Je4HM8YtkUdTh7EicT81jgYgGrAJVtPOCAVw1BGadBAL61dMjIMrPLKEy/5XdOwTYVFIyI5Zg5Y9HE471qlCYWOPLQh4HPxDXGiyBOA76GWdSeciM/KKhYSBwMvUXK0I+MYsPKgjTuuuvQqgQSO1uiKSDi+S9Va1NwfyjmkKj+9f9oaQoDdgtCT8Y1nxpTgBa4gQEzCguTtWBqADPVM00hNK5YlU2yyNwBW+ROCNPke5ctQF/ovcOmWCnEGcldlde4rq6Pq/oSi3w1Pw=="]
        search_configs = []
        for x in range(11):
            search_configs.append(
                {
                    "group_id": streamGroup,
                    "threshold": 0.9,
                    "top_k": 5,
                }
            )
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: search_configs' length is between 1 and 10"

        # 7.测试searchfeature,topk为空或者超出范围（3-5），期望接口返回失败
        features = [
            "U09GMUZhAAAQBAAAAAEAAAAAAAAEAAAAAAAAAAAAAAAyFxVGIw3ltI5jJPHdTOdpMVBxcGOLuDhv9YTSHWZltkJHI4QqW3YqmykY8MFYidmu7g5xQKjOFMGZQkaogMCoHUgtsXhPblVX8vSSEOh1GieXjvG7Xxu7m61cirXyRLv2KHdi66VZnQ0WoqddSpvbfXTf+3i1jHjs3PKSPFP0GJ2Xza2eWmsiQwYbK+K9nrw8KM86C5Ch+E1mJW6XfeaImrYdjRjhqRHPAFmjzk22MpRYoiJaks2QhNBjy6TUZWj+xcPBTg2wYrPddtI53zm0fJQ3Wtc4hZTqat/oJrTNled5kJ7NoXqP967l+re3Wt3igFcMHHsUhvvTz8Ie1CudEtasM14ut7D02HyKGuTXifUfztOKCFXUQ76vXjC470LsSoCbEM9t6b/nOq7hN3OSyZrYTuvRh4S+G0ypE/F9AEeUAUaBFYmgPS0tVNexccveZ75NXNFXCwfMd0eeG3hKzSIOVaKF2lGZAw1ck+95mpx0g7jLczri0JLttchXFzZge3VCWxB4J9bKDuYQps46Clhm6FMLApeyGoKT4Dd8nq5OAtqBkc2c1o1VTSc+xXATGRRBSTXI+8DijjNktMQTUoSKbZ59JYYeej7wHFVdGF5Xtz8R16T8/VWWNxrpu3Z/Z24KP1+oQhe8O1vIQF31rDlWh3SxZHMjKI2bMjkBijq39EMOrvOHQ9ttJh+P0r0VpzgQezrm7V1KtJ/SmKeG1Q2h+X2nvZ7zL6x2zRVF7//KN2+TRZ2T6be8e02GpY4UG2g6wbq9wARFG1L1TAaj/czCk3Ts4vv02c8gML0I1UD5PNuOYXSQDcCcnTrfgaNibl6tH9EgB77hYqCFQRcfNfpHgJXGITyUPPKhmx3D+gIHCitc46eLijmsuwdcJqU0xHj6dQrufgFuVmltskunVbVoIg1k9EdJxYqalSYyu2dviz/3WmEoACZYNITnBt79DoFzNvK3dQiPBKhvH0kcKKE8bHM3E32Oa9BXDBdK7ZrnZJSFAOizJoA9QqTCSgzrTaDdufO5FkGBi09k4hzJgow7D4T5cANHOh/AoDZNjJNZngoYkXbA0rVQXYraXLU09JI0UFVf6Ho4Ya9x1/EQgtftK+Je4HM8YtkUdTh7EicT81jgYgGrAJVtPOCAVw1BGadBAL61dMjIMrPLKEy/5XdOwTYVFIyI5Zg5Y9HE471qlCYWOPLQh4HPxDXGiyBOA76GWdSeciM/KKhYSBwMvUXK0I+MYsPKgjTuuuvQqgQSO1uiKSDi+S9Va1NwfyjmkKj+9f9oaQoDdgtCT8Y1nxpTgBa4gQEzCguTtWBqADPVM00hNK5YlU2yyNwBW+ROCNPke5ctQF/ovcOmWCnEGcldlde4rq6Pq/oSi3w1Pw=="]
        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
                "top_k": 0,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: search_configs[0].top_k is invalid"

        search_configs = [
            {
                "group_id": streamGroup,
                "threshold": 0.9,
                "top_k": 21,
            },
        ]
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: search_configs[0].top_k is invalid"

        # 8.删除person
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup,person_id="cyf1")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf2")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf3")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf4")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf5")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="zxq")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    # bug
    def test_scenario_person_010_SearchImageWithBound(self, config_obj, staticGroup, streamGroup, ArgusdbApi):
        """ SearchImageWithBound """
        """
        1.测试api接口添加会员,steamgroup里添加cyf1,cyf2,cyf3,cyf4期望添加成功
        2.添加了Bounding的测试,group中有4条结果,传top3，期望返回列表为3
        3.测试apisearchimage,带bound参数，twoface,传大框，期望搜索的是大脸人员wsh，期望返回正确
        4.添加了Bounding的测试,group中没有搜到结果,期望返回列表为空
        5.添加了Bounding的测试, image里没有face，期望接口返回noface的错误提示
        6.测试动态入库的功能，动态入库的底库图，期望能search出来; 动态库所绑定的静态库中personadd的人，搜索动态库时搜索不出来
        """
        # 1.测试api接口添加会员,steamgroup里添加cyf1,cyf2,cyf3,cyf4期望添加成功
        ak = config_obj.Argus.ak
        personID = "cyf1"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf2"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf2.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf3"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf3.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "cyf4"  # 1440 * 1080
        override = "1"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf4.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 2.添加了Bounding的测试,group中有4条结果,传top3，期望返回列表为3
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        img = Image.open(file_path)
        width = img.width
        height = img.height
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": width, "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=streamGroup, bounding=bounding,threshold=0.9, top_k=3)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 3
        assert resp.json_get("list.0.person_id") == "cyf1"
        assert resp.json_get("list.0.feature_id")
        assert resp.json_get("list.0.score") >= 0.99

        # 3. 测试apisearchimage,带bound参数，twoface,传大框，期望搜索的是大脸人员wsh，期望返回正确
        file_path = os.path.join(config.goimage_path, "twoface.jpg")
        img = Image.open(file_path)
        width = img.width
        height = img.height
        # 大框，含两张脸，期望返回大face 诗涵
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": width, "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=streamGroup, bounding=bounding,
                                                  threshold=0.9, top_k=3)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0

        # 左边小脸，凤姐
        file_path = os.path.join(config.goimage_path, "twoface.jpg")
        img = Image.open(file_path)
        width = img.width
        height = img.height
        # 大框，含两张脸，期望返回大face 诗涵
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": int(width/2), "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=streamGroup, bounding=bounding,
                                                  threshold=0.9, top_k=3)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 3

        # 右边大脸，诗涵
        file_path = os.path.join(config.goimage_path, "twoface.jpg")
        img = Image.open(file_path)
        width = img.width
        height = img.height
        # 大框，含两张脸，期望返回大face 诗涵
        bounding = {
            "vertices": [
                {"x": int(width / 2), "y": 1},
                {"x": width, "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=streamGroup, bounding=bounding,
                                                  threshold=0.9, top_k=5)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0

        # 4.添加了Bounding的测试,group中没有搜到结果,期望返回列表为空
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        img = Image.open(file_path)
        width = img.width
        height = img.height
        # 大框，含两张脸，期望返回大face 诗涵
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": width, "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, bounding=bounding,
                                                  threshold=0.9, top_k=5)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0

        # 5.添加了Bounding的测试, image里没有face，期望接口返回noface的错误提示
        file_path = os.path.join(config.goimage_path, "nobody.jpg")
        img = Image.open(file_path)
        width = img.width
        height = img.height
        # 大框，含两张脸，期望返回大face 诗涵
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": width, "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=staticGroup, bounding=bounding,
                                                  threshold=0.9, top_k=5)

        assert resp.status_code == 500
        assert resp.json_get("error_code") == 2
        assert resp.json_get("error_msg") == "INTERNAL: overlap failed: no face"
        # assert len(resp.json_get("list")) == 0

        # 删除person
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf1")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf2")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf3")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=streamGroup, person_id="cyf4")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_person_011_dynamic_penestrain(self, config_obj, ArgusdbApi, ArguspedestrianApi):
        """ 测试动态入库的功能，动态入库的底库图，期望能search出来; 动态库所绑定的静态库中personadd的人，搜索动态库时搜索不出来"""
        ak = config_obj.Argus.ak
        group_name1 = "staticDb_1_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold1 = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold1, group_name=group_name1,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        group_id1 = resp.json_get("group_id")
        time_utils.sleep(1)
        log().info("static group1:%s" % group_id1)

        group_name3 = "streamDb_bind_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold3 = "FACE"
        group_size = 6000000
        bind_groups = [group_id1]
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold3, group_name=group_name3,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        group_id3 = resp.json_get("group_id")
        log().info("stream group3:%s" % group_id3)
        time_utils.sleep(65)

        # 静态库添加cyf
        personID = "cyf1"  # 1440 * 1080
        override = "0"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=group_id1, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 搜索动态库里，cyf返回搜索列表为空
        img = Image.open(file_path)
        width = img.width
        height = img.height
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": width, "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=group_id3, bounding=bounding,
                                                  threshold=0.9, top_k=5)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0

        # 动态推送诗涵
        image_path = os.path.join(config.goimage_path, "face/wsh/shihan1.jpg")
        timestamp = time_utils.get_timestamp()
        resp = ArguspedestrianApi.Pedestrian_face(group_id3, image_path, timestamp, requestId="facerequestID", ak=ak, device_id="testdevice", camera_name="testcamera")
        assert resp.status_code == 200
        time_utils.sleep(10)

        # 搜索动态库里，wsh返回搜索列表为1
        img = Image.open(image_path)
        width = img.width
        height = img.height
        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": width, "y": height}
            ]
        }
        bounding = json.dumps(bounding)
        resp = ArgusdbApi.SearchImagePostFromFile(image_path, ak=ak, group_id=group_id3, bounding=bounding,
                                                  threshold=0.9, top_k=5)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        person_id = resp.json_get("list.0.person_id")

        resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=group_id3, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == person_id
        assert resp.json_get("list.0.image")

        # 删除库
        resp = ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id1)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        time_utils.sleep(2)

        resp = ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=group_id3)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_person_012_DbMultiFaceSearch(self, config_obj, ArgusdbApi, ArguspedestrianApi):
        """ 测试动态入库的功能，动态入库的底库图，期望能search出来; 动态库所绑定的静态库中personadd的人，搜索动态库时搜索不出来"""
        """
        1. 动态推送诗涵
        2. 动态推送cyf
        3. 用带有towface的图调用multisearch接口，期望能搜出来shihan和cyf
        """
        ak = config_obj.Argus.ak
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = None
        group_tag = None
        expired_time = 180
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        streamGroup = resp.json_get("group_id")
        time_utils.sleep(65)

        image_path = os.path.join(config.goimage_path, "face/wsh/shihan1.jpg")
        timestamp = time_utils.get_timestamp()
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testcamera")
        assert resp.status_code == 200
        time_utils.sleep(2)

        image_path = os.path.join(config.goimage_path, "face/cyf/cyf4.jpg")
        timestamp = time_utils.get_timestamp()
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testcamera")
        assert resp.status_code == 200
        time_utils.sleep(2)

        file_path = os.path.join(config.goimage_path, "twoface.jpg")
        resp = ArgusdbApi.SearchImageMultiFaceFromFile(file_path, ak=ak, group_id=streamGroup, threshold=0.5,
                                                       top_k=5)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("results")) == 3
        count = 0
        for idx, res in enumerate(resp.json_get("results")):
            if len(res["list"]) != 0:
                count += 1
                with check: assert res["list"][0]["score"] >= 0.9
                with check: assert res["quality"] >= 0.7
        assert count == 2

    def test_scenario_person_013_ImageDetect(self, config_obj, ArgusdbApi):
        """ 图片检测"""
        ak = config_obj.Argus.ak
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = None
        group_tag = None
        expired_time = 180
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        streamGroup = resp.json_get("group_id")
        time_utils.sleep(65)

        ak = config_obj.Argus.ak
        group_id = streamGroup
        image = ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/wsh/shihan1.jpg"))
        resp = ArgusdbApi.DB_ImageDetectPostApi(ak=ak, group_id=group_id, image=image)
        assert resp.status_code == 200
        #TODO 子木配合修改配置

    # TODO 子木确认用法
    # def test_scenario_person_014_bgImage(self, config_obj, ArgusdbApi, ArguspedestrianApi):
    #     """ 测试获取背景大图"""
    #     """
    #     1. 创建动态库，打开存图开关
    #     1. 动态推送诗涵
    #     2. 获取背景大图
    #     """
    #     ak = config_obj.Argus.ak
    #     group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
    #     group_mold = "PEDESTRIAN"
    #     group_size = 6000000
    #     bind_groups = None
    #     group_tag = None
    #     expired_time = 180
    #     pedes_cb_url = config_obj.Argus.pedes_cb_url
    #     merge_cb_url = None
    #     resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
    #                                         group_mold=group_mold, group_name=group_name,
    #                                         group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
    #                                         pedes_cb_url=pedes_cb_url, save_image_option=True)
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert resp.json_get("group_id")
    #     assert resp.json_get("feature_version") == config_obj.Argus.feature_version
    #     streamGroup = resp.json_get("group_id")
    #     time_utils.sleep(2)
    #
    #     image_path = os.path.join(config.goimage_path, "face/wsh/shihan1.jpg")
    #     timestamp = None
    #     requestId = "shihan1"
    #     resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
    #                                               camera_name="testcamera", requestId=requestId)
    #     assert resp.status_code == 200
    #     time_utils.sleep(2)  # TODO 这里需要等65秒嘛？
    #
    #     resp = ArgusdbApi.DB_GetBgImageGetApi(ak=ak, group_id=streamGroup, bg_request_id=requestId)
    #     assert resp.status_code == 200
    #     assert resp.json_get("request_id") == requestId
    #     assert resp.json_get("bg_oss_url")

    # 存图的先不测
    # def test_scenario_person_015_SaveImageOption(self, config_obj, ArgusdbApi):
    #     """ 测试不存图开关"""
    #     """
    #     staticid1:不存图
    #     staticid2:存图
    #     streamid1:不存图
    #     streamid2:存图
    #     1. 测试静态库不存图，查询person返回image为空
    #     2. 测试静态库存图， 查询person返回image有值
    #     3. 测试动态库不存图，查询person返回image为空
    #     4. 测试动态库存图，查询person返回image有值
    #
    #     TODO 更新库的save_image_option参数后，对库中原有图片是否有影响？ 对新插入的图片有什么影响？
    #     """
    #     ak = config_obj.Argus.ak
    #     group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
    #     group_mold = "FACE"
    #     group_size = 5000000
    #     group_tag = None
    #     pedes_cb_url = config_obj.Argus.pedes_cb_url
    #     save_image_option = False
    #     resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
    #                                         group_size=group_size, group_tag=group_tag,save_image_option=save_image_option,
    #                                         pedes_cb_url=pedes_cb_url, is_delete=False)
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert resp.json_get("group_id")
    #     assert resp.json_get("feature_version") == config_obj.Argus.feature_version
    #     staticid1 = resp.json_get("group_id")
    #     time_utils.sleep(30)
    #     # 添加人
    #     personID = "cyf"
    #     override = "0"
    #     file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
    #     resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticid1, person_id=personID,
    #                                                override=override)
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert resp.json_get("person_id") == personID
    #     time_utils.sleep(2)
    #
    #     # 再创建一个静态库
    #     group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
    #     group_mold = "FACE"
    #     group_size = 5000000
    #     group_tag = None
    #     pedes_cb_url = config_obj.Argus.pedes_cb_url
    #     save_image_option = True
    #     resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
    #                                         group_size=group_size, group_tag=group_tag, save_image_option=save_image_option,
    #                                         pedes_cb_url=pedes_cb_url, is_delete=False)
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert resp.json_get("group_id")
    #     assert resp.json_get("feature_version") == config_obj.Argus.feature_version
    #     staticid2 = resp.json_get("group_id")
    #     time_utils.sleep(30)
    #     personID2 = "cyf"
    #     override = "0"
    #     file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
    #     resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticid2, person_id=personID2,
    #                                                override=override)
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert resp.json_get("person_id") == personID2
    #
    #     # 创建动态库
    #     group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
    #     group_mold = "FACE"
    #     group_size = 6000000
    #     bind_groups = None
    #     group_tag = None
    #     expired_time = 100
    #     pedes_cb_url = config_obj.Argus.pedes_cb_url
    #     merge_cb_url = None
    #     save_image_option = False
    #     resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
    #                                         group_mold=group_mold, group_name=group_name,save_image_option=save_image_option,
    #                                         group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
    #                                         pedes_cb_url=pedes_cb_url, is_delete=False)
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert resp.json_get("group_id")
    #     assert resp.json_get("feature_version") == config_obj.Argus.feature_version
    #     streamid1 = resp.json_get("group_id")
    #     time_utils.sleep(65)
    #
    #     # 推人
    #     image_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
    #     timestamp = time_utils.get_timestamp()
    #     resp = ArguspedestrianApi.Pedestrian_face(streamid1, image_path, timestamp, ak=ak, device_id="testdevice",
    #                                               camera_name="testcamera", requestId="faceRequestID1")
    #     assert resp.status_code == 200
    #     time_utils.sleep(1)
    #
    #     image_path = os.path.join(config.goimage_path, "face/wsh/shihan4.jpg")
    #     timestamp = time_utils.get_timestamp()
    #     resp = ArguspedestrianApi.Pedestrian_face(streamid1, image_path, timestamp, ak=ak, device_id="testdevice",
    #                                               camera_name="testcamera", requestId="faceRequestID2")
    #     assert resp.status_code == 200
    #     time_utils.sleep(1)
    #
    #     # 创建动态库2
    #     group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
    #     group_mold = "FACE"
    #     group_size = 6000000
    #     bind_groups = None
    #     group_tag = None
    #     expired_time = 100
    #     pedes_cb_url = config_obj.Argus.pedes_cb_url
    #     merge_cb_url = None
    #     save_image_option = True
    #     resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
    #                                         group_mold=group_mold, group_name=group_name,save_image_option=save_image_option,
    #                                         group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
    #                                         pedes_cb_url=pedes_cb_url, is_delete=False)
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert resp.json_get("group_id")
    #     assert resp.json_get("feature_version") == config_obj.Argus.feature_version
    #     streamid2 = resp.json_get("group_id")
    #     time_utils.sleep(65)
    #
    #     # 推人
    #     image_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
    #     timestamp = time_utils.get_timestamp()
    #     resp = ArguspedestrianApi.Pedestrian_face(streamid2, image_path, timestamp, ak=ak, device_id="testdevice",
    #                                               camera_name="testcamera", requestId="faceRequestID1")
    #     assert resp.status_code == 200
    #     time_utils.sleep(1)
    #
    #     image_path = os.path.join(config.goimage_path, "face/wsh/shihan4.jpg")
    #     timestamp = time_utils.get_timestamp()
    #     resp = ArguspedestrianApi.Pedestrian_face(streamid2, image_path, timestamp, ak=ak, device_id="testdevice",
    #                                               camera_name="testcamera", requestId="faceRequestID2")
    #     assert resp.status_code == 200
    #     time_utils.sleep(1)
    #
    #     log().info("staticid1=%s" % staticid1)
    #     log().info("staticid2=%s" % staticid2)
    #     log().info("streamid1=%s" % streamid1)
    #     log().info("streamid2=%s" % streamid2)
    #     # 1. 测试静态库不存图，查询person返回image为空
    #     resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=staticid1, person_id="cyf")
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert len(resp.json_get("list")) == 1
    #     assert resp.json_get("list.0.person_id") == "cyf"
    #     assert not resp.json_get("list.0.image")
    #     # 2. 测试静态库存图， 查询person返回image有值
    #     resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=staticid1, person_id="cyf")
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert len(resp.json_get("list")) == 1
    #     assert resp.json_get("list.0.person_id") == "cyf"
    #     assert resp.json_get("list.0.image")
    #     # 3. 测试动态库不存图，查询person返回image为空
    #     file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
    #     resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=streamid1, threshold="0.9", top_k="5")
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert len(resp.json_get("list")) == 1
    #     assert resp.json_get("list.0.person_id")
    #     assert resp.json_get("list.0.score") >= 0.999
    #
    #     person_id = resp.json_get("list.0.person_id")
    #     resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=streamid1, person_id=person_id)
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert len(resp.json_get("list")) == 1
    #     assert resp.json_get("list.0.person_id") == person_id
    #     assert not resp.json_get("list.0.image")
    #     # 4. 测试动态库存图，查询person返回image有值
    #     file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
    #     resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=streamid2, threshold="0.9", top_k="5")
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert len(resp.json_get("list")) == 1
    #     assert resp.json_get("list.0.person_id")
    #     assert resp.json_get("list.0.score") >= 0.999
    #
    #     person_id = resp.json_get("list.0.person_id")
    #     resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=streamid2, person_id=person_id)
    #     assert resp.status_code == 200
    #     assert resp.json_get("error_code") == 0
    #     assert resp.json_get("error_msg") == "OK"
    #     assert len(resp.json_get("list")) == 1
    #     assert resp.json_get("list.0.person_id") == person_id
    #     assert resp.json_get("list.0.image")
