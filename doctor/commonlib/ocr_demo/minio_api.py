#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   minio_api.py
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/14 下午2:27   wangan      1.0         None
'''
import json
import time
import requests
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class MinioApi(object):
    """ 端业务测api"""
    def __init__(self, host):
        super(MinioApi, self).__init__()
        self._host = host

    @property
    def host(self):
        return self._host

    @property
    def token(self):
        token = self.loginApi()
        return token

    @property
    def user_agent(self):
        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"

    @staticmethod
    def log(msg, level="INFO", end=None):
        """　simple log for job　"""
        if end:
            print("[%-10s%s] %s" % (level, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg), end=end)
        else:
            print("[%-10s%s] %s" % (level, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))

    #登录minio拿到token
    def loginApi(self, ak="minio", sk="BGnr7REn"):
        """ 登陆"""
        path = "/minio/webrpc"
        url = self.host + path
        data = {"id": 1,
                "jsonrpc": "2.0",
                "params":
                    {"username": ak,
                     "password": sk},
                "method": "Web.Login"}
        header = {"User-Agent": self.user_agent}
        r = requests.post(url, json=data, headers=header, verify=False)
        resp_json = r.json()
        return resp_json["result"]["token"]

    def downloadImage(self, resource_path, save_path):
        path = "/%s?token=%s" % (resource_path, self.token)
        url = self.host + path
        header = {
            "User-Agent": self.user_agent}
        r = requests.get(url, headers=header, verify=False)
        with open(save_path, 'wb') as f:
            f.write(r.content)
        self.log("[SUCCESS]download finish. path:%s" % save_path)

    def download(self, data, save_path):
        path = "/minio/zip?token=%s" % self.token
        url = self.host + path
        header = {
            "User-Agent": self.user_agent}
        r = requests.post(url, json=data, headers=header, verify=False)
        with open(save_path, 'wb') as f:
            f.write(r.content)
        self.log("[SUCCESS]download finish. path:%s" % save_path)

    def downloadBigFile(self, data, save_path):
        self.log("downloading...")
        path = "/minio/zip?token=%s" % self.token
        url = self.host + path
        header = {
            "User-Agent": self.user_agent}
        start_time = time.time()
        with requests.post(url, json=data, headers=header, verify=False, stream=True) as r:
            # size = r.headers.get('Content-Length')  # 返回内容有多少字节
            # print(size)
            with open(save_path, 'wb') as file:
                j = 1  #
                # b = round(int(size) / (1024 * 1024), 3)  # 总文件大小 字节转成MB单位，并保留3位小数
                for i in r.iter_content(chunk_size=1024*4):  # 将所有的字节以 1024字节 分开，每次循环下载1kb（1024字节）
                    file.write(i)
                    print('\b' * 40, end='')
                    a = j * 1024 * 4 / (1024 * 1024)  # 已下载文件大小 字节转成MB单位，并保留3位小数
                    if a <= 1024:
                        print("%s MB Speed: %s MB/s" % (round(a, 3), round(j*4/(1024*(time.time()-start_time)), 2)), end='')  # 下载百分比格式
                    else:
                        print("%s MB Speed: %s MB/s" % (round(a/1024, 3), round(j*4/(1024*(time.time()-start_time)), 2)), end='')  # 下载百分比格式
                    j += 1
        print(' =========下载完成=========')

    def downOneFile(self, data, save_path):
        # self.log('%s\n --->>>\n  %s' % (srcUrl, localFile))
        path = "/minio/zip?token=%s" % self.token
        url = self.host + path
        header = {
            "User-Agent": self.user_agent}
        startTime = time.time()
        with requests.post(url, json=data, headers=header, verify=False) as r:
            contentLength = int(r.headers['content-length'])
            line = 'content-length: %dB/ %.2fKB/ %.2fMB'
            line = line % (contentLength, contentLength / 1024, contentLength / 1024 / 1024)
            print(line)
            downSize = 0
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(8192):
                    if chunk:
                        f.write(chunk)
                    downSize += len(chunk)
                    line = '%d KB/s - %.2f MB， 共 %.2f MB'
                    line = line % (downSize / 1024 / (time.time() - startTime), downSize / 1024 / 1024, contentLength / 1024 / 1024)
                    print(line, end='\r')
                    if downSize >= contentLength:
                        break
        timeCost = time.time() - startTime
        line = '共耗时: %.2f s, 平均速度: %.2f KB/s'
        line = line % (timeCost, downSize / 1024 / timeCost)
        self.log(line)

    def upload(self, upload_path, local_path):
        self.log("uploading...")
        path = "/minio/upload/%s" % upload_path
        url = self.host + path
        header = {
            "Authorization": "Bearer %s" % self.token,
            "User-Agent": self.user_agent}
        r = requests.put(url, data=open(local_path, 'rb'), headers=header, verify=False)
        if r.reason == 'OK':
            self.log("[SUCCESS]upload finish. upload_path:%s" % upload_path)
        else:
            self.log("[ERROR]upload failed. reason:%s" % r.reason)


class PrivateMinioApi(MinioApi):
    def __init__(self):
        host = "http://10.4.7.29:55577"
        super(PrivateMinioApi, self).__init__(host)

def backData(origin_host, target_host=None, data=None):
    try:
        MinioApi.log("start: %s" % json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False))
        MinioApi.log("origin host:%s" % origin_host)
        if target_host:
            MinioApi.log("target_host host:%s" % target_host)
        MinioApi(host=origin_host).downOneFile(data["data"], data["save_path"])
        if "upload_path" in data:
            MinioApi(host=target_host).upload(data["upload_path"], data["save_path"])
        MinioApi.log("finish!")
    except Exception as e:
        MinioApi.log("Error:%s" % str(e))

def backZhanDian(origin_host, target_host, upload_dir, zhandian_id_list):
    """ 备份完整站点"""
    for zhandian_id in zhandian_id_list:
        data = {
                "data": {"bucketName": "test", "prefix": "", "objects": ["%s/" % zhandian_id]},
                "save_path": "%s.zip" % zhandian_id,
                "upload_path": "%s/%s.zip" % (upload_dir, zhandian_id)
        }
        backData(origin_host, target_host, data)

def downloadImage(host, algo_path, output_dir=None):
    if not output_dir:
        domain = host.split("//")[-1]
        output_dir = "output/%s" % domain
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    bucketName = algo_path.split("/")[0]
    prefix = "/".join(algo_path.split("/")[1:-1])
    image_name = algo_path.split("/")[-1]
    data_list = [
        {
            "data": {
                "bucketName": bucketName,
                "prefix": "%s" % prefix,
                "objects": [image_name]
            },
            "save_path": "%s/%s" % (output_dir, image_name),
        },
    ]
    for data in data_list:
        backData(host, target_host=None, data=data)

if __name__ == '__main__':
    origin_host = "http://10.10.18.54:33859"

    resource_path = "minio/fell-detective/v1.0.0/account1/5bc037662804414f8e770ea8e7b68884/4ae40c1d-4821-46b4-bc5f-31ad75a10ab0/2022/11/26/20221126-89704434-0a580af4a8f5-00000006-001dbafc"
    output_dir = "/home/SENSETIME/wangan/belt/alarm_images"
    save_path = "%s/%s" % (output_dir, "1.jpeg")
    MinioApi(host=origin_host).downloadImage(resource_path, save_path)