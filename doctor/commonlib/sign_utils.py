#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sign_utils.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/26 下午4:18   wangan      1.0         None
'''
import base64
import hashlib
import random
import time
import datetime
import hmac
import jwt


def getTime(offset=0):
    ts = int(time.mktime(datetime.datetime.now().timetuple()))
    if offset != 0:
        ts += offset
    return ts


def getUuid(_len=32):
    # _list = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
    _list = "abcdef0123456789"
    return "".join([_list[random.randint(0, len(_list) - 1)] for _ in range(_len)])


def getMd5(origin):
    """ 获取MD5"""
    m2 = hashlib.md5()
    m2.update(origin.encode("utf8"))
    return m2.hexdigest()


def getMd5ByFile(file_path):
    """ 获取MD5"""
    with open(file_path, 'rb') as fp:
        data = fp.read()

    m2 = hashlib.md5()
    m2.update(data)
    return base64.b64encode(m2.digest())


def base64Encode(js):
    """ 字符串转base64"""
    return base64.urlsafe_b64encode(js).replace(b"=", b"")


def base64Decode(bs):
    """ base64转字节"""
    rem = len(bs) % 4  # 取余
    if rem > 0:
        bs += b'=' * (4 - rem)

    return base64.urlsafe_b64decode(bs)


def genAuthSignByActionConfigKey(action, ts=None, config_key="SENSETIME_CLOUD"):
    """生成auth的签名    """
    if ts is None:
        ts = getTime()
    if not action.startswith("/"):
        action = "/%s" % action
    src = action + str(ts) + config_key
    print(src)
    m2 = hashlib.md5()
    m2.update(src.encode("utf8"))
    return m2.hexdigest(), str(ts)


def genTokenSignByActionSk(action, sk, ts=None):
    """生成auth的签名    """
    if ts is None:
        ts = getTime()
    if not action.startswith("/"):
        action = "/%s" % action
    src = action + str(ts) + sk
    print(src)
    m2 = hashlib.md5()
    m2.update(src.encode("utf8"))
    return m2.hexdigest(), str(ts)


def genAuthSignByAkSk(ak, sk, ts=None, nonce=None):
    if ts is None:
        ts = getTime()
    if nonce is None:
        nonce = getUuid()
    _list = [ak, nonce, str(ts)]
    _list.sort()
    src = "".join(_list)
    # 第一个参数是密钥key，第二个参数是待加密的字符串，第三个参数是hash函数
    mac = hmac.new(sk.encode("utf8"), src.encode("utf8"), hashlib.sha256)
    # print(mac.digest())  # 打印出字符串的ascii格式
    return mac.hexdigest(), str(ts), nonce

# 通过ak,sk生成token
def encode_jwt_token(ak, sk, allowaccess=None):
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }
    payload = {
        "iss": ak,
        # "exp": int(time.time()) + 43200 * 2 *24 *2,  # 有效期30分钟
        "exp": int(time.time()) + 3600 * 24,  # 有效期30分钟
        # "nbf": int(time.time()) - 5
    }
    if allowaccess:
        payload.update({"allowaccess": allowaccess})
    token = jwt.encode(payload, sk, headers=headers)
    if isinstance(token, bytes):
        token = token.decode()
    return token

def genAuthSignByAkSkForMinos(ak, sk, expire_at=None):
    """
    header权限校验
    该API每个接口调用时必须传入header,作为权限校验只用。
    生成签名需要的参数
          AK:  租户的AK
          SK: 租户的SK
          expireAt: 过期时间 秒级时间戳
          requestAt: 请求时间
     2. 生成签名:
        md5("{AK},{SK}, {expireAt}, {requestAt}")
     3. Header
        Authorization:  {"expire_at":1635143508,"request_at":1635143448,"signature":"7e8bca7a5f8de5b342385184956e30b4","ak":"98be21bc-aa83-441d-8868-543fa789a67c"}
     4. 校验
        从Header里取出Authorization，解析json字符串，查询SK,然后重新计算 signature
    """
    if not expire_at:
        expire_at = getTime(offset=24 * 60 * 60)
    request_at = getTime()
    _list = (ak, sk, str(expire_at), str(request_at))
    src = ",".join(_list)
    return getMd5(src), expire_at, request_at


# 通过ak,sk生成token
def encode_jwt_token_pt(ak, sk, allowaccess=None):
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }
    payload = {
        "iss": ak,
        "exp": int(time.time()) + 172800,  # 有效期48小时
        "nbf": int(time.time()) - 5
    }
    if allowaccess:
        payload.update({"allowaccess": allowaccess})
    token = jwt.encode(payload, sk, headers=headers)
    if isinstance(token, bytes):
        token = token.decode()
    return token

def decode_jwt_token(token,sk):
    data = None
    try:
        data = jwt.decode(token, sk, algorithms=['HS256'],options={"verify_exp": False,"verify_aud": False})
    except Exception as e:
        print(e)
    return data
    



if __name__ == '__main__':
    # sign, ts, nonce = genAuthSignByAkSk('l1-6de97bac-h038ace5a157', 'e70271be71d0ccad146a246b605e48bf')
    # sign, ts, nonce = genAuthSignByAkSk('l1-f37b7f8c-w0f55aa0948a', 'l1-f37b7f8c-w0f55aa0948a')
    # print("sign=%s" % sign)
    # print("ts=%s" % ts)
    # print("nonce=%s" % nonce)
    # pass
    # print(getMd5("qwer1234"))
    # print(getUuid())
    # print(getUuid())
    # print(getUuid())
    # print(getUuid())
    # print(getUuid())
    # ts = int(time.mktime(datetime.datetime.now().timetuple()))
    # print("ts:%s" % ts)
    # print("sign:%s " % gen_auth_sign("/rest/1.0/internal/auth.createAccount", ts))
    # print("sign:%s " % gen_auth_sign("/rest/1.0/internal/auth.info", ts))
    # print("sign:%s " % gen_auth_sign("/rest/1.0/internal/auth.getInfoByUid", ts))
    # sk = '441354cb5d7877b4ca353d59e2078eec'
    # print("sign:%s " % get_token_sign("/rest/1.0/auth/token.get", ts, sk))

    # info = {
    #     "request_id": "test_request_id",
    #     "error_code": 0,
    #     "ak": "l1-74c97cbd-20401460aa71",
    #     "sk": "aeb2a5a91a6a332171a737be35cbecb9",
    #     "level": 1
    # }
    #
    # print("sign:%s " % gen_auth_2_sign(info["ak"], info["sk"], str(1603702936), nonce="123456"))

    # print(getMd5("App12345678"))
    # print(encode_jwt_token("2JqKQlqGVnZAcSZcynoaa1kTJwa",
    #       "Amg1QCYZztT6gZJWobKixpbzEGqsBXSP"))
    # ak1="2InLRgh3SLjVwMyOCC5GaHUUuCM"
    # sk1="iwNLs3A2NQ9OApQKaqlukl9LTYjhqOFi"
    # ak2="2InLbVxL0781vyePOxav6yLlmXF"
    # sk2="gx6mUgLrMSfP5UpNJibbAlWYD4bPFheL"
    # ak3="2IxBvg7vyj8qlQtRyr3DgsVIFUI"
    # sk3="344Kt8OKFwyOpFXvo18DIHMv97VUuzcg"  
    # ak4="2InN7IwAmep0a04mbPnKn2i0hsn"
    # sk4="bDx7zM6lmtmVVf0CsX8wiaJT6Iukw0gH" 

    # ak5="2IoIhpKyHG3jVofHglTMYwXDfOM"
    # sk5="tbbAtcjwQlWoWdAAAqfbP8IVLW2dNqMF"
    # ak6="2Mobf9c72Vo3aQVoWcaV54JkhCf"
    # sk6="Xp6EINE1YQIrqCEN0yzo7zMbH2odsVmA"
    

    # ak = "2Ix9mhYJzbvMBuSKtEPCEfhRld8" #15011263680
    # sk = "kk3zYlNXpr5MdxdWQP8YUAji1Gah2a6h"
    # ak = "2N8CSUQC0NIdpIcnXZhQpSDBj42" #15011263680
    # sk = "1RB0HG8Fh0EPl1urQKEmGTdj9N9cTmLa"

    # ak = "2N8V349Dqtls7HE5ioZFq8OQxYq"
    # sk = "tm0FRuFPYRjfbgUBUnd5xNAOKbRLnRPn" 

    # ak = "2NJmcI5M36pYjyIefyq9PIBIfML" #15011263680
    # sk = "kFh0Dhvw90Kz8Z8KZRgMbEMP0TBbUgiY"
   
    # ak = "2JnWk8or7JuJqtBr3MthdJxCdfL"
    # sk = "XXIF0I3kUSSJR88NMgKsno4nAzPitUvS"
    ak="naidvezDyrelAdNaifMyHyitCyshobHa"
    sk="2371d3f1d1eb4eb5a5ad9c8dac0d02cc"
    # ak = "2NP9CvquOgCGP9tM1pHC7nHY5DN"
    # sk = "cexPS8gSplWTJ9LjJgKOG8zz7l9QJxrE"

    # ak="2NPBJBsve5zRdrSD2d9MPotmSyB"
    # sk="Omzq2pjWN8aCu0zm4E3HUztkrpz3B1Zm"

    # ak="2NPD6iRi1dGPupZiZtt6W7bUurL"
    # sk="ijKEPxcwKSe3qlN1joTC3E7lrJWv3HEa"
    # ak="2OXzMGrVjTWMtbwYlM6L3avxswt"
    # sk="D7Tba3EpuweR69R2UBF38yG4BtTj9Hut"
    # ak="2PgY7UwEPk9yJxfpS8lmw7fh7UG"
    # sk="LMbQLhr7DBziNZLWBDM9v8MGepMUo15w"
    # ak = "2PdikkghZm9pA4ITFY3YrvhQpya"
    # sk = "ltMiPwCtz0d5e1XakOlnlLOHO0kX8gil"
    # ak = "2OXzMGrVjTWMtbwYlM6L3avxswt"
    # sk = "D7Tba3EpuweR69R2UBF38yG4BtTj9Hut"
    # ak = "2OXzMGrVjTWMtbwYlM6L3avxswt"
    # sk = "D7Tba3EpuweR69R2UBF38yG4BtTj9Hut"
    token=encode_jwt_token(ak,sk)
    print (token)
    # biz_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJmNTA3NDI4NS1jZjFjLTQ1NzQtODkwYi0wNWYwMDJiYzBkMjYiLCJleHAiOjE2ODk3Mzc1MjEsImlzcyI6IjJNTUxtbHo1cWxrS0lmUWx3Rmg2Tm5wZ3BBWSIsIm5iZiI6MTY4OTczNjYyMSwic2lkIjoiSExJMlNtMVB4Z053bmtVd2V0bEZVRDZGcVFpemZ3TWsxTlRHIiwidXJsIjpbIkg1R2V0U2Vzc2lvbkNvbmZpZyIsIkludGVyYWN0aXZlTGl2ZW5lc3MiXX0.P9UlWG4sy62Pv5wfM1ayHNd_OkodUQXK47ZmJlnddMY"
    # biz_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI3NmYwMDMxYy1mMjI2LTRkMWUtYmNhYS01YWQ5NjY5ZmJkMWYiLCJleHAiOjE2ODk3Mzk3MDEsImlzcyI6IjJNTUxtbHo1cWxrS0lmUWx3Rmg2Tm5wZ3BBWSIsIm5iZiI6MTY4OTczODgwMSwic2lkIjoiSExJMlNtNXB3UGJlZ3BJSEZ4ZFJKcHVqYkpSR2Z6TWsxTlRHIiwidXJsIjpbIkg1R2V0U2Vzc2lvbkNvbmZpZyIsIkludGVyYWN0aXZlTGl2ZW5lc3MiXX0.bAZWWHppv8CNV9cD-ZMb0QExnTENqzs6XPDOlV_4Vsk"
    # biz_token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIiLCJleHAiOjE2ODk3NDA5MTEsImlzcyI6IjJNTUxtbHo1cWxrS0lmUWx3Rmg2Tm5wZ3BBWSIsIm5iZiI6MTY4OTc0MDAxMSwic2lkIjoiSElEMlNtOEh4TGNVYXM1QzV5UUhQSER6d0tDMTNoTWsxTlRHIiwidXJsIjpbIkg1R2V0U2Vzc2lvbkNvbmZpZyIsIkg1T0NSSURDYXJkIiwiSDVVcGRhdGVJRENhcmQiLCJJbnRlcmFjdGl2ZUxpdmVuZXNzIiwiU2NhbkNhcmQiXX0.tRibhNJ1X5C7Smo-aN5DYmBA5v9zEs9raCEL6CTGLQU"
    # sk = "IHK8ZlTVxa9vx35N7LFbxM0aMYhL3AR2"
    # decode_jwt_token(biz_token,sk)

