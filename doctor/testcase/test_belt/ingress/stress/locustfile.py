import urllib3
urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser
from locust.clients import ResponseContextManager
from locust.runners import logger
import requests
from core import toml_utils
from defines.nebula_final.edge_service_business import EdgeSwaggerBusiness


class ApiTask(TaskSet):

    # @task
    # def listPortraitDbs(self):
    #     interf = self.user.edgeApi.Portraits_ListPortraitDbsGetApi(sendRequest=False)
    #     with self.client.get(interf.path, headers=interf.headers, verify=False, catch_response=True) as res:
    #         res: ResponseContextManager
    #         if res.status_code != 200:
    #             res.failure(res.text)

    #测试的时候找子木模拟一个接口
    @task
    def listPortraitDbs(self):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..q_GAmT5-4BvxpgPigEnKQV8tS17wHbbz9bnzXtRcGLE"
        header = {"Authorization": "bearer %s" % token}
        url="待定"
        data="待定"

        with self.client.post(url, data=data, headers=header, verify=False, catch_response=True) as res:
             res: ResponseContextManager
             if res.status_code != 200:
                 res.failure(res.text)


    def on_start(self):
        logger.info('hello')

    def on_stop(self):
        logger.info('goodbye')

class User(HttpUser):
    host = 'https://10.151.5.205:5043'
    config_obj = toml_utils.gen_config_obj("nebula_dev")
    edgeApi = EdgeSwaggerBusiness(host, config_obj=config_obj, ext_info=None)
    edgeApi.freshToken()
    tasks = [ApiTask, ]

if __name__ == '__main__':
    pass