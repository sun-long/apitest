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
    # @task
    # def getIngress(self):
    #     url = "http://crd-test.sensetime.com/ras"
    #     headers = {
    #         "X-Belt-Action": "TestGet",
    #         "X-Request-ID": "test1",
    #         "X-Belt-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJhbGxvd2FjY2VzcyI6WyJUZXN0UG9zdCIsIlRlc3RHZXQiXX0=.VSvZposkmq7CvE9U4dbyqG5vwllH9gkexu034I6NBlc",
    #         "X-Belt-Version": "v1"
    #     }
    #     #把client.get的返回值作为res存起来
    #     with self.client.get(url=url, verify=False, headers=headers,catch_response=True) as res:
    #         #表示这个res是一个ResponseContextManager类型，他就可以用里面的一些方法了
    #          res: ResponseContextManager
    #         #这里可以写一些逻辑，例如返回值不等于200,或者返回结果里报错了等等
    #          if res.status_code != 200:
    #              #将失败的请求写入到failure里，供前端页面展示
    #              res.failure(res.text)

    # @task
    # def postIngress(self):
    #     url = "http://crd-test.sensetime.com/ras"
    #     headers = {
    #         "X-Belt-Action": "TestPost",
    #         "X-Request-ID": "test1",
    #         "X-Belt-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJhbGxvd2FjY2VzcyI6WyJUZXN0UG9zdCJdfQo=.VSvZposkmq7CvE9U4dbyqG5vwllH9gkexu034I6NBlc",
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

    # 集成环境
    # 集成环境
    @task
    def getIngress(self):
        url = "https://ras.sensebelt.com/FallDetection?paging.offset=0&paging.limit=100000&verbose=True"
        headers = {
            "X-Belt-Action": "ListFallDetectionAssignments",
            "X-Belt-Signature": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyTjVkOG8wMzFqeDBRcVVtWkQwYzJMUU5UODUiLCJleHAiOjE2Nzk0MzI2MzUsIm5iZiI6MTY3OTM4OTQzMH0.IdQBxno-0vEkBOiB0OFG3aEUNYvHs6px7g0Ln6dcsn8",
            "X-Belt-Version": "v1"
        }
        #把client.get的返回值作为res存起来
        with self.client.get(url=url, verify=False, headers=headers,catch_response=True) as res:
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
    host = 'https://alb-dcc-center-1-cn-shanghai-1.test-sensebelt.com/ras'
    tasks = [ApiTask, ]

if __name__ == '__main__':
    pass