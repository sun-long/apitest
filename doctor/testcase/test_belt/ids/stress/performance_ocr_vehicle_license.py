import urllib3
urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser
from locust.clients import ResponseContextManager
from locust.runners import logger
import requests
from core import toml_utils
from defines.nebula_final.edge_service_business import EdgeSwaggerBusiness
from commonlib.api_lib.base_api import BaseApi
import json
class ApiTask(TaskSet):

    #测试的时候找子木模拟一个接口
    @task
    def ocr_idcrad(self):
        # url = "https://crd-test.sensetime.com/ids-wrapper/v1/ocr/bankcard"
        url = "https://alb-dcc-1-cn-shanghai-1.test-sensebelt.com/ids/ocr"
        headers = {
            "X-Belt-Action": "OCRVehicleLicense",
            "X-Request-ID": "test1",
            "X-Belt-Signature": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIySnFKcERvRWVvd01UNEpDZjdGcDUxNkhHelUiLCJleHAiOjE2NzMwMTQzMDMsIm5iZiI6MTY3Mjk3MTA5OH0.ObVoTSCEAScwP3dWU2IxUmL-PIcyA-VNvU4B7o4z2Zs",
            "X-Belt-Version": "v1"
        }
        # base64_image=str(BaseApi.imageToBase64(f"/Users/weishuting/code/gitlab.sz.sensetime.com/cloud/new_apitest/apitest/image/ocr/vehicle_license/performance_vehicle_small.jpg"))

        base64_image=str(BaseApi.imageToBase64(f"/Users/weishuting/code/gitlab.sz.sensetime.com/cloud/new_apitest/apitest/image/ocr/vehicle_license/performance_vehicle_big.jpg"))        
        body={
                    "encrypt_info": {
                        "algorithm": "ENCRPT_ALGORITHM_NONE",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": base64_image
                }
        body_str=json.dumps(body)
        # body_str={}
        #把client.get的返回值作为res存起来
        with self.client.post(url=url,verify=False, data=body_str, headers=headers,catch_response=True) as res:
            #表示这个res是一个ResponseContextManager类型，他就可以用里面的一些方法了
             res: ResponseContextManager
            #这里可以写一些逻辑，例如返回值不等于200,或者返回结果里报错了等等
             if res.status_code != 200:
                 #将失败的请求写入到failure里，供前端页面展示
                 res.failure(res.text)

    def on_start(self):
        logger.info('hello')

    def on_stop(self):
        logger.info('goodbye')


class User(HttpUser):
    # host = 'https://crd-test.sensetime.com/ids-wrapper/v1/ocr/bankcard'
    host = 'https://alb-dcc-1-cn-shanghai-1.test-sensebelt.com/ids/ocr'   
    min_wait = 1000
    max_wait = 1000    
    tasks = [ApiTask]

if __name__ == '__main__':
    pass