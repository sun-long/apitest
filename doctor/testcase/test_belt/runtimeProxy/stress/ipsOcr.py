import os

import urllib3

from commonlib import config
from defines.belt.ipsocr_service_business import IpsocrSwaggerBusiness

urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser, between
from locust.clients import ResponseContextManager
from locust.runners import logger

from core import toml_utils


class ApiTask(TaskSet):

    @task
    def batchTemplate(self):
        """ 测试负载"""
        interf = self.user.IpsocrApi.BatchTemplatePostApi(region_type=self.user.region_type, type=self.user.type, images=self.user.images, sendRequest=False)
        with self.client.post(interf.url, headers=interf.headers, json=interf.body, verify=False, catch_response=True) as res:
            res: ResponseContextManager
            if res.status_code == 200:
                res.success()
            else:
                res.failure(res.text)

    @task
    def getSystemInfo(self):
        """ 测试负载"""
        interf = self.user.IpsocrApi.GetSystemInfoGetApi(sendRequest=False)
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
    IpsocrApi = IpsocrSwaggerBusiness(host, config_obj=config_obj,  ext_info=None)
    image1 = os.path.join(config.image_path, "go_image/belt/tempidcardimgdata.jpeg")
    region_type = "CHINA"
    type = "OCR_IDCARD_CLASS"
    images = [
        {
            "format": "IMAGE_JPEG",
            "data": IpsocrApi.imageToBase64(image1)
        }
    ]
    tasks = [ApiTask, ]

if __name__ == '__main__':
    pass