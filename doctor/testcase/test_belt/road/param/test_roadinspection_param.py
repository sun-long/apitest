#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestRoadinspectionParam(object):
    """ roadInspection Param测试"""

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
    ])
    def test_api_BotRoadProServer_HealthInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  健康检查. """
        intef = RoadinspectionApi.BotRoadProServer_HealthGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BotRoadProServer_ListAdministrativeLevelInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  道路行政级别 prefix=road-inspection-pro version=v1
Actio... """
        intef = RoadinspectionApi.BotRoadProServer_ListAdministrativeLevelGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BotRoadProServer_ListCoordinateSystemInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  坐标系列表 prefix=road-inspection-pro version=v1
Action... """
        intef = RoadinspectionApi.BotRoadProServer_ListCoordinateSystemGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BotRoadProServer_ListCountryInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  国家列表 prefix=road-inspection-pro version=v1 Action=... """
        intef = RoadinspectionApi.BotRoadProServer_ListCountryGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BotRoadProServer_ListFunctionLevelInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  道路功能级别 prefix=road-inspection-pro version=v1 Actio... """
        intef = RoadinspectionApi.BotRoadProServer_ListFunctionLevelGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BotRoadProServer_ListLabelTypeInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  道路病害类型 prefix=road-inspection-pro version=v1 Actio... """
        intef = RoadinspectionApi.BotRoadProServer_ListLabelTypeGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BotRoadProServer_ListPavementLevelInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  路面类型 prefix=road-inspection-pro version=v1 Action=... """
        intef = RoadinspectionApi.BotRoadProServer_ListPavementLevelGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('country', 'invalidcountry'),
        ('country', ''),
        ('country', None),
    ])
    def test_api_BotRoadProServer_ListProvinceInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  省份列表 prefix=road-inspection-pro version=v1 Action=... """
        country = None
        intef = RoadinspectionApi.BotRoadProServer_ListProvinceGetApi(country=country, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BotRoadProServer_ListRoadTypeInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  道路类型 prefix=road-inspection-pro version=v1 Action=... """
        intef = RoadinspectionApi.BotRoadProServer_ListRoadTypeGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('aggregation_id', 'invalidaggregation_id'),
        ('aggregation_id', ''),
        ('aggregation_id', None),
    ])
    def test_api_BotRoadProServer_DeleteEventInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  删除道路事件 prefix=road-inspection-pro version=v1 Actio... """
        aggregation_id = None
        intef = RoadinspectionApi.BotRoadProServer_DeleteEventPostApi(aggregation_id=aggregation_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('aggregation_id', 'invalidaggregation_id'),
        ('aggregation_id', ''),
        ('aggregation_id', None),
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
    ])
    def test_api_BotRoadProServer_ListEventHistoryInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  道路事件历史 prefix=road-inspection-pro version=v1 Actio... """
        aggregation_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = RoadinspectionApi.BotRoadProServer_ListEventHistoryGetApi(aggregation_id=aggregation_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('start_time', 'invalidstart_time'),
        ('start_time', ''),
        ('start_time', None),
        ('end_time', 'invalidend_time'),
        ('end_time', ''),
        ('end_time', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('label', 'invalidlabel'),
        ('label', ''),
        ('label', None),
        ('section_id', 'invalidsection_id'),
        ('section_id', ''),
        ('section_id', None),
        ('aggregation_id', 'invalidaggregation_id'),
        ('aggregation_id', ''),
        ('aggregation_id', None),
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
    ])
    def test_api_BotRoadProServer_ListEventsInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  道路事件列表 prefix=road-inspection-pro version=v1 Actio... """
        start_time = None
        end_time = None
        device_id = None
        label = None
        section_id = None
        aggregation_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = RoadinspectionApi.BotRoadProServer_ListEventsGetApi(start_time=start_time, end_time=end_time, device_id=device_id, label=label, section_id=section_id, aggregation_id=aggregation_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_BotRoadProServer_GetRoadInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  查询道路 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        intef = RoadinspectionApi.BotRoadProServer_GetRoadGetApi(id=id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('identifier', 'invalididentifier'),
        ('identifier', ''),
        ('identifier', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('short_name', 'invalidshort_name'),
        ('short_name', ''),
        ('short_name', None),
        ('function_level', 'invalidfunction_level'),
        ('function_level', ''),
        ('function_level', None),
        ('administrative_level', 'invalidadministrative_level'),
        ('administrative_level', ''),
        ('administrative_level', None),
        ('road_type', 'invalidroad_type'),
        ('road_type', ''),
        ('road_type', None),
        ('pavement_type', 'invalidpavement_type'),
        ('pavement_type', ''),
        ('pavement_type', None),
    ])
    def test_api_BotRoadProServer_CreateRoadInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  创建道路 prefix=road-inspection-pro version=v1 Action=... """
        identifier = None
        name = None
        short_name = None
        function_level = None
        administrative_level = None
        road_type = None
        pavement_type = None
        intef = RoadinspectionApi.BotRoadProServer_CreateRoadPostApi(identifier=identifier, name=name, short_name=short_name, function_level=function_level, administrative_level=administrative_level, road_type=road_type, pavement_type=pavement_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_BotRoadProServer_DeleteRoadInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  删除道路 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        intef = RoadinspectionApi.BotRoadProServer_DeleteRoadPostApi(id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('function_level', 'invalidfunction_level'),
        ('function_level', ''),
        ('function_level', None),
        ('administrative_level', 'invalidadministrative_level'),
        ('administrative_level', ''),
        ('administrative_level', None),
        ('road_type', 'invalidroad_type'),
        ('road_type', ''),
        ('road_type', None),
        ('pavement_type', 'invalidpavement_type'),
        ('pavement_type', ''),
        ('pavement_type', None),
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
    ])
    def test_api_BotRoadProServer_ListRoadInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  道路列表 prefix=road-inspection-pro version=v1 Action=... """
        function_level = None
        administrative_level = None
        road_type = None
        pavement_type = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = RoadinspectionApi.BotRoadProServer_ListRoadGetApi(function_level=function_level, administrative_level=administrative_level, road_type=road_type, pavement_type=pavement_type, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BotRoadProServer_ListRoadSelectionItemsInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  道路列表下拉选项,全量不分页,只返回id和 identifier-name
prefix=road-... """
        intef = RoadinspectionApi.BotRoadProServer_ListRoadSelectionItemsGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
        ('identifier', 'invalididentifier'),
        ('identifier', ''),
        ('identifier', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('short_name', 'invalidshort_name'),
        ('short_name', ''),
        ('short_name', None),
        ('function_level', 'invalidfunction_level'),
        ('function_level', ''),
        ('function_level', None),
        ('administrative_level', 'invalidadministrative_level'),
        ('administrative_level', ''),
        ('administrative_level', None),
        ('road_type', 'invalidroad_type'),
        ('road_type', ''),
        ('road_type', None),
        ('pavement_type', 'invalidpavement_type'),
        ('pavement_type', ''),
        ('pavement_type', None),
    ])
    def test_api_BotRoadProServer_UpdateRoadInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  更新道路 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        identifier = None
        name = None
        short_name = None
        function_level = None
        administrative_level = None
        road_type = None
        pavement_type = None
        intef = RoadinspectionApi.BotRoadProServer_UpdateRoadPostApi(id=id, identifier=identifier, name=name, short_name=short_name, function_level=function_level, administrative_level=administrative_level, road_type=road_type, pavement_type=pavement_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_BotRoadProServer_GetSectionInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  查询路段 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        intef = RoadinspectionApi.BotRoadProServer_GetSectionGetApi(id=id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('road_id', 'invalidroad_id'),
        ('road_id', ''),
        ('road_id', None),
        ('province', 'invalidprovince'),
        ('province', ''),
        ('province', None),
        ('country', 'invalidcountry'),
        ('country', ''),
        ('country', None),
        ('starting_point', 'invalidstarting_point'),
        ('starting_point', ''),
        ('starting_point', None),
        ('terminal_point', 'invalidterminal_point'),
        ('terminal_point', ''),
        ('terminal_point', None),
    ])
    def test_api_BotRoadProServer_CreateSectionInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  创建路段 prefix=road-inspection-pro version=v1 Action=... """
        name = None
        road_id = None
        province = None
        country = None
        starting_point = None
        terminal_point = None
        intef = RoadinspectionApi.BotRoadProServer_CreateSectionPostApi(name=name, road_id=road_id, province=province, country=country, starting_point=starting_point, terminal_point=terminal_point, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_BotRoadProServer_DeleteSectionInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  删除路段 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        intef = RoadinspectionApi.BotRoadProServer_DeleteSectionPostApi(id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
    ])
    def test_api_BotRoadProServer_ListSectionInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  路段列表 prefix=road-inspection-pro version=v1 Action=... """
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = RoadinspectionApi.BotRoadProServer_ListSectionGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BotRoadProServer_ListSectionSelectionInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  路段列表下拉选项,全量不分页,只返回id和name prefix=road-inspection-p... """
        intef = RoadinspectionApi.BotRoadProServer_ListSectionSelectionGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('road_id', 'invalidroad_id'),
        ('road_id', ''),
        ('road_id', None),
        ('province', 'invalidprovince'),
        ('province', ''),
        ('province', None),
        ('country', 'invalidcountry'),
        ('country', ''),
        ('country', None),
        ('starting_point', 'invalidstarting_point'),
        ('starting_point', ''),
        ('starting_point', None),
        ('terminal_point', 'invalidterminal_point'),
        ('terminal_point', ''),
        ('terminal_point', None),
    ])
    def test_api_BotRoadProServer_UpdateSectionInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  更新路段 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        name = None
        road_id = None
        province = None
        country = None
        starting_point = None
        terminal_point = None
        intef = RoadinspectionApi.BotRoadProServer_UpdateSectionPostApi(id=id, name=name, road_id=road_id, province=province, country=country, starting_point=starting_point, terminal_point=terminal_point, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_BotRoadProServer_GetStakeInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  查询路桩 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        intef = RoadinspectionApi.BotRoadProServer_GetStakeGetApi(id=id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('coordinate_system', 'invalidcoordinate_system'),
        ('coordinate_system', ''),
        ('coordinate_system', None),
        ('longitude', 'invalidlongitude'),
        ('longitude', ''),
        ('longitude', None),
        ('latitude', 'invalidlatitude'),
        ('latitude', ''),
        ('latitude', None),
        ('section_id', 'invalidsection_id'),
        ('section_id', ''),
        ('section_id', None),
        ('stake_serial_number', 'invalidstake_serial_number'),
        ('stake_serial_number', ''),
        ('stake_serial_number', None),
    ])
    def test_api_BotRoadProServer_CreateStakeInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  创建路桩 prefix=road-inspection-pro version=v1 Action=... """
        coordinate_system = None
        longitude = None
        latitude = None
        section_id = None
        stake_serial_number = None
        intef = RoadinspectionApi.BotRoadProServer_CreateStakePostApi(coordinate_system=coordinate_system, longitude=longitude, latitude=latitude, section_id=section_id, stake_serial_number=stake_serial_number, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_BotRoadProServer_DeleteStakeInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  删除路桩 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        intef = RoadinspectionApi.BotRoadProServer_DeleteStakePostApi(id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('section_id', 'invalidsection_id'),
        ('section_id', ''),
        ('section_id', None),
        ('stake_serial_number', 'invalidstake_serial_number'),
        ('stake_serial_number', ''),
        ('stake_serial_number', None),
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
    ])
    def test_api_BotRoadProServer_ListStakeInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  路桩列表 prefix=road-inspection-pro version=v1 Action=... """
        section_id = None
        stake_serial_number = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = RoadinspectionApi.BotRoadProServer_ListStakeGetApi(section_id=section_id, stake_serial_number=stake_serial_number, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('stake_id', 'invalidstake_id'),
        ('stake_id', ''),
        ('stake_id', None),
        ('longitude', 'invalidlongitude'),
        ('longitude', ''),
        ('longitude', None),
        ('latitude', 'invalidlatitude'),
        ('latitude', ''),
        ('latitude', None),
    ])
    def test_api_BotRoadProServer_UpdateStakeInvalidParam(self, invalidParam, config_obj, RoadinspectionApi):
        """  更新路桩 prefix=road-inspection-pro version=v1 Action=... """
        stake_id = None
        longitude = None
        latitude = None
        intef = RoadinspectionApi.BotRoadProServer_UpdateStakePostApi(stake_id=stake_id, longitude=longitude, latitude=latitude, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
