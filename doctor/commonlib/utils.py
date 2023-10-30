#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import csv
import datetime
import os
import json
import codecs
import shutil
import smtplib
import types
import re
import requests
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import yaml

from commonlib import config, time_utils
from commonlib.log_utils import log

filepath = os.path.realpath(__file__)
reportname = os.path.split(filepath)
CFpath = reportname[0]

import struct

CURRENT_LOG_PATH = None



def get_video_duration(video_file):
    """ 获取视频时长"""
    with open(video_file, 'rb') as fp:
        data = fp.read()

    index = data.find(b'mvhd') + 4
    time_scale = struct.unpack('>I', data[index + 13:index + 13 + 4])
    durations = struct.unpack('>I', data[index + 13 + 4:index + 13 + 4 + 4])
    duration = durations[0] / time_scale[0]
    return duration

def download_file(url, target_path, cookie=None):
    """ 下载文件"""
    # 把下载地址发送给requests模块
    if cookie:
        f = requests.get(url, headers={"cookie": cookie})
    else:
        f = requests.get(url)
    # 下载文件
    with open(target_path, "wb") as code:
        code.write(f.content)

def upload_file(url, file_path, headers=None):
    """ 上传文件"""
    if not headers:
        headers = {
            'Content-Type': 'application/json'
        }
    # files = {'file': open(file_path, 'rb')}
    with open(file_path, 'rb') as payload:
        response = requests.put(url, data=payload, headers=headers)
        # response = requests.put(url, files=files, headers=headers)
    return response

def read_file(url):
    """ 下载文件"""
    # 把下载地址发送给requests模块
    f = requests.get(url)
    return f.text

def zhuanyi(data):
    """"""
    return json.dumps(data)

def dezhuanyi(_str):
    """"""
    return json.loads(_str)

def read_post_data_yaml(path):
    """ 读取yaml文件"""
    if not path.startswith("/"):
        if not path.endswith('.yaml'):
            path = "%s.yaml" % path
        path = os.path.join(config.project_path, "data/post_data_conf", path)
    if not os.path.isfile(path):
        raise Exception('%s 不存在' % path)
    return read_yaml(path)


def read_contract(contract_path):
    if not contract_path.startswith("/"):
        contract_path = os.path.join(config.contract_path, contract_path)
    if not os.path.exists(contract_path):
        log().info('contract file is not exist.path:%s' % contract_path)
        return
    obj = None
    try:
        obj = read_yaml(contract_path)
    except:
        log().info('read contract failed.path:%s' % contract_path)
    return obj


def read_csv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        # print(type(reader))
        result = [row for row in reader]
    return result

def read_yaml(path):
    """ 读取yaml文件"""
    with open(path, "r") as f:
        result = yaml.load(f, Loader=yaml.FullLoader)
    return result

def read_temp_json(path):
    """
    :param path:
    :return:
    """
    if not path.startswith("/"):
        path = os.path.join(config.temp_path, path)
    _str = ""
    if os.path.isfile(path):
        with open(path, "r") as f:
            _str = json.load(f)
    return _str

def read_file_json(path):
    """
    :param path:
    :return:
    """
    if not path.startswith("/"):
        path = os.path.join(config.project_path, path)
    res = []
    if os.path.isfile(path):
        with open(path, "r") as f:
            for jsonstr in f.readlines():
                res.append(json.loads(jsonstr))
    return res

def readConfigMap(path, url_prefix, action_name="X-Belt-Action"):
    """ 读取configMap"""
    if not path.startswith("/"):
        path = os.path.join(config.project_path, "data/configmap", path)
    data = None
    try:
        # 打开文件
        with open(path, "r", encoding="utf-8") as f:
            import yaml
            data = yaml.load(f,Loader=yaml.FullLoader)
    except Exception as e:
        raise
    services = data["data"]["kong.yml"]["services"]
    res = {}
    for s in services:
        if url_prefix not in s["url"]:
            continue
        key = s["url"].split(url_prefix)[-1]
        if key not in res:
            res[key] = {}
        for route_info in s["routes"]:
            method = route_info["methods"][0].lower()
            res[key][method] = {
                "paths": route_info["paths"][0],
                "action": route_info["headers"][action_name][0],
                "version": route_info["headers"]['X-Belt-Version'][0] if "X-Belt-Version" in route_info["headers"] else "v1",
            }
    return res


