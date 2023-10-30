#!/usr/bin/env python
# -*- encoding: utf-8 -*-

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
    def test_api_VerifyIDCard_01(self, config_obj, testVerifyIDCard_official,expiry_date_right,IdentityApi):
        """ 验证二要素身份核验_验证核验功能_设置身份证号正确+名字匹配_有效期大于出生日期_预期匹配"""
        name = testVerifyIDCard_official.name
        id_card_number = testVerifyIDCard_official.id_card_number
        resp = IdentityApi.verifyIDCard(name, id_card_number, expiry_date=expiry_date_right)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"

        # TODO 不是很理解这块是要验证什么，如果只是要验证verify_result字段是否等于MATCH，感觉可以直接判断值即可 by wangan
        # with open(schema_path, 'r') as f:
        #     schema = json.load(f)
        # identityVerifyResult_schema=schema["definitions"]["identityVerifyResult"]
        # identityVerifyResult=resp.resp_json["verify_result"]
        # assert schema_validator(identityVerifyResult,identityVerifyResult_schema)
        # identityVerifyResult=='MATCH'

    def test_api_VerifyIDCard_02(self, config_obj, testVerifyIDCard_official, IdentityApi):
        """ 验证二要素身份核验_验证有效期的有效性_设置身份证号正确+名字匹配_有效期小于出生日期_预期非三方源错误"""
        name = testVerifyIDCard_official.name
        id_card_number = testVerifyIDCard_official.id_card_number
        expiry_date = "1930-11-11"
        resp = IdentityApi.verifyIDCard(name, id_card_number, expiry_date=expiry_date)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "id card expired"
        assert resp.json_get("error.details.0.reason") == 12003004
        assert resp.json_get("error.message") == "E12003004: id card expired"

        # TODO 以下为旧代码，明确的resp结果可以直接验证结果是否正确，如果上面的例子
        # # name = None
        # # id_card_number = None
        # expiry_date="1930-11-11"
        # encrypt_info={
        #     "algorithm": "ENCRPT_ALGORITHM_NONE",
        #     "version": 0,
        #     # "iv": "string",
        #     "encrypted_fields": [
        #     "string"
        #     ],
        #     "data": "string"
        # }
        # resp = IdentityApi.IdentityService_VerifyIDCardPostApi(name=testVerifyIDCard_official.name, idcard_number=testVerifyIDCard_official.id_card_number, expiry_date=expiry_date, encrypt_info=encrypt_info)
        # assert resp.status_code != 200
        # assert resp.status_code != 500
        # error_message=resp.resp_json["error"]["message"]
        # assert "auth verify" not in error_message
    @pytest.mark.Paid
    def test_api_VerifyIDCard_03(self, config_obj, testVerifyIDCard_official_suit_wrong, IdentityApi):
        """ 验证二要素身份核验_验证核验功能_设置身份证号正确+名字不匹配_预期三方源错误"""
        name = testVerifyIDCard_official_suit_wrong.name
        id_card_number = testVerifyIDCard_official_suit_wrong.id_card_number
        resp = IdentityApi.verifyIDCard(name, id_card_number)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "authority source invalid card info"
        assert resp.json_get("error.details.0.reason") == 12003024
        assert resp.json_get("error.message") == "E12003024: authority source invalid card info"

        # expiry_date = "2050-12-12"
        # encrypt_info={
        #     "algorithm": "ENCRPT_ALGORITHM_NONE",
        #     "version": 0,
        #     # "iv": "string",
        #     "encrypted_fields": [
        #     "string"
        #     ],
        #     "data": "string"
        # }
        # resp = IdentityApi.IdentityService_VerifyIDCardPostApi(name=testVerifyIDCard_official_suit_wrong.name, idcard_number=testVerifyIDCard_official_suit_wrong.id_card_number, expiry_date=expiry_date, encrypt_info=encrypt_info)
        # assert resp.status_code != 200
        # assert resp.status_code != 500
        #
        # error_message=resp.resp_json["error"]["message"]
        # #返回错误，错误属于三方源的
        # assert "auth verify"in error_message

    def test_api_VerifyIDCard_04(self, config_obj, testVerifyIDCard_official_birth_wrong, IdentityApi):
        """ 验证二要素身份核验_验证弱格式核验功能是否正确_设置错误的身份证号码_预期非三方源错误"""
        name = testVerifyIDCard_official_birth_wrong.name
        id_card_number = testVerifyIDCard_official_birth_wrong.id_card_number
        resp = IdentityApi.verifyIDCard(name, id_card_number)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid id card number"
        assert resp.json_get("error.details.0.reason") == 12003002
        assert resp.json_get("error.message") == "E12003002: invalid id card number"

        # expiry_date = "2050-12-12"
        # encrypt_info={
        #     "algorithm": "ENCRPT_ALGORITHM_NONE",
        #     "version": 0,
        #     # "iv": "string",
        #     "encrypted_fields": [
        #     "string"
        #     ],
        #     "data": "string"
        # }
        # resp = IdentityApi.IdentityService_VerifyIDCardPostApi(name=testVerifyIDCard_official_birth_wrong.name, idcard_number=testVerifyIDCard_official_birth_wrong.id_card_number, expiry_date=expiry_date, encrypt_info=encrypt_info)
        # assert resp.status_code != 200
        # assert resp.status_code != 500
        # error_message=resp.resp_json["error"]["message"]
        # #返回错误，错误不属于三方源的，是弱格式核验功能的错误
        # assert "auth verify" not in error_message

    def test_api_VerifyIDCard_05(self, config_obj, testVerifyIDCard_official_number_wrong, IdentityApi):
        """ 验证二要素身份核验_验证弱格式核验功能是否正确_设置身份证位数不对_预期非三方源错误"""
        name = testVerifyIDCard_official_number_wrong.name
        id_card_number = testVerifyIDCard_official_number_wrong.id_card_number
        resp = IdentityApi.verifyIDCard(name, id_card_number)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid id card number"
        assert resp.json_get("error.details.0.reason") == 12003002
        assert resp.json_get("error.message") == "E12003002: invalid id card number"

        # expiry_date = "2050-12-12"
        # encrypt_info={
        #     "algorithm": "ENCRPT_ALGORITHM_NONE",
        #     "version": 0,
        #     # "iv": "string",
        #     "encrypted_fields": [
        #     "string"
        #     ],
        #     "data": "string"
        # }
        # resp = IdentityApi.IdentityService_VerifyIDCardPostApi(name=testVerifyIDCard_official_number_wrong.name, idcard_number=testVerifyIDCard_official_number_wrong.id_card_number, expiry_date=expiry_date, encrypt_info=encrypt_info)
        # assert resp.status_code != 200
        # assert resp.status_code != 500
        # error_message=resp.resp_json["error"]["message"]
        # #返回错误，错误不属于三方源的，是弱格式核验功能的错误
        # assert "auth verify" not in error_message
    @pytest.mark.Paid
    def test_api_VerifyIDCard_06(self, config_obj, testVerifyIDCard_common, IdentityApi, user_info):
        """ 验证二要素身份核验_验证加密功能_姓名和身份证号加密"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"idcard_number": testVerifyIDCard_common.id_card_number,
                "name": testVerifyIDCard_common.name,
                "expiry_date": "2030-02-23"
                }
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["idcard_number", "name", "expiry_date"],
            "data": cypher
        }
        resp = IdentityApi.verifyIDCard(expiry_date="", encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
    @pytest.mark.Paid    
    def test_api_VerifyIDCard_06_1(self, config_obj, testVerifyIDCard_common, IdentityApi, user_info):
        """ 验证二要素身份核验_验证gcm加密功能_姓名和身份证号加密"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"idcard_number": testVerifyIDCard_common.id_card_number,
                "name": testVerifyIDCard_common.name,
                "expiry_date": "2030-02-23"
                }
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": ["idcard_number", "name", "expiry_date"],
            "data": cypher
        }
        resp = IdentityApi.verifyIDCard(expiry_date="", encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
    @pytest.mark.Paid 
    def test_api_VerifyIDCard_07(self, config_obj, testVerifyIDCard_official, IdentityApi):
        """ 验证二要素身份核验_失效时间为0000时表示长期，可正常身份证核验"""
        name = testVerifyIDCard_official.name
        id_card_number = testVerifyIDCard_official.id_card_number
        resp = IdentityApi.verifyIDCard(name, id_card_number, expiry_date="0000")
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
    @pytest.mark.Paid
    def test_api_VerifyIDCardFace_08(self, config_obj, testVerifyIDCard_official, IdentityApi):
        """ 验证二要素身份核验_失效时间为当天，可正常身份证核验"""
        name = testVerifyIDCard_official.name
        id_card_number = testVerifyIDCard_official.id_card_number
        expiry_date=time.strftime("%Y-%m-%d", time.localtime()) 
        resp = IdentityApi.verifyIDCard(name, id_card_number, expiry_date=expiry_date)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
    @pytest.mark.Paid
    def test_api_VerifyIDCardFace_01(self, config_obj, testVerifyIDCardFace_official,IdentityApi):
        """ 验证三要素身份核验_验证核验功能_设置身份证号正确+名字+图片匹配_有效期大于出生日期_预期匹配"""
        name = testVerifyIDCardFace_official.name
        id_card_number = testVerifyIDCardFace_official.id_card_number
        image = testVerifyIDCardFace_official.image
        resp = IdentityApi.verifyIDCardFace(name, id_card_number, image=image)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
        # assert resp.json_get("score")== 0.97999996 
    @pytest.mark.Paid           
    def test_api_VerifyIDCardFace_02(self, config_obj, testVerifyIDCardFace_image_suit_wrong,IdentityApi):
        """验证三要素身份核验_验证核验功能_设置身份证号正确+正确名字+图片不匹配_有效期大于出生日期_预期返回face_unmatch"""
        name = testVerifyIDCardFace_image_suit_wrong.name
        id_card_number = testVerifyIDCardFace_image_suit_wrong.id_card_number
        image = testVerifyIDCardFace_image_suit_wrong.image
        resp = IdentityApi.verifyIDCardFace(name, id_card_number, image=image)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "FACE_UNMATCH"



    @pytest.mark.Paid
    def test_api_VerifyIDCardFace_02_0(self, config_obj, testVerifyIDCardFace_suit_wrong,IdentityApi):
        """验证三要素身份核验_验证核验功能_设置身份证号正确+错误名字+图片匹配_有效期大于出生日期_预期返回三方源错误"""
        name = testVerifyIDCardFace_suit_wrong.name
        id_card_number = testVerifyIDCardFace_suit_wrong.id_card_number
        image = testVerifyIDCardFace_suit_wrong.image
        resp = IdentityApi.verifyIDCardFace(name, id_card_number, image=image)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "authority source invalid card info"
        assert resp.json_get("error.details.0.reason") == 12003024
        assert resp.json_get("error.message") == "E12003024: authority source invalid card info"

        # # name = None
        # # id_card_number = None
        # # image = None
        # expiry_date="2030-02-28"
        # base64_image=str(BaseApi.imageToBase64(os.path.join(Image_Path,testVerifyIDCardFace_suit_wrong.image)))
        # encrypt_info={
        #     "algorithm": "ENCRPT_ALGORITHM_NONE",
        #     "version": 0,
        #     "encrypted_fields": [
        #     "string"
        #     ],
        #     "data": "string"
        # }
        # resp = IdentityApi.IdentityService_VerifyIDCardFacePostApi(name=testVerifyIDCardFace_suit_wrong.name, idcard_number=testVerifyIDCardFace_suit_wrong.id_card_number, image=base64_image, expiry_date=expiry_date, encrypt_info=encrypt_info)
        # assert resp.status_code != 200
        # assert resp.status_code != 500
        # error_message=resp.resp_json["error"]["message"]
        # assert "auth verify"  in error_message
    @pytest.mark.Paid
    def test_api_VerifyIDCardFace_03(self, config_obj, testVerifyIDCardFace_official_resize,IdentityApi):
        """验证三要素身份核验_验证不同图片大小对核验的影响_图片大小依次_1M_130K_40K_25k_10k_格式依次_jpeg_bmp_png_预期匹配"""
        name = testVerifyIDCardFace_official_resize.name
        id_card_number = testVerifyIDCardFace_official_resize.id_card_number
        image = testVerifyIDCardFace_official_resize.image
        resp = IdentityApi.verifyIDCardFace(name, id_card_number, image=image)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
        # if "tester_50.jpeg" in image:
        #     assert resp.json_get("score") ==0.97499996 

        #
        # # name = None
        # # id_card_number = None
        # # image = None
        # expiry_date="2030-02-28"
        # base64_image=str(BaseApi.imageToBase64(os.path.join(Image_Path,testVerifyIDCardFace_official_resize.image)))
        # encrypt_info={
        #     "algorithm": "ENCRPT_ALGORITHM_NONE",
        #     "version": 0,
        #     "encrypted_fields": [
        #     "string"
        #     ],
        #     "data": "string"
        # }
        # resp = IdentityApi.IdentityService_VerifyIDCardFacePostApi(name=testVerifyIDCardFace_official_resize.name, idcard_number=testVerifyIDCardFace_official_resize.id_card_number, image=base64_image, expiry_date=expiry_date, encrypt_info=encrypt_info)
        # assert resp.status_code == 200
        # assert resp.status_code != 500
        # with open(schema_path, 'r') as f:
        #     schema = json.load(f)
        # identityVerifyResult_schema=schema["definitions"]["identityVerifyResult"]
        # identityVerifyResult=resp.resp_json["verify_result"]
        # assert schema_validator(identityVerifyResult,identityVerifyResult_schema)
        # identityVerifyResult=='MATCH'
        # score=resp.resp_json["score"]
        # assert score
    @pytest.mark.Paid
    def test_api_VerifyIDCardFace_04(self, config_obj, testVerifyIDCardFace_common, IdentityApi, user_info):
        """验证三要素身份核验_验证加密功能_request姓名和身份证号以及图片加密"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"idcard_number": testVerifyIDCardFace_common.id_card_number,
                "name": testVerifyIDCardFace_common.name,
                "expiry_date": "2030-03-23",
                "image": IdentityApi.idsImageToBase64(testVerifyIDCardFace_common.image)}
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["idcard_number", "name", "expiry_date", "image"],
            "data": cypher
        }
        resp = IdentityApi.verifyIDCardFace(expiry_date="", encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
        # assert resp.json_get("score") ==0.97999996   

        # # name = None
        # # id_card_number = None
        # base64_image=str(BaseApi.imageToBase64(os.path.join(Image_Path,testVerifyIDCardFace_common.image)))
        # expiry_date="2030-03-23"
        # ak_sk = config_obj.EnvInfo.ak_sk
        # SK=config_obj.get(ak_sk).sk
        # cryptor = AESCipher(SK)
        # jstr={"idcard_number":testVerifyIDCardFace_common.id_card_number,
        #       "name":testVerifyIDCardFace_common.name,
        #       "expiry_date":expiry_date,
        #       "image":base64_image}
        #
        # txt = json.dumps(jstr)
        # cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        # feilds=["idcard_number","name","expiry_date","image"]
        # encrypt_info={
        #     "algorithm": "AES_256_CBC",
        #     "version": 0,
        #     "encrypted_fields": feilds,
        #     "data": cypher
        # }
        # resp = IdentityApi.IdentityService_VerifyIDCardFacePostApi(name="", idcard_number="", image="",expiry_date="", encrypt_info=encrypt_info)
        # assert resp.status_code == 200
        # assert resp.status_code != 500
        # #验证schema
        # with open(schema_path, 'r') as f:
        #     schema = json.load(f)
        # identityVerifyResult_schema=schema["definitions"]["identityVerifyResult"]
        # identityVerifyResult=resp.resp_json["verify_result"]
        # assert schema_validator(identityVerifyResult,identityVerifyResult_schema)
        # identityVerifyResult=='MATCH'
    @pytest.mark.Paid
    def test_api_VerifyIDCardFace_04_1(self, config_obj, testVerifyIDCardFace_common, IdentityApi, user_info):
        """验证三要素身份核验_验证GCM加密功能_request姓名和身份证号以及图片加密"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"idcard_number": testVerifyIDCardFace_common.id_card_number,
                "name": testVerifyIDCardFace_common.name,
                "expiry_date": "2030-03-23",
                "image": IdentityApi.idsImageToBase64(testVerifyIDCardFace_common.image)}
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": ["idcard_number", "name", "expiry_date", "image"],
            "data": cypher
        }
        resp = IdentityApi.verifyIDCardFace(expiry_date="", encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
         #assert resp.json_get("score") ==0.97999996  
    @pytest.mark.Paid
    def test_api_VerifyIDCardFace_05(self, config_obj, testVerifyIDCardFace_common, IdentityApi):
        """ 验证三要素身份核验_失效时间为0000时表示长期，可正常身份证核验"""
        name = testVerifyIDCardFace_common.name
        id_card_number = testVerifyIDCardFace_common.id_card_number
        image = testVerifyIDCardFace_common.image
        resp = IdentityApi.verifyIDCardFace(name, id_card_number, image=image,expiry_date="0000")
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
         #assert resp.json_get("score") ==0.97999996  
    @pytest.mark.Paid
    def test_api_VerifyIDCardFace_06(self, config_obj, testVerifyIDCardFace_common, IdentityApi):
        """ 验证三要素身份核验_失效时间为当天，可正常身份证核验"""
        name = testVerifyIDCardFace_common.name
        id_card_number = testVerifyIDCardFace_common.id_card_number
        image = testVerifyIDCardFace_common.image
        expiry_date=time.strftime("%Y-%m-%d", time.localtime()) 
        resp = IdentityApi.verifyIDCardFace(name, id_card_number, image=image,expiry_date=expiry_date)
        assert resp.status_code == 200
        assert resp.json_get("verify_result") == "MATCH"
         #assert resp.json_get("score") ==0.97999996  
    @pytest.mark.Paid
    def test_api_VerifyIDCard_error_code_12003001(self, config_obj, testVerifyIDCard_official_name_wrong, IdentityApi):
        """ 验证二要素身份核验_验证错误码_invalid name"""
        name = testVerifyIDCard_official_name_wrong.name
        id_card_number = testVerifyIDCard_official_name_wrong.id_card_number
        resp = IdentityApi.verifyIDCard(name, id_card_number)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid name"
        assert resp.json_get("error.details.0.reason") == 12003001

    def test_api_VerifyIDCard_error_code_12003001_0(self, config_obj, testVerifyIDCard_official_name_wrong, IdentityApi):
        """ 验证二要素身份核验_验证错误码_invalid name_设置为None"""
        name = None
        id_card_number = testVerifyIDCard_official_name_wrong.id_card_number
        resp = IdentityApi.verifyIDCard(name, id_card_number)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid name"
        assert resp.json_get("error.details.0.reason") == 12003001


    def test_api_VerifyIDCard_error_code_12003003(self, config_obj, testVerifyIDCard_official, expiry_date_wrong,IdentityApi):
        """ 验证二要素身份核验_验证错误码_invalid expiry date"""
        name = testVerifyIDCard_official.name
        id_card_number = testVerifyIDCard_official.id_card_number
        resp = IdentityApi.verifyIDCard(name, id_card_number,expiry_date=expiry_date_wrong)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid expiry date"
        assert resp.json_get("error.details.0.reason") == 12003003


    def test_api_VerifyIDCard_error_code_12003006(self, config_obj, testVerifyIDCardFace_common,IdentityApi):
        """ 验证三要素身份核验_验证错误码_image data is empty"""
        name = testVerifyIDCardFace_common.name
        id_card_number = testVerifyIDCardFace_common.id_card_number
        resp = IdentityApi.verifyIDCardFace(name, id_card_number, image=None)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "image data is empty"
        assert resp.json_get("error.details.0.reason") == 12003006
    @pytest.mark.Paid
    def test_api_VerifyIDCardFace_12003023(self, config_obj, testVerifyIDCardFace_common, IdentityApi):
        """ 验证三要素身份核验_验证错误码字_图片无效"""
        name = testVerifyIDCardFace_common.name
        id_card_number = testVerifyIDCardFace_common.id_card_number
        image = "identify/ruanzhihua_fuzzy.png"
        expiry_date=time.strftime("%Y-%m-%d", time.localtime()) 
        resp = IdentityApi.verifyIDCardFace(name, id_card_number, image=image)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "authority source invalid image"
        assert resp.json_get("error.details.0.reason") == 12003023

if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])