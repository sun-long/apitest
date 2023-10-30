import urllib3
urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser, tag,between,constant_throughput
from locust.clients import ResponseContextManager
from locust.runners import logger
from core import toml_utils
from commonlib.api_lib.base_api import BaseApi
import json
import os
import time
import queue
from commonlib.api_lib.AES_new import *
from commonlib import config, time_utils, sign_utils,utils

class ApiTask(TaskSet):
    @task
    def face1vn_search_person(self):
        
        url = "/face"
        headers = {
            "X-Belt-Action": "SearchPerson",
            "X-Request-ID": "testface1vn",
            "X-Belt-Signature": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyTW9iZjljNzJWbzNhUVZvV2NhVjU0SmtoQ2YiLCJleHAiOjE2Nzk2NjgzOTIsIm5iZiI6MTY3OTYyNTE4N30.ZXs7sYoJVPCDpPfjpWusp258CJmtYkDy-6Ib4OGQzNM",
            "X-Belt-Version": "v1"
        }
        image_path=os.path.join(config.ids_image_path, "face1vn/3M.jpg")
        base64_image=str(BaseApi.imageToBase64(image_path))
        body={"image":base64_image,
               "db_id": "168782031247910594",
               "min_score": 0,
               "top_k": 10
            }
        body_str=json.dumps(body)
        start_time = time.time()
        #把client.get的返回值作为res存起来
        with self.client.post(url=url,verify=False, data=body_str, headers=headers,catch_response=True) as res:
            #表示这个res是一个ResponseContextManager类型，他就可以用里面的一些方法了
            res: ResponseContextManager
            #这里可以写一些逻辑，例如返回值不等于200,或者返回结果里报错了等等
            if res.status_code != 200:
                 #将失败的请求写入到failure里，供前端页面展示
                res.failure(str(res.status_code)+res.text)
     

             

    def on_start(self):
        logger.info('hello')


    def on_stop(self):
        logger.info('goodbye')
  

class User(HttpUser):
    host = 'https://ids.test.sensebelt.net'
    tasks = [ApiTask]

if __name__ == '__main__':
    pass