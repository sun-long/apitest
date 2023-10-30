#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.arguspedestrian_service_swagger import ArguspedestrianSwaggerApi
from commonlib import config, time_utils, sign_utils, utils
from PIL import Image
"""
使用说明：


"""


class ArguspedestrianSwaggerBusiness(ArguspedestrianSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(ArguspedestrianSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息
        self.configMap = utils.readConfigMap("argus.yaml", "http://ingress-meister-landfill.argus:11000")

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        if inte_obj.path in self.configMap:
            info = self.configMap[inte_obj.path][inte_obj.method]
            inte_obj.set_headers('X-Belt-Action', info["action"])
            inte_obj.set_headers('X-Belt-Version', info["version"])
            inte_obj.set_path_prefix(info["paths"])
        else:
            raise Exception("no support PATH:%s" % inte_obj.path)


    def Pedestrian_face(self, group_id, image_path, timestamp, requestId=None,
                        device_id="device_id", camera_id="camera_id", camera_name="camera_name",
                        associates=None, faceTrack=None, loginToken=None, sendRequest=True, print_log=True,
                        interface_desc=None, ak=None, rect=None, origin_rect=None):
        img = Image.open(image_path)
        width = img.width
        height = img.height

        bg_image_upload = None
        body = None
        device =  {
            "device_id": device_id,   # 必须，设备id，一个设备可能对应多个摄像头
            "camera_id": camera_id,   # 必须，摄像头id
            "camera_name": camera_name, # 可选，摄像头名字
            "group_id": group_id,  # 可选，该设备绑定的库id，若使用的是Argus平台纳管的端/边设备可不填（如SenseGo EdgeCube, SenseGo Lens等），否则必须填写
        }
        face =  {
            "rect": {        # 必须，人脸在人脸外扩图中的框
                "left": 0,
                "right": width,
                "top": 0,
                "bottom": height
            },
            "origin_rect": { # 必须，人脸在原图中的框
                "left": 0,
                "right": width,
                "top": 0,
                "bottom": height
            },
            "frame_id": int(120*25 + int(timestamp)/400 - 1),   # 可选，帧id
            "track_id": str(timestamp * 1000),  # 必须，设备上识别出的人员id
            "track_ts": timestamp * 1000    # 必须，该图片被摄像头捕获的时间，unix时间戳（单位ms）
        }
        if rect:
            face["rect"].update(rect)
        if origin_rect:
            face["origin_rect"].update(rect)
        flag = None
        image = {
            "snap_image": self.imageToBase64(image_path)
        }
        location = None
        meta = None
        misc = None
        monitor = {
            "face_total_cost":40,
            "body_total_cost":40
        }
        relation = None
        timestamp = time_utils.get_timestamp(timestamp)
        intef = self.Pedestrain_RecognizePostApi(associates=associates, bg_image_upload=bg_image_upload,
                                                              body=body, device=device, face=face, faceTrack=faceTrack,
                                                              flag=flag, image=image, location=location, meta=meta,
                                                              misc=misc, monitor=monitor, relation=relation,
                                                              timestamp=timestamp, loginToken=loginToken,
                                                              sendRequest=False, print_log=print_log,
                                                              interface_desc=interface_desc)
        if requestId:
            intef.set_headers("X-Request-Id", requestId)
        return intef.request() if sendRequest else intef