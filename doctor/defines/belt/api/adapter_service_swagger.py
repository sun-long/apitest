#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class AdapterSwaggerApi(BaseApi):
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

    def NewDBPostApi(self, name=None, feature_version=None, description=None, db_size=None, create_bucket=None, type=None, extra_db_type=None, bucket_flattened=None, bucket_encrypt=None, enable_isolated_feature_table=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NewDB """
        """  path: [post]/v1/face/new_db API """
        """  body: 
                {
                    "bucket_encrypt": false,
                    "bucket_flattened": false,
                    "create_bucket": false,
                    "db_size": "",
                    "description": "",
                    "enable_isolated_feature_table": false,
                    "extra_db_type": "",
                    "feature_version": 0,
                    "name": "",
                    "type": {}
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "db_id": ""
                }

        """

        intef = collections.interface("adapter", "NewDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("feature_version", feature_version)
        intef.update_body("description", description)
        intef.update_body("db_size", db_size)
        intef.update_body("create_bucket", create_bucket)
        intef.update_body("type", type)
        intef.update_body("extra_db_type", extra_db_type)
        intef.update_body("bucket_flattened", bucket_flattened)
        intef.update_body("bucket_encrypt", bucket_encrypt)
        intef.update_body("enable_isolated_feature_table", enable_isolated_feature_table)
        return intef.request() if sendRequest else intef

    def DeleteDBPostApi(self, db_id=None, delete_bucket=None, type=None, extra_db_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteDB """
        """  path: [post]/v1/face/delete_db API """
        """  body: 
                {
                    "db_id": "",
                    "delete_bucket": false,
                    "extra_db_type": "",
                    "type": {}
                }
        """
        """  resp:
                200(sucessfull response):
                ""

        """
        intef = collections.interface("adapter", "DeleteDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("delete_bucket", delete_bucket)
        intef.update_body("type", type)
        intef.update_body("extra_db_type", extra_db_type)
        return intef.request() if sendRequest else intef

    def BatchAddImageToDBPostApi(self, db_id=None, images=None, save_images=None, type=None, extra_db_type=None, auto_rotation=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchAddImageToDB """
        """  path: [post]/v1/face/batch_add_image_to_db API """
        """  body: 
                {
                    "auto_rotation": false,
                    "db_id": "",
                    "extra_db_type": "",
                    "images": [
                        {
                            "extra_info": "",
                            "image": {
                                "bounding": {
                                    "vertices": [
                                        {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    ]
                                },
                                "face_selection": "[LargestFace]",
                                "image": {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            },
                            "key": "",
                            "quality_threshold": 0
                        }
                    ],
                    "save_images": false,
                    "type": {}
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "items": [
                        {
                            "face_info": {
                                "algo": {
                                    "app_name": "",
                                    "app_version": 0,
                                    "data": {},
                                    "object_type": "",
                                    "object_version": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    }
                                },
                                "associations": [
                                    {
                                        "associated_object_info": {
                                            "camera_info": {
                                                "camera_id": "",
                                                "device_id": "",
                                                "device_type": "",
                                                "internal_id": {},
                                                "place_code": "",
                                                "place_name": "",
                                                "platform_id": "",
                                                "source_id": "",
                                                "tollgate_id": "",
                                                "tollgate_name": "",
                                                "zone_id": ""
                                            },
                                            "captured_time": "",
                                            "extra_fields": {
                                                "additionalProp1": "",
                                                "additionalProp2": "",
                                                "additionalProp3": ""
                                            },
                                            "extra_info": "",
                                            "feature": {
                                                "blob": "",
                                                "type": "",
                                                "version": 0
                                            },
                                            "ns_id": "",
                                            "object": {},
                                            "object_index_in_frame": 0,
                                            "panoramic_image": {
                                                "cache_url": "",
                                                "data": "",
                                                "format": {},
                                                "image_id": "",
                                                "url": ""
                                            },
                                            "portrait_image": {
                                                "cache_url": "",
                                                "data": "",
                                                "format": {},
                                                "image_id": "",
                                                "url": ""
                                            },
                                            "producer_annotation": {
                                                "algorithm_version": "",
                                                "component": "",
                                                "worker_type": ""
                                            },
                                            "received_time": "",
                                            "relative_time": "",
                                            "track_event": {}
                                        },
                                        "association_type": "",
                                        "object_id": "",
                                        "type": {}
                                    }
                                ],
                                "automobile": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "track_id": 0
                                },
                                "carplate": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        }
                                    },
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    }
                                },
                                "crowd": {},
                                "cyclist": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "track_id": 0
                                },
                                "diagnose_summaries": [
                                    {
                                        "diagnosis_item": {},
                                        "score": 0,
                                        "type_item": {}
                                    }
                                ],
                                "diagnosis": {},
                                "event": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        }
                                    },
                                    "event_id": "",
                                    "event_status": {},
                                    "event_type": "",
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "rule": {
                                        "direction": {
                                            "X": 0,
                                            "Y": 0
                                        },
                                        "duration": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "X": 0,
                                                    "Y": 0
                                                }
                                            ]
                                        },
                                        "rule_id": "",
                                        "type": "EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                    }
                                },
                                "face": {
                                    "angle": {
                                        "pitch": 0,
                                        "roll": 0,
                                        "yaw": 0
                                    },
                                    "attributes": {
                                        "additionalProp1": "",
                                        "additionalProp2": "",
                                        "additionalProp3": ""
                                    },
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        }
                                    },
                                    "ears_landmarks": [
                                        {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    ],
                                    "ears_scores": 0,
                                    "face_score": 0,
                                    "forehead_landmarks": [
                                        {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    ],
                                    "landmarks": {
                                        "X": 0,
                                        "Y": 0
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "track_id": 0
                                },
                                "human_powered_vehicle": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "track_id": 0
                                },
                                "object_id": "",
                                "other": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        }
                                    }
                                },
                                "pedestrian": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        }
                                    },
                                    "pedestrian_score": 0,
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "track_id": 0
                                },
                                "portrait_image_location": {
                                    "panoramic_image_size": {
                                        "height": 0,
                                        "width": 0
                                    },
                                    "portrait_image_in_panoramic": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "portrait_in_panoramic": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    }
                                },
                                "trajectory": {
                                    "points": [
                                        {
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "timestamp": ""
                                        }
                                    ]
                                },
                                "type": "OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER",
                                "watercraft": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "type": {},
                                            "value": 0
                                        }
                                    },
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    }
                                }
                            },
                            "feature_id": "",
                            "image_url": "",
                            "orientation_type": "ClockWiseUnknown/ClockWise0/ClockWise90/ClockWise180/ClockWise270"
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": "OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR"
                        }
                    ]
                }

        """
        intef = collections.interface("adapter", "BatchAddImageToDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("images", images)
        intef.update_body("save_images", save_images)
        intef.update_body("type", type)
        intef.update_body("extra_db_type", extra_db_type)
        intef.update_body("auto_rotation", auto_rotation)
        return intef.request() if sendRequest else intef

    def DeleteImageFromDBPostApi(self, db_id=None, key=None, feature_id=None, delete_image=None, type=None, extra_db_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteImageFromDB """
        """  path: [post]/v1/face/delete_image_from_db API """
        """  body: 
                {
                    "db_id": "",
                    "delete_image": false,
                    "extra_db_type": "",
                    "feature_id": "",
                    "key": "",
                    "type": {}
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "items": [
                        {
                            "feature_id": "",
                            "image_url": ""
                        }
                    ],
                    "key": "",
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": "OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR"
                        }
                    ]
                }

        """
        intef = collections.interface("adapter", "DeleteImageFromDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("key", key)
        intef.update_body("feature_id", feature_id)
        intef.update_body("delete_image", delete_image)
        intef.update_body("type", type)
        intef.update_body("extra_db_type", extra_db_type)
        return intef.request() if sendRequest else intef

    def FeatureBatchAddPostApi(self, col_id=None, items=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):

        """  FeatureBatchAdd """
        """  path: [post]/v1/databases/{col_id}/batch_add API """
        """  body: 
                {
                    "col_id": "",
                    "items": [
                        {
                            "extra_info": "",
                            "feature": {
                                "blob": "",
                                "type": "",
                                "version": 0
                            },
                            "id": "",
                            "image_id": "",
                            "key": "",
                            "meta_data": "",
                            "seq_id": ""
                        }
                    ]
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "ids": [],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": "OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR"
                        }
                    ]
                }

        """
        i = 1
        intef = collections.interface("adapter", "FeatureBatchAdd")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        #intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("items", items)
        return intef.request() if sendRequest else intef

    def DetectAndExtractPostApi(self, image=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DetectAndExtract """
        """  path: [post]/v1/face/detect_and_extract API """
        """  body: 
                {
                    "feature_version": 0,
                    "image": {
                        "auto_rotation_thresh": 0,
                        "face_selection": "[LargestFace]",
                        "image": {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    }
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "annotation": {
                        "algo": {
                            "app_name": "",
                            "app_version": 0,
                            "data": {},
                            "object_type": "",
                            "object_version": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "associations": [
                            {
                                "associated_object_info": {
                                    "camera_info": {
                                        "camera_id": "",
                                        "device_id": "",
                                        "device_type": "",
                                        "internal_id": {},
                                        "place_code": "",
                                        "place_name": "",
                                        "platform_id": "",
                                        "source_id": "",
                                        "tollgate_id": "",
                                        "tollgate_name": "",
                                        "zone_id": ""
                                    },
                                    "captured_time": "",
                                    "extra_fields": {
                                        "additionalProp1": "",
                                        "additionalProp2": "",
                                        "additionalProp3": ""
                                    },
                                    "extra_info": "",
                                    "feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "ns_id": "",
                                    "object": {},
                                    "object_index_in_frame": 0,
                                    "panoramic_image": {
                                        "cache_url": "",
                                        "data": "",
                                        "format": {},
                                        "image_id": "",
                                        "url": ""
                                    },
                                    "portrait_image": {
                                        "cache_url": "",
                                        "data": "",
                                        "format": {},
                                        "image_id": "",
                                        "url": ""
                                    },
                                    "producer_annotation": {
                                        "algorithm_version": "",
                                        "component": "",
                                        "worker_type": ""
                                    },
                                    "received_time": "",
                                    "relative_time": "",
                                    "track_event": {}
                                },
                                "association_type": "",
                                "object_id": "",
                                "type": {}
                            }
                        ],
                        "automobile": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "carplate": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "crowd": {},
                        "cyclist": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "diagnose_summaries": [
                            {
                                "diagnosis_item": {},
                                "score": 0,
                                "type_item": {}
                            }
                        ],
                        "diagnosis": {},
                        "event": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "event_id": "",
                            "event_status": {},
                            "event_type": "",
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "rule": {
                                "direction": {
                                    "X": 0,
                                    "Y": 0
                                },
                                "duration": "",
                                "roi": {
                                    "vertices": [
                                        {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    ]
                                },
                                "rule_id": "",
                                "type": "EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                            }
                        },
                        "face": {
                            "angle": {
                                "pitch": 0,
                                "roll": 0,
                                "yaw": 0
                            },
                            "attributes": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "ears_landmarks": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ],
                            "ears_scores": 0,
                            "face_score": 0,
                            "forehead_landmarks": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ],
                            "landmarks": {
                                "X": 0,
                                "Y": 0
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "human_powered_vehicle": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "object_id": "",
                        "other": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            }
                        },
                        "pedestrian": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "pedestrian_score": 0,
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "portrait_image_location": {
                            "panoramic_image_size": {
                                "height": 0,
                                "width": 0
                            },
                            "portrait_image_in_panoramic": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "portrait_in_panoramic": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "trajectory": {
                            "points": [
                                {
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "timestamp": ""
                                }
                            ]
                        },
                        "type": "OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER",
                        "watercraft": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        }
                    },
                    "feature": {
                        "blob": "",
                        "type": "",
                        "version": 0
                    }
                }

        """
        intef = collections.interface("adapter", "DetectAndExtract")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def CompareOneToOnePostApi(self, one=None, other=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CompareOneToOne """
        """  path: [post]/v1/face/compare_one_to_one API """
        """  body: 
                {
                    "feature_version": 0,
                    "one": {
                        "bounding": {
                            "vertices": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ]
                        },
                        "face_selection": "[LargestFace]",
                        "image": {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    },
                    "other": {
                        "bounding": {
                            "vertices": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ]
                        },
                        "face_selection": "[LargestFace]",
                        "image": {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    }
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "one": {
                        "algo": {
                            "app_name": "",
                            "app_version": 0,
                            "data": {},
                            "object_type": "",
                            "object_version": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "associations": [
                            {
                                "associated_object_info": {
                                    "camera_info": {
                                        "camera_id": "",
                                        "device_id": "",
                                        "device_type": "",
                                        "internal_id": {},
                                        "place_code": "",
                                        "place_name": "",
                                        "platform_id": "",
                                        "source_id": "",
                                        "tollgate_id": "",
                                        "tollgate_name": "",
                                        "zone_id": ""
                                    },
                                    "captured_time": "",
                                    "extra_fields": {
                                        "additionalProp1": "",
                                        "additionalProp2": "",
                                        "additionalProp3": ""
                                    },
                                    "extra_info": "",
                                    "feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "ns_id": "",
                                    "object": {},
                                    "object_index_in_frame": 0,
                                    "panoramic_image": {
                                        "cache_url": "",
                                        "data": "",
                                        "format": {},
                                        "image_id": "",
                                        "url": ""
                                    },
                                    "portrait_image": {
                                        "cache_url": "",
                                        "data": "",
                                        "format": {},
                                        "image_id": "",
                                        "url": ""
                                    },
                                    "producer_annotation": {
                                        "algorithm_version": "",
                                        "component": "",
                                        "worker_type": ""
                                    },
                                    "received_time": "",
                                    "relative_time": "",
                                    "track_event": {}
                                },
                                "association_type": "",
                                "object_id": "",
                                "type": {}
                            }
                        ],
                        "automobile": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "carplate": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "crowd": {},
                        "cyclist": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "diagnose_summaries": [
                            {
                                "diagnosis_item": {},
                                "score": 0,
                                "type_item": {}
                            }
                        ],
                        "diagnosis": {},
                        "event": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "event_id": "",
                            "event_status": {},
                            "event_type": "",
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "rule": {
                                "direction": {
                                    "X": 0,
                                    "Y": 0
                                },
                                "duration": "",
                                "roi": {
                                    "vertices": [
                                        {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    ]
                                },
                                "rule_id": "",
                                "type": "EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                            }
                        },
                        "face": {
                            "angle": {
                                "pitch": 0,
                                "roll": 0,
                                "yaw": 0
                            },
                            "attributes": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "ears_landmarks": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ],
                            "ears_scores": 0,
                            "face_score": 0,
                            "forehead_landmarks": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ],
                            "landmarks": {
                                "X": 0,
                                "Y": 0
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "human_powered_vehicle": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "object_id": "",
                        "other": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            }
                        },
                        "pedestrian": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "pedestrian_score": 0,
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "portrait_image_location": {
                            "panoramic_image_size": {
                                "height": 0,
                                "width": 0
                            },
                            "portrait_image_in_panoramic": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "portrait_in_panoramic": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "trajectory": {
                            "points": [
                                {
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "timestamp": ""
                                }
                            ]
                        },
                        "type": "OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER",
                        "watercraft": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        }
                    },
                    "other": {
                        "algo": {
                            "app_name": "",
                            "app_version": 0,
                            "data": {},
                            "object_type": "",
                            "object_version": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "associations": [
                            {
                                "associated_object_info": {
                                    "camera_info": {
                                        "camera_id": "",
                                        "device_id": "",
                                        "device_type": "",
                                        "internal_id": {},
                                        "place_code": "",
                                        "place_name": "",
                                        "platform_id": "",
                                        "source_id": "",
                                        "tollgate_id": "",
                                        "tollgate_name": "",
                                        "zone_id": ""
                                    },
                                    "captured_time": "",
                                    "extra_fields": {
                                        "additionalProp1": "",
                                        "additionalProp2": "",
                                        "additionalProp3": ""
                                    },
                                    "extra_info": "",
                                    "feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "ns_id": "",
                                    "object": {},
                                    "object_index_in_frame": 0,
                                    "panoramic_image": {
                                        "cache_url": "",
                                        "data": "",
                                        "format": {},
                                        "image_id": "",
                                        "url": ""
                                    },
                                    "portrait_image": {
                                        "cache_url": "",
                                        "data": "",
                                        "format": {},
                                        "image_id": "",
                                        "url": ""
                                    },
                                    "producer_annotation": {
                                        "algorithm_version": "",
                                        "component": "",
                                        "worker_type": ""
                                    },
                                    "received_time": "",
                                    "relative_time": "",
                                    "track_event": {}
                                },
                                "association_type": "",
                                "object_id": "",
                                "type": {}
                            }
                        ],
                        "automobile": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "carplate": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "crowd": {},
                        "cyclist": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "diagnose_summaries": [
                            {
                                "diagnosis_item": {},
                                "score": 0,
                                "type_item": {}
                            }
                        ],
                        "diagnosis": {},
                        "event": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "event_id": "",
                            "event_status": {},
                            "event_type": "",
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "rule": {
                                "direction": {
                                    "X": 0,
                                    "Y": 0
                                },
                                "duration": "",
                                "roi": {
                                    "vertices": [
                                        {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    ]
                                },
                                "rule_id": "",
                                "type": "EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                            }
                        },
                        "face": {
                            "angle": {
                                "pitch": 0,
                                "roll": 0,
                                "yaw": 0
                            },
                            "attributes": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "ears_landmarks": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ],
                            "ears_scores": 0,
                            "face_score": 0,
                            "forehead_landmarks": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ],
                            "landmarks": {
                                "X": 0,
                                "Y": 0
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "human_powered_vehicle": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "object_id": "",
                        "other": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            }
                        },
                        "pedestrian": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "pedestrian_score": 0,
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "portrait_image_location": {
                            "panoramic_image_size": {
                                "height": 0,
                                "width": 0
                            },
                            "portrait_image_in_panoramic": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "portrait_in_panoramic": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "trajectory": {
                            "points": [
                                {
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "timestamp": ""
                                }
                            ]
                        },
                        "type": "OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER",
                        "watercraft": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        }
                    },
                    "score": 0
                }

        """
        intef = collections.interface("adapter", "CompareOneToOne")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("one", one)
        intef.update_body("other", other)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def SearchImageInDBsPostApi(self, image=None, dbs=None, type=None, dropped_fields=None, extra_db_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  SearchImageInDBs """
        """  path: [post]/v1/face/search_image_in_dbs API """
        """  body: 
                {
                    "dbs": [
                        {
                            "db_id": "",
                            "min_score": 0,
                            "top_k": 0
                        }
                    ],
                    "dropped_fields": [
                        "ITEM_EXTRA_INFO/ITEM_META_DATA"
                    ],
                    "extra_db_type": "",
                    "image": {
                        "bounding": {
                            "vertices": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ]
                        },
                        "face_selection": "[LargestFace]",
                        "image": {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    },
                    "type": ""
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "query_face_info": {
                        "algo": {
                            "app_name": "",
                            "app_version": 0,
                            "data": {},
                            "object_type": "",
                            "object_version": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "associations": [
                            {
                                "associated_object_info": {
                                    "camera_info": {
                                        "camera_id": "",
                                        "device_id": "",
                                        "device_type": "",
                                        "internal_id": {},
                                        "place_code": "",
                                        "place_name": "",
                                        "platform_id": "",
                                        "source_id": "",
                                        "tollgate_id": "",
                                        "tollgate_name": "",
                                        "zone_id": ""
                                    },
                                    "captured_time": "",
                                    "extra_fields": {
                                        "additionalProp1": "",
                                        "additionalProp2": "",
                                        "additionalProp3": ""
                                    },
                                    "extra_info": "",
                                    "feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "ns_id": "",
                                    "object": {},
                                    "object_index_in_frame": 0,
                                    "panoramic_image": {
                                        "cache_url": "",
                                        "data": "",
                                        "format": {},
                                        "image_id": "",
                                        "url": ""
                                    },
                                    "portrait_image": {
                                        "cache_url": "",
                                        "data": "",
                                        "format": {},
                                        "image_id": "",
                                        "url": ""
                                    },
                                    "producer_annotation": {
                                        "algorithm_version": "",
                                        "component": "",
                                        "worker_type": ""
                                    },
                                    "received_time": "",
                                    "relative_time": "",
                                    "track_event": {}
                                },
                                "association_type": "",
                                "object_id": "",
                                "type": {}
                            }
                        ],
                        "automobile": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "carplate": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "crowd": {},
                        "cyclist": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "diagnose_summaries": [
                            {
                                "diagnosis_item": {},
                                "score": 0,
                                "type_item": {}
                            }
                        ],
                        "diagnosis": {},
                        "event": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "event_id": "",
                            "event_status": {},
                            "event_type": "",
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "rule": {
                                "direction": {
                                    "X": 0,
                                    "Y": 0
                                },
                                "duration": "",
                                "roi": {
                                    "vertices": [
                                        {
                                            "X": 0,
                                            "Y": 0
                                        }
                                    ]
                                },
                                "rule_id": "",
                                "type": "EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                            }
                        },
                        "face": {
                            "angle": {
                                "pitch": 0,
                                "roll": 0,
                                "yaw": 0
                            },
                            "attributes": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "ears_landmarks": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ],
                            "ears_scores": 0,
                            "face_score": 0,
                            "forehead_landmarks": [
                                {
                                    "X": 0,
                                    "Y": 0
                                }
                            ],
                            "landmarks": {
                                "X": 0,
                                "Y": 0
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "human_powered_vehicle": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "object_id": "",
                        "other": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            }
                        },
                        "pedestrian": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "pedestrian_score": 0,
                            "quality": 0,
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "track_id": 0
                        },
                        "portrait_image_location": {
                            "panoramic_image_size": {
                                "height": 0,
                                "width": 0
                            },
                            "portrait_image_in_panoramic": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            },
                            "portrait_in_panoramic": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        },
                        "trajectory": {
                            "points": [
                                {
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "timestamp": ""
                                }
                            ]
                        },
                        "type": "OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER",
                        "watercraft": {
                            "attributes_with_score": {
                                "additionalProp1": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp2": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                },
                                "additionalProp3": {
                                    "category": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "type": {},
                                    "value": 0
                                }
                            },
                            "rectangle": {
                                "vertices": [
                                    {
                                        "X": 0,
                                        "Y": 0
                                    }
                                ]
                            }
                        }
                    },
                    "results": {
                        "code": 0,
                        "error": "",
                        "status": "OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR"
                    },
                    "search_results": [
                        {
                            "db_id": "",
                            "similat_results": [
                                {
                                    "item": {
                                        "extra_info": "",
                                        "feature": {
                                            "blob": "",
                                            "type": "",
                                            "version": 0
                                        },
                                        "id": "",
                                        "image_id": "",
                                        "key": "",
                                        "meta_data": "",
                                        "seq_id": ""
                                    },
                                    "score": 0
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("adapter", "SearchImageInDBs")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("dbs", dbs)
        intef.update_body("type", type)
        intef.update_body("dropped_fields", dropped_fields)
        intef.update_body("extra_db_type", extra_db_type)
        return intef.request() if sendRequest else intef

    def FeatureBatchSearchPostApi(self, db_type, col_id, features=None, consistency=None, top_k=None, min_score=None, return_raw_feature=None, dropped_fields=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchSearch """
        """  path: [post]v1/databases/{col_id}/batch_search API """
        """  body: 
                {
                    "col_id": "",
                    "consistency": {},
                    "dropped_fields": [],
                    "feature": [
                        {
                            "blob": "",
                            "type": "",
                            "version": 0
                        }
                    ],
                    "min_score": 0,
                    "return_raw_feature": false,
                    "top_k": 0
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "col_id": "",
                    "feature_results": [
                        {
                            "results": []
                        }
                    ],
                    "is_refined": false,
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": "OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR"
                        }
                    ]
                }

        """
        intef = collections.interface("adapter", "FeatureBatchSearch")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("features", features)
        intef.update_body("consistency", consistency)
        intef.update_body("top_k", top_k)
        intef.update_body("min_score", min_score)
        intef.update_body("return_raw_feature", return_raw_feature)
        intef.update_body("dropped_fields", dropped_fields)
        return intef.request() if sendRequest else intef

    def FeatureBatchGetByKeyPostApi(self, db_type, col_id, consistency=None, ignore_details=None, keys=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchGetByKey """
        """  path: [post]/v1/databases/{col_id}/batch_get_by_key API """
        """  body: 
                {
                    "col_id": "",
                    "consistency": {},
                    "ignore_details": false,
                    "keys": []
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "items": [
                        {
                            "items": [
                                {
                                    "extra_info": "",
                                    "feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "id": "",
                                    "image_id": "",
                                    "key": "",
                                    "meta_data": "",
                                    "seq_id": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": "OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR"
                        }
                    ]
                }

        """
        intef = collections.interface("adapter", "FeatureBatchGetByKey")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("consistency", consistency)
        intef.update_body("ignore_details", ignore_details)
        intef.update_body("keys", keys)
        return intef.request() if sendRequest else intef

    def TaskNewPostApi(self, task=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskNew """
        """  path: [post]/v1/tasks API """
        """  body: 
                {
                    "task": {
                        "camera_info": {
                            "camera_id": "",
                            "device_id": "",
                            "device_type": "",
                            "internal_id": {},
                            "place_code": "",
                            "place_name": "",
                            "platform_id": "",
                            "source_id": "",
                            "tollgate_id": "",
                            "tollgate_name": "",
                            "zone_id": ""
                        },
                        "config_udpate_time": "",
                        "creation_time": "",
                        "feature_version": 0,
                        "ns_id": "",
                        "object_type": {},
                        "schedule_config": {},
                        "source_address": "",
                        "storage_policy": {
                            "binary_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {},
                                "osg": {}
                            },
                            "panoramic_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {},
                                "osg": {}
                            },
                            "portrait_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {},
                                "osg": {}
                            }
                        },
                        "task_id": "",
                        "task_object_config": {
                            "algo_config": {
                                "app_name": "",
                                "app_version": 0,
                                "data": {}
                            },
                            "crowd_config": {},
                            "crowd_config_v2": {},
                            "decoder_config": {},
                            "face_config": {},
                            "faceped_config": {},
                            "path_config": {},
                            "rules": [
                                {
                                    "deriction": {
                                        "X": 0,
                                        "Y": 0
                                    },
                                    "duration": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "rule_id": "",
                                    "type": {}
                                }
                            ],
                            "snapshot_config": {}
                        },
                        "task_user_data": "",
                        "video_parameter": {
                            "bit_rate": 0,
                            "bit_rate_type": {},
                            "frame_rate": 0,
                            "height": 0,
                            "i_frame_interval": 0,
                            "stream_type": {},
                            "video_format": {},
                            "width": 0
                        }
                    }
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "task": {
                        "camera_info": {
                            "camera_id": "",
                            "device_id": "",
                            "device_type": "",
                            "internal_id": {},
                            "place_code": "",
                            "place_name": "",
                            "platform_id": "",
                            "source_id": "",
                            "tollgate_id": "",
                            "tollgate_name": "",
                            "zone_id": ""
                        },
                        "config_udpate_time": "",
                        "creation_time": "",
                        "feature_version": 0,
                        "ns_id": "",
                        "object_type": {},
                        "schedule_config": {},
                        "source_address": "",
                        "storage_policy": {
                            "binary_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {},
                                "osg": {}
                            },
                            "panoramic_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {},
                                "osg": {}
                            },
                            "portrait_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {},
                                "osg": {}
                            }
                        },
                        "task_id": "",
                        "task_object_config": {
                            "algo_config": {
                                "app_name": "",
                                "app_version": 0,
                                "data": {}
                            },
                            "crowd_config": {},
                            "crowd_config_v2": {},
                            "decoder_config": {},
                            "face_config": {},
                            "faceped_config": {},
                            "path_config": {},
                            "rules": [
                                {
                                    "deriction": {
                                        "X": 0,
                                        "Y": 0
                                    },
                                    "duration": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "X": 0,
                                                "Y": 0
                                            }
                                        ]
                                    },
                                    "rule_id": "",
                                    "type": {}
                                }
                            ],
                            "snapshot_config": {}
                        },
                        "task_user_data": "",
                        "video_parameter": {
                            "bit_rate": 0,
                            "bit_rate_type": {},
                            "frame_rate": 0,
                            "height": 0,
                            "i_frame_interval": 0,
                            "stream_type": {},
                            "video_format": {},
                            "width": 0
                        }
                    }
                }

        """
        intef = collections.interface("adapter", "TaskNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task", task)
        return intef.request() if sendRequest else intef

    def TaskListGetApi(self, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskList """
        """  path: [get]/v1/tasks API """
        """  params: 
                参数名称：page_request.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条; 默认值为0. 返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page_request.limit　类型：integer　描述：长度, 取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page_request.total　类型：integer　描述：可选, 总任务数, 请求无须填此参数, 响应时填写
        """
        """  resp:
                200(sucessfull response):
                {
                    "page_response": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "tasks": [
                        {
                            "info": {
                                "camera_info": {
                                    "camera_id": "",
                                    "device_id": "",
                                    "device_type": "",
                                    "internal_id": {},
                                    "place_code": "",
                                    "place_name": "",
                                    "platform_id": "",
                                    "source_id": "",
                                    "tollgate_id": "",
                                    "tollgate_name": "",
                                    "zone_id": ""
                                },
                                "config_udpate_time": "",
                                "creation_time": "",
                                "feature_version": 0,
                                "ns_id": "",
                                "object_type": {},
                                "schedule_config": {},
                                "source_address": "",
                                "storage_policy": {
                                    "binary_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {},
                                        "osg": {}
                                    },
                                    "panoramic_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {},
                                        "osg": {}
                                    },
                                    "portrait_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {},
                                        "osg": {}
                                    }
                                },
                                "task_id": "",
                                "task_object_config": {
                                    "algo_config": {
                                        "app_name": "",
                                        "app_version": 0,
                                        "data": {}
                                    },
                                    "crowd_config": {},
                                    "crowd_config_v2": {},
                                    "decoder_config": {},
                                    "face_config": {},
                                    "faceped_config": {},
                                    "path_config": {},
                                    "rules": [
                                        {
                                            "deriction": {
                                                "X": 0,
                                                "Y": 0
                                            },
                                            "duration": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "X": 0,
                                                        "Y": 0
                                                    }
                                                ]
                                            },
                                            "rule_id": "",
                                            "type": {}
                                        }
                                    ],
                                    "snapshot_config": {}
                                },
                                "task_user_data": "",
                                "video_parameter": {
                                    "bit_rate": 0,
                                    "bit_rate_type": {},
                                    "frame_rate": 0,
                                    "height": 0,
                                    "i_frame_interval": 0,
                                    "stream_type": {},
                                    "video_format": {},
                                    "width": 0
                                }
                            },
                            "rtsp_preview_address": "",
                            "status": {
                                "error_message": "",
                                "last_received_time": "",
                                "status": {}
                            }
                        }
                    ]
                }

        """
        intef = collections.interface("adapter", "TaskList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def TaskDeleteDeleteApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskDelete """
        """  path: [delete]/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200(sucessfull response):
                ""

        """
        intef = collections.interface("adapter", "TaskDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def CompareFeaturePostApi(self, one=None, other=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CompareFeature """
        """  path: [post]/v1/compare_feature API """
        """  body: 
                {
                    "one": {
                        "blob": "",
                        "type": "",
                        "version": 0
                    },
                    "other": {
                        "blob": "",
                        "type": "",
                        "version": 0
                    }
                }
        """
        """  resp:
                200(sucessfull response):
                {
                    "score": 0
                }

        """
        intef = collections.interface("adapter", "CompareFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("one", one)
        intef.update_body("other", other)
        return intef.request() if sendRequest else intef

    def DownloadObjectGetApi(self, bucket_name, object_key, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DownloadObject """
        """  path: [get]/_/{bucket_name}/{object_key} API """
        """  params: 

        """
        """  resp:
                200(sucessfull response):
                ""

        """
        intef = collections.interface("adapter", "DownloadObject")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.set_path_param("object_key", object_key)
        return intef.request() if sendRequest else intef

