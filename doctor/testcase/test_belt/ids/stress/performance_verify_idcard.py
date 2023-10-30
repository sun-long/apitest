import urllib3
urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser
from locust.clients import ResponseContextManager
from locust.runners import logger
import json

path="D:\\CRD\\testdata\\406\\testdata1"


body_list = [
    {"name": "古聪灵", "idcard_number": "510107199109021296"},
    {"name": "黎骕", "idcard_number": "430503199010230510"},
    {"name": "袁卓", "idcard_number": "430981198409127714"},
]

class ApiTask(TaskSet):

    @task
    def my_task(self):
        url = "/identity"
        headers = {
            "X-Belt-Action": "VerifyIDCard",
            "X-Request-ID": "test",
            "X-Belt-Signature": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIyT0R3aW5SbUh1SWlCYTBaclBRZzVFYlpEeUgiLCJleHAiOjE2ODExNTE5ODQsIm5iZiI6MTY4MTEwODc3OX0.HYahX95-I42Hl4AttcfLL3JV4fYN9qYrbMYYw8kvjSo",
            "X-Belt-Version": "v1"
        }
        for body in body_list:
            body_str=json.dumps(body)
            
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
    host = 'https://ids.test.sensebelt.net'
    min_wait = 10000
    max_wait = 10000    
    tasks = [ApiTask]

if __name__ == '__main__':
    pass