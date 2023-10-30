import pytest
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
import time
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
@pytest.mark.checkin
@pytest.mark.ids
class TestIdentityApi(object):
    """ identity Api测试"""

    @pytest.fixture(scope="class", autouse=True)
    def init_func(self, config_obj):
        # 初始化测试集
        # 所有test运行前运行一次，接收外部参数env_obj，初始化测试环境
        log().info("==========%s测试开始==========" % self.__class__.__name__)

    def teardown_class(self):
        # 所有test运行完后运行一次
        log().info("==========%s测试结束==========\n" % self.__name__)
        log().info("clear tasks finish")

    def setup_method(self, method):
        # 每个测试用例执行之前做操作
        log().info("用例%s开始" % method.__name__)

    def teardown_method(self, method):
        # 每个测试用例执行之后做操作
        log().info("用例%s结束" % method.__name__)


    def test_api_IdentityService_VerifyBankcard_CBC(self, config_obj, user_info,IdentityApi):
        """验证银行卡四要素核验_加密_CBC"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"verify_info":{
            "name": "陈瑜",
            "mobile": "13144800721",
            "bankcard_number": "6212264000044821409",
            "idcard_number": "430903199311243317"
        }}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["verify_info"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = IdentityApi.IdentityService_VerifyBankcardPostApi(verify_info=None, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("verify_result")=="MATCH"

