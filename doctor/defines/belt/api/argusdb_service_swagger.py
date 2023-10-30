#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class ArgusdbSwaggerApi(BaseApi):
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

    def DB_BatchSearchFeaturePostApi(self, ak=None, features=None, search_configs=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/batch_search/feature API """
        """  body: 
                {
                    "ak": "",
                    "features": [],
                    "search_configs": [
                        {
                            "group_id": "",
                            "threshold": 0,
                            "top_k": 0
                        }
                    ]
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": "",
                    "results": [
                        {
                            "code": 0,
                            "feature_results": [
                                {
                                    "code": 0,
                                    "list": [
                                        {
                                            "feature_id": "",
                                            "person_id": "",
                                            "score": 0
                                        }
                                    ],
                                    "msg": ""
                                }
                            ],
                            "group_id": "",
                            "msg": ""
                        }
                    ]
                }

        """
        intef = collections.interface("argusDb", "DB_BatchSearchFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("features", features)
        intef.update_body("search_configs", search_configs)
        return intef.request() if sendRequest else intef

    def DB_BatchSearchImagePostApi(self, ak=None, images=None, search_configs=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/batch_search/image API """
        """  body: 
                {
                    "ak": "",
                    "images": [
                        {
                            "bounding": {
                                "vertices": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ]
                            },
                            "data": ""
                        }
                    ],
                    "search_configs": [
                        {
                            "group_id": "",
                            "threshold": 0,
                            "top_k": 0
                        }
                    ]
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": "",
                    "results": [
                        {
                            "code": 0,
                            "feature_results": [
                                {
                                    "code": 0,
                                    "list": [
                                        {
                                            "feature_id": "",
                                            "person_id": "",
                                            "score": 0
                                        }
                                    ],
                                    "msg": ""
                                }
                            ],
                            "group_id": "",
                            "msg": ""
                        }
                    ]
                }

        """
        intef = collections.interface("argusDb", "DB_BatchSearchImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("images", images)
        intef.update_body("search_configs", search_configs)
        return intef.request() if sendRequest else intef

    def DB_GetBgImageGetApi(self, ak=None, group_id=None, bg_request_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [get]/argus/v1/db/bg_image API """
        """  params: 
                *参数名称：ak　类型：string　描述：ak
                *参数名称：group_id　类型：string　描述：group_id
                *参数名称：bg_request_id　类型：string　描述：bg_request_i
        """
        """  resp:
                200(OK):
                {
                    "bg_oss_url": "",
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_GetBgImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ak", ak)
        intef.update_params("group_id", group_id)
        intef.update_params("bg_request_id", bg_request_id)
        return intef.request() if sendRequest else intef

    def DB_DeletePersonPostApi(self, ak=None, group_id=None, person_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/delete_person API """
        """  body: 
                {
                    "ak": "",
                    "group_id": "",
                    "person_id": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "ak": "",
                    "group_id": "",
                    "person_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_DeletePerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("group_id", group_id)
        intef.update_body("person_id", person_id)
        return intef.request() if sendRequest else intef

    def DB_DeleteStaticGroupPostApi(self, ak=None, group_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/delete_static_group API """
        """  body: 
                {
                    "ak": "",
                    "group_id": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_DeleteStaticGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("group_id", group_id)
        return intef.request() if sendRequest else intef

    def DB_DeleteStreamGroupPostApi(self, ak=None, group_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/delete_stream_group API """
        """  body: 
                {
                    "ak": "",
                    "group_id": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_DeleteStreamGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("group_id", group_id)
        return intef.request() if sendRequest else intef

    def DB_ImageDetectPostApi(self, ak=None, group_id=None, image=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/image_detect API """
        """  body: 
                {
                    "ak": "",
                    "group_id": "",
                    "image": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "headpose": {
                        "pitch": 0,
                        "roll": 0,
                        "yaw": 0
                    },
                    "quality": 0,
                    "rect": {
                        "bottom": 0,
                        "left": 0,
                        "right": 0,
                        "top": 0
                    },
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_ImageDetect")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("group_id", group_id)
        intef.update_body("image", image)
        return intef.request() if sendRequest else intef

    def DB_GetPersonGetApi(self, ak=None, group_id=None, person_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [get]/argus/v1/db/person API """
        """  params: 
                *参数名称：ak　类型：string　描述：ak
                *参数名称：group_id　类型：string　描述：group_id
                *参数名称：person_id　类型：string　描述：person_i
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "list": [
                        {
                            "image": "",
                            "person_id": ""
                        }
                    ],
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_GetPerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ak", ak)
        intef.update_params("group_id", group_id)
        intef.update_params("person_id", person_id)
        return intef.request() if sendRequest else intef

    def DB_CreatePersonPostApi(self, ak=None, bounding=None, group_id=None, image=None, override=None, person_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/person API """
        """  body: 
                {
                    "ak": "",
                    "bounding": {
                        "vertices": [
                            {
                                "x": 0,
                                "y": 0
                            }
                        ]
                    },
                    "group_id": "",
                    "image": "",
                    "override": "",
                    "person_id": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "person_id": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_CreatePerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        # intef.set_headers("Content-Type", "multipart/form-data")
        intef.update_body("ak", ak)
        intef.update_body("bounding", bounding)
        intef.update_body("group_id", group_id)
        intef.update_body("image", image)
        intef.update_body("override", override)
        intef.update_body("person_id", person_id)
        return intef.request() if sendRequest else intef

    def DB_ListPersonGetApi(self, ak=None, group_id=None, limit=None, offset=None, reversed=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [get]/argus/v1/db/person/list API """
        """  params: 
                *参数名称：ak　类型：string　描述：ak
                *参数名称：group_id　类型：string　描述：group_id
                *参数名称：limit　类型：integer　描述：limit
                *参数名称：offset　类型：integer　描述：offset
                参数名称：reversed　类型：boolean　描述：reverse
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "limit": 0,
                    "list": [
                        {
                            "image": "",
                            "person_id": ""
                        }
                    ],
                    "offset": 0,
                    "request_id": "",
                    "reversed": false,
                    "total": 0
                }

        """
        intef = collections.interface("argusDb", "DB_ListPerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ak", ak)
        intef.update_params("group_id", group_id)
        intef.update_params("limit", limit)
        intef.update_params("offset", offset)
        intef.update_params("reversed", reversed)
        return intef.request() if sendRequest else intef

    def DB_CreatePersonByFeaturePostApi(self, ak=None, feature=None, group_id=None, override=None, person_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/person_by_feature API """
        """  body: 
                {
                    "ak": "",
                    "feature": "",
                    "group_id": "",
                    "override": "",
                    "person_id": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "person_id": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_CreatePersonByFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("feature", feature)
        intef.update_body("group_id", group_id)
        intef.update_body("override", override)
        intef.update_body("person_id", person_id)
        return intef.request() if sendRequest else intef

    def DB_SearchFeaturePostApi(self, ak=None, feature=None, group_id=None, threshold=None, top_k=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/search/feature API """
        """  body: 
                {
                    "ak": "",
                    "feature": "",
                    "group_id": "",
                    "threshold": 0,
                    "top_k": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "list": [
                        {
                            "feature_id": "",
                            "person_id": "",
                            "score": 0
                        }
                    ],
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_SearchFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("feature", feature)
        intef.update_body("group_id", group_id)
        intef.update_body("threshold", threshold)
        intef.update_body("top_k", top_k)
        return intef.request() if sendRequest else intef

    def DB_SearchImagePostApi(self, ak=None, bounding=None, group_id=None, image=None, threshold=None, top_k=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/search/image API """
        """  body: 
                {
                    "ak": "",
                    "bounding": {},
                    "group_id": "",
                    "image": "",
                    "threshold": 0,
                    "top_k": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "list": [
                        {
                            "feature_id": "",
                            "person_id": "",
                            "score": 0
                        }
                    ],
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_SearchImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("bounding", bounding)
        intef.update_body("group_id", group_id)
        intef.update_body("image", image)
        intef.update_body("threshold", threshold)
        intef.update_body("top_k", top_k)
        return intef.request() if sendRequest else intef

    def DB_SearchImageMultiFacePostApi(self, ak=None, bounding=None, group_id=None, image=None, threshold=None, top_k=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/search/image/multi_face API """
        """  body: 
                {
                    "ak": "",
                    "bounding": {},
                    "group_id": "",
                    "image": "",
                    "threshold": 0,
                    "top_k": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": "",
                    "results": [
                        {
                            "code": 0,
                            "list": [
                                {
                                    "feature_id": "",
                                    "person_id": "",
                                    "score": 0
                                }
                            ],
                            "msg": "",
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ]
                            }
                        }
                    ]
                }

        """
        intef = collections.interface("argusDb", "DB_SearchImageMultiFace")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("bounding", bounding)
        intef.update_body("group_id", group_id)
        intef.update_body("image", image)
        intef.update_body("threshold", threshold)
        intef.update_body("top_k", top_k)
        return intef.request() if sendRequest else intef

    def DB_GetStaticGroupGetApi(self, ak=None, group_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [get]/argus/v1/db/static_group API """
        """  params: 
                *参数名称：ak　类型：string　描述：ak
                *参数名称：group_id　类型：string　描述：group_i
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "list": [
                        {
                            "bind_groups": [],
                            "event_cb_url": "",
                            "expired_time": 0,
                            "feature_version": "",
                            "group_id": "",
                            "group_mold": "",
                            "group_name": "",
                            "group_size": 0,
                            "merge_cb_url": "",
                            "pedes_cb_url": "",
                            "peer_cb_url": ""
                        }
                    ],
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_GetStaticGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ak", ak)
        intef.update_params("group_id", group_id)
        return intef.request() if sendRequest else intef

    def DB_CreateStaticGroupPostApi(self, ak=None, al_cb_url=None, auto=None, bind_groups=None, conf_type=None, event_cb_url=None, expired_time=None, feature_version=None, group_mold=None, group_name=None, group_size=None, group_tag=None, ll_cb_url=None, merge_cb_url=None, opq_model=None, pedes_cb_url=None, pedes_tag=None, peer_cb_url=None, product_line=None, sync=None, use_cache=None, use_logic_layer=None, use_multi_face=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None,save_image_option=None):
        """  DB API """
        """  path: [post]/argus/v1/db/static_group API """
        """  body: 
                {
                    "ak": "",
                    "al_cb_url": "",
                    "auto": false,
                    "bind_groups": [],
                    "conf_type": 0,
                    "event_cb_url": "",
                    "expired_time": 0,
                    "feature_version": "",
                    "group_mold": "",
                    "group_name": "",
                    "group_size": 0,
                    "group_tag": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    },
                    "ll_cb_url": "",
                    "merge_cb_url": "",
                    "opq_model": "",
                    "pedes_cb_url": "",
                    "pedes_tag": 0,
                    "peer_cb_url": "",
                    "product_line": 0,
                    "sync": false,
                    "use_cache": false,
                    "use_logic_layer": false,
                    "use_multi_face": false
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "feature_version": "",
                    "group_id": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_CreateStaticGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("al_cb_url", al_cb_url)
        intef.update_body("auto", auto)
        intef.update_body("bind_groups", bind_groups)
        intef.update_body("conf_type", conf_type)
        intef.update_body("event_cb_url", event_cb_url)
        intef.update_body("expired_time", expired_time)
        intef.update_body("feature_version", feature_version)
        intef.update_body("group_mold", group_mold)
        intef.update_body("group_name", group_name)
        intef.update_body("group_size", group_size)
        intef.update_body("group_tag", group_tag)
        intef.update_body("ll_cb_url", ll_cb_url)
        intef.update_body("merge_cb_url", merge_cb_url)
        intef.update_body("opq_model", opq_model)
        intef.update_body("pedes_cb_url", pedes_cb_url)
        intef.update_body("pedes_tag", pedes_tag)
        intef.update_body("peer_cb_url", peer_cb_url)
        intef.update_body("product_line", product_line)
        intef.update_body("sync", sync)
        intef.update_body("use_cache", use_cache)
        intef.update_body("use_logic_layer", use_logic_layer)
        intef.update_body("use_multi_face", use_multi_face)
        intef.update_body("save_image_option", save_image_option)
        return intef.request() if sendRequest else intef

    def DB_ListStaticGroupGetApi(self, ak=None, group_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [get]/argus/v1/db/static_group/list API """
        """  params: 
                *参数名称：ak　类型：string　描述：ak
                *参数名称：group_type　类型：string　描述：group_typ
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "list": [
                        {
                            "bind_groups": [],
                            "event_cb_url": "",
                            "expired_time": 0,
                            "feature_version": "",
                            "group_id": "",
                            "group_mold": "",
                            "group_name": "",
                            "group_size": 0,
                            "merge_cb_url": "",
                            "pedes_cb_url": "",
                            "peer_cb_url": ""
                        }
                    ],
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_ListStaticGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ak", ak)
        intef.update_params("group_type", group_type)
        return intef.request() if sendRequest else intef

    def DB_GetStreamGroupGetApi(self, ak=None, group_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [get]/argus/v1/db/stream_group API """
        """  params: 
                *参数名称：ak　类型：string　描述：ak
                *参数名称：group_id　类型：string　描述：group_i
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "list": [
                        {
                            "bind_groups": [],
                            "event_cb_url": "",
                            "expired_time": 0,
                            "feature_version": "",
                            "group_id": "",
                            "group_mold": "",
                            "group_name": "",
                            "group_size": 0,
                            "merge_cb_url": "",
                            "pedes_cb_url": "",
                            "peer_cb_url": ""
                        }
                    ],
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_GetStreamGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ak", ak)
        intef.update_params("group_id", group_id)
        return intef.request() if sendRequest else intef

    def DB_CreateStreamGroupPostApi(self, ak=None, al_cb_url=None, auto=None, bind_groups=None, conf_type=None, event_cb_url=None, expired_time=None, feature_version=None, group_mold=None, group_name=None, group_size=None, group_tag=None, ll_cb_url=None, merge_cb_url=None, opq_model=None, pedes_cb_url=None, pedes_tag=None, peer_cb_url=None, product_line=None, sync=None, use_cache=None, use_logic_layer=None, use_multi_face=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None, save_image_option=None):
        """  DB API """
        """  path: [post]/argus/v1/db/stream_group API """
        """  body: 
                {
                    "ak": "",
                    "al_cb_url": "",
                    "auto": false,
                    "bind_groups": [],
                    "conf_type": 0,
                    "event_cb_url": "",
                    "expired_time": 0,
                    "feature_version": "",
                    "group_mold": "",
                    "group_name": "",
                    "group_size": 0,
                    "group_tag": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    },
                    "ll_cb_url": "",
                    "merge_cb_url": "",
                    "opq_model": "",
                    "pedes_cb_url": "",
                    "pedes_tag": 0,
                    "peer_cb_url": "",
                    "product_line": 0,
                    "sync": false,
                    "use_cache": false,
                    "use_logic_layer": false,
                    "use_multi_face": false
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "feature_version": "",
                    "group_id": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_CreateStreamGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("al_cb_url", al_cb_url)
        intef.update_body("auto", auto)
        intef.update_body("bind_groups", bind_groups)
        intef.update_body("conf_type", conf_type)
        intef.update_body("event_cb_url", event_cb_url)
        intef.update_body("expired_time", expired_time)
        intef.update_body("feature_version", feature_version)
        intef.update_body("group_mold", group_mold)
        intef.update_body("group_name", group_name)
        intef.update_body("group_size", group_size)
        intef.update_body("group_tag", group_tag)
        intef.update_body("ll_cb_url", ll_cb_url)
        intef.update_body("merge_cb_url", merge_cb_url)
        intef.update_body("opq_model", opq_model)
        intef.update_body("pedes_cb_url", pedes_cb_url)
        intef.update_body("pedes_tag", pedes_tag)
        intef.update_body("peer_cb_url", peer_cb_url)
        intef.update_body("product_line", product_line)
        intef.update_body("sync", sync)
        intef.update_body("use_cache", use_cache)
        intef.update_body("use_logic_layer", use_logic_layer)
        intef.update_body("use_multi_face", use_multi_face)
        intef.update_body("save_image_option", save_image_option)
        return intef.request() if sendRequest else intef

    def DB_ListStreamGroupGetApi(self, ak=None, group_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [get]/argus/v1/db/stream_group/list API """
        """  params: 
                *参数名称：ak　类型：string　描述：ak
                *参数名称：group_type　类型：string　描述：group_typ
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "list": [
                        {
                            "bind_groups": [],
                            "event_cb_url": "",
                            "expired_time": 0,
                            "feature_version": "",
                            "group_id": "",
                            "group_mold": "",
                            "group_name": "",
                            "group_size": 0,
                            "merge_cb_url": "",
                            "pedes_cb_url": "",
                            "peer_cb_url": ""
                        }
                    ],
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_ListStreamGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ak", ak)
        intef.update_params("group_type", group_type)
        return intef.request() if sendRequest else intef

    def DB_UpdatePersonPostApi(self, ak=None, group_id=None, image=None, person_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/update_person API """
        """  body: 
                {
                    "ak": "",
                    "group_id": "",
                    "image": "",
                    "person_id": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_UpdatePerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("group_id", group_id)
        intef.update_body("image", image)
        intef.update_body("person_id", person_id)
        return intef.request() if sendRequest else intef

    def DB_UpdateStaticGroupPostApi(self, ak=None, bind_groups=None, event_cb_url=None, expired_time=None, group_id=None, group_mold=None, group_name=None, merge_cb_url=None, pedes_cb_url=None, peer_cb_url=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/update_static_group API """
        """  body: 
                {
                    "ak": "",
                    "bind_groups": [],
                    "event_cb_url": "",
                    "expired_time": 0,
                    "group_id": "",
                    "group_mold": "",
                    "group_name": "",
                    "merge_cb_url": "",
                    "pedes_cb_url": "",
                    "peer_cb_url": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_UpdateStaticGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("bind_groups", bind_groups)
        intef.update_body("event_cb_url", event_cb_url)
        intef.update_body("expired_time", expired_time)
        intef.update_body("group_id", group_id)
        intef.update_body("group_mold", group_mold)
        intef.update_body("group_name", group_name)
        intef.update_body("merge_cb_url", merge_cb_url)
        intef.update_body("pedes_cb_url", pedes_cb_url)
        intef.update_body("peer_cb_url", peer_cb_url)
        return intef.request() if sendRequest else intef

    def DB_UpdateStreamGroupPostApi(self, ak=None, bind_groups=None, event_cb_url=None, expired_time=None, group_id=None, group_mold=None, group_name=None, merge_cb_url=None, pedes_cb_url=None, peer_cb_url=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DB API """
        """  path: [post]/argus/v1/db/update_stream_group API """
        """  body: 
                {
                    "ak": "",
                    "bind_groups": [],
                    "event_cb_url": "",
                    "expired_time": 0,
                    "group_id": "",
                    "group_mold": "",
                    "group_name": "",
                    "merge_cb_url": "",
                    "pedes_cb_url": "",
                    "peer_cb_url": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusDb", "DB_UpdateStreamGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("bind_groups", bind_groups)
        intef.update_body("event_cb_url", event_cb_url)
        intef.update_body("expired_time", expired_time)
        intef.update_body("group_id", group_id)
        intef.update_body("group_mold", group_mold)
        intef.update_body("group_name", group_name)
        intef.update_body("merge_cb_url", merge_cb_url)
        intef.update_body("pedes_cb_url", pedes_cb_url)
        intef.update_body("peer_cb_url", peer_cb_url)
        return intef.request() if sendRequest else intef

