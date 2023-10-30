import base64
import json
import os
from Cryptodome.Cipher import AES

# 需要安装相关模块，如 pycryptodome
# pip install pycryptodome


NonceSize = 12


NonceSize = 12


class AESGCMCryptor:
    def __init__(self, key):
        keyLen = len(key)

        if keyLen not in [16, 24, 32]:
            raise ValueError('Invalid key size, must be 16, 24, or 32 bytes')

        self.key = key.encode()

    def encrypt(self, plaintext):
        # if isinstance(plaintext, str):
        #    plaintext = plaintext.encode(encoding)
        nonce = os.urandom(NonceSize)
        aes_cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
        ciphertext, tag = aes_cipher.encrypt_and_digest(plaintext.encode())
        ciphertext = nonce + ciphertext + tag
        return base64.b64encode(ciphertext).decode()

    # decrypt decrypt the ciphertext and verify the authentication tag
    def decrypt(self, ciphertext, encoding='utf-8'):
        ciphertext = base64.b64decode(ciphertext.encode('utf-8'))
        nonce = ciphertext[:NonceSize]
        tag = ciphertext[-16:]
        ciphertext = ciphertext[NonceSize:-16]

        aes_cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
        plaintext = aes_cipher.decrypt_and_verify(ciphertext, tag)
        if encoding:
            plaintext = plaintext.decode(encoding)
        return plaintext


if __name__ == '__main__':
    # key = '0123456789abcdef0123456789abcdef'
    # ak="2OXzMGrVjTWMtbwYlM6L3avxswt"
    key="D7Tba3EpuweR69R2UBF38yG4BtTj9Hut"


    plainText = '{"image": "This is a secret message."}'

    aes_cryptor = AESGCMCryptor(key)
    cipherText = aes_cryptor.encrypt(plainText)

    print('Plain text:', plainText)
    print('Key:', key)
    print('Cipher text:', cipherText)

    resp = 'VnVTMWpaMnVWYmhWleOjWJog83D1BtDDE3+sATPhdNR+4Ycg/jhZ0SGKfunXiAgZjs+AhM6928Q76leEtOs3oK5G+KW6VqMi6QIDKK5Sfihj25sACwPJqq9MtLX0iAbxqLRWg8yl73f89x0bJ2kktJ0yvT2CticXecWeFQ5+Ki23Saef4spFcrr4cyn52IjeuVnCJJ0cCWsqT/AWfKhPh/o/yy306+aabXF3dMG7GJF3RknJtluP3aGm98B+Dwufaa2W2/rl+YG+MKFIAuZwz5MvvEkK8u5C8XiaQLCBUTrlo6fb2P8jkS1VSfizha9DoxMRNpT7a7+m5fQ='
    decryptedText = aes_cryptor.decrypt(cipherText)
    print('Decrypted text:', decryptedText)
    decryptedText = json.loads(decryptedText)

# class AESGCMCryptor:
#     def __init__(self, key):
#         """
#         :param key: 密钥, 32字节
#         """
#         self.key = key.encode()

#     def encrypt(self, plain_text):
#         """ 加密 """

#         kwargs = {
#             'key': self.key,
#             'mode': AES.MODE_GCM
#         }

#         nonce = "012345678912".encode()  # os.urandom(12)
#         kwargs['nonce'] = nonce
#         #kwargs['mac_len'] = 16
#         # 拼接 IV和密文
#         cipher_text = nonce + AES.new(**kwargs).encrypt(plain_text.encode())

#         # BASE64编码
#         return base64.b64encode(cipher_text).decode()

#     def decrypt(self, cipher_text):
#         """ 解密 """

#         cipher_text = base64.b64decode(cipher_text.encode())
#         kwargs = {
#             'key': self.key,
#             'mode': AES.MODE_GCM
#         }

#         kwargs['nonce'] = cipher_text[:12]
#         #kwargs['mac_len'] = 16
#         plain_text = AES.new(**kwargs).decrypt(cipher_text[16:])
#         return plain_text
