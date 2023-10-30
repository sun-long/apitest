#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# from commonlib import sign_utils
from locust.runners import logger
from locust.clients import ResponseContextManager
from locust import TaskSet, task, HttpUser
import urllib3
import json
import base64
import os
import random
import time
urllib3.disable_warnings()


def get_file_path_by_name():
    '''
    获取指定路径下所有文件的绝对路径
    '''
    L = []
    for root, dirs, files in os.walk(r"D:/CRD/apitest/resource/images/go_image/ids_face/accuracy/liveness"):  # 获取所有文件
        for file in files:  # 遍历所有文件名
            if os.path.splitext(file)[1] == '.jpg':   # 指定尾缀  ***重要***
                L.append(os.path.join(root, file))  # 拼接处绝对路径并放入列表
    # print('总文件数目：', len(L))
    # print(L)
    return L


class ApiTask(TaskSet):

    @task
    def postIngress(self):
        url = "/face"
        headers = {
            "X-Belt-Action": "AddPerson",
            "X-Belt-Version": "v1",
            "X-Belt-Signature": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyTDRZOE04d1pZMmxFRnI3czlJcVFHVlV3RXEiLCJleHAiOjE2Nzc3MzMzMTAsIm5iZiI6MTY3NzU1MzMwNX0.YLYDWeH9793T5KvQiTRmgN3FZClI4pvRG_asawzwRlw"
        }

        photo = r'D:\\CRD\\apitest\\resource\\images\\go_image\\face1vsN\\face\\201k.jpg'  # 图片路径
        #random.choice(get_file_path_by_name())
        with open(photo, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            image = base64_data.decode()
        body = {
    "db_id": "166602161550019077",
    "person_id": str(random.randint(1000000000000, 9999999999999)),
    "images": [ 
            image
        ],
    "extra_info": "string",
    "auto_rotate": True,
    "min_quality_level": "QUALITY_LEVEL_NONE",
    "tag_ids": ["167188383934721710"
    ],
  "encrypt_info": {
    "algorithm": "ENCRPT_ALGORITHM_NONE",
    "version": 0,
    "encrypted_fields": [
      "string"
    ],
    "data": "string"
  }
}
        # 把client.get的返回值作为res存起来
        data = json.dumps(body)
        # encode_jwt_token()
        with self.client.post(url=url, verify=False, headers=headers, catch_response=True, data=data) as res:
            # 表示这个res是一个ResponseContextManager类型，他就可以用里面的一些方法了
            res: ResponseContextManager
            if res.status_code != 200:
                # 将失败的请求写入到failure里，供前端页面展示
                res.failure(res.text)

    def on_start(self):
        logger.info('开始测试')

    def on_stop(self):
        logger.info('结束测试')


class User(HttpUser):
    host = 'https://ids.test.sensebelt.net'
    tasks = [ApiTask, ]
    min_wait = 1000  # 用户行为间隔的最小的等待时间，毫秒
    max_wait = 2000   # 用户行为间隔的最大的等待时间，毫秒, 默认1秒


if __name__ == '__main__':
    pass
