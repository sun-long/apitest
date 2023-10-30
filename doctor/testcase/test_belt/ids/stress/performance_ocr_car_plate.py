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
    def ocr_car_plate(self):
        
        self.client.request_name="ocr_car_plate"
        url = "/ocr"
        token = self.user.queue_token.get()
        self.user.queue_token.put(token)
        headers = {
            "X-Belt-Action": "OCRCarPlate",
            "X-Request-ID": "testCarPlate",
            "X-Belt-Signature": token,
            "X-Belt-Version": "v1"
        }
        image_path=os.path.join(config.ids_image_path, "ocr/car_plate/performance_car_plate_small.jpg")
        base64_image=str(BaseApi.imageToBase64(image_path))
        body={"image":base64_image}
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
        time_cost = time.time() - start_time
        # 
        # if time_cost >0.2:
        #     pass
        # else:
        #     wait_time = 0.2 - round(time_cost,2)
        #     time.sleep(wait_time)         


    def on_start(self):
        logger.info('hello')
        # ak = "2Jqmqs5AaTf7VkaeischoCsKVKh"
        # sk = "ui2TJY8zNhm0ycai1ovfjRV3Lpiaa2V9"
        # self.token = sign_utils.encode_jwt_token(ak,sk)
    

    def on_stop(self):
        logger.info('goodbye')

def get_tokens(filename):
    config_path = os.path.join(config.project_path, f"testcase/test_belt/ids/stress/{filename}")
    aksk_list=[]

    token_q = queue.Queue()
    if os.path.exists(config_path):
        aksk_list = utils.read_csv(config_path)
        for line in aksk_list:
            token =  sign_utils.encode_jwt_token_pt(line[0].strip(), line[1].strip())
            logger.info(f'token:{token}')
            token_q.put_nowait(token)
    return token_q        

class User(HttpUser):
    host = 'https://ids.test.sensebelt.net'
    tasks = [ApiTask]
    filename = "aksk_test.csv"
    queue_token = get_tokens(filename)

if __name__ == '__main__':
    pass