def save_json_file(name, data, add=False):
    """ 保存临时信息"""
    data = json.dumps(data, sort_keys=True, indent=2)
    name = "%s_%s.json" % (name, time_utils.get_time_str())
    write_file(name, data, add=add)

def save_post_data(name, data, save_dir=None):
    """ 保存报文数据"""
    data = json.dumps(data, sort_keys=True, indent=2)
    if not save_dir:
        save_dir = 'post_data'
    post_data_dir = os.path.join(CURRENT_LOG_PATH, save_dir)
    if not os.path.exists(post_data_dir):
        os.makedirs(post_data_dir)
    name = os.path.join(post_data_dir, name)
    write_file(name, data)
    return name

def save_str_data(name, data, save_dir=None):
    """ 保存文本文件"""
    if not save_dir:
        save_dir = 'post_data'
    post_data_dir = os.path.join(CURRENT_LOG_PATH, save_dir)
    if not os.path.exists(post_data_dir):
        os.makedirs(post_data_dir)
    name = os.path.join(post_data_dir, name)
    write_file(name, data)
    return name

def write_file(path, context, delete=True, add=False):
    if not path.startswith("/"):
        path = os.path.join(config.temp_path, path)
    if os.path.isfile(path) and delete:
        os.remove(path)
    _format = 'a' if add else 'w'
    with open(path, _format) as f:
        f.write(context)
    print("文件写入成功.path:%s" % path)

def write_pm_file(path, context, delete=True, add=False):
    if os.path.isfile(path) and delete:
        os.remove(path)
    _format = 'a' if add else 'w'
    with open(path, _format) as f:
        f.write(context)
    log().info("pm文件写入成功.path:%s" % path)

def write_cov_file(path, context, delete=True, add=False):
    if os.path.isfile(path) and delete:
        os.remove(path)
    _format = 'a' if add else 'w'
    with open(path, _format) as f:
        f.write(context)
    log().info("cov文件写入成功.path:%s" % path)

def write_error_file(path, context, delete=True):
    if not path.startswith("/"):
        path = os.path.join(CURRENT_LOG_PATH, 'error_log', '%s.log' % path)
    try:
        if os.path.isfile(path) and delete:
            os.remove(path)
        with open(path, 'w') as f:
            f.write(context)
    except Exception() as e:
        log().info("写错误日志失败：%s" % path)
    # print("文件写入成功.path:%s" % path)


def write_request_file(path, context):
    data = json.dumps(context, sort_keys=True, indent=2)
    if not path.startswith("/"):
        if CURRENT_LOG_PATH:
            path = os.path.join(CURRENT_LOG_PATH, 'request', '%s.postman_collection.json' % path)
        else:
            path = os.path.join(config.project_path, '%s.postman_collection.json' % path)

    write_file(path, data)
    log().info("pm文件生成成功.path:%s" % path)

def replace_special_characters(filename):
    # 定义要替换的特殊字符，这里列出一些示例
    special_characters = r'[|?*]'
    # 替换特殊字符为空格
    new_filename = re.sub(special_characters, '_', filename)
    return new_filename

def write_error_file_in_result(path, context):
    try:
        path = replace_special_characters(path)
        with open("%s.log" % path, 'w') as f:
            f.write(context)
        print("error文件写入成功.path:%s" % path)
    except Exception() as e:
        # print("error文件写入失败.path:%s, %s" % (path, str(e)))
        pass


def write_alaxy_result(path, result):
    result = json.dumps(result, sort_keys=True, indent=2)
    with open(path, 'w') as f:
        f.write(result)
    print("alaxy文件写入成功.path:%s" % path)

def write_request_file_in_result(path, context,result_dir):
    data = json.dumps(context, sort_keys=True, indent=2)
    path = '%s/%s.postman_collection.json' % (result_dir, path)
    write_pm_file(path, data)
    log().info("pm文件生成成功.path:%s" % path)

def get_file_size(file_path, change=True):
    """ 获取文件大小，单位：M/KB
    :param change:
    :param file_path:
    :return:
    """
    # file_path = unicode(file_path, 'utf8')
    file_size = os.path.getsize(file_path)
    if change:
        # file_size = file_size / float(1024 * 1024)
        file_size = file_size / float(1024)
    return round(file_size, 2)


