import urllib3
urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser
from locust.clients import ResponseContextManager
from locust.runners import logger
import json

path="D:\\CRD\\testdata\\406\\testdata1"


body_list = [
    {"name": "古聪灵", "idnumber": "510107199109021296"},
    {"name": "黎骕", "idnumber": "430503199010230510"},
    {"name": "袁卓", "idnumber": "430981198409127714"},
]

class ApiTask(TaskSet):

    @task
    def my_task(self):
        url = "/validity/idnumber_verification"
        headers = {
                "Authorization": "key=c129e5f8af054b2e9c1cb4b324da660c,timestamp=1673492953483,nonce=3487897D3F9349FD84B9B12119488F7A,signature=cd74fdaa4308646d6a2dec74519b80e4a91ee955785de35149fc970323b7a95b",
            }
        body={"name": "古聪灵", "idnumber": "510107199109021296"}
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
    host = 'https://v2-auth-api.visioncloudapi.com'
    min_wait = 10000
    max_wait = 10000    
    tasks = [ApiTask]

if __name__ == '__main__':
    pass