#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestRoadinspectionApi(object):
    """ roadInspection Api测试"""

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

    def test_api_BotRoadProServer_Health(self, config_obj, RoadinspectionApi):
        """  健康检查. """
        resp = RoadinspectionApi.BotRoadProServer_HealthGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListAdministrativeLevel(self, config_obj, RoadinspectionApi):
        """  道路行政级别 prefix=road-inspection-pro version=v1
Actio... """
        resp = RoadinspectionApi.BotRoadProServer_ListAdministrativeLevelGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListCoordinateSystem(self, config_obj, RoadinspectionApi):
        """  坐标系列表 prefix=road-inspection-pro version=v1
Action... """
        resp = RoadinspectionApi.BotRoadProServer_ListCoordinateSystemGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListCountry(self, config_obj, RoadinspectionApi):
        """  国家列表 prefix=road-inspection-pro version=v1 Action=... """
        resp = RoadinspectionApi.BotRoadProServer_ListCountryGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListFunctionLevel(self, config_obj, RoadinspectionApi):
        """  道路功能级别 prefix=road-inspection-pro version=v1 Actio... """
        resp = RoadinspectionApi.BotRoadProServer_ListFunctionLevelGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListLabelType(self, config_obj, RoadinspectionApi):
        """  道路病害类型 prefix=road-inspection-pro version=v1 Actio... """
        resp = RoadinspectionApi.BotRoadProServer_ListLabelTypeGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListPavementLevel(self, config_obj, RoadinspectionApi):
        """  路面类型 prefix=road-inspection-pro version=v1 Action=... """
        resp = RoadinspectionApi.BotRoadProServer_ListPavementLevelGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListProvince(self, config_obj, RoadinspectionApi):
        """  省份列表 prefix=road-inspection-pro version=v1 Action=... """
        country = None
        resp = RoadinspectionApi.BotRoadProServer_ListProvinceGetApi(country=country)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListRoadType(self, config_obj, RoadinspectionApi):
        """  道路类型 prefix=road-inspection-pro version=v1 Action=... """
        resp = RoadinspectionApi.BotRoadProServer_ListRoadTypeGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_DeleteEvent(self, config_obj, RoadinspectionApi):
        """  删除道路事件 prefix=road-inspection-pro version=v1 Actio... """
        aggregation_id = None
        resp = RoadinspectionApi.BotRoadProServer_DeleteEventPostApi(aggregation_id=aggregation_id)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListEventHistory(self, config_obj, RoadinspectionApi):
        """  道路事件历史 prefix=road-inspection-pro version=v1 Actio... """
        aggregation_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = RoadinspectionApi.BotRoadProServer_ListEventHistoryGetApi(aggregation_id=aggregation_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListEvents(self, config_obj, RoadinspectionApi):
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
        resp = RoadinspectionApi.BotRoadProServer_ListEventsGetApi(start_time=start_time, end_time=end_time, device_id=device_id, label=label, section_id=section_id, aggregation_id=aggregation_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_GetRoad(self, config_obj, RoadinspectionApi):
        """  查询道路 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        resp = RoadinspectionApi.BotRoadProServer_GetRoadGetApi(id=id)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_CreateRoad(self, config_obj, RoadinspectionApi):
        """  创建道路 prefix=road-inspection-pro version=v1 Action=... """
        identifier = None
        name = None
        short_name = None
        function_level = None
        administrative_level = None
        road_type = None
        pavement_type = None
        resp = RoadinspectionApi.BotRoadProServer_CreateRoadPostApi(identifier=identifier, name=name, short_name=short_name, function_level=function_level, administrative_level=administrative_level, road_type=road_type, pavement_type=pavement_type)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_DeleteRoad(self, config_obj, RoadinspectionApi):
        """  删除道路 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        resp = RoadinspectionApi.BotRoadProServer_DeleteRoadPostApi(id=id)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListRoad(self, config_obj, RoadinspectionApi):
        """  道路列表 prefix=road-inspection-pro version=v1 Action=... """
        function_level = None
        administrative_level = None
        road_type = None
        pavement_type = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = RoadinspectionApi.BotRoadProServer_ListRoadGetApi(function_level=function_level, administrative_level=administrative_level, road_type=road_type, pavement_type=pavement_type, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListRoadSelectionItems(self, config_obj, RoadinspectionApi):
        """  道路列表下拉选项,全量不分页,只返回id和 identifier-name
prefix=road-... """
        resp = RoadinspectionApi.BotRoadProServer_ListRoadSelectionItemsGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_UpdateRoad(self, config_obj, RoadinspectionApi):
        """  更新道路 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        identifier = None
        name = None
        short_name = None
        function_level = None
        administrative_level = None
        road_type = None
        pavement_type = None
        resp = RoadinspectionApi.BotRoadProServer_UpdateRoadPostApi(id=id, identifier=identifier, name=name, short_name=short_name, function_level=function_level, administrative_level=administrative_level, road_type=road_type, pavement_type=pavement_type)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_GetSection(self, config_obj, RoadinspectionApi):
        """  查询路段 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        resp = RoadinspectionApi.BotRoadProServer_GetSectionGetApi(id=id)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_CreateSection(self, config_obj, RoadinspectionApi):
        """  创建路段 prefix=road-inspection-pro version=v1 Action=... """
        name = None
        road_id = None
        province = None
        country = None
        starting_point = None
        terminal_point = None
        resp = RoadinspectionApi.BotRoadProServer_CreateSectionPostApi(name=name, road_id=road_id, province=province, country=country, starting_point=starting_point, terminal_point=terminal_point)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_DeleteSection(self, config_obj, RoadinspectionApi):
        """  删除路段 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        resp = RoadinspectionApi.BotRoadProServer_DeleteSectionPostApi(id=id)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListSection(self, config_obj, RoadinspectionApi):
        """  路段列表 prefix=road-inspection-pro version=v1 Action=... """
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = RoadinspectionApi.BotRoadProServer_ListSectionGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListSectionSelection(self, config_obj, RoadinspectionApi):
        """  路段列表下拉选项,全量不分页,只返回id和name prefix=road-inspection-p... """
        resp = RoadinspectionApi.BotRoadProServer_ListSectionSelectionGetApi()
        assert resp.status_code == 200

    def test_api_BotRoadProServer_UpdateSection(self, config_obj, RoadinspectionApi):
        """  更新路段 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        name = None
        road_id = None
        province = None
        country = None
        starting_point = None
        terminal_point = None
        resp = RoadinspectionApi.BotRoadProServer_UpdateSectionPostApi(id=id, name=name, road_id=road_id, province=province, country=country, starting_point=starting_point, terminal_point=terminal_point)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_GetStake(self, config_obj, RoadinspectionApi):
        """  查询路桩 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        resp = RoadinspectionApi.BotRoadProServer_GetStakeGetApi(id=id)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_CreateStake(self, config_obj, RoadinspectionApi):
        """  创建路桩 prefix=road-inspection-pro version=v1 Action=... """
        coordinate_system = None
        longitude = None
        latitude = None
        section_id = None
        stake_serial_number = None
        resp = RoadinspectionApi.BotRoadProServer_CreateStakePostApi(coordinate_system=coordinate_system, longitude=longitude, latitude=latitude, section_id=section_id, stake_serial_number=stake_serial_number)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_DeleteStake(self, config_obj, RoadinspectionApi):
        """  删除路桩 prefix=road-inspection-pro version=v1 Action=... """
        id = None
        resp = RoadinspectionApi.BotRoadProServer_DeleteStakePostApi(id=id)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_ListStake(self, config_obj, RoadinspectionApi):
        """  路桩列表 prefix=road-inspection-pro version=v1 Action=... """
        section_id = None
        stake_serial_number = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = RoadinspectionApi.BotRoadProServer_ListStakeGetApi(section_id=section_id, stake_serial_number=stake_serial_number, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_BotRoadProServer_UpdateStake(self, config_obj, RoadinspectionApi):
        """  更新路桩 prefix=road-inspection-pro version=v1 Action=... """
        stake_id = None
        longitude = None
        latitude = None
        resp = RoadinspectionApi.BotRoadProServer_UpdateStakePostApi(stake_id=stake_id, longitude=longitude, latitude=latitude)
        assert resp.status_code == 200
