import urllib3
urllib3.disable_warnings()
from locust import TaskSet, task, HttpUser
from locust.clients import ResponseContextManager
from locust.runners import logger
import base64
import json
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

path="/Users/weishuting/Downloads/testdata"


api_key = "4ef1630905344248811f2c8760ec9cea"
api_secret = "02ae388741de4f499b814ab34a51743a"

def aes_256_cbc_encrypt(data, key, iv):
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8')[:16])
        ciphertext = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        return base64.b64encode(ciphertext).decode('utf-8')


class ApiTask(TaskSet):

    @task
    def my_task(self):
        url = "/identity/idnumber_verification/stateless"
        headers = {
                "Authorization": "key=4ef1630905344248811f2c8760ec9cea,timestamp=1680835810987,nonce=e9e9cb65d4ee11ed8ae9309c235f64ef,signature=9ab0e61de3028ad3890f75fba2855123d0422c8676b751f031e2a1767957af46",
                # "Encrypted": True
            }
        for file in os.listdir(path):
            print(file)
            image_path = os.path.join(path, file)
            with open(image_path, 'rb') as f:
                    image_content = f.read()
                    image_base64 = base64.b64encode(image_content).decode("utf-8")
                    
            if file.startswith("gucongling_"):
                body = {
                    "name": "古聪灵",
                    "idnumber": "510107199109021296",
                    "image": image_base64,
                }
                # body = {
                #     "name": aes_256_cbc_encrypt("古聪灵", api_key , api_secret), # => pHo410+lumhbYvavFBnCsA==
                #     "idnumber": aes_256_cbc_encrypt("510107199109021296", api_key, api_secret) # => XYde2/2HzLIviVU8WzP9lbh7RpjLiP2/EqjlzmqWmEk=
                # }

            elif file.startswith("lixiao_"):          
                body = {
                    "name": "黎骕",
                    "idnumber": "430503199010230510",
                    "image": image_base64,
                }
                # body = {
                #     "name": aes_256_cbc_encrypt("黎骕", api_key , api_secret), # => pHo410+lumhbYvavFBnCsA==
                #     "idnumber": aes_256_cbc_encrypt("430503199010230510", api_key, api_secret) # => XYde2/2HzLIviVU8WzP9lbh7RpjLiP2/EqjlzmqWmEk=
                # }
            else:
                body = {
                    "name": "袁卓",
                    "idnumber": "430981198409127714",
                    "image": image_base64,
                }
                # body = {
                #     "name": aes_256_cbc_encrypt("袁卓", api_key , api_secret), # => pHo410+lumhbYvavFBnCsA==
                #     "idnumber": aes_256_cbc_encrypt("430981198409127714", api_key, api_secret) # => XYde2/2HzLIviVU8WzP9lbh7RpjLiP2/EqjlzmqWmEk=
                # }
                
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