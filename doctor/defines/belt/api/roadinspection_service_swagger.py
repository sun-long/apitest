#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class RoadinspectionSwaggerApi(BaseApi):
    """ web接口"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        self.host = host
        self.ext_info = ext_info
        self.config_obj = config_obj
        self.token = token
        self.host_map = self.readHostMap(collections.name)
        self.TOKEN_NAME = ""
        self.TOKEN_VALUE = "%s"  # token默认信息
        collections.init(self, conf=config_obj, ext_info=ext_info)

    def genPostMan(self):
        """ 生成postman接口文件"""
        self.ext_info.isRequestOpened = True
        self.genPostManFromSwagger(collections)

    def BotRoadProServer_HealthGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  健康检查. """
        """  path: [get]/health API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "message": "",
                    "time": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_Health")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListAdministrativeLevelGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  道路行政级别 prefix=road-inspection-pro version=v1
Actio... """
        """  path: [get]/v1/dicts/administrative-level API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "items": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListAdministrativeLevel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListCoordinateSystemGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  坐标系列表 prefix=road-inspection-pro version=v1
Action... """
        """  path: [get]/v1/dicts/coordinate-system API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "items": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListCoordinateSystem")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListCountryGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  国家列表 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/dicts/country API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "items": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListCountry")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListFunctionLevelGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  道路功能级别 prefix=road-inspection-pro version=v1 Actio... """
        """  path: [get]/v1/dicts/function-level API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "items": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListFunctionLevel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListLabelTypeGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  道路病害类型 prefix=road-inspection-pro version=v1 Actio... """
        """  path: [get]/v1/dicts/label-type API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "items": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListLabelType")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListPavementLevelGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  路面类型 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/dicts/pavement-level API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "items": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListPavementLevel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListProvinceGetApi(self, country=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  省份列表 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/dicts/province API """
        """  params: 
                参数名称：country　类型：string　描述：国家
        """
        """  resp:
                200(A successful response.):
                {
                    "items": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListProvince")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("country", country)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListRoadTypeGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  道路类型 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/dicts/road-type API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "items": [
                        {
                            "key": "",
                            "value": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListRoadType")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_DeleteEventPostApi(self, aggregation_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除道路事件 prefix=road-inspection-pro version=v1 Actio... """
        """  path: [post]/v1/events/delete API """
        """  body: 
                {
                    "aggregation_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_DeleteEvent")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("aggregation_id", aggregation_id)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListEventHistoryGetApi(self, aggregation_id=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  道路事件历史 prefix=road-inspection-pro version=v1 Actio... """
        """  path: [get]/v1/events/history API """
        """  params: 
                参数名称：aggregation_id　类型：string　描述：聚合ID.
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "events": [
                        {
                            "aggregation": {
                                "aggregation_id": "",
                                "first_capture_time": "",
                                "last_capture_time": ""
                            },
                            "breakage_size": {
                                "size": 0,
                                "type": ""
                            },
                            "capture_time": "",
                            "device": {
                                "capture_source": "",
                                "device_id": "",
                                "device_sn": ""
                            },
                            "direction": {
                                "code": "",
                                "desc": "",
                                "from_to": ""
                            },
                            "id": "",
                            "image": {
                                "rectangle": {
                                    "height": 0,
                                    "left": 0,
                                    "top": 0,
                                    "width": 0
                                },
                                "size": {
                                    "height": 0,
                                    "width": 0
                                },
                                "url": ""
                            },
                            "label": {
                                "desc": "",
                                "name": ""
                            },
                            "location": {
                                "lat": 0,
                                "lon": 0
                            },
                            "quality": 0,
                            "road": {
                                "identifier": "",
                                "name": "",
                                "type_desc": "",
                                "type_name": ""
                            },
                            "section": {
                                "id": 0,
                                "name": ""
                            },
                            "stake": {
                                "identifier": ""
                            }
                        }
                    ],
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListEventHistory")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("aggregation_id", aggregation_id)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListEventsGetApi(self, start_time=None, end_time=None, device_id=None, label=None, section_id=None, aggregation_id=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  道路事件列表 prefix=road-inspection-pro version=v1 Actio... """
        """  path: [get]/v1/events/list API """
        """  params: 
                参数名称：start_time　类型：string　描述：[必填]开始时间 "2006-01-02T15:04:05Z07:00".
                参数名称：end_time　类型：string　描述：[必填]结束时间 "2006-01-02T15:04:05Z07:00".
                参数名称：device_id　类型：string　描述：[可选]设备id.
                参数名称：label　类型：string　描述：病害类型.
                参数名称：section_id　类型：string　描述：路段id.
                参数名称：aggregation_id　类型：string　描述：病害聚合id.
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "events": [
                        {
                            "aggregation": {
                                "aggregation_id": "",
                                "first_capture_time": "",
                                "last_capture_time": ""
                            },
                            "breakage_size": {
                                "size": 0,
                                "type": ""
                            },
                            "capture_time": "",
                            "device": {
                                "capture_source": "",
                                "device_id": "",
                                "device_sn": ""
                            },
                            "direction": {
                                "code": "",
                                "desc": "",
                                "from_to": ""
                            },
                            "id": "",
                            "image": {
                                "rectangle": {
                                    "height": 0,
                                    "left": 0,
                                    "top": 0,
                                    "width": 0
                                },
                                "size": {
                                    "height": 0,
                                    "width": 0
                                },
                                "url": ""
                            },
                            "label": {
                                "desc": "",
                                "name": ""
                            },
                            "location": {
                                "lat": 0,
                                "lon": 0
                            },
                            "quality": 0,
                            "road": {
                                "identifier": "",
                                "name": "",
                                "type_desc": "",
                                "type_name": ""
                            },
                            "section": {
                                "id": 0,
                                "name": ""
                            },
                            "stake": {
                                "identifier": ""
                            }
                        }
                    ],
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListEvents")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("start_time", start_time)
        intef.update_params("end_time", end_time)
        intef.update_params("device_id", device_id)
        intef.update_params("label", label)
        intef.update_params("section_id", section_id)
        intef.update_params("aggregation_id", aggregation_id)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_GetRoadGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询道路 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/road API """
        """  params: 
                参数名称：id　类型：integer　描述：id
        """
        """  resp:
                200(A successful response.):
                {
                    "administrative_level": "",
                    "function_level": "",
                    "id": 0,
                    "identifier": "",
                    "name": "",
                    "pavement_type": "",
                    "road_type": "",
                    "short_name": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_GetRoad")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_CreateRoadPostApi(self, identifier=None, name=None, short_name=None, function_level=None, administrative_level=None, road_type=None, pavement_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建道路 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [post]/v1/road API """
        """  body: 
                {
                    "administrative_level": "",
                    "function_level": "",
                    "identifier": "",
                    "name": "",
                    "pavement_type": "",
                    "road_type": "",
                    "short_name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "id": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_CreateRoad")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("identifier", identifier)
        intef.update_body("name", name)
        intef.update_body("short_name", short_name)
        intef.update_body("function_level", function_level)
        intef.update_body("administrative_level", administrative_level)
        intef.update_body("road_type", road_type)
        intef.update_body("pavement_type", pavement_type)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_DeleteRoadPostApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除道路 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [post]/v1/road/delete API """
        """  body: 
                {
                    "id": 0
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_DeleteRoad")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListRoadGetApi(self, function_level=None, administrative_level=None, road_type=None, pavement_type=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  道路列表 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/road/list API """
        """  params: 
                参数名称：function_level　类型：string　描述：[可选]功能等级.
                参数名称：administrative_level　类型：string　描述：[可选]行政级别.
                参数名称：road_type　类型：string　描述：[可选]道路类型.
                参数名称：pavement_type　类型：string　描述：[可选]路面类型.
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "data": [
                        {
                            "administrative_level": "",
                            "administrative_level_desc": "",
                            "function_level": "",
                            "function_level_desc": "",
                            "id": 0,
                            "identifier": "",
                            "name": "",
                            "pavement_type": "",
                            "pavement_type_desc": "",
                            "road_type": "",
                            "road_type_desc": "",
                            "short_name": ""
                        }
                    ],
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListRoad")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("function_level", function_level)
        intef.update_params("administrative_level", administrative_level)
        intef.update_params("road_type", road_type)
        intef.update_params("pavement_type", pavement_type)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListRoadSelectionItemsGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  道路列表下拉选项,全量不分页,只返回id和 identifier-name
prefix=road-... """
        """  path: [get]/v1/road/selections API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "roads": [
                        {
                            "id": 0,
                            "name": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListRoadSelectionItems")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_UpdateRoadPostApi(self, id=None, identifier=None, name=None, short_name=None, function_level=None, administrative_level=None, road_type=None, pavement_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新道路 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [post]/v1/road/update API """
        """  body: 
                {
                    "administrative_level": "",
                    "function_level": "",
                    "id": 0,
                    "identifier": "",
                    "name": "",
                    "pavement_type": "",
                    "road_type": "",
                    "short_name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_UpdateRoad")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("identifier", identifier)
        intef.update_body("name", name)
        intef.update_body("short_name", short_name)
        intef.update_body("function_level", function_level)
        intef.update_body("administrative_level", administrative_level)
        intef.update_body("road_type", road_type)
        intef.update_body("pavement_type", pavement_type)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_GetSectionGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询路段 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/section API """
        """  params: 
                参数名称：id　类型：integer　描述：id
        """
        """  resp:
                200(A successful response.):
                {
                    "country": "",
                    "id": 0,
                    "name": "",
                    "province": "",
                    "road_id": 0,
                    "road_identifier": "",
                    "road_name": "",
                    "starting_point": "",
                    "terminal_point": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_GetSection")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_CreateSectionPostApi(self, name=None, road_id=None, province=None, country=None, starting_point=None, terminal_point=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建路段 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [post]/v1/section API """
        """  body: 
                {
                    "country": "",
                    "name": "",
                    "province": "",
                    "road_id": 0,
                    "starting_point": "",
                    "terminal_point": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "id": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_CreateSection")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("road_id", road_id)
        intef.update_body("province", province)
        intef.update_body("country", country)
        intef.update_body("starting_point", starting_point)
        intef.update_body("terminal_point", terminal_point)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_DeleteSectionPostApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除路段 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [post]/v1/section/delete API """
        """  body: 
                {
                    "id": 0
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_DeleteSection")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListSectionGetApi(self, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  路段列表 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/section/list API """
        """  params: 
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "data": [
                        {
                            "country": "",
                            "id": 0,
                            "name": "",
                            "province": "",
                            "road_id": 0,
                            "road_identifier": "",
                            "road_name": "",
                            "starting_point": "",
                            "terminal_point": ""
                        }
                    ],
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListSection")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListSectionSelectionGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  路段列表下拉选项,全量不分页,只返回id和name prefix=road-inspection-p... """
        """  path: [get]/v1/section/selections API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "sections": [
                        {
                            "id": 0,
                            "name": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListSectionSelection")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_UpdateSectionPostApi(self, id=None, name=None, road_id=None, province=None, country=None, starting_point=None, terminal_point=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新路段 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [post]/v1/section/update API """
        """  body: 
                {
                    "country": "",
                    "id": 0,
                    "name": "",
                    "province": "",
                    "road_id": 0,
                    "starting_point": "",
                    "terminal_point": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_UpdateSection")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("name", name)
        intef.update_body("road_id", road_id)
        intef.update_body("province", province)
        intef.update_body("country", country)
        intef.update_body("starting_point", starting_point)
        intef.update_body("terminal_point", terminal_point)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_GetStakeGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询路桩 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/stake API """
        """  params: 
                参数名称：id　类型：integer　描述：id
        """
        """  resp:
                200(A successful response.):
                {
                    "coordinate_system": "",
                    "id": 0,
                    "latitude": 0,
                    "longitude": 0,
                    "road_identifier": "",
                    "section_id": 0,
                    "section_name": "",
                    "stake_serial_number": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_GetStake")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_CreateStakePostApi(self, coordinate_system=None, longitude=None, latitude=None, section_id=None, stake_serial_number=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建路桩 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [post]/v1/stake API """
        """  body: 
                {
                    "coordinate_system": "",
                    "latitude": 0,
                    "longitude": 0,
                    "section_id": 0,
                    "stake_serial_number": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "id": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_CreateStake")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("coordinate_system", coordinate_system)
        intef.update_body("longitude", longitude)
        intef.update_body("latitude", latitude)
        intef.update_body("section_id", section_id)
        intef.update_body("stake_serial_number", stake_serial_number)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_DeleteStakePostApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除路桩 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [post]/v1/stake/delete API """
        """  body: 
                {
                    "id": 0
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_DeleteStake")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_ListStakeGetApi(self, section_id=None, stake_serial_number=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  路桩列表 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [get]/v1/stake/list API """
        """  params: 
                参数名称：section_id　类型：integer　描述：路段id.
                参数名称：stake_serial_number　类型：string　描述：路桩编号支持前缀匹配.
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "data": [
                        {
                            "coordinate_system": "",
                            "id": 0,
                            "latitude": 0,
                            "longitude": 0,
                            "road_identifier": "",
                            "section_id": 0,
                            "section_name": "",
                            "stake_serial_number": ""
                        }
                    ],
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_ListStake")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("section_id", section_id)
        intef.update_params("stake_serial_number", stake_serial_number)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def BotRoadProServer_UpdateStakePostApi(self, stake_id=None, longitude=None, latitude=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新路桩 prefix=road-inspection-pro version=v1 Action=... """
        """  path: [post]/v1/stake/update API """
        """  body: 
                {
                    "latitude": 0,
                    "longitude": 0,
                    "stake_id": 0
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("roadInspection", "BotRoadProServer_UpdateStake")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("stake_id", stake_id)
        intef.update_body("longitude", longitude)
        intef.update_body("latitude", latitude)
        return intef.request() if sendRequest else intef

