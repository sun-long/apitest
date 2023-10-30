import base64
import requests
import datetime
import hmac
import hashlib
# HAMC 加密解算
def get_sha256(AK, SK):
    if AK and SK == "":
        return "1", "1"
    else:
        AK_ID = AK
        AK_SECRET = SK
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
        # dd = datetime.datetime.utcnow().strftime(GMT_FORMAT)
        dd = datetime.datetime.now().strftime(GMT_FORMAT)
        date_str = f"date: {dd}"
        key = AK_SECRET.encode('utf-8')  # sha256加密的key
        message = date_str.encode('utf-8')  # 待sha256加密的内容
        sign = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()
        Authorization = f'hmac username="{AK_ID}", algorithm="hmac-sha256", headers="date", signature="{sign}"'
        return dd, Authorization

def iamToken(ak, sk):
    """ iam鉴权"""
    return get_sha256(ak, sk)

def authToken(ak, sk, host):
    """ auth鉴权"""
    url = "%s/openapi/v2/user-management/openapi/v2/auth/access-token" % host
    data = {
      "ak": ak,
      "sk": sk
    }
    resp = requests.post(url, json=data, verify=False)
    accessToken = resp.json()["data"]["accessToken"]
    return accessToken


if __name__ == '__main__':
    # pre
    # ak = "64351850679dd97ec930da34"
    # sk = "88c1b5f64af3e8e74b029f356b719781"
    # host = "https://sensegalaxy-pre-release.sensetime.com"
    # test
    ak = "0001591d-bc97-4ced-96b6-e60f9c541d84"
    sk = "zgR5HXdytYIvHPLnRLOuoVooYOvUVwnx"
    host = "https://sensegalaxy-test.sensetime.com"
    token = authToken(ak, sk, host)
    print(token)

    # dd, Authorization = iamToken(ak, sk)
    # print(dd)
    # print(Authorization)


