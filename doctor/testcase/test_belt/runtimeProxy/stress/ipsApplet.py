import os

import urllib3

from commonlib import config

urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser, between
from locust.clients import ResponseContextManager
from locust.runners import logger

from core import toml_utils
from defines.belt.ipsapplet_service_business import IpsappletSwaggerBusiness


class ApiTask(TaskSet):

    @task
    def batchProcess(self):
        """ 测试负载"""
        interf = self.user.IpsappletApi.BatchProcessPostApi(requests=self.user.requests_proxy, sendRequest=False)
        with self.client.post(interf.url, headers=interf.headers, json=interf.body, verify=False, catch_response=True) as res:
            res: ResponseContextManager
            if res.status_code != 200:
                res.failure(res.text)

    @task
    def getSystemInfo(self):
        """ 测试负载"""
        interf = self.user.IpsappletApi.GetSystemInfoGetApi(sendRequest=False)
        print(interf.path)
        print(interf.headers)
        with self.client.get(interf.url, headers=interf.headers, verify=False, catch_response=True) as res:
            res: ResponseContextManager
            if res.status_code == 200:
                res.success()
            else:
                res.failure(res.text)

    def on_start(self):
        logger.info('hello')

    def on_stop(self):
        logger.info('goodbye')


class User(HttpUser):
    wait_time = between(0.1, 3)
    config_obj = toml_utils.gen_config_obj("belt_dev")
    host = config_obj.EnvInfo.BeltCloud.RunTimeProxyService
    IpsappletApi = IpsappletSwaggerBusiness(host, config_obj=config_obj)
    image1 = os.path.join(config.image_path, "go_image/face/wsh/shihan1.jpg")
    image2 = os.path.join(config.image_path, "go_image/face/wsh/shihan2.jpg")
    requests_proxy = [
        {
            "images": [
                {"data": IpsappletApi.imageToBase64(image1), },
                {"data": IpsappletApi.imageToBase64(image2), },
            ],
            "config": {
                "value": "{\"stages\":[\"headpose\",\"eyestate\",\"liveness\",\"feature\",\"defake\"]}"
            }
        },
    ]
    tasks = [ApiTask, ]

if __name__ == '__main__':
    pass