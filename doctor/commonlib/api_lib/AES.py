#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   AES.py    
@Contact :   weishuting@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 下午6:52   weishuting      1.0         None
'''
# -*- coding: utf-8 -*-
import base64
import json
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

def get_encrypt_info(key,iv,fields,encrypt_data_src):
    """返回加密信息
    return：{
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": fields,
            "data": encrypt_data
            }
    param:key 为sk
    iv：偏移向量，16位
    fields：编码的字段
    data：编码的数据=base64(iv+加密数据)

    """  
    instance_AESCBCCipher=AESCBCCipher(key,iv)
    encrypt_data_src_string=json.dumps(encrypt_data_src)
    encrypt_data_dst=instance_AESCBCCipher.encrypt(encrypt_data_src_string)
    encrypt_data_dst=str(encrypt_data_dst)
    data_before_base64=iv+encrypt_data_dst
    data=base64.b64encode(data_before_base64)
    encrypt_info={
        "algorithm": "AES_256_CBC",
        "version": 0,
        # "iv": iv,
        "encrypted_fields": fields,
        "data": data
    }
    return encrypt_info  

def get_decrypt_info(key,iv,response):
    data=response["encrypt_info"]["data"]
    instance_AESCBCCipher=AESCBCCipher(key,iv)
    decrypt_data_string=instance_AESCBCCipher.decrypt(data)
    decrypt_data_json=json.loads(decrypt_data_string)
    return decrypt_data_json  
    

class AESCBCCipher(object):
    def __init__(self, key, iv):
        self.key = bytes(key, encoding='utf-8')
        self.iv = bytes(iv, encoding='utf-8')
        self.mode = AES.MODE_CBC
        self.aes_cipher = AES.new(self.key, self.mode, self.iv)

    # def encrypt(self, data=None):
    #     # aes_cipher = AES.new(self.key, self.mode, self.iv)
    #     ciphertext = self.aes_cipher.encrypt(pad(bytes(data, encoding='utf-8'), 16))
    #     # print(str(base64.b64encode(ciphertext), encoding='utf-8'))
    #     return str(base64.b64encode(ciphertext), encoding='utf-8')


    def encrypt(self, data=None):
        ciphertext = self.aes_cipher.encrypt(pad(bytes(data, encoding='utf-8'), 16))
        return ciphertext

    def encrypt_bytes(self, data=None):
        # aes_cipher = AES.new(self.key, self.mode, self.iv)
        ciphertext = self.aes_cipher.encrypt(pad(data, 16))
        # print(str(base64.b64encode(ciphertext), encoding='utf-8'))
        return str(base64.b64encode(ciphertext), encoding='utf-8')

    def decrypt(self, data=None):
        # aes_cipher = AES.new(self.key, self.mode, self.iv)
        bytes_decoded = base64.decodebytes(bytes(data, encoding='utf-8'))
        source_data = unpad(self.aes_cipher.decrypt(bytes_decoded), 16)
        # print(str(source_data, encoding='utf-8'))
        return str(source_data, encoding='utf-8')




class AESGCMCipher(object):
    """
    # help doc:
    # https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book
    # /symmetric-key-ciphers/aes-encrypt-decrypt-examples.html
    """
    def __init__(self, key, nonce):
        """

        :param key: 使用api_key
        :param nonce: 使用api_secret的前12字节
        """
        self.key = bytes(key, encoding='utf-8')
        self.nonce = bytes(nonce, encoding='utf-8')
        self.mode = AES.MODE_GCM

    def encrypt(self, msg):
        aes_cipher = AES.new(key=self.key, mode=self.mode, nonce=self.nonce)
        if type(msg) == str:
            cipher_text, authTag = aes_cipher.encrypt_and_digest(bytes(msg, encoding="utf-8"))
            return (cipher_text, aes_cipher.nonce, authTag)
        elif type(msg) == bytes:
            cipher_text, authTag = aes_cipher.encrypt_and_digest(msg)
            return (cipher_text, aes_cipher.nonce, authTag)

    def decrypt(self, encrypted_msg):
        (cipher_text, authTag) = (encrypted_msg[:-16], encrypted_msg[-16:])
        # "decrypt() can only be called after initialization or an update()" 故不可以使用self.aes_cipher
        aes_cipher = AES.new(key=self.key, mode=self.mode, nonce=self.nonce)
        plaintext = aes_cipher.decrypt_and_verify(cipher_text, authTag)
        return str(plaintext, encoding="utf-8")


if __name__ == '__main__':
    # pass
    # AES-256-CBC demo
    # senseid_conf = SenseIdConfig("dev.ini")
    # cipher = AESCBCCipher(senseid_conf.get('AES', 'key'), senseid_conf.get('AES', 'iv')[0:16])
    cipher = AESCBCCipher('1b62d5a411604437bbc0905a05563a4e', '1b62d5a411604437bbc0905a05563a4e'[0:16])
    # data = '310108199310291537'
    data={ "image":"1234567890"}
    data_str=json.dumps(data)
    data_dict=json.loads(data_str)
    encrypted_string = cipher.encrypt(data_str)
    print(encrypted_string)

    decrypted_string = cipher.decrypt(encrypted_string)

    print(decrypted_string)
    decrypted_dict=json.loads(decrypted_string)
    print(decrypted_dict)
    # AES-256-GCM demo
    # senseid_conf = SenseIdConfig("dev.ini")
    # cipher = AESGCMCipher(senseid_conf.get('AES', 'key'), senseid_conf.get('AES', 'iv')[0:12])
    # message = "hello world"
    # encrypted_message = cipher.encrypt(message)
    # print("encrypted_message", {
    #     'ciphertext': binascii.hexlify(encrypted_message[0]),
    #     'base64 ciphertext': str(base64.b64encode(encrypted_message[0]+encrypted_message[2])),
    #     'aesIV': binascii.hexlify(encrypted_message[1]),
    #     'authTag': binascii.hexlify(encrypted_message[2])
    #     })
    #
    # decrypted_msg = cipher.decrypt(encrypted_message)
    # print("decrypted_msg", decrypted_msg)


