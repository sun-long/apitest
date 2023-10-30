import base64
import hashlib
from Cryptodome import Random
from Cryptodome.Cipher import AES
import json

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        # self.key = hashlib.sha256(key.encode()).digest()
        self.key = key

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        self.key=bytes(self.key, encoding='utf-8')        
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        byte_data=iv + cipher.encrypt(raw.encode())
        return str(base64.b64encode(byte_data),encoding="utf-8")

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

if __name__=='__main__':
    cryptor = AESCipher("12345678876543211234567887654321")
    image_data = open("/Users/weishuting/code/gitlab.sz.sensetime.com/cloud/apitest/image/ocr/idcard/normal/idcard_front_03.jpg", "rb").read()
    jstr={"image":str(image_data)}
    txt = json.dumps(jstr)

    cypher = cryptor.encrypt(txt)
    print(cypher)

    print(cryptor.decrypt(cypher))