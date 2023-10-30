import base64
import json


def base64Encode(js):
    """ 字符串转base64"""
    return base64.urlsafe_b64encode(js).replace(b"=", b"")


def base64Decode(bs):
    """ base64转字节"""
    rem = len(bs) % 4  # 取余
    if rem > 0:
        bs += b'=' * (4 - rem)

    return base64.urlsafe_b64decode(bs)

payload={"allowaccess": ["getface"],"iat": 1516239022,"sub": "1234567890","name":"John Doe"}
payload_json=json.dumps(payload, separators=(',', ':'), sort_keys=True)
print(base64Encode(payload_json.encode()))