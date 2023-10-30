#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class ArgusipsSwaggerApi(BaseApi):
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

    def CompareFeaturePostApi(self, one=None, other=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/compare_feature API """
        """  body: 
                {
                    "feature_version": "",
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
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "score": 0
                }

        """
        intef = collections.interface("argusIps", "CompareFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("one", one)
        intef.update_body("other", other)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def CompareImagePostApi(self, one=None, other=None, detect_mode=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/compare_image API """
        """  body: 
                {
                    "detect_mode": "[Default]Default/Slow",
                    "feature_version": "",
                    "one": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    },
                    "other": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "score": 0
                }

        """
        intef = collections.interface("argusIps", "CompareImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("one", one)
        intef.update_body("other", other)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def FaceDetectPostApi(self, image=None, detect_mode=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/face_detect API """
        """  body: 
                {
                    "detect_mode": "[Default]Default/Slow",
                    "feature_version": "",
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "response": {
                        "face_info": [
                            {
                                "associations": [
                                    {
                                        "object_id": "",
                                        "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                                    }
                                ],
                                "automobile": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "crowd": {
                                    "density_map": "",
                                    "density_size": {
                                        "height": 0,
                                        "width": 0
                                    },
                                    "incident": [
                                        {
                                            "id": "",
                                            "start_time": "",
                                            "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                            "stop_time": "",
                                            "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                            "update_time": ""
                                        }
                                    ],
                                    "quantity": "",
                                    "strand_map": {
                                        "data": "",
                                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                        "url": ""
                                    }
                                },
                                "cyclist": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "event": {
                                    "event_id": "",
                                    "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rule": {
                                        "direction": {
                                            "x": 0,
                                            "y": 0
                                        },
                                        "duration": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "rule_id": "",
                                        "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
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
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "face_score": 0,
                                    "landmarks": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "human_powered_vehicle": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "object_id": "",
                                "pedestrian": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "portrait_image_location": {
                                    "panoramic_image_size": {
                                        "height": 0,
                                        "width": 0
                                    },
                                    "portrait_image_in_panoramic": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "portrait_in_panoramic": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    }
                                },
                                "scenario": {
                                    "objects": [
                                        {
                                            "attributes_with_score": {
                                                "additionalProp1": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp2": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp3": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                }
                                            },
                                            "quality": 0,
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                        }
                                    ]
                                },
                                "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                            }
                        ]
                    },
                    "result": {
                        "code": 0,
                        "error": "",
                        "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                    }
                }

        """
        intef = collections.interface("argusIps", "FaceDetect")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def FaceDetectAndExtractPostApi(self, image=None, face_selection=None, detect_mode=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/face_detect_and_extract API """
        """  body: 
                {
                    "detect_mode": "[Default]Default/Slow",
                    "face_selection": "[LargestFace]LargestFace",
                    "feature_version": "",
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "response": {
                        "face_info": {
                            "associations": [
                                {
                                    "object_id": "",
                                    "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                                }
                            ],
                            "automobile": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "crowd": {
                                "density_map": "",
                                "density_size": {
                                    "height": 0,
                                    "width": 0
                                },
                                "incident": [
                                    {
                                        "id": "",
                                        "start_time": "",
                                        "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                        "stop_time": "",
                                        "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                        "update_time": ""
                                    }
                                ],
                                "quantity": "",
                                "strand_map": {
                                    "data": "",
                                    "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                    "url": ""
                                }
                            },
                            "cyclist": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "event": {
                                "event_id": "",
                                "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "rule": {
                                    "direction": {
                                        "x": 0,
                                        "y": 0
                                    },
                                    "duration": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rule_id": "",
                                    "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
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
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "face_score": 0,
                                "landmarks": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ],
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "human_powered_vehicle": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "object_id": "",
                            "pedestrian": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "portrait_image_location": {
                                "panoramic_image_size": {
                                    "height": 0,
                                    "width": 0
                                },
                                "portrait_image_in_panoramic": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "portrait_in_panoramic": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                }
                            },
                            "scenario": {
                                "objects": [
                                    {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                    }
                                ]
                            },
                            "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                        },
                        "feature": {
                            "blob": "",
                            "type": "",
                            "version": 0
                        }
                    },
                    "result": {
                        "code": 0,
                        "error": "",
                        "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                    }
                }

        """
        intef = collections.interface("argusIps", "FaceDetectAndExtract")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("face_selection", face_selection)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def FaceDetectAndExtractAllPostApi(self, image=None, detect_mode=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/face_detect_and_extract_all API """
        """  body: 
                {
                    "detect_mode": "[Default]Default/Slow",
                    "feature_version": "",
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "responses": [
                        {
                            "face_info": {
                                "associations": [
                                    {
                                        "object_id": "",
                                        "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                                    }
                                ],
                                "automobile": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "crowd": {
                                    "density_map": "",
                                    "density_size": {
                                        "height": 0,
                                        "width": 0
                                    },
                                    "incident": [
                                        {
                                            "id": "",
                                            "start_time": "",
                                            "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                            "stop_time": "",
                                            "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                            "update_time": ""
                                        }
                                    ],
                                    "quantity": "",
                                    "strand_map": {
                                        "data": "",
                                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                        "url": ""
                                    }
                                },
                                "cyclist": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "event": {
                                    "event_id": "",
                                    "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rule": {
                                        "direction": {
                                            "x": 0,
                                            "y": 0
                                        },
                                        "duration": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "rule_id": "",
                                        "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
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
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "face_score": 0,
                                    "landmarks": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "human_powered_vehicle": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "object_id": "",
                                "pedestrian": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "portrait_image_location": {
                                    "panoramic_image_size": {
                                        "height": 0,
                                        "width": 0
                                    },
                                    "portrait_image_in_panoramic": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "portrait_in_panoramic": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    }
                                },
                                "scenario": {
                                    "objects": [
                                        {
                                            "attributes_with_score": {
                                                "additionalProp1": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp2": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp3": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                }
                                            },
                                            "quality": 0,
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                        }
                                    ]
                                },
                                "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                            },
                            "feature": {
                                "blob": "",
                                "type": "",
                                "version": 0
                            }
                        }
                    ],
                    "result": {
                        "code": 0,
                        "error": "",
                        "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                    }
                }

        """
        intef = collections.interface("argusIps", "FaceDetectAndExtractAll")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def FaceExtractWithBoundingPostApi(self, image=None, bounding=None, crop_image=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/face_extract_with_bounding API """
        """  body: 
                {
                    "bounding": {
                        "vertices": [
                            {
                                "x": 0,
                                "y": 0
                            }
                        ]
                    },
                    "crop_image": false,
                    "feature_version": "",
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "response": {
                        "align_score": 0,
                        "face_score": 0,
                        "feature": {
                            "blob": "",
                            "type": "",
                            "version": 0
                        }
                    },
                    "result": {
                        "code": 0,
                        "error": "",
                        "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                    }
                }

        """
        intef = collections.interface("argusIps", "FaceExtractWithBounding")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("bounding", bounding)
        intef.update_body("crop_image", crop_image)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def FaceDetectAndExtractWithOverlapPostApi(self, image=None, bounding=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/face_extract_with_overlap API """
        """  body: 
                {
                    "bounding": {
                        "vertices": [
                            {
                                "x": 0,
                                "y": 0
                            }
                        ]
                    },
                    "feature_version": "",
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "response": {
                        "face_info": {
                            "associations": [
                                {
                                    "object_id": "",
                                    "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                                }
                            ],
                            "automobile": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "crowd": {
                                "density_map": "",
                                "density_size": {
                                    "height": 0,
                                    "width": 0
                                },
                                "incident": [
                                    {
                                        "id": "",
                                        "start_time": "",
                                        "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                        "stop_time": "",
                                        "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                        "update_time": ""
                                    }
                                ],
                                "quantity": "",
                                "strand_map": {
                                    "data": "",
                                    "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                    "url": ""
                                }
                            },
                            "cyclist": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "event": {
                                "event_id": "",
                                "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "rule": {
                                    "direction": {
                                        "x": 0,
                                        "y": 0
                                    },
                                    "duration": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rule_id": "",
                                    "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
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
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "face_score": 0,
                                "landmarks": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ],
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "human_powered_vehicle": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "object_id": "",
                            "pedestrian": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "portrait_image_location": {
                                "panoramic_image_size": {
                                    "height": 0,
                                    "width": 0
                                },
                                "portrait_image_in_panoramic": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "portrait_in_panoramic": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                }
                            },
                            "scenario": {
                                "objects": [
                                    {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                    }
                                ]
                            },
                            "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                        },
                        "feature": {
                            "blob": "",
                            "type": "",
                            "version": 0
                        }
                    },
                    "result": {
                        "code": 0,
                        "error": "",
                        "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                    }
                }

        """
        intef = collections.interface("argusIps", "FaceDetectAndExtractWithOverlap")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("bounding", bounding)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def StructDetectPostApi(self, image=None, mode=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/struct_detect API """
        """  body: 
                {
                    "feature_version": "",
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    },
                    "mode": "[Default]Default/Panonamic/Portrait"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "response": {
                        "object_infos": [
                            {
                                "associations": [
                                    {
                                        "object_id": "",
                                        "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                                    }
                                ],
                                "automobile": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "crowd": {
                                    "density_map": "",
                                    "density_size": {
                                        "height": 0,
                                        "width": 0
                                    },
                                    "incident": [
                                        {
                                            "id": "",
                                            "start_time": "",
                                            "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                            "stop_time": "",
                                            "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                            "update_time": ""
                                        }
                                    ],
                                    "quantity": "",
                                    "strand_map": {
                                        "data": "",
                                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                        "url": ""
                                    }
                                },
                                "cyclist": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "event": {
                                    "event_id": "",
                                    "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rule": {
                                        "direction": {
                                            "x": 0,
                                            "y": 0
                                        },
                                        "duration": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "rule_id": "",
                                        "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
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
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "face_score": 0,
                                    "landmarks": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "human_powered_vehicle": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "object_id": "",
                                "pedestrian": {
                                    "attributes_with_score": {
                                        "additionalProp1": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp2": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        },
                                        "additionalProp3": {
                                            "category": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                            "value": 0
                                        }
                                    },
                                    "quality": 0,
                                    "rectangle": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "track_id": ""
                                },
                                "portrait_image_location": {
                                    "panoramic_image_size": {
                                        "height": 0,
                                        "width": 0
                                    },
                                    "portrait_image_in_panoramic": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "portrait_in_panoramic": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    }
                                },
                                "scenario": {
                                    "objects": [
                                        {
                                            "attributes_with_score": {
                                                "additionalProp1": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp2": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp3": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                }
                                            },
                                            "quality": 0,
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                        }
                                    ]
                                },
                                "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                            }
                        ]
                    },
                    "result": {
                        "code": 0,
                        "error": "",
                        "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                    }
                }

        """
        intef = collections.interface("argusIps", "StructDetect")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("mode", mode)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def StructDetectAndExtractPostApi(self, image=None, mode=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/struct_detect_and_extract API """
        """  body: 
                {
                    "feature_version": "",
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    },
                    "mode": "[Default]Default/Panonamic/Portrait"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "response": {
                        "objects": [
                            {
                                "feature": {
                                    "blob": "",
                                    "type": "",
                                    "version": 0
                                },
                                "object_info": {
                                    "associations": [
                                        {
                                            "object_id": "",
                                            "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                                        }
                                    ],
                                    "automobile": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "crowd": {
                                        "density_map": "",
                                        "density_size": {
                                            "height": 0,
                                            "width": 0
                                        },
                                        "incident": [
                                            {
                                                "id": "",
                                                "start_time": "",
                                                "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                                "stop_time": "",
                                                "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                                "update_time": ""
                                            }
                                        ],
                                        "quantity": "",
                                        "strand_map": {
                                            "data": "",
                                            "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                            "url": ""
                                        }
                                    },
                                    "cyclist": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "event": {
                                        "event_id": "",
                                        "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "rule": {
                                            "direction": {
                                                "x": 0,
                                                "y": 0
                                            },
                                            "duration": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "rule_id": "",
                                            "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
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
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "face_score": 0,
                                        "landmarks": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ],
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "human_powered_vehicle": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "object_id": "",
                                    "pedestrian": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "portrait_image_location": {
                                        "panoramic_image_size": {
                                            "height": 0,
                                            "width": 0
                                        },
                                        "portrait_image_in_panoramic": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "portrait_in_panoramic": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        }
                                    },
                                    "scenario": {
                                        "objects": [
                                            {
                                                "attributes_with_score": {
                                                    "additionalProp1": {
                                                        "category": "",
                                                        "roi": {
                                                            "vertices": [
                                                                {
                                                                    "x": 0,
                                                                    "y": 0
                                                                }
                                                            ]
                                                        },
                                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                        "value": 0
                                                    },
                                                    "additionalProp2": {
                                                        "category": "",
                                                        "roi": {
                                                            "vertices": [
                                                                {
                                                                    "x": 0,
                                                                    "y": 0
                                                                }
                                                            ]
                                                        },
                                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                        "value": 0
                                                    },
                                                    "additionalProp3": {
                                                        "category": "",
                                                        "roi": {
                                                            "vertices": [
                                                                {
                                                                    "x": 0,
                                                                    "y": 0
                                                                }
                                                            ]
                                                        },
                                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                        "value": 0
                                                    }
                                                },
                                                "quality": 0,
                                                "rectangle": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                            }
                                        ]
                                    },
                                    "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                                }
                            }
                        ]
                    },
                    "result": {
                        "code": 0,
                        "error": "",
                        "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                    }
                }

        """
        intef = collections.interface("argusIps", "StructDetectAndExtract")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("mode", mode)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def StructExtractWithBoundingPostApi(self, image=None, bounding=None, object_type=None, crop_image=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ips/struct_extract_with_bounding API """
        """  body: 
                {
                    "bounding": {
                        "vertices": [
                            {
                                "x": 0,
                                "y": 0
                            }
                        ]
                    },
                    "crop_image": false,
                    "feature_version": "",
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    },
                    "object_type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "response": {
                        "feature": {
                            "blob": "",
                            "type": "",
                            "version": 0
                        },
                        "object_info": {
                            "associations": [
                                {
                                    "object_id": "",
                                    "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                                }
                            ],
                            "automobile": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "crowd": {
                                "density_map": "",
                                "density_size": {
                                    "height": 0,
                                    "width": 0
                                },
                                "incident": [
                                    {
                                        "id": "",
                                        "start_time": "",
                                        "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                        "stop_time": "",
                                        "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                        "update_time": ""
                                    }
                                ],
                                "quantity": "",
                                "strand_map": {
                                    "data": "",
                                    "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                    "url": ""
                                }
                            },
                            "cyclist": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "event": {
                                "event_id": "",
                                "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "rule": {
                                    "direction": {
                                        "x": 0,
                                        "y": 0
                                    },
                                    "duration": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rule_id": "",
                                    "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
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
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "face_score": 0,
                                "landmarks": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ],
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "human_powered_vehicle": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "object_id": "",
                            "pedestrian": {
                                "attributes_with_score": {
                                    "additionalProp1": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp2": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    },
                                    "additionalProp3": {
                                        "category": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                        "value": 0
                                    }
                                },
                                "quality": 0,
                                "rectangle": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "track_id": ""
                            },
                            "portrait_image_location": {
                                "panoramic_image_size": {
                                    "height": 0,
                                    "width": 0
                                },
                                "portrait_image_in_panoramic": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "portrait_in_panoramic": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                }
                            },
                            "scenario": {
                                "objects": [
                                    {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                    }
                                ]
                            },
                            "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO"
                        }
                    },
                    "result": {
                        "code": 0,
                        "error": "",
                        "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                    }
                }

        """
        intef = collections.interface("argusIps", "StructExtractWithBounding")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("bounding", bounding)
        intef.update_body("object_type", object_type)
        intef.update_body("crop_image", crop_image)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def OCRTemplatePostApi(self, region_type=None, type=None, image=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/ocr/template API """
        """  body: 
                {
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    },
                    "region_type": "[UNKNOWN_REGION]UNKNOWN_REGION/CHINA/UK/HK/MACAO",
                    "type": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "errno": 0,
                        "message": "",
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "response": {
                        "objects": [
                            {
                                "areas": [
                                    {
                                        "name": "",
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ],
                                        "score": 0,
                                        "texts": [
                                            {
                                                "cell_position": {
                                                    "bottom_right_col": 0,
                                                    "bottom_right_row": 0,
                                                    "top_left_col": 0,
                                                    "top_left_row": 0
                                                },
                                                "chars": [
                                                    {
                                                        "roi": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ],
                                                        "score": 0,
                                                        "val": "",
                                                        "valid": false
                                                    }
                                                ],
                                                "content": "",
                                                "multiline": false,
                                                "name": "",
                                                "roi": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ],
                                                "score": 0,
                                                "subtexts": [
                                                    {
                                                        "content": "",
                                                        "roi": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ],
                                                        "score": 0,
                                                        "valid": false
                                                    }
                                                ],
                                                "valid": false
                                            }
                                        ],
                                        "valid": false
                                    }
                                ],
                                "document_retrieve_feature": {
                                    "blob": "",
                                    "type": "",
                                    "version": 0
                                },
                                "landmarks": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ],
                                "object_detect_info": [],
                                "rectify_matrix": {
                                    "columns": 0,
                                    "data": [],
                                    "order": "[ROW_MAJOR]ROW_MAJOR/COLUMN_MAJOR",
                                    "rows": 0
                                },
                                "type": ""
                            }
                        ]
                    },
                    "result": {
                        "code": 0,
                        "error": "",
                        "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                    }
                }

        """
        intef = collections.interface("argusIps", "OCRTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("region_type", region_type)
        intef.update_body("type", type)
        intef.update_body("image", image)
        return intef.request() if sendRequest else intef

