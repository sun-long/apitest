import pytest
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
import time
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
@pytest.mark.ids
@pytest.mark.checkin
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
        
    def test_api_IdentityService_VerifyEnterprise_match(self, config_obj, IdentityApi):
            """验证企业四要素_验证核验功能_输入match的企业四要素_预期返回结果为match"""
            verify_info={
            "enterprise_name": "平江县虹桥镇李浣货物运输站",
            "enterprise_no": "92430626MA4R8G2U4X",
            "artificial_person":"李浣珍",
            "idcard_number": "430626198703124513"
            }            
            encrypt_info = None
            resp = IdentityApi.IdentityService_VerifyEnterprisePostApi(verify_info=verify_info, encrypt_info=encrypt_info)
            assert resp.status_code == 200
            assert resp.json_get("verify_result")=="MATCH"