def init_test_dir(pytest_config):
    result_path = pytest_config.option.result_path
    error_path = os.path.join(result_path, "error")
    pm_path = pytest_config.option.pmpath
    if os.path.exists(result_path):
        shutil.rmtree(result_path)
    os.makedirs(result_path)
    os.makedirs(error_path)

    if os.path.exists(pm_path):
        shutil.rmtree(pm_path)
    os.makedirs(pm_path)

def json_check(expect, reality):
    """请求结果的基础校验"""
    global key_num, key_type
    check_ret = True
    key_num, key_type = [], []
    dict_ergodic(expect, reality)
    if key_num:
        log().info("预期结果多出字段%s" % key_num)
        check_ret = False
    if key_type:
        log().info("预期结果的字段类型为%s" % key_type)
        check_ret = False
    key_num, key_type = [], []
    dict_ergodic(reality, expect)
    if key_num:
        log().info("实际结果多出字段%s" % key_num)
        check_ret = False
    if key_type:
        log().info("实际结果的字段类型为%s" % key_type)
        check_ret = False
    return check_ret


def dict_ergodic(a, b):
    """遍历两个字典，比较字段个数、类型"""
    for key in a.keys():
        if key not in b.keys():
            key_num.append((key, a[key]))
        else:
            if not isinstance(a[key], type(b[key])):
                key_type.append((key, a[key], type(a[key])))
            elif isinstance(a[key], dict):
                dict_ergodic(a[key], b[key])



#
# def ssh(ip, user, pw, cmd, port=22):
#     '''连接liunx服务器执行命令
#        :return out （list类型）
#        '''
#     try:
#         ssh = paramiko.SSHClient()
#         # ssh.load_system_host_keys()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(hostname=ip, port=port, username=user, password=pw, timeout=20)
#         stdin, stdout, stderr = ssh.exec_command(cmd)
#         out = stdout.readlines()
#         return out
#     except Exception as e:
#         log().error("ssh_error：" + str(e))
#     finally:
#         ssh.close()


def getdatatodic(data):
    '''http请求转成dict'''
    # t = str(data, encoding="utf-8")
    t = data.decode()
    log().info('http请求：' + t)
    d = t.split('&')
    g = {}
    for i in d:
        j = i.split('=')
        g[j[0]] = j[1]
    log().info('http请求转换dict后:' + str(g))
    return g


def send_mail(sender, psw, receiver, smtpserver, reportfile, port=25):
    '''
    smtp.163.com:25
    smtp.qq.com:465
    '''
    '''发送最新的测试报告内容'''
    # 打开测试报告
    with open(reportfile, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg["from"] = sender
    msg["to"] = receiver
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(reportfile, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def writefile(file_path, mode, data):
    '''w 写  a 追加
    codecs 处理编码'''
    f = codecs.open(file_path, mode, 'utf-8')
    f.write(data)
    f.close()


def write_result(info):
    path = os.path.dirname(os.path.dirname(__file__))
    result_path = os.path.join(path, "result/result.txt")
    with open(result_path, 'a+') as f:
        f.write(info)


def getdistrictcode():
    '''生成区号列表，供生成身份证事使用'''
    path = os.path.join(CFpath, '../tools/districtcode.txt')
    with open(path, encoding='gbk') as file:
        data = file.read()
    districtlist = data.split('\n')
    # print u"districtlist=%s" % districtlist
    global codelist
    codelist = []
    for node in districtlist:
        # print node
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state": state, "city": city, "district": district, "code": code})


def genneratorMobile():
    '''随机生成手机号'''

    # 第二位数字
    second = [3, 5, 7, 8][random.randint(0, 3)]
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 最后八位数字
    suffix = random.randint(9999999, 100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


def genneratorId(howold):
    '''随机生成身份证号'''

    # 生成区号列表
    getdistrictcode()
    # 拼接身份证前17位
    code_city = codelist[random.randint(0, len(codelist))]
    myid = code_city['code']  # 地区项
    city = code_city['city']
    # myid = myid + str(random.randint(1978,1988)) #年份项
    # da  = date.today()+timedelta(days=random.randint(1,366)) #月份和日期项
    birthday = datetime.datetime.now() + datetime.timedelta(days=-(int(howold) * 365 + 20))
    birthday = birthday.strftime("%Y%m%d")
    myid = myid + birthday
    myid = myid + str(random.randint(100, 300))  # ，顺序号简单处理
    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(myid)):
        count = count + int(myid[i]) * weight[i]
    myid = myid + checkcode[str(count % 11)]  # 算出校验码
    return myid


def getName():
    ''' 随机生成中文名 '''
    last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                  '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                  '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

    first_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
                   '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
                   '乾', '坤', '善']
    name_all = random.choice(last_names) + random.choice(first_names) + random.choice(first_names)
    return name_all


def gen_mobile():
    ''' 生成符合风控规则的手机号 '''
    # 前三位数字
    str1 = [
        '130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
        '145', '147', '149',
        '150', '151', '152', '153', '155', '156', '157', '158', '159',
        '165', '166', '167',
        '170', '171', '173', '17400', '17401', '17402', '17403', '17404', '17405', '175', '176', '177', '178',
        '180', '181', '182', '183', '184', '185', '186', '187', '188', '189',
        '191', '198', '199'
    ][random.randint(0, 50)]

    # 后几位数字
    return str1 + "".join(random.choice("0123456789") for i in range(11 - len(str1)))

def get_project_dir():
    '''

    :return: 获取项目根目录
    '''
    log().info( "根目录是：{}".format(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))))
    return  os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def find_file(filename, search_path):
    for dirpath, dirnames, filenames in os.walk(search_path):
        if filename in filenames:
            return os.path.join(dirpath, filename)
    return None

