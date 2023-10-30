#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   parse_alarm.py
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/26 下午4:41   wangan      1.0         None
'''
import json
import os

req_body = {"data":"{\"task\":{\"app_name\":\"action_recgnition_template\",\"app_version\":1,\"hold_on\":true,\"context_id\":\"10002022112608354144701\",\"userkey\":\"1872465d-4cf3-426c-a604-3201f6ad081a\",\"callback\":{\"type\":1,\"data\":{\"value\":\"{\\\"topic\\\": \\\"test.belt.crd.bot.ars\\\"}\"},\"oss_config\":{\"type\":2,\"format\":\"v1.0.0/account1/6c276cba1cf44beba6a94dd5870526b0/1872465d-4cf3-426c-a604-3201f6ad081a/%Y/%m/%d\",\"data\":{\"value\":\"{\\\"bucket\\\": \\\"fell-detective\\\"}\"}}},\"source\":{\"type\":1,\"address\":\"rtsp://10.4.132.35:8554/085200_new.264\",\"data\":{\"value\":\"{}\"}},\"data\":{\"value\":\"{\\\"image\\\":\\\"http://minio-default.sensego-crd-dev.svc.cluster.local:9000/fell-detective/v1.0.0/account1/6c276cba1cf44beba6a94dd5870526b0/1872465d-4cf3-426c-a604-3201f6ad081a/2022/11/26/20221126-17fdbd6f-0a580af4a8f5-0000000f-0021369c?X-Amz-Algorithm=AWS4-HMAC-SHA256\\\\u0026X-Amz-Credential=minio%2F20221126%2Fminio%2Fs3%2Faws4_request\\\\u0026X-Amz-Date=20221126T084117Z\\\\u0026X-Amz-Expires=604800\\\\u0026X-Amz-SignedHeaders=host\\\\u0026X-Amz-Signature=6b3d32a2af307dbd4867bc0f76435b654706d1c63f2832b9bf565e52576e1532\\\",\\\"targets\\\":[{\\\"ctx_id\\\":\\\"10002022112608354144701\\\",\\\"type\\\":\\\"tumble\\\",\\\"roi\\\":{\\\"height\\\":356,\\\"left\\\":838,\\\"width\\\":420},\\\"confidence\\\":0.96990407}]}\"},\"extra_info\":\"{\\\"AIDE_TASK_GRAY\\\":true,\\\"AIDE_TASK_REQ\\\":\\\"{\\\\\\\"task\\\\\\\":{\\\\\\\"task_id\\\\\\\":\\\\\\\"10002022112608353953401\\\\\\\",\\\\\\\"object_type\\\\\\\":\\\\\\\"OBJECT_ALGO\\\\\\\",\\\\\\\"source_address\\\\\\\":\\\\\\\"rtsp://10.4.132.35:8554/085200_new.264\\\\\\\",\\\\\\\"camera_info\\\\\\\":{\\\\\\\"internal_id\\\\\\\":{\\\\\\\"region_id\\\\\\\":2,\\\\\\\"camera_idx\\\\\\\":2}},\\\\\\\"task_object_config\\\\\\\":{\\\\\\\"algo_config\\\\\\\":{\\\\\\\"app_name\\\\\\\":\\\\\\\"com.sensetime.algo.home.based.care\\\\\\\",\\\\\\\"app_version\\\\\\\":10101,\\\\\\\"data\\\\\\\":{\\\\\\\"value\\\\\\\":\\\\\\\"{\\\\\\\\\\\\\\\"rules\\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\\"type\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"tumble\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"rule_id\\\\\\\\\\\\\\\":\\\\\\\\\\\\\\\"a\\\\\\\\\\\\\\\",\\\\\\\\\\\\\\\"roi\\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\\"vertices\\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\\"x\\\\\\\\\\\\\\\":0,\\\\\\\\\\\\\\\"y\\\\\\\\\\\\\\\":1},{\\\\\\\\\\\\\\\"x\\\\\\\\\\\\\\\":100,\\\\\\\\\\\\\\\"y\\\\\\\\\\\\\\\":100},{\\\\\\\\\\\\\\\"vertices\\\\\\\\\\\\\\\":[{\\\\\\\\\\\\\\\"x\\\\\\\\\\\\\\\":200,\\\\\\\\\\\\\\\"y\\\\\\\\\\\\\\\":200},{\\\\\\\\\\\\\\\"x\\\\\\\\\\\\\\\":400,\\\\\\\\\\\\\\\"y\\\\\\\\\\\\\\\":400}]}]}]}\\\\\\\"}}}}}\\\"}\"},\"creation_time\":{\"seconds\":1669452076,\"nanos\":782230520}}"}
data = req_body["data"]

def zhuanyi(data):
    """"""
    return json.dumps(data)

def dezhuanyi(_str):
    """"""
    return json.loads(_str)

def save_json(data, save_path):
    data = json.dumps(data, sort_keys=True, indent=2)
    with open(save_path, 'w') as f:
        f.write(data)
    print("文件写入成功.path:%s" % save_path)

data = dezhuanyi(data)
data_value = dezhuanyi(data['task']["data"]["value"])
data['task']["data"]["value"] = data_value
task_name = data['task']['source']['address'].split("/")[-1].split(".")[0]
task_dir = "/home/SENSETIME/wangan/belt/msg/%s" % task_name
creation_time = data['creation_time']['seconds']
if not os.path.exists(task_dir):
    os.makedirs(task_dir)
save_path = os.path.join(task_dir, "%s.json" % creation_time)
save_json(data, save_path)

i = 1