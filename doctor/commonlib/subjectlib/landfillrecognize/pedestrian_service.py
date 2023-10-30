#!/usr/local/bin/python3
#coding:utf-8
import os
import base64
from PIL import Image
import requests
import json
import hashlib

def pedestrian(baseurl,ak,groupID,deviceID,cameraID,filepath,requesttype,ts):
    f = open(filepath, "rb")
    img = Image.open(filepath)
    width = img.width
    height = img.height
    url = baseurl + "/argus/v1/recognize/pedestrian"
    if requesttype == "facerect":
        data = {
            "timestamp": int(ts/1000),
            "device": {
                "device_id": deviceID,
                "camera_id": cameraID,
                "camera_name": cameraID,
                "group_id": groupID
            },
            "image": {
                "snap_image": str(base64.b64encode(f.read()), encoding="utf-8")
            },
            "face": {
                "rect": {
                    "left": 0,
                    "top": 0,
                    "right": 850,
                    "bottom": 850
                },
                "origin_rect": {
                    "left": 0,
                    "top": 0,
                    "right": 850,
                    "bottom": 850
                },
                "track_id": str(ts),
                "frame_id": ts,
                "track_ts": ts
            },
            "monitor": {
                "face_total_cost": 40
            },
            "meta": {
                "extra": "testextra"
            }
        }
    elif requesttype == "face":
        data = {
            "timestamp": int(ts/1000),
            "device": {
                "device_id": deviceID,
                "camera_id": cameraID,
                "camera_name": cameraID,
                "group_id": groupID
            },
            "image": {
                "snap_image": str(base64.b64encode(f.read()), encoding="utf-8")
            },
            "face": {
                "rect": {
                    "left": 0,
                    "top": 0,
                    "right": width,
                    "bottom": height
                },
                "origin_rect": {
                    "left": 0,
                    "top": 0,
                    "right": width,
                    "bottom": height
                },
                "track_id": str(ts),
                "frame_id": ts,
                "track_ts": ts
            },
            "monitor": {
                "face_total_cost": 40
            },
            "meta": {
                "extra": "testextra"
            }
        }
    elif requesttype == "body":
        data = {
            "timestamp": int(ts/1000),
            "device": {
                "device_id": deviceID,
                "camera_id": cameraID,
                "camera_name": cameraID,
                "group_id": groupID
            },
            "image": {
                "snap_image": str(base64.b64encode(f.read()), encoding="utf-8")
            },
            "body": {
                "origin_rect": {
                    "left": 0,
                    "top": 0,
                    "right": width,
                    "bottom": height
                },
                "track_id": str(ts),
                "frame_id": ts,
                "track_ts": ts
            },
            "monitor": {
                "body_total_cost": 50
            },
            "meta": {
                "extra": "testextra"
            }
        }
    elif requesttype == "facebody":
        data = {
            "timestamp": int(ts/1000),
            "device": {
                "device_id": deviceID,
                "camera_id": cameraID,
                "camera_name": cameraID,
                "group_id": groupID
            },
            "image": {
                "snap_image": str(base64.b64encode(f.read()), encoding="utf-8")
            },
            "face": {
                "rect": {
                    "left": 0,
                    "top": 0,
                    "right": width,
                    "bottom": height
                },
                "origin_rect": {
                    "left": 0,
                    "top": 0,
                    "right": width,
                    "bottom": height
                },
                "track_id": str(ts),
                "frame_id": ts,
                "track_ts": ts
            },
            "body": {
                "origin_rect": {
                    "left": 0,
                    "top": 0,
                    "right": width,
                    "bottom": height
                },
                "track_id": str(ts),
                "frame_id": ts,
                "track_ts": ts
            },
            "monitor": {
                "face_total_cost": 40,
                "body_total_cost": 50
            },
            "meta": {
                "extra": "testextra"
            }
        }
    headers = {
        'Content-Type': 'application/json',
        'ak': ak
    }
    response = requests.post(url, json=data,headers=headers)
    return json.loads(response.content)

def AddStreamGroup(baseurl,ak,groupname,staticgroupids):
    url = baseurl + "/argus/v1/db/stream_group"
    data= {
        "ak": ak,
        "group_name": groupname,
        "group_mold": "PEDESTRIAN",
        "group_size": 5000000,
        "pedes_cb_url": "testurl",
        "expired_time":180,
        "bind_groups":staticgroupids
    }
    response = requests.post(url, json=data)
    return json.loads(response.content)

def AddStaticGroup(baseurl,ak,groupname):
    url = baseurl + "/argus/v1/db/static_group"
    data= {
        "ak": ak,
        "group_name": groupname,
        "group_mold": "FACE",
        "group_size": 5000000
    }
    response = requests.post(url, json=data)
    return json.loads(response.content)

def DelStreamGroup(baseurl,ak,groupid):
    url = baseurl + "/argus/v1/db/stream_group"
    data = {
        "ak": ak,
        "group_id": groupid
    }
    response = requests.delete(url, json=data)
    return json.loads(response.content)

def DelStaticGroup(baseurl,ak,groupid):
    url = baseurl + "/argus/v1/db/static_group"
    data = {
        "ak": ak,
        "group_id": groupid
    }
    response = requests.delete(url, json=data)
    return json.loads(response.content)

def GetToken(baseurl,name,pwd):
    url = baseurl + "/argus/operation/v1/login"
    data = {
        "name": name,
        "password": hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()
    }
    response = requests.post(url, json=data)
    return json.loads(response.content)

if __name__ == '__main__':

    pass