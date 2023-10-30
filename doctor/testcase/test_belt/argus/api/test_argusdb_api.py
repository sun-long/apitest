#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArgusdbApi(object):
    """ argusDb Api测试"""

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

    def test_api_DB_BatchSearchFeature(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        features = None
        search_configs = None
        resp = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs)
        assert resp.status_code == 200

    def test_api_DB_BatchSearchImage(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        images = None
        search_configs = None
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200

    def test_api_DB_GetBgImage(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        bg_request_id = None
        resp = ArgusdbApi.DB_GetBgImageGetApi(ak=ak, group_id=group_id, bg_request_id=bg_request_id)
        assert resp.status_code == 200

    def test_api_DB_DeletePerson(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        person_id = None
        resp = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=group_id, person_id=person_id)
        assert resp.status_code == 200

    def test_api_DB_DeleteStaticGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        resp = ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200

    def test_api_DB_DeleteStreamGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        resp = ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200

    def test_api_DB_ImageDetect(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        image = None
        resp = ArgusdbApi.DB_ImageDetectPostApi(ak=ak, group_id=group_id, image=image)
        assert resp.status_code == 200

    def test_api_DB_GetPerson(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        person_id = None
        resp = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=group_id, person_id=person_id)
        assert resp.status_code == 200

    def test_api_DB_CreatePerson(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        bounding = None
        group_id = None
        image = None
        override = None
        person_id = None
        resp = ArgusdbApi.DB_CreatePersonPostApi(ak=ak, bounding=bounding, group_id=group_id, image=image, override=override, person_id=person_id)
        assert resp.status_code == 200

    def test_api_DB_ListPerson(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        limit = None
        offset = None
        reversed = None
        resp = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id=group_id, limit=limit, offset=offset, reversed=reversed)
        assert resp.status_code == 200

    def test_api_DB_CreatePersonByFeature(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        feature = None
        group_id = None
        override = None
        person_id = None
        resp = ArgusdbApi.DB_CreatePersonByFeaturePostApi(ak=ak, feature=feature, group_id=group_id, override=override, person_id=person_id)
        assert resp.status_code == 200

    def test_api_DB_SearchFeature(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        feature = None
        group_id = None
        threshold = None
        top_k = None
        resp = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, feature=feature, group_id=group_id, threshold=threshold, top_k=top_k)
        assert resp.status_code == 200

    def test_api_DB_SearchImage(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        bounding = None
        group_id = None
        image = None
        threshold = None
        top_k = None
        resp = ArgusdbApi.DB_SearchImagePostApi(ak=ak, bounding=bounding, group_id=group_id, image=image, threshold=threshold, top_k=top_k)
        assert resp.status_code == 200

    def test_api_DB_SearchImageMultiFace(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        bounding = None
        group_id = None
        image = None
        threshold = None
        top_k = None
        resp = ArgusdbApi.DB_SearchImageMultiFacePostApi(ak=ak, bounding=bounding, group_id=group_id, image=image, threshold=threshold, top_k=top_k)
        assert resp.status_code == 200

    def test_api_DB_GetStaticGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = config_obj.Argus.ak
        group_id = "dc5c7ae5a8"
        resp = ArgusdbApi.DB_GetStaticGroupGetApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200

    def test_api_DB_CreateStaticGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        al_cb_url = None
        auto = None
        bind_groups = None
        conf_type = None
        event_cb_url = None
        expired_time = None
        feature_version = None
        group_mold = None
        group_name = None
        group_size = None
        group_tag = None
        ll_cb_url = None
        merge_cb_url = None
        opq_model = None
        pedes_cb_url = None
        pedes_tag = None
        peer_cb_url = None
        product_line = None
        sync = None
        use_cache = None
        use_logic_layer = None
        use_multi_face = None
        resp = ArgusdbApi.DB_CreateStaticGroupPostApi(ak=ak, al_cb_url=al_cb_url, auto=auto, bind_groups=bind_groups, conf_type=conf_type, event_cb_url=event_cb_url, expired_time=expired_time, feature_version=feature_version, group_mold=group_mold, group_name=group_name, group_size=group_size, group_tag=group_tag, ll_cb_url=ll_cb_url, merge_cb_url=merge_cb_url, opq_model=opq_model, pedes_cb_url=pedes_cb_url, pedes_tag=pedes_tag, peer_cb_url=peer_cb_url, product_line=product_line, sync=sync, use_cache=use_cache, use_logic_layer=use_logic_layer, use_multi_face=use_multi_face)
        assert resp.status_code == 200

    def test_api_DB_ListStaticGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_type = None
        resp = ArgusdbApi.DB_ListStaticGroupGetApi(ak=ak, group_type=group_type)
        assert resp.status_code == 200

    def test_api_DB_GetStreamGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = config_obj.Argus.ak
        # group_id = "7210ff24da"
        group_id = "5157110063"
        resp = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200

    def test_api_DB_CreateStreamGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        al_cb_url = None
        auto = None
        bind_groups = None
        conf_type = None
        event_cb_url = None
        expired_time = None
        feature_version = None
        group_mold = None
        group_name = None
        group_size = None
        group_tag = None
        ll_cb_url = None
        merge_cb_url = None
        opq_model = None
        pedes_cb_url = None
        pedes_tag = None
        peer_cb_url = None
        product_line = None
        sync = None
        use_cache = None
        use_logic_layer = None
        use_multi_face = None
        resp = ArgusdbApi.DB_CreateStreamGroupPostApi(ak=ak, al_cb_url=al_cb_url, auto=auto, bind_groups=bind_groups, conf_type=conf_type, event_cb_url=event_cb_url, expired_time=expired_time, feature_version=feature_version, group_mold=group_mold, group_name=group_name, group_size=group_size, group_tag=group_tag, ll_cb_url=ll_cb_url, merge_cb_url=merge_cb_url, opq_model=opq_model, pedes_cb_url=pedes_cb_url, pedes_tag=pedes_tag, peer_cb_url=peer_cb_url, product_line=product_line, sync=sync, use_cache=use_cache, use_logic_layer=use_logic_layer, use_multi_face=use_multi_face)
        assert resp.status_code == 200

    def test_api_DB_ListStreamGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = config_obj.Argus.ak
        group_type = None
        resp = ArgusdbApi.DB_ListStreamGroupGetApi(ak=ak, group_type=group_type)
        assert resp.status_code == 200

    def test_api_DB_UpdatePerson(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        image = None
        person_id = None
        resp = ArgusdbApi.DB_UpdatePersonPostApi(ak=ak, group_id=group_id, image=image, person_id=person_id)
        assert resp.status_code == 200

    def test_api_DB_UpdateStaticGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        bind_groups = None
        event_cb_url = None
        expired_time = None
        group_id = None
        group_mold = None
        group_name = None
        merge_cb_url = None
        pedes_cb_url = None
        peer_cb_url = None
        resp = ArgusdbApi.DB_UpdateStaticGroupPostApi(ak=ak, bind_groups=bind_groups, event_cb_url=event_cb_url, expired_time=expired_time, group_id=group_id, group_mold=group_mold, group_name=group_name, merge_cb_url=merge_cb_url, pedes_cb_url=pedes_cb_url, peer_cb_url=peer_cb_url)
        assert resp.status_code == 200

    def test_api_DB_UpdateStreamGroup(self, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        bind_groups = None
        event_cb_url = None
        expired_time = None
        group_id = None
        group_mold = None
        group_name = None
        merge_cb_url = None
        pedes_cb_url = None
        peer_cb_url = None
        resp = ArgusdbApi.DB_UpdateStreamGroupPostApi(ak=ak, bind_groups=bind_groups, event_cb_url=event_cb_url, expired_time=expired_time, group_id=group_id, group_mold=group_mold, group_name=group_name, merge_cb_url=merge_cb_url, pedes_cb_url=pedes_cb_url, peer_cb_url=peer_cb_url)
        assert resp.status_code == 200
