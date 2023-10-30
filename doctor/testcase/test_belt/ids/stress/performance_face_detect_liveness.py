import urllib3
urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser
from locust.clients import ResponseContextManager
from locust.runners import logger
import requests
from core import toml_utils
# from defines.nebula_final.edge_service_business import EdgeSwaggerBusiness
from commonlib.api_lib.base_api import BaseApi
import json
class ApiTask(TaskSet):

    #测试的时候找子木模拟一个接口
    @task
    def ocr_idcrad(self):
        url = "/face"
        headers = {
            "X-Belt-Action": "DetectLiveness",
            "X-Request-ID": "test1",
            "X-Belt-Signature": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJuYWlkdmV6RHlyZWxBZE5haWZNeUh5aXRDeXNob2JIYSIsImV4cCI6MTY5ODAzMDE0MH0.utGXUR9g3bl2K8ptvNpNvE3rs7_b59fXMMK7QtasZbE",
            "X-Belt-Version": "v1"
        }
        # image_path="/Users/weishuting/code/belt-beta-new/doctor/resource/images/go_image/ids_ws_face/w2_162k.jpg"
        image_path="/Users/weishuting/code/belt-beta-new/doctor/resource/images/go_image/ids_ws_face/w2_400k.jpg"
        # image_path="/Users/weishuting/code/belt-beta-new/doctor/resource/images/go_image/ids_ws_face/w2_516k.jpg"
        base64_image=str(BaseApi.imageToBase64(image_path))
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
            "image": base64_image,
            "min_quality_level": "NORMAL"
        }

        body_str=json.dumps(body)
        #把client.get的返回值作为res存起来
        with self.client.post(url=url,verify=False, data=body_str, headers=headers,catch_response=True) as res:
            #表示这个res是一个ResponseContextManager类型，他就可以用里面的一些方法了
             res: ResponseContextManager
            #这里可以写一些逻辑，例如返回值不等于200,或者返回结果里报错了等等

             if res.status_code != 200:
                 #将失败的请求写入到failure里，供前端页面展示
                 res.failure(res.text)

    # @task
    # def postIngress(self):
    #     url = "http://crd-test.sensetime.com/ras"
    #     headers = {
    #         "X-Belt-Action": "OCRIDCard",
    #         "X-Request-ID": "test1",
    #         "X-Belt-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIySXN5SDZqSkRFNTNWelVNcGk4RmRRdjFZQU8iLCJleHAiOjE2NzEwMjk0NjAsIm5iZiI6MTY3MDk4NjI1NX0.qYRjXV4_ryKTzfuQknzq7vh94bi9RfxLAOCocPWCRgs",
    #         "X-Belt-Version": "v1"
    #     }
    #     #把client.get的返回值作为res存起来
    #     with self.client.post(url=url, verify=False, headers=headers,catch_response=True) as res:
    #         #表示这个res是一个ResponseContextManager类型，他就可以用里面的一些方法了
    #          res: ResponseContextManager
    #         #这里可以写一些逻辑，例如返回值不等于200,或者返回结果里报错了等等
    #          if res.status_code != 200:
    #              #将失败的请求写入到failure里，供前端页面展示
    #              res.failure(res.text)

    def on_start(self):
        logger.info('hello')

    def on_stop(self):
        logger.info('goodbye')


class User(HttpUser):
    host = 'https://ids.test.sensebelt.net'
    min_wait = 10000
    max_wait = 10000    
    tasks = [ApiTask]

if __name__ == '__main__':
    pass