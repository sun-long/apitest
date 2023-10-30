import pytest
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
import time
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
@pytest.mark.P0
@pytest.mark.Regression
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
        
    @pytest.mark.Paid
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

    @pytest.mark.Paid
    def test_api_IdentityService_VerifyEnterprise_cryptor_CBC(self, config_obj,user_info,IdentityApi):
            """验证企业四要素_验证加密功能_设置CBC加密方式_输入match的企业四要素_设置身份证、姓名字段加密_预期返回结果为match"""
            cryptor = AESCipher(user_info.sk)
            jstr = {"verify_info": {
            "enterprise_name": "平江县虹桥镇李浣货物运输站",
            "enterprise_no": "92430626MA4R8G2U4X",
            "artificial_person":"李浣珍",
            "idcard_number": "430626198703124513"
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
            resp = IdentityApi.IdentityService_VerifyEnterprisePostApi( encrypt_info=encrypt_info)
            assert resp.status_code == 200
            assert resp.json_get("verify_result")=="MATCH"
            
    @pytest.mark.Paid
    def test_api_IdentityService_VerifyEnterprise_cryptor_GCM(self, config_obj,user_info,IdentityApi):
            """验证企业四要素_验证加密功能_设置GCM加密方式_输入match的企业四要素_设置身份证、姓名字段加密_预期返回结果为match"""
            cryptor = AESGCMCryptor(user_info.sk)
            jstr = {"verify_info": {
            "enterprise_name": "平江县虹桥镇李浣货物运输站",
            "enterprise_no": "92430626MA4R8G2U4X",
            "artificial_person":"李浣珍",
            "idcard_number": "430626198703124513"
            }}
            txt = json.dumps(jstr)
            cypher = cryptor.encrypt(txt)
            # de_cypher=cryptor.decrypt(cypher)
            feilds=["verify_info"]        
            encrypt_info={
                "algorithm": "AES_256_GCM",
                "version": 0,
                "encrypted_fields": feilds,
                "data": cypher
            }
            resp = IdentityApi.IdentityService_VerifyEnterprisePostApi( encrypt_info=encrypt_info)
            assert resp.status_code == 200
            assert resp.json_get("verify_result")=="MATCH"

    @pytest.mark.Paid
    def test_api_IdentityService_VerifyEnterprise_cryptor_12005005(self, config_obj,user_info,IdentityApi):
            """验证企业四要素_验证错误码字_权威源中存在，但是企业名称、法人姓名和法人身份证号一致，企业标识不一致"""
            verify_info={
            "enterprise_name": "平江县虹桥镇李浣货物运输站",
            "enterprise_no": "92430626MA4R8G2X",
            "artificial_person":"李浣珍",
            "idcard_number": "430626198703124513"
            }            
            encrypt_info = None
            resp = IdentityApi.IdentityService_VerifyEnterprisePostApi(verify_info=verify_info, encrypt_info=encrypt_info)
            assert resp.status_code == 200
            assert resp.json_get("verify_result") == "MISMATCH"

    def test_api_IdentityService_VerifyEnterprise_cryptor_12003120(self, config_obj,user_info,IdentityApi):
            """验证企业四要素_验证错误码字_无效的企业名称"""
            verify_info={
            "enterprise_no": "92430626MA4R8G2X",
            "artificial_person":"李浣珍",
            "idcard_number": "430626198703124513"
            }            
            encrypt_info = None
            resp = IdentityApi.IdentityService_VerifyEnterprisePostApi(verify_info=verify_info, encrypt_info=encrypt_info)
            assert resp.status_code == 400
            assert resp.json_get("error.code") == 3
            assert resp.json_get("error.details.0.message") == "invalid enterprise name"
            assert resp.json_get("error.details.0.reason") == 12003120

    def test_api_IdentityService_VerifyEnterprise_cryptor_12003121(self, config_obj,user_info,IdentityApi):
            """验证企业四要素_验证错误码字_无效的社会代码"""
            verify_info={
            "enterprise_name": "平江县虹桥镇李浣货物运输站",
            "artificial_person":"李浣珍",
            "idcard_number": "430626198703124513"
            }            
            encrypt_info = None
            resp = IdentityApi.IdentityService_VerifyEnterprisePostApi(verify_info=verify_info, encrypt_info=encrypt_info)
            assert resp.status_code == 400
            assert resp.json_get("error.code") == 3
            assert resp.json_get("error.details.0.message") == "invalid enterprise number"
            assert resp.json_get("error.details.0.reason") ==12003121

         