# -*- coding: utf-8 -*-
import json

from locust import User, task, TaskSet, events, between, FastHttpUser, HttpUser
from locust.clients import ResponseContextManager
from locust.runners import logger

import time
import os

from commonlib import config
from commonlib.api_lib.base_api import BaseApi
import urllib3

urllib3.disable_warnings()


def success_call(name, recvText, total_time):
    events.request.fire(
        request_type="[Success]",
        name=name,
        response_time=total_time,
        response_length=len(recvText)
    )


def fail_call(name, total_time, e):
    events.request.fire(
        request_type="[Fail]",
        name=name,
        response_time=total_time,
        response_length=0,
        exception=e,
    )


class CTIDStressTaskSet(TaskSet):
    """
    任务集
    """

    def on_start(self):
        logger.info("hello")
        host1 = "https://ids.test.sensebelt.net/verify/atom/bio-face/engine"
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        images_path = config.ctid_image_path
        img_path_t = "normal_single_face_20KB.jpg"
        img_path_t1 = os.path.join(images_path, img_path_t)
        img_path_t2 = os.path.join(images_path, img_path_t)
        photoData1 = BaseApi.imageToBase64(img_path_t1)
        photoData2 = BaseApi.imageToBase64(img_path_t2)
        data = {
            "bizSerialNo": bizSerialNo,
            "photoData1": photoData1,
            "photoData2": photoData2
        }
        self.body = json.dumps(data)

    def on_stop(self):
        logger.info('goodbye')

    @task
    def two_photos_verify(self):
        # self.client.post('/')
        url = "https://ids.test.sensebelt.net/verify/atom/bio-face/engine/two-photos-verify"
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        images_path = config.ctid_image_path
        img_path_t = "normal_single_face_20KB.jpg"
        img_path_t1 = os.path.join(images_path, img_path_t)
        img_path_t2 = os.path.join(images_path, img_path_t)
        photoData1 = BaseApi.imageToBase64(img_path_t1)
        photoData2 = BaseApi.imageToBase64(img_path_t2)
        data = {
            "bizSerialNo": bizSerialNo,
            "photoData1": photoData1,
            "photoData2": photoData2
        }
        body = json.dumps(data)
        start = time.time()
        with self.client.post(url=url, verify=False, data=body, catch_response=True) as resp:
            # 表示这个res是一个ResponseContextManager类型，他就可以用里面的一些方法了
            resp: ResponseContextManager

            # total_time = int((time.time() - start) * 1000)
            # success_call(name='two_photos_verify', recvText="ok", total_time=total_time)
            # fail_call(name='two_photos_verify_fail', total_time=total_time, e=e)
            if resp.status_code != 200:
                logger.info(resp.status_code)
            #assert resp.status_code == 200
            if resp.status_code != 200 or resp.json()["errCode"] != '000':
                # 将失败的请求写入到failure里，供前端页面展示
                resp.failure(resp.text)
            else:
                resp.success()
            #logger.info(resp.text)


class CTIDUser(HttpUser):
    """
    - 会产生并发用户实例
    - 产生的用户实例会依据规则去执行任务集

    """
    # 定义的任务集
    tasks = [CTIDStressTaskSet, ]
    host = "https://ids.test.sensebelt.net/verify/atom/bio-face/engine/two-photos-verify"
    wait_time = between(0, 0.5)