def enctry(s):
    k = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
    encry_str = ""
    for i, j in zip(s, k):
      # i为字符，j为秘钥字符
      temp = str(ord(i)+ord(j))+'_'  # 加密字符 = 字符的Unicode码 + 秘钥的Unicode码
      encry_str = encry_str + temp
    return encry_str

def dectry(p):
    k = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
    dec_str = ""
    for i, j in zip(p.split("_")[:-1], k):
        # i 为加密字符，j为秘钥字符
        temp = chr(int(i) - ord(j))  # 解密字符 = (加密Unicode码字符 - 秘钥字符的Unicode码)的单字节字符
        dec_str = dec_str+temp
    return dec_str

def get_video_duration_cv2(filename):
    import cv2
    cap = cv2.VideoCapture(filename)
    if cap.isOpened():
        for x in range(20):
            print('%s->%s' % (x, cap.get(x)))
        fps = cap.get(cv2.CAP_PROP_FPS)
        # 获取视频总帧数
        frame_all = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        i = frame_all * (-1) / fps
        rate = cap.get(5)
        frame_num = cap.get(7)
        return frame_num/rate
    return -1


def timeConvert(size): # 单位换算
    M, H = 60, 60**2
    if size < M:
        return str(size)+u'秒'
    if size < H:
        return u'%s分钟%s秒'%(int(size/M),int(size%M))
    else:
        hour = int(size/H)
        mine = int(size%H/M)
        second = int(size%H%M)
        tim_srt = u'%s小时%s分钟%s秒'%(hour,mine,second)
        return tim_srt

def get_video_duration_cv3(filename):
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(filename)
    # file_time = timeConvert(clip.duration)
    return clip.duration


def gen_mac_address():
    import random
    Maclist = []
    for i in range(1, 7):
        RANDSTR = "".join(random.sample("0123456789abcdef", 2))
        Maclist.append(RANDSTR)
    RANDMAC = ":".join(Maclist)
    return RANDMAC


def base64ToFile(file_path, base64String):
    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(base64String))
    log().info("%s 写入成功" % file_path)

def json_get(_path, target):
    """ 获取指定路径的数据"""
    name_list = _path.split(".")
    for name in name_list[:-1]:
        if name.isdigit():
            target = target[int(name)]
        else:
            target = target[name]
    if name_list[-1].isdigit():
        res = target[int(name_list[-1])]
    else:
        res = target[name_list[-1]]
    return res




if __name__ == '__main__':
    # duration = get_video_duration_cv2("/home/SENSETIME/wangan/Downloads/argus_short-video_3cfa946d622319e5ba49616bfbaeab608c8ef1fb0cf0c6ac650b8b650151df39.mp4")
    # print(duration)
    print(enctry(""))