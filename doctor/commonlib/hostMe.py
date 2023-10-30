#!/usr/bin/python3
import http.server
import json
import os
import sys
import time

MsgPath = '/home/SENSETIME/wangan/belt/msg'

def dezhuanyi(_str):
    """"""
    return json.loads(_str)

def save_json(data, save_path):
    data = json.dumps(data, sort_keys=True, indent=2)
    with open(save_path, 'w') as f:
        f.write(data)
    print("文件写入成功.path:%s" % save_path)

class RequestHandlerImpl(http.server.BaseHTTPRequestHandler):
    """
    自定义一个 HTTP 请求处理器
    """
    
    def do_GET(self):
        """
        处理 GET 请求, 处理其他请求需实现对应的 do_XXX() 方法
        """
        # print(self.server)                # HTTPServer 实例
        # print(self.client_address)        # 客户端地址和端口: (host, port)
        # print(self.requestline)           # 请求行, 例如: "GET / HTTP/1.1"
        # print(self.command)               # 请求方法, "GET"/"POST"等
        # print(self.path)                  # 请求路径, Host 后面部分
        # print(self.headers)               # 请求头, 通过 headers["header_name"] 获取值
        # self.rfile                        # 请求输入流
        # self.wfile                        # 响应输出流

        # 1. 发送响应code
        self.send_response(200)

        # 2. 发送响应头
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        # 3. 发送响应内容（此处流不需要关闭）
        self.wfile.write("Hello World\n".encode("utf-8"))

    def do_POST(self):
        """
        处理 POST 请求
        """
        received_time = int(time.time())
        # 0. 获取请求Body中的内容（需要指定读取长度, 不指定会阻塞）
        req_body = self.rfile.read(int(self.headers["Content-Length"])).decode()

        print("req_body: \n" + req_body)
        if "data" in req_body:
            try:
                t1 = time.time()
                data = dezhuanyi(req_body)
                # data = dezhuanyi(data['data'])
                # data_value = dezhuanyi(data['task']["data"]["value"])
                # data['task']["data"]["value"] = data_value
                task_name = data['assignmentid']
                task_dir = "%s/%s" % (MsgPath, task_name)
                creation_time = data['creation_time']
                if not os.path.exists(task_dir):
                    os.makedirs(task_dir)
                save_path = os.path.join(task_dir, "%s.json" % creation_time)
                data["receive_time"] = received_time
                save_json(data, save_path)
                print("delay:%s" % (round(time.time() - t1, 2)))
            except Exception as e:
                print("error:%s" % str(e))

        # 1. 发送响应code
        self.send_response(200)

        # 2. 发送响应头
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        # 3. 发送响应内容（此处流不需要关闭）
        self.wfile.write(("Hello World").encode("utf-8"))


server_address = ("", 9999)

httpd = http.server.HTTPServer(server_address, RequestHandlerImpl)

httpd.serve_forever()

