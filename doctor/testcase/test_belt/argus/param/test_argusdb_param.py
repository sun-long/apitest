#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArgusdbParam(object):
    """ argusDb Param测试"""

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

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('features', 'invalidfeatures'),
        ('features', ''),
        ('features', None),
        ('search_configs', 'invalidsearch_configs'),
        ('search_configs', ''),
        ('search_configs', None),
    ])
    def test_api_DB_BatchSearchFeatureInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        features = None
        search_configs = None
        intef = ArgusdbApi.DB_BatchSearchFeaturePostApi(ak=ak, features=features, search_configs=search_configs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('search_configs', 'invalidsearch_configs'),
        ('search_configs', ''),
        ('search_configs', None),
    ])
    def test_api_DB_BatchSearchImageInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        images = None
        search_configs = None
        intef = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('bg_request_id', 'invalidbg_request_id'),
        ('bg_request_id', ''),
        ('bg_request_id', None),
    ])
    def test_api_DB_GetBgImageInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        bg_request_id = None
        intef = ArgusdbApi.DB_GetBgImageGetApi(ak=ak, group_id=group_id, bg_request_id=bg_request_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
    ])
    def test_api_DB_DeletePersonInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        person_id = None
        intef = ArgusdbApi.DB_DeletePersonPostApi(ak=ak, group_id=group_id, person_id=person_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
    ])
    def test_api_DB_DeleteStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        intef = ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
    ])
    def test_api_DB_DeleteStreamGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        intef = ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=group_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
    ])
    def test_api_DB_ImageDetectInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        image = None
        intef = ArgusdbApi.DB_ImageDetectPostApi(ak=ak, group_id=group_id, image=image, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
    ])
    def test_api_DB_GetPersonInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        person_id = None
        intef = ArgusdbApi.DB_GetPersonGetApi(ak=ak, group_id=group_id, person_id=person_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('bounding', 'invalidbounding'),
        ('bounding', ''),
        ('bounding', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('override', 'invalidoverride'),
        ('override', ''),
        ('override', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
    ])
    def test_api_DB_CreatePersonInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        bounding = None
        group_id = None
        image = None
        override = None
        person_id = None
        intef = ArgusdbApi.DB_CreatePersonPostApi(ak=ak, bounding=bounding, group_id=group_id, image=image, override=override, person_id=person_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('limit', 'invalidlimit'),
        ('limit', ''),
        ('limit', None),
        ('offset', 'invalidoffset'),
        ('offset', ''),
        ('offset', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_DB_ListPersonInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        limit = None
        offset = None
        reversed = None
        intef = ArgusdbApi.DB_ListPersonGetApi(ak=ak, group_id=group_id, limit=limit, offset=offset, reversed=reversed, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('feature', 'invalidfeature'),
        ('feature', ''),
        ('feature', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('override', 'invalidoverride'),
        ('override', ''),
        ('override', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
    ])
    def test_api_DB_CreatePersonByFeatureInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        feature = None
        group_id = None
        override = None
        person_id = None
        intef = ArgusdbApi.DB_CreatePersonByFeaturePostApi(ak=ak, feature=feature, group_id=group_id, override=override, person_id=person_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('feature', 'invalidfeature'),
        ('feature', ''),
        ('feature', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('threshold', 'invalidthreshold'),
        ('threshold', ''),
        ('threshold', None),
        ('top_k', 'invalidtop_k'),
        ('top_k', ''),
        ('top_k', None),
    ])
    def test_api_DB_SearchFeatureInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        feature = None
        group_id = None
        threshold = None
        top_k = None
        intef = ArgusdbApi.DB_SearchFeaturePostApi(ak=ak, feature=feature, group_id=group_id, threshold=threshold, top_k=top_k, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('bounding', 'invalidbounding'),
        ('bounding', ''),
        ('bounding', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('threshold', 'invalidthreshold'),
        ('threshold', ''),
        ('threshold', None),
        ('top_k', 'invalidtop_k'),
        ('top_k', ''),
        ('top_k', None),
    ])
    def test_api_DB_SearchImageInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        bounding = None
        group_id = None
        image = None
        threshold = None
        top_k = None
        intef = ArgusdbApi.DB_SearchImagePostApi(ak=ak, bounding=bounding, group_id=group_id, image=image, threshold=threshold, top_k=top_k, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('bounding', 'invalidbounding'),
        ('bounding', ''),
        ('bounding', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('threshold', 'invalidthreshold'),
        ('threshold', ''),
        ('threshold', None),
        ('top_k', 'invalidtop_k'),
        ('top_k', ''),
        ('top_k', None),
    ])
    def test_api_DB_SearchImageMultiFaceInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        bounding = None
        group_id = None
        image = None
        threshold = None
        top_k = None
        intef = ArgusdbApi.DB_SearchImageMultiFacePostApi(ak=ak, bounding=bounding, group_id=group_id, image=image, threshold=threshold, top_k=top_k, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
    ])
    def test_api_DB_GetStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        intef = ArgusdbApi.DB_GetStaticGroupGetApi(ak=ak, group_id=group_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('al_cb_url', 'invalidal_cb_url'),
        ('al_cb_url', ''),
        ('al_cb_url', None),
        ('auto', 'invalidauto'),
        ('auto', ''),
        ('auto', None),
        ('bind_groups', 'invalidbind_groups'),
        ('bind_groups', ''),
        ('bind_groups', None),
        ('conf_type', 'invalidconf_type'),
        ('conf_type', ''),
        ('conf_type', None),
        ('event_cb_url', 'invalidevent_cb_url'),
        ('event_cb_url', ''),
        ('event_cb_url', None),
        ('expired_time', 'invalidexpired_time'),
        ('expired_time', ''),
        ('expired_time', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('group_mold', 'invalidgroup_mold'),
        ('group_mold', ''),
        ('group_mold', None),
        ('group_name', 'invalidgroup_name'),
        ('group_name', ''),
        ('group_name', None),
        ('group_size', 'invalidgroup_size'),
        ('group_size', ''),
        ('group_size', None),
        ('group_tag', 'invalidgroup_tag'),
        ('group_tag', ''),
        ('group_tag', None),
        ('ll_cb_url', 'invalidll_cb_url'),
        ('ll_cb_url', ''),
        ('ll_cb_url', None),
        ('merge_cb_url', 'invalidmerge_cb_url'),
        ('merge_cb_url', ''),
        ('merge_cb_url', None),
        ('opq_model', 'invalidopq_model'),
        ('opq_model', ''),
        ('opq_model', None),
        ('pedes_cb_url', 'invalidpedes_cb_url'),
        ('pedes_cb_url', ''),
        ('pedes_cb_url', None),
        ('pedes_tag', 'invalidpedes_tag'),
        ('pedes_tag', ''),
        ('pedes_tag', None),
        ('peer_cb_url', 'invalidpeer_cb_url'),
        ('peer_cb_url', ''),
        ('peer_cb_url', None),
        ('product_line', 'invalidproduct_line'),
        ('product_line', ''),
        ('product_line', None),
        ('sync', 'invalidsync'),
        ('sync', ''),
        ('sync', None),
        ('use_cache', 'invaliduse_cache'),
        ('use_cache', ''),
        ('use_cache', None),
        ('use_logic_layer', 'invaliduse_logic_layer'),
        ('use_logic_layer', ''),
        ('use_logic_layer', None),
        ('use_multi_face', 'invaliduse_multi_face'),
        ('use_multi_face', ''),
        ('use_multi_face', None),
    ])
    def test_api_DB_CreateStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
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
        intef = ArgusdbApi.DB_CreateStaticGroupPostApi(ak=ak, al_cb_url=al_cb_url, auto=auto, bind_groups=bind_groups, conf_type=conf_type, event_cb_url=event_cb_url, expired_time=expired_time, feature_version=feature_version, group_mold=group_mold, group_name=group_name, group_size=group_size, group_tag=group_tag, ll_cb_url=ll_cb_url, merge_cb_url=merge_cb_url, opq_model=opq_model, pedes_cb_url=pedes_cb_url, pedes_tag=pedes_tag, peer_cb_url=peer_cb_url, product_line=product_line, sync=sync, use_cache=use_cache, use_logic_layer=use_logic_layer, use_multi_face=use_multi_face, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_type', 'invalidgroup_type'),
        ('group_type', ''),
        ('group_type', None),
    ])
    def test_api_DB_ListStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_type = None
        intef = ArgusdbApi.DB_ListStaticGroupGetApi(ak=ak, group_type=group_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
    ])
    def test_api_DB_GetStreamGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        intef = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('al_cb_url', 'invalidal_cb_url'),
        ('al_cb_url', ''),
        ('al_cb_url', None),
        ('auto', 'invalidauto'),
        ('auto', ''),
        ('auto', None),
        ('bind_groups', 'invalidbind_groups'),
        ('bind_groups', ''),
        ('bind_groups', None),
        ('conf_type', 'invalidconf_type'),
        ('conf_type', ''),
        ('conf_type', None),
        ('event_cb_url', 'invalidevent_cb_url'),
        ('event_cb_url', ''),
        ('event_cb_url', None),
        ('expired_time', 'invalidexpired_time'),
        ('expired_time', ''),
        ('expired_time', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('group_mold', 'invalidgroup_mold'),
        ('group_mold', ''),
        ('group_mold', None),
        ('group_name', 'invalidgroup_name'),
        ('group_name', ''),
        ('group_name', None),
        ('group_size', 'invalidgroup_size'),
        ('group_size', ''),
        ('group_size', None),
        ('group_tag', 'invalidgroup_tag'),
        ('group_tag', ''),
        ('group_tag', None),
        ('ll_cb_url', 'invalidll_cb_url'),
        ('ll_cb_url', ''),
        ('ll_cb_url', None),
        ('merge_cb_url', 'invalidmerge_cb_url'),
        ('merge_cb_url', ''),
        ('merge_cb_url', None),
        ('opq_model', 'invalidopq_model'),
        ('opq_model', ''),
        ('opq_model', None),
        ('pedes_cb_url', 'invalidpedes_cb_url'),
        ('pedes_cb_url', ''),
        ('pedes_cb_url', None),
        ('pedes_tag', 'invalidpedes_tag'),
        ('pedes_tag', ''),
        ('pedes_tag', None),
        ('peer_cb_url', 'invalidpeer_cb_url'),
        ('peer_cb_url', ''),
        ('peer_cb_url', None),
        ('product_line', 'invalidproduct_line'),
        ('product_line', ''),
        ('product_line', None),
        ('sync', 'invalidsync'),
        ('sync', ''),
        ('sync', None),
        ('use_cache', 'invaliduse_cache'),
        ('use_cache', ''),
        ('use_cache', None),
        ('use_logic_layer', 'invaliduse_logic_layer'),
        ('use_logic_layer', ''),
        ('use_logic_layer', None),
        ('use_multi_face', 'invaliduse_multi_face'),
        ('use_multi_face', ''),
        ('use_multi_face', None),
    ])
    def test_api_DB_CreateStreamGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
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
        intef = ArgusdbApi.DB_CreateStreamGroupPostApi(ak=ak, al_cb_url=al_cb_url, auto=auto, bind_groups=bind_groups, conf_type=conf_type, event_cb_url=event_cb_url, expired_time=expired_time, feature_version=feature_version, group_mold=group_mold, group_name=group_name, group_size=group_size, group_tag=group_tag, ll_cb_url=ll_cb_url, merge_cb_url=merge_cb_url, opq_model=opq_model, pedes_cb_url=pedes_cb_url, pedes_tag=pedes_tag, peer_cb_url=peer_cb_url, product_line=product_line, sync=sync, use_cache=use_cache, use_logic_layer=use_logic_layer, use_multi_face=use_multi_face, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_type', 'invalidgroup_type'),
        ('group_type', ''),
        ('group_type', None),
    ])
    def test_api_DB_ListStreamGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_type = None
        intef = ArgusdbApi.DB_ListStreamGroupGetApi(ak=ak, group_type=group_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
    ])
    def test_api_DB_UpdatePersonInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  DB API """
        ak = None
        group_id = None
        image = None
        person_id = None
        intef = ArgusdbApi.DB_UpdatePersonPostApi(ak=ak, group_id=group_id, image=image, person_id=person_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('bind_groups', 'invalidbind_groups'),
        ('bind_groups', ''),
        ('bind_groups', None),
        ('event_cb_url', 'invalidevent_cb_url'),
        ('event_cb_url', ''),
        ('event_cb_url', None),
        ('expired_time', 'invalidexpired_time'),
        ('expired_time', ''),
        ('expired_time', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('group_mold', 'invalidgroup_mold'),
        ('group_mold', ''),
        ('group_mold', None),
        ('group_name', 'invalidgroup_name'),
        ('group_name', ''),
        ('group_name', None),
        ('merge_cb_url', 'invalidmerge_cb_url'),
        ('merge_cb_url', ''),
        ('merge_cb_url', None),
        ('pedes_cb_url', 'invalidpedes_cb_url'),
        ('pedes_cb_url', ''),
        ('pedes_cb_url', None),
        ('peer_cb_url', 'invalidpeer_cb_url'),
        ('peer_cb_url', ''),
        ('peer_cb_url', None),
    ])
    def test_api_DB_UpdateStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
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
        intef = ArgusdbApi.DB_UpdateStaticGroupPostApi(ak=ak, bind_groups=bind_groups, event_cb_url=event_cb_url, expired_time=expired_time, group_id=group_id, group_mold=group_mold, group_name=group_name, merge_cb_url=merge_cb_url, pedes_cb_url=pedes_cb_url, peer_cb_url=peer_cb_url, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('bind_groups', 'invalidbind_groups'),
        ('bind_groups', ''),
        ('bind_groups', None),
        ('event_cb_url', 'invalidevent_cb_url'),
        ('event_cb_url', ''),
        ('event_cb_url', None),
        ('expired_time', 'invalidexpired_time'),
        ('expired_time', ''),
        ('expired_time', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('group_mold', 'invalidgroup_mold'),
        ('group_mold', ''),
        ('group_mold', None),
        ('group_name', 'invalidgroup_name'),
        ('group_name', ''),
        ('group_name', None),
        ('merge_cb_url', 'invalidmerge_cb_url'),
        ('merge_cb_url', ''),
        ('merge_cb_url', None),
        ('pedes_cb_url', 'invalidpedes_cb_url'),
        ('pedes_cb_url', ''),
        ('pedes_cb_url', None),
        ('peer_cb_url', 'invalidpeer_cb_url'),
        ('peer_cb_url', ''),
        ('peer_cb_url', None),
    ])
    def test_api_DB_UpdateStreamGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
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
        intef = ArgusdbApi.DB_UpdateStreamGroupPostApi(ak=ak, bind_groups=bind_groups, event_cb_url=event_cb_url, expired_time=expired_time, group_id=group_id, group_mold=group_mold, group_name=group_name, merge_cb_url=merge_cb_url, pedes_cb_url=pedes_cb_url, peer_cb_url=peer_cb_url, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
