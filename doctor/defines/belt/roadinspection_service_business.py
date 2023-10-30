#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.roadinspection_service_swagger import RoadinspectionSwaggerApi


"""
使用说明：


"""


class RoadinspectionSwaggerBusiness(RoadinspectionSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(RoadinspectionSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

        # prefix = "%s/road-inspection-pro" % inte_obj.path_prefix
        # inte_obj.set_path_prefix(prefix)
        if inte_obj.path == '/v1/dicts/administrative-level':
            inte_obj.set_headers('X-Belt-Action', 'ListAdministrativeLevel')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/dicts/coordinate-system':
            inte_obj.set_headers('X-Belt-Action', 'ListCoordinateSystem')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/dicts/country':
            inte_obj.set_headers('X-Belt-Action', 'ListCountry')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/dicts/function-level':
            inte_obj.set_headers('X-Belt-Action', 'ListFunctionLevel')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/dicts/label-type':
            inte_obj.set_headers('X-Belt-Action', 'ListLabelType')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/dicts/pavement-level':
            inte_obj.set_headers('X-Belt-Action', 'ListPavementLevel')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/dicts/province':
            inte_obj.set_headers('X-Belt-Action', 'ListProvince')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/dicts/road-type':
            inte_obj.set_headers('X-Belt-Action', 'ListRoadType')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/events/delete':
            inte_obj.set_headers('X-Belt-Action', 'DeleteEvent')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/events/history':
            inte_obj.set_headers('X-Belt-Action', 'ListEventHistory')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/events/list':
            inte_obj.set_headers('X-Belt-Action', 'ListEvent')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/road':
            inte_obj.set_headers('X-Belt-Version', 'v1')
            if inte_obj.method == "get":
                inte_obj.set_headers('X-Belt-Action', 'GetRoad')
            elif inte_obj.method == "post":
                inte_obj.set_headers('X-Belt-Action', 'CreateRoad')
            else:
                raise
        elif inte_obj.path == '/v1/road/delete':
            inte_obj.set_headers('X-Belt-Action', 'DeleteRoad')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/road/list':
            inte_obj.set_headers('X-Belt-Action', 'ListRoad')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/road/selections':
            inte_obj.set_headers('X-Belt-Action', 'ListRoadSelections')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/road/update':
            inte_obj.set_headers('X-Belt-Action', 'UpdateRoad')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/section':
            inte_obj.set_headers('X-Belt-Version', 'v1')
            if inte_obj.method == "get":
                inte_obj.set_headers('X-Belt-Action', 'GetSection')
            elif inte_obj.method == "post":
                inte_obj.set_headers('X-Belt-Action', 'CreateSection')
            else:
                raise
        elif inte_obj.path == '/v1/section/delete':
            inte_obj.set_headers('X-Belt-Action', 'DeleteSection')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/section/list':
            inte_obj.set_headers('X-Belt-Action', 'ListSection')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/section/selections':
            inte_obj.set_headers('X-Belt-Action', 'ListSectionSelection')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/section/update':
            inte_obj.set_headers('X-Belt-Action', 'UpdateSection')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/stake':
            inte_obj.set_headers('X-Belt-Version', 'v1')
            if inte_obj.method == "get":
                inte_obj.set_headers('X-Belt-Action', 'GetStake')
            elif inte_obj.method == "post":
                inte_obj.set_headers('X-Belt-Action', 'CreateStake')
            else:
                raise
        elif inte_obj.path == '/v1/stake/delete':
            inte_obj.set_headers('X-Belt-Action', 'DeleteStake')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/stake/list':
            inte_obj.set_headers('X-Belt-Action', 'ListStake')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/stake/update':
            inte_obj.set_headers('X-Belt-Action', 'UpdateStake')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        else:
            inte_obj.set_headers('X-Belt-Action', inte_obj.path_action)
            inte_obj.set_headers('X-Belt-Version', inte_obj.path_version)