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

# urllib3.disable_warnings()

def get_file_path_by_name():
    '''
    获取指定路径下所有文件的绝对路径
    '''
    L = []
    for root, dirs, files in os.walk(r"D:/CRD/apitest/resource/images/go_image/ids_face/accuracy"):  # 获取所有文件
        for file in files:  # 遍历所有文件名
            if os.path.splitext(file)[1] == '.jpg':   # 指定尾缀  ***重要***
                L.append(os.path.join(root, file))  # 拼接处绝对路径并放入列表
    # print('总文件数目：', len(L))
    # print(L)
    return L


class ApiTask(TaskSet):

    @task
    def postIngress(self):
        url = "/ids/face"
        headers = {
            "X-Belt-Action": "DetectLiveness",
            "X-Belt-Version": "v1",
            "X-Belt-Signature": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIySXRSS0Q2eVhreUhOa0Y3ODhQeEdzMlVhdDkiLCJleHAiOjE2NzEyMDEyNzQsIm5iZiI6MTY3MTE5OTQ2OX0.hi4eIPdXqhpbNORpGGuDJjXiAFJYOQ7FlT1vNrGMB0U"
        }

        photo = r'D:\\CRD\\apitest\\resource\\images\\go_image\\ids_face\\accuracy\\g9.jpg'  # 图片路径
        # random.choice(get_file_path_by_name())
        with open(photo, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            image = base64_data.decode()
        # 人脸质量控制等级.
        # enum QualityLevel {
        # 不做质量检测过滤.
        # QUALITY_LEVEL_NONE = 0;
        # 低质量.
        # LOW = 1;
        # 普通.
        # NORMAL = 2;
        # 高质量等级.
        # HIGH = 3;
        # }
        body = {
            "disable_defake": False,
            "encrypt_info": {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "data": "string",
                "encrypted_fields": [
                    "string"
                ],
                "iv": "string",
                "version": 0
            },
            "image": image,
            "min_quality_level": "NORMAL"
        }
        # 把client.get的返回值作为res存起来
        data = json.dumps(body)
        # encode_jwt_token()
        with self.client.post(url=url, verify=False, headers=headers, catch_response=True, data=data) as res:
            # 表示这个res是一个ResponseContextManager类型，他就可以用里面的一些方法了
            res: ResponseContextManager
            # 这里可以写一些逻辑，例如返回值不等于200,或者返回结果里报错了等等
            if res.status_code != 200:
                # 将失败的请求写入到failure里，供前端页面展示
                res.failure(res.text)

    def on_start(self):
        logger.info('hello')

    def on_stop(self):
        logger.info('goodbye')


class User(HttpUser):
    host = 'https://172.20.26.107'
    tasks = [ApiTask, ]
    min_wait = 1000  # 用户行为间隔的最小的等待时间，毫秒
    max_wait = 2000   # 用户行为间隔的最大的等待时间，毫秒, 默认1秒


if __name__ == '__main__':
    pass
