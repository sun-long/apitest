import urllib3
urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser
from locust.clients import ResponseContextManager
from locust.runners import logger
import requests
from core import toml_utils
from defines.nebula_final.edge_service_business import EdgeSwaggerBusiness


class ApiTask(TaskSet):

    #测试的时候找子木模拟一个接口
    @task
    def getBaidu(self):
        url = "https://www.baidu.com/"
        #把client.get的返回值作为res存起来
        with self.client.get(url, verify=False, catch_response=True) as res:
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
    host = 'https://www.baidu.com/'
    tasks = [ApiTask, ]

if __name__ == '__main__':
    pass