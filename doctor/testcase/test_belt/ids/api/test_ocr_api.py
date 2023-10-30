#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config
from commonlib.log_utils import log
from commonlib.api_lib.base_api import BaseApi
from commonlib.api_lib.validator import schema_validator, digit_number_validator, idc_verify
from commonlib.api_lib.AES_new import *
# import cv2
from PIL import Image, ImageDraw
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor

def image_draw_rectangle(imgpath,suffix,box):
    im = Image.open(imgpath)
    draw = ImageDraw.Draw(im)
    draw.line([box[0]["x"],box[0]["y"], box[1]["x"],box[1]["y"]],  fill=(255, 0, 0), width=2)
    draw.line([box[1]["x"],box[1]["y"], box[2]["x"],box[2]["y"]],  fill=(255, 0, 0), width=2)
    draw.line([box[2]["x"],box[2]["y"], box[3]["x"],box[3]["y"]],  fill=(255, 0, 0), width=2)
    draw.line([box[3]["x"],box[3]["y"], box[0]["x"],box[0]["y"]],  fill=(255, 0, 0), width=2)
    # 显示图片
    #im.show()
    im.save(os.path.splitext(imgpath)[0]+suffix+os.path.splitext(imgpath)[1])
@pytest.mark.P0
@pytest.mark.Regression
class TestOcrApi(object):
    """ ocr Api测试"""

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

    def test_api_OCRBankcard_01(self, config_obj, OcrApi, testImage_ocr_bankcard_format):
        """验证银行卡单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_正例"""
        resp = OcrApi.OCRBankcard(testImage_ocr_bankcard_format)
        assert resp.status_code == 200
        assert len(resp.json_get("bankcard.card_number")) in [19, 16, 17]  # TODO 验证数字直接验证即可
        required_list = ["card_number", "bank_name", "bank_id", "card_name", "card_type"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="bankcard"), "Json_schema验证失败"

    def test_api_OCRBankcard_roi_new(self, config_obj, OcrApi, testImage_ocr_bankcard_roi):
        """验证银行卡单接口_验证roi区域"""
        resp = OcrApi.OCRBankcard(testImage_ocr_bankcard_roi)
        assert resp.status_code == 200
        detail=resp.json_get("detailed_info")
        bankcard_number=detail["detect_details"]["bankcard.card_number"]
        vertices=bankcard_number["roi"]["vertices"]
        assert vertices==[{"x":34, "y":105}, {"x":297, "y":108}, {"x":297, "y":127}, {"x":34, "y":124}]
    @pytest.mark.skip("ids1.11此特性产品暂时不加")
    def test_api_OCRBankcard_roi(self, config_obj, OcrApi, testImage_ocr_bankcard_roi):
        """验证银行卡单接口_验证roi区域"""
        resp = OcrApi.OCRBankcard(testImage_ocr_bankcard_roi)
        assert resp.status_code == 200
        detail=resp.json_get("detailed_info")
        for key,item in detail["detect_details"].items():
            vertices=item["roi"]["vertices"]
            filename=os.path.join(config.ids_image_path,testImage_ocr_bankcard_roi)
            suffix = item["field_name"]
            image_draw_rectangle(filename, suffix, vertices)
            # img=cv2.imread(filename)
            # cv2.line(img,(vertices[0]["x"],vertices[0]["y"]),(vertices[1]["x"],vertices[1]["y"]),(255, 0, 0), 2)
            # cv2.line(img,(vertices[1]["x"],vertices[1]["y"]),(vertices[2]["x"],vertices[2]["y"]),(255, 0, 0), 2)
            # cv2.line(img,(vertices[2]["x"],vertices[2]["y"]),(vertices[3]["x"],vertices[3]["y"]),(255, 0, 0), 2)
            # cv2.line(img,(vertices[3]["x"],vertices[3]["y"]),(vertices[0]["x"],vertices[0]["y"]),(255, 0, 0), 2)
            # new_image=os.path.splitext(filename)[0]+item["field_name"]+os.path.splitext(filename)[1]
            # cv2.imwrite(new_image, img)
        bankcard=resp.json_get("bankcard")
        assert len(bankcard)==len(detail["detect_details"])




    def test_api_OCRBankcard_02(self, config_obj, OcrApi, testImage_ocr_bankcard_type):
        """验证银行卡单接口_验证支持不同卡类型功能_输入不同卡类型__信用卡_准信用卡_借记卡_预消费卡_正例"""
        resp = OcrApi.OCRBankcard(testImage_ocr_bankcard_type)
        assert resp.status_code == 200
        assert len(resp.json_get("bankcard.card_number")) in [19, 16, 17]  # TODO 验证数字直接验证即可
        required_list = ["card_number", "bank_name", "bank_id", "card_name", "card_type"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="bankcard"), "Json_schema验证失败"


    def test_api_OCRBankcard_03(self, config_obj, OcrApi,testImage_ocr_bankcard_common, user_info):
        """验证银行卡单接口_验证加密功能_image参数加且response加密_正例"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_bankcard_common)}
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields":  ["image"],
            "data": cypher
        }
        resp = OcrApi.OCRBankcard(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert "bankcard" in resp.json_get("encrypt_info.encrypted_fields"), "bankcard 不在encrypt_info.encrypted_fields中"
        # 解密
        encrypt_info_data = cryptor.decrypt(resp.json_get("encrypt_info.data"))
        encrypt_info_data = json.loads(encrypt_info_data)
        assert "bankcard" in encrypt_info_data, "bankcard不在解密后的encrypt_info.data中"
        assert len(encrypt_info_data["bankcard"]["card_number"]) in [19, 16, 17]
        required_list = ["card_number", "bank_name", "bank_id", "card_name", "card_type"]
        ocrBankcard_schema = resp.get_definitions_by_name("ocrBankcard")  # 根据名字获取definitions
        ocrBankcard_schema.update({"required": required_list})
        assert schema_validator(encrypt_info_data["bankcard"], ocrBankcard_schema)


    def test_api_OCRBankcard_03_1(self, config_obj, OcrApi,testImage_ocr_bankcard_common, user_info):
        """验证银行卡单接口_验证GCM加密功能_image参数加且response加密_正例"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_bankcard_common)}
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields":  ["image"],
            "data": cypher
        }
        resp = OcrApi.OCRBankcard(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert "bankcard" in resp.json_get("encrypt_info.encrypted_fields"), "bankcard 不在encrypt_info.encrypted_fields中"
        # 解密
        encrypt_info_data = cryptor.decrypt(resp.json_get("encrypt_info.data"))
        encrypt_info_data = json.loads(encrypt_info_data)
        assert "bankcard" in encrypt_info_data, "bankcard不在解密后的encrypt_info.data中"
        assert len(encrypt_info_data["bankcard"]["card_number"]) in [19, 16, 17]
        required_list = ["card_number", "bank_name", "bank_id", "card_name", "card_type"]
        ocrBankcard_schema = resp.get_definitions_by_name("ocrBankcard")  # 根据名字获取definitions
        ocrBankcard_schema.update({"required": required_list})
        assert schema_validator(encrypt_info_data["bankcard"], ocrBankcard_schema)      

    def test_api_OCRBusinessLicense_01(self, config_obj, OcrApi,testImage_ocr_business_license):
        """验证营业执照单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_正例"""
        resp = OcrApi.OCRBusinessLicense(testImage_ocr_business_license)
        assert resp.status_code == 200
        required_list=["name","code","type","address","artificial_person","business_scope","register_date"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="business_license"), "Json_schema验证失败"
        assert len(resp.json_get("business_license.code")) in [18]

    @pytest.mark.skip("ids1.11此特性产品暂时不加")
    def test_api_OCRBusinessLicense_roi(self, config_obj, OcrApi, testImage_ocr_business_roi):
        """验证营业执照单接口_验证roi区域"""
        resp = OcrApi.OCRBusinessLicense(testImage_ocr_business_roi)
        assert resp.status_code == 200
        detail=resp.json_get("detailed_info")
        for key,item in detail["detect_details"].items():
            if  len(item["roi"])!=0:
                vertices=item["roi"]["vertices"]
                filename=os.path.join(config.ids_image_path,testImage_ocr_business_roi)
                suffix = item["field_name"]
                image_draw_rectangle(filename, suffix, vertices)
                # img=cv2.imread(filename)
                # cv2.line(img,(vertices[0]["x"],vertices[0]["y"]),(vertices[1]["x"],vertices[1]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[1]["x"],vertices[1]["y"]),(vertices[2]["x"],vertices[2]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[2]["x"],vertices[2]["y"]),(vertices[3]["x"],vertices[3]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[3]["x"],vertices[3]["y"]),(vertices[0]["x"],vertices[0]["y"]),(255, 0, 0), 2)
                # new_image=os.path.splitext(filename)[0]+item["field_name"]+os.path.splitext(filename)[1]
                # cv2.imwrite(new_image, img)
        business_license=resp.json_get("business_license")
        assert len(business_license)==len(detail["detect_details"])

    def test_api_OCRBusinessLicense_02(self, config_obj, OcrApi,testImage_ocr_business_license_common,user_info):
        """验证营业执照单接口_验证加密功能_image参数加且response加密_正例"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_business_license_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRBusinessLicense(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        #验证解密后的bankcard字段
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="business_license":
                    ocrBusinessLicense=data_json[k]
        assert len(ocrBusinessLicense["code"])in [18]
        required_list=["name","code","type","address","artificial_person","serial_number","business_scope","operation_period","capital","register_date","registration_authority_seal"]
        ocrBusinessLicense_schema = resp.get_definitions_by_name("ocrBusinessLicense")  # 根据名字获取definitions
        ocrBusinessLicense_schema.update({"required": required_list})
        assert schema_validator(ocrBusinessLicense, ocrBusinessLicense_schema)


    def test_api_OCRBusinessLicense_02_01(self, config_obj, OcrApi,testImage_ocr_business_license_common,user_info):
        """验证营业执照单接口_验证GCM加密功能_image参数加且response加密_正例"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_business_license_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRBusinessLicense(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        #验证解密后的bankcard字段
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="business_license":
                    ocrBusinessLicense=data_json[k]
        assert len(ocrBusinessLicense["code"])in [18]
        required_list=["name","code","type","address","artificial_person","serial_number","business_scope","operation_period","capital","register_date","registration_authority_seal"]
        ocrBusinessLicense_schema = resp.get_definitions_by_name("ocrBusinessLicense")  # 根据名字获取definitions
        ocrBusinessLicense_schema.update({"required": required_list})
        assert schema_validator(ocrBusinessLicense, ocrBusinessLicense_schema)


    def test_api_OCRDrivingLicense_01(self, config_obj, testImage_ocr_driving_license_01,OcrApi):

        """验证驾驶证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_包含两页面_正例"""
        resp = OcrApi.OCRDrivingLicense(testImage_ocr_driving_license_01)
        assert resp.status_code == 200
        #第一页
        required_list=["id","name","sex","nationality","address","birth_date","issue_date","class","valid_from","valid_to"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="first_page"), "Json_schema验证失败"
        #第二页   
        required_list=["id","name","file_no","record","barcode"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="second_page"), "Json_schema验证失败"
    @pytest.mark.skip("ids1.11此特性产品暂时不加")
    def test_api_OCRDrivingLicense_roi(self, config_obj, OcrApi, testImage_ocr_driving_license_roi):
        """验证驾驶证单接口_验证roi区域"""
        resp = OcrApi.OCRDrivingLicense(testImage_ocr_driving_license_roi)
        assert resp.status_code == 200
        detail=resp.json_get("detailed_info")
        for key,item in detail["detect_details"].items():
            if  len(item["roi"])!=0:
                vertices=item["roi"]["vertices"]
                filename=os.path.join(config.ids_image_path,testImage_ocr_driving_license_roi)
                suffix = item["field_name"]
                image_draw_rectangle(filename, suffix, vertices)
                # img=cv2.imread(filename)
                # cv2.line(img,(vertices[0]["x"],vertices[0]["y"]),(vertices[1]["x"],vertices[1]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[1]["x"],vertices[1]["y"]),(vertices[2]["x"],vertices[2]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[2]["x"],vertices[2]["y"]),(vertices[3]["x"],vertices[3]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[3]["x"],vertices[3]["y"]),(vertices[0]["x"],vertices[0]["y"]),(255, 0, 0), 2)
                # new_image=os.path.splitext(filename)[0]+item["field_name"]+os.path.splitext(filename)[1]
                # cv2.imwrite(new_image, img)
        second_page=resp.json_get("second_page")
        first_page=resp.json_get("first_page")
        assert (len(second_page)+len(first_page))==len(detail["detect_details"])



    def test_api_OCRDrivingLicense_02(self, config_obj, testImage_ocr_driving_license_first,OcrApi):
        """验证驾驶证单接口_验证支持单页面检测功能_输入第一页_单页_正例"""
        resp = OcrApi.OCRDrivingLicense(testImage_ocr_driving_license_first)
        assert resp.status_code == 200
        #第一页
        required_list=["id","name","sex","nationality","address","birth_date","issue_date","class","valid_from","valid_to"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="first_page"), "Json_schema验证失败"

    def test_api_OCRDrivingLicense_03(self, config_obj, testImage_ocr_driving_license_second,OcrApi):
        """验证驾驶证单接口_验证支持单页面检测功能_输入第二页_单页_正例"""
        resp = OcrApi.OCRDrivingLicense(testImage_ocr_driving_license_second)
        assert resp.status_code == 200
        #第二页   
        required_list=["id","name","file_no","record","barcode"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="second_page"), "Json_schema验证失败"


    def test_api_OCRDrivingLicense_04_1(self, config_obj, testImage_ocr_driving_license_common,OcrApi,user_info):
        """验证驾驶证单接口_验证gcm加密功能_image参数加且response加密_正例"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_driving_license_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRDrivingLicense(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        #验证解密后的bankcard字段
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="first_page":
                    ocrDriverFirstPage=data_json[k]
            if k=="second_page":
                    ocrDriverSecondPage=data_json[k]                
        
        #第一页
        required_list=["id","name","sex","nationality","address","birth_date","issue_date","class","valid_from","valid_to"]
        ocrDriverFirstPage_schema = resp.get_definitions_by_name("ocrDriverFirstPage")  # 根据名字获取definitions
        ocrDriverFirstPage_schema.update({"required": required_list})
        assert schema_validator(ocrDriverFirstPage, ocrDriverFirstPage_schema)
        #第二页
        required_list=["id","name","file_no","record","barcode"]
        ocrDriverSecondPage_schema = resp.get_definitions_by_name("ocrDriverSecondPage")  # 根据名字获取definitions
        ocrDriverSecondPage_schema.update({"required": required_list})
        assert schema_validator(ocrDriverSecondPage, ocrDriverSecondPage_schema)

    def test_api_OCRDrivingLicense_04(self, config_obj, testImage_ocr_driving_license_common,OcrApi,user_info):
        """验证驾驶证单接口_验证加密功能_image参数加且response加密_正例"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_driving_license_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRDrivingLicense(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        #验证解密后的bankcard字段
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="first_page":
                    ocrDriverFirstPage=data_json[k]
            if k=="second_page":
                    ocrDriverSecondPage=data_json[k]                
        
        #第一页
        required_list=["id","name","sex","nationality","address","birth_date","issue_date","class","valid_from","valid_to"]
        ocrDriverFirstPage_schema = resp.get_definitions_by_name("ocrDriverFirstPage")  # 根据名字获取definitions
        ocrDriverFirstPage_schema.update({"required": required_list})
        assert schema_validator(ocrDriverFirstPage, ocrDriverFirstPage_schema)
        #第二页
        required_list=["id","name","file_no","record","barcode"]
        ocrDriverSecondPage_schema = resp.get_definitions_by_name("ocrDriverSecondPage")  # 根据名字获取definitions
        ocrDriverSecondPage_schema.update({"required": required_list})
        assert schema_validator(ocrDriverSecondPage, ocrDriverSecondPage_schema)
        
    def test_api_OCRHKMacauExitEntryPermit_01(self, config_obj, testImage_ocr_hk_macau_exit_entry_permit,OcrApi):
        """验证港澳通行证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_正例"""
        resp = OcrApi.OCRHKMacauExitEntryPermit(testImage_ocr_hk_macau_exit_entry_permit)
        assert resp.status_code == 200
        required_list=["issue_address","birth_date","card_number","name","name_pinyin","sex","expiry_date"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="hk_macau_exit_entry_permit"), "Json_schema验证失败"

    @pytest.mark.skip("ids1.11此特性产品暂时不加")
    def test_api_OCRHKMacauExitEntryPermit_roi(self, config_obj, testImage_ocr_hk_macau_exit_entry_permit_roi,OcrApi):
        """验证港澳通行证单接口_roi"""
        resp = OcrApi.OCRHKMacauExitEntryPermit(testImage_ocr_hk_macau_exit_entry_permit_roi)
        assert resp.status_code == 200
        detail=resp.json_get("detailed_info")
        for key,item in detail["detect_details"].items():
            if  len(item["roi"])!=0:
                vertices=item["roi"]["vertices"]
                filename=os.path.join(config.ids_image_path,testImage_ocr_hk_macau_exit_entry_permit_roi)
                suffix = item["field_name"]
                image_draw_rectangle(filename, suffix, vertices)
                # img=cv2.imread(filename)
                # cv2.line(img,(vertices[0]["x"],vertices[0]["y"]),(vertices[1]["x"],vertices[1]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[1]["x"],vertices[1]["y"]),(vertices[2]["x"],vertices[2]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[2]["x"],vertices[2]["y"]),(vertices[3]["x"],vertices[3]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[3]["x"],vertices[3]["y"]),(vertices[0]["x"],vertices[0]["y"]),(255, 0, 0), 2)
                # new_image=os.path.splitext(filename)[0]+item["field_name"]+os.path.splitext(filename)[1]
                # cv2.imwrite(new_image, img)
        hk_macau_exit_entry_permit=resp.json_get("hk_macau_exit_entry_permit")
        assert len(hk_macau_exit_entry_permit)==len(detail["detect_details"])

    def test_api_OCRHKMacauExitEntryPermit_02(self, config_obj, testImage_ocr_hk_macau_exit_entry_permit_common,OcrApi,user_info):
        """验证港澳通行证单接口_验证加密功能_image参数加且response加密_正例"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_hk_macau_exit_entry_permit_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRHKMacauExitEntryPermit(image="", encrypt_info=encrypt_info)
        assert resp.status_code == 200  
        #验证解密后的bankcard字段
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="hk_macau_exit_entry_permit":
                    ocrHKMacauExitEntryPermit=data_json[k]
        required_list=["issue_address","birth_date","card_number","name","name_pinyin","sex","expiry_date"]
        ocrHKMacauExitEntryPermit_schema = resp.get_definitions_by_name("ocrHKMacauExitEntryPermit")  # 根据名字获取definitions
        ocrHKMacauExitEntryPermit_schema.update({"required": required_list})
        assert schema_validator(ocrHKMacauExitEntryPermit, ocrHKMacauExitEntryPermit_schema)

    def test_api_OCRHKMacauExitEntryPermit_02_1(self, config_obj, testImage_ocr_hk_macau_exit_entry_permit_common,OcrApi,user_info):
        """验证港澳通行证单接口_验证gcm加密功能_image参数加且response加密_正例"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_hk_macau_exit_entry_permit_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRHKMacauExitEntryPermit(image="", encrypt_info=encrypt_info)
        assert resp.status_code == 200  
        #验证解密后的bankcard字段
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="hk_macau_exit_entry_permit":
                    ocrHKMacauExitEntryPermit=data_json[k]
        required_list=["issue_address","birth_date","card_number","name","name_pinyin","sex","expiry_date"]
        ocrHKMacauExitEntryPermit_schema = resp.get_definitions_by_name("ocrHKMacauExitEntryPermit")  # 根据名字获取definitions
        ocrHKMacauExitEntryPermit_schema.update({"required": required_list})
        assert schema_validator(ocrHKMacauExitEntryPermit, ocrHKMacauExitEntryPermit_schema)


    def test_api_OCRIDCard_01(self, config_obj,testImage_ocr_idcard_01, OcrApi):
        """验证身份证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_正面_正例. """
        side = 'FRONT'              
        resp = OcrApi.OCRIDCard(testImage_ocr_idcard_01, side=side)
        assert resp.status_code == 200
        required_list=["side","name","sex","nation","birth_date","address","number"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="idcard"), "Json_schema验证失败"
        assert idc_verify(resp.resp_json["idcard"]["number"])
        resp.json_get("idcard.side")=='FRONT'



    def test_api_OCRIDCard_02(self, config_obj,testImage_ocr_idcard_02, OcrApi):
        """验证身份证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_反面_正例. """
        side = 'BACK'              
        resp = OcrApi.OCRIDCard(testImage_ocr_idcard_02, side=side)
        assert resp.status_code == 200
        required_list=["authority","expiry_date","issue_date"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="idcard"), "Json_schema验证失败"
        resp.json_get("idcard.side")=='BACK'

    def test_api_OCRIDCard_03(self, config_obj,testImage_ocr_idcard_03, OcrApi):
        """验证身份证单接口_验证质量检测功能_设置质量检测_验证质量输出以及是否与实际匹配_正例. """
        side = 'AUTO'
        detect_quality = True
        resp = OcrApi.OCRIDCard(testImage_ocr_idcard_03, side=side,detect_quality=detect_quality)
        assert resp.status_code == 200
        assert resp.json_get("quality_level")


    def test_api_OCRIDCard_04(self, config_obj,testImage_ocr_idcard_04, OcrApi):
        """验证身份证单接口_验证支持其他身份证类型功能_设置不同来源的身份证_临时身份证__正例. """
        side = 'AUTO'
        resp = OcrApi.OCRIDCard(testImage_ocr_idcard_04, side=side)
        assert resp.status_code == 200
        required_list=["side","name","sex","nation","birth_date","number","idcard_source"]
        #required_list=["side","name","sex","nation","birth_date","address","number","idcard_source"]#临时身份证此图识别不出地址
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="idcard"), "Json_schema验证失败"
        assert idc_verify(resp.resp_json["idcard"]["number"])


    def test_api_OCRIDCard_05(self, config_obj,testImage_ocr_idcard_03, OcrApi):
        """验证身份证单接口_验证默认功能_不设置side_预期能够正常识别_正例 """
        resp = OcrApi.OCRIDCard(testImage_ocr_idcard_03)
        assert resp.status_code == 200

    def test_api_OCRIDCard_06_1(self, config_obj,testImage_ocr_idcard_common, OcrApi,user_info):
        """验证身份证单接口_验证gcm加密_正例. """
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_idcard_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRIDCard(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="idcard":
                    ocrIDCard=data_json[k] 
        required_list=["side","name","sex","nation","birth_date","address","number"]
        ocrIDCard_schema = resp.get_definitions_by_name("ocrIDCard")  # 根据名字获取definitions
        ocrIDCard_schema.update({"required": required_list})
        del ocrIDCard_schema["properties"]["side"]  
        del ocrIDCard_schema["properties"]["idcard_source"]  
        
        assert schema_validator(ocrIDCard, ocrIDCard_schema)
        assert idc_verify(ocrIDCard["number"])

    def test_api_OCRIDCard_06(self, config_obj,testImage_ocr_idcard_common, OcrApi,user_info):
        """验证身份证单接口_验证加密_正例. """
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_idcard_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRIDCard(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="idcard":
                    ocrIDCard=data_json[k] 
        required_list=["side","name","sex","nation","birth_date","address","number"]
        ocrIDCard_schema = resp.get_definitions_by_name("ocrIDCard")  # 根据名字获取definitions
        ocrIDCard_schema.update({"required": required_list})
        del ocrIDCard_schema["properties"]["side"]  
        del ocrIDCard_schema["properties"]["idcard_source"]  
        
        assert schema_validator(ocrIDCard, ocrIDCard_schema)
        assert idc_verify(ocrIDCard["number"])



    def test_api_OCRIDCard_07(self, config_obj,testImage_ocr_idcard_rect_roi, OcrApi):
        """验证身份证单接口_验证身份证坐标_预期输出正确的身份证坐标_正例"""           
        resp = OcrApi.OCRIDCard(image=testImage_ocr_idcard_rect_roi)
        assert resp.status_code == 200
        vertices=resp.json_get("roi.vertices")
        if "idcard_front" in testImage_ocr_idcard_rect_roi:
             assert vertices==[{"x":155, "y":197}, {"x":1933, "y":220}, {"x":1918, "y":1303}, {"x":146, "y":1291}]
        if "idcard_back" in testImage_ocr_idcard_rect_roi:
             assert vertices==[{"x":83, "y":88}, {"x":609, "y":82}, {"x":617, "y":411}, {"x":79, "y":411}]
        if "idcard_temp_front" in testImage_ocr_idcard_rect_roi:
             assert vertices==[{"x":117, "y":146}, {"x":897, "y":146}, {"x":897, "y":639}, {"x":117, "y":639}]
        if "idcard_temp_back" in testImage_ocr_idcard_rect_roi:
             assert vertices==[{"x":70, "y":176}, {"x":1002, "y":176}, {"x":1002, "y":749}, {"x":70, "y":749}]
        #存储图片
        # img=cv2.imread(filename)
        # cv2.line(img,(vertices[0]["x"],vertices[0]["y"]),(vertices[1]["x"],vertices[1]["y"]),(0, 255, 0), 2)
        # cv2.line(img,(vertices[1]["x"],vertices[1]["y"]),(vertices[2]["x"],vertices[2]["y"]),(0, 255, 0), 2)
        # cv2.line(img,(vertices[2]["x"],vertices[2]["y"]),(vertices[3]["x"],vertices[3]["y"]),(0, 255, 0), 2)
        # cv2.line(img,(vertices[3]["x"],vertices[3]["y"]),(vertices[0]["x"],vertices[0]["y"]),(0, 255, 0), 2)
        # new_image=os.path.splitext(filename)[0]+"_roi"+os.path.splitext(filename)[1]
        # cv2.imwrite(new_image, img)

    def test_api_OCRIDCard_08(self, config_obj,testImage_ocr_idcard_quality, OcrApi):
        """验证身份证单接口_验证身份证质量按照等级输出_结果为extremely_high的时候不输出quality_item_正例"""
        detect_quality=True         
        resp = OcrApi.OCRIDCard(image=testImage_ocr_idcard_quality,detect_quality=detect_quality)
        assert resp.status_code == 200
        assert resp.json_get("quality_level")
        quality_level=resp.json_get("quality_level")
        if quality_level=="HIGH":
             assert "quality_items" not in resp.resp_json
        else:
             assert resp.json_get("quality_items")


    def test_api_OCRIDCard_10(self, config_obj,testImage_ocr_idcard_back_long_time, OcrApi):
        """验证身份证单接口_验证身份证反面失效时间为长期时输出000"""
        resp = OcrApi.OCRIDCard(image=testImage_ocr_idcard_back_long_time)
        assert resp.status_code == 200
        expiry_date=resp.json_get("idcard.expiry_date")
        assert expiry_date=="0000"

    def test_api_OCRIDCard_11(self, config_obj,testImage_ocr_idcard_common, OcrApi):
        """验证身份证单接口_输入为原件的时候来源为原件. """
        side = 'FRONT'              
        resp = OcrApi.OCRIDCard(testImage_ocr_idcard_common, side=side)
        assert resp.status_code == 200
        assert resp.resp_json["idcard"]["idcard_source"]=="ORIGIN"

    def test_api_OCRIDCard_roi(self, config_obj, testImage_ocr_idcard_roi,OcrApi):
        """验证icard接口_验证ROI"""
        resp = OcrApi.OCRIDCard(testImage_ocr_idcard_roi)
        assert resp.status_code == 200
        detail=resp.json_get("detailed_info")
        for key,item in detail["detect_details"].items():
            if  "idcard_source" not in key:
                vertices=item["roi"]["vertices"]
                filename=os.path.join(config.ids_image_path,testImage_ocr_idcard_roi)
                suffix = item["field_name"]
                image_draw_rectangle(filename, suffix, vertices)
                # img=cv2.imread(filename)
                # cv2.line(img,(vertices[0]["x"],vertices[0]["y"]),(vertices[1]["x"],vertices[1]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[1]["x"],vertices[1]["y"]),(vertices[2]["x"],vertices[2]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[2]["x"],vertices[2]["y"]),(vertices[3]["x"],vertices[3]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[3]["x"],vertices[3]["y"]),(vertices[0]["x"],vertices[0]["y"]),(255, 0, 0), 2)
                # new_image=os.path.splitext(filename)[0]+item["field_name"]+os.path.splitext(filename)[1]
                # cv2.imwrite(new_image, img)

        

  
    def test_api_OCRPassport_01(self, config_obj, testImage_ocr_passport,OcrApi):
        """验证护照单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_正例"""
        resp = OcrApi.OCRPassport(testImage_ocr_passport)
        assert resp.status_code == 200
        # required_list=["type","country_code","passport_no","name","sex","nationality","birth_date","birth_place","issue_date","issue_place","expiry_date","authority","mrz_code_1","mrz_code_2"]
        required_list=["type","country_code","passport_no","sex","nationality","birth_date","birth_place","issue_place","expiry_date","authority","mrz_code_1","mrz_code_2"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="passport"), "Json_schema验证失败"

    @pytest.mark.skip("ids1.11此特性产品暂时不加")
    def test_api_OCRPassport_roi(self, config_obj, testImage_ocr_passpor_roi,OcrApi):
        """验证护照单接口_验证ROI"""
        resp = OcrApi.OCRPassport(testImage_ocr_passpor_roi)
        assert resp.status_code == 200
        detail=resp.json_get("detailed_info")
        for key,item in detail["detect_details"].items():
            if  len(item["roi"])!=0:
                vertices=item["roi"]["vertices"]
                filename=os.path.join(config.ids_image_path,testImage_ocr_passpor_roi)
                suffix = item["field_name"]
                image_draw_rectangle(filename, suffix, vertices)
                # img=cv2.imread(filename)
                # cv2.line(img,(vertices[0]["x"],vertices[0]["y"]),(vertices[1]["x"],vertices[1]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[1]["x"],vertices[1]["y"]),(vertices[2]["x"],vertices[2]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[2]["x"],vertices[2]["y"]),(vertices[3]["x"],vertices[3]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[3]["x"],vertices[3]["y"]),(vertices[0]["x"],vertices[0]["y"]),(255, 0, 0), 2)
                # new_image=os.path.splitext(filename)[0]+item["field_name"]+os.path.splitext(filename)[1]
                # cv2.imwrite(new_image, img)
        passport=resp.json_get("passport")
        assert len(passport)==len(detail["detect_details"])


    def test_api_OCRPassport_02(self, config_obj, testImage_ocr_passport_common,OcrApi,user_info):
        """验证护照单接口_验证加密功能_image参数加且response加密_正例"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_passport_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRPassport(encrypt_info=encrypt_info)
        assert resp.status_code == 200   
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="passport":
                    ocrPassport=data_json[k]        
        # required_list=["type","country_code","passport_no","name","sex","nationality","birth_date","birth_place","issue_date","issue_place","expiry_date","authority","mrz_code_1","mrz_code_2"]
        required_list=["type","country_code","passport_no","sex","nationality","birth_date","birth_place","issue_place","expiry_date","authority","mrz_code_1","mrz_code_2"]
        ocrPassport_schema = resp.get_definitions_by_name("ocrPassport")  # 根据名字获取definitions
        ocrPassport_schema.update({"required": required_list})
        assert schema_validator(ocrPassport, ocrPassport_schema)
        

    def test_api_OCRPassport_02_1(self, config_obj, testImage_ocr_passport_common,OcrApi,user_info):
        """验证护照单接口_验证gcm加密功能_image参数加且response加密_正例"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_passport_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRPassport(encrypt_info=encrypt_info)
        assert resp.status_code == 200   
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="passport":
                    ocrPassport=data_json[k]        
        # required_list=["type","country_code","passport_no","name","sex","nationality","birth_date","birth_place","issue_date","issue_place","expiry_date","authority","mrz_code_1","mrz_code_2"]
        required_list=["type","country_code","passport_no","sex","nationality","birth_date","birth_place","issue_place","expiry_date","authority","mrz_code_1","mrz_code_2"]
        ocrPassport_schema = resp.get_definitions_by_name("ocrPassport")  # 根据名字获取definitions
        ocrPassport_schema.update({"required": required_list})
        assert schema_validator(ocrPassport, ocrPassport_schema)
        


    def test_api_OCRTaiwanExitEntryPermit_01(self, config_obj,testImage_ocr_taiwan_exit_entry_permit, OcrApi):
        """验证台湾通行证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_正例"""
        resp = OcrApi.OCRTaiwanExitEntryPermit(testImage_ocr_taiwan_exit_entry_permit)
        assert resp.status_code == 200
        required_list=["issue_address","birth_date","card_number","name","name_pinyin","sex","expiry_date"]

        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="taiwan_exit_entry_permit"), "Json_schema验证失败"

    @pytest.mark.skip("ids1.11此特性产品暂时不加")
    def test_api_OCRTaiwanExitEntryPermit_roi(self, config_obj,testImage_ocr_taiwan_exit_entry_permit_roi, OcrApi):
        """验证台湾通行证单接口_验证roi"""
        resp = OcrApi.OCRTaiwanExitEntryPermit(testImage_ocr_taiwan_exit_entry_permit_roi)
        assert resp.status_code == 200
        detail=resp.json_get("detailed_info")
        for key,item in detail["detect_details"].items():
            if  len(item["roi"])!=0:
                vertices=item["roi"]["vertices"]
                filename=os.path.join(config.ids_image_path,testImage_ocr_taiwan_exit_entry_permit_roi)
                suffix = item["field_name"]
                image_draw_rectangle(filename, suffix, vertices)
                # img=cv2.imread(filename)
                # cv2.line(img,(vertices[0]["x"],vertices[0]["y"]),(vertices[1]["x"],vertices[1]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[1]["x"],vertices[1]["y"]),(vertices[2]["x"],vertices[2]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[2]["x"],vertices[2]["y"]),(vertices[3]["x"],vertices[3]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[3]["x"],vertices[3]["y"]),(vertices[0]["x"],vertices[0]["y"]),(255, 0, 0), 2)
                # new_image=os.path.splitext(filename)[0]+item["field_name"]+os.path.splitext(filename)[1]
                # cv2.imwrite(new_image, img)
        taiwan_exit_entry_permit=resp.json_get("taiwan_exit_entry_permit")
        assert len(taiwan_exit_entry_permit)==len(detail["detect_details"])




    def test_api_OCRTaiwanExitEntryPermit_02(self, config_obj,testImage_ocr_taiwan_exit_entry_permit_common, OcrApi,user_info):
        """验证台湾通行证接口_验证加密功能_image参数加且response加密_正例"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_taiwan_exit_entry_permit_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRTaiwanExitEntryPermit(image="", encrypt_info=encrypt_info)
        assert resp.status_code == 200   
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="taiwan_exit_entry_permit":
                    ocrTaiwanExitEntryPermit=data_json[k]     
        required_list=["issue_address","birth_date","card_number","name","name_pinyin","sex","expiry_date"]
        ocrTaiwanExitEntryPermit_schema = resp.get_definitions_by_name("ocrTaiwanExitEntryPermit")  # 根据名字获取definitions
        ocrTaiwanExitEntryPermit_schema.update({"required": required_list})
        assert schema_validator(ocrTaiwanExitEntryPermit, ocrTaiwanExitEntryPermit_schema)


    def test_api_OCRTaiwanExitEntryPermit_02_1(self, config_obj,testImage_ocr_taiwan_exit_entry_permit_common, OcrApi,user_info):
        """验证台湾通行证接口_验证gcm加密功能_image参数加且response加密_正例"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_taiwan_exit_entry_permit_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRTaiwanExitEntryPermit(image="", encrypt_info=encrypt_info)
        assert resp.status_code == 200   
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="taiwan_exit_entry_permit":
                    ocrTaiwanExitEntryPermit=data_json[k]     
        required_list=["issue_address","birth_date","card_number","name","name_pinyin","sex","expiry_date"]
        ocrTaiwanExitEntryPermit_schema = resp.get_definitions_by_name("ocrTaiwanExitEntryPermit")  # 根据名字获取definitions
        ocrTaiwanExitEntryPermit_schema.update({"required": required_list})
        assert schema_validator(ocrTaiwanExitEntryPermit, ocrTaiwanExitEntryPermit_schema)


    def test_api_OCRVehicleLicense_01(self, config_obj,testImage_ocr_vehicle_license_01, OcrApi):
        """验证行驶证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_两页一起_正例"""
        resp = OcrApi.OCRVehicleLicense(testImage_ocr_vehicle_license_01)
        assert resp.status_code == 200
        #第一页
        required_list=["plate_no","vehicle_type","owner","address","use_character","model","vin","engine_no","register_date","issue_date"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="first_page"), "Json_schema验证失败"
          
        #第二页
        required_list=["plate_no","apc","gross_mass","unladen_mass","overall_dimension","inspection_record","barcode"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="second_page"), "Json_schema验证失败"
    @pytest.mark.skip("ids1.11此特性产品暂时不加")
    def test_api_OCRVehicleLicense_roi(self, config_obj,testImage_ocr_vehicle_license_roi, OcrApi):
        """验证行驶证单接口_验证roi"""
        resp = OcrApi.OCRVehicleLicense(testImage_ocr_vehicle_license_roi)
        assert resp.status_code == 200
        detail=resp.json_get("detailed_info")
        for key,item in detail["detect_details"].items():
            if  len(item["roi"])!=0:
                vertices=item["roi"]["vertices"]
                filename=os.path.join(config.ids_image_path,testImage_ocr_vehicle_license_roi)
                suffix = item["field_name"]
                image_draw_rectangle(filename, suffix, vertices)
                # img=cv2.imread(filename)
                # cv2.line(img,(vertices[0]["x"],vertices[0]["y"]),(vertices[1]["x"],vertices[1]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[1]["x"],vertices[1]["y"]),(vertices[2]["x"],vertices[2]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[2]["x"],vertices[2]["y"]),(vertices[3]["x"],vertices[3]["y"]),(255, 0, 0), 2)
                # cv2.line(img,(vertices[3]["x"],vertices[3]["y"]),(vertices[0]["x"],vertices[0]["y"]),(255, 0, 0), 2)
                # new_image=os.path.splitext(filename)[0]+item["field_name"]+os.path.splitext(filename)[1]
                # cv2.imwrite(new_image, img)
        second_page=resp.json_get("second_page")
        first_page=resp.json_get("first_page")

        assert (len(first_page)+len(second_page))==len(detail["detect_details"])

    def test_api_OCRVehicleLicense_02(self, config_obj,testImage_ocr_vehicle_license_first, OcrApi):
        """验证行驶证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_第一页_正例"""
        resp = OcrApi.OCRVehicleLicense(testImage_ocr_vehicle_license_first)
        assert resp.status_code == 200
        required_list=["plate_no","vehicle_type","owner","address","use_character","model","vin","engine_no","register_date","issue_date"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="first_page"), "Json_schema验证失败"
                     
                     

    def test_api_OCRVehicleLicense_03(self, config_obj,testImage_ocr_vehicle_license_second, OcrApi):
        """验证行驶证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_第二页_正例"""
        resp = OcrApi.OCRVehicleLicense(testImage_ocr_vehicle_license_second)
        assert resp.status_code == 200
        #第二页
        required_list=["plate_no","apc","gross_mass","unladen_mass","overall_dimension","inspection_record"]
        # required_list=["plate_no","apc","gross_mass","unladen_mass","overall_dimension","inspection_record","barcode"]

        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="second_page"), "Json_schema验证失败"

    # def test_api_OCRVehicleLicense_04(self, config_obj,testImage_ocr_vehicle_license_extra, OcrApi):
    #     """验证行驶证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_第三页_正例"""
    #     resp = OcrApi.OCRVehicleLicense(testImage_ocr_vehicle_license_extra)
    #     assert resp.status_code == 200
    #     #确保有第三页的字段
    #     required_list=["inspection_record"]
    #     assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="extra_page"), "Json_schema验证失败"

    def test_api_OCRVehicleLicense_05(self, config_obj,testImage_ocr_vehicle_license_common, OcrApi,user_info):
        """验证行驶证接口_验证加密功能_image参数加且response加密_正例"""
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_vehicle_license_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRVehicleLicense(encrypt_info=encrypt_info)
        assert resp.status_code == 200         
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="first_page":
                    ocrVehicleFirstPage=data_json[k]
            if k=="second_page":
                    ocrVehicleSecondPage=data_json[k]     
        #第一页
        required_list=["plate_no","vehicle_type","owner","address","use_character","model","vin","engine_no","register_date","issue_date"]
        ocrVehicleFirstPage_schema = resp.get_definitions_by_name("ocrVehicleFirstPage")  # 根据名字获取definitions
        ocrVehicleFirstPage_schema.update({"required": required_list})
        assert schema_validator(ocrVehicleFirstPage, ocrVehicleFirstPage_schema)
        #第二页
        required_list=["plate_no","apc","gross_mass","unladen_mass","overall_dimension","inspection_record","barcode"]
        ocrVehicleSecondPage_schema = resp.get_definitions_by_name("ocrVehicleSecondPage")  # 根据名字获取definitions
        ocrVehicleSecondPage_schema.update({"required": required_list})
        assert schema_validator(ocrVehicleSecondPage, ocrVehicleSecondPage_schema)



    def test_api_OCRVehicleLicense_05_1(self, config_obj,testImage_ocr_vehicle_license_common, OcrApi,user_info):
        """验证行驶证接口_验证gcm加密功能_image参数加且response加密_正例"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": OcrApi.idsImageToBase64(testImage_ocr_vehicle_license_common)}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = OcrApi.OCRVehicleLicense(encrypt_info=encrypt_info)
        assert resp.status_code == 200         
        encrypt_info_data=resp.resp_json["encrypt_info"]["data"]
        encrypt_info_feilds=resp.resp_json["encrypt_info"]["encrypted_fields"]
        data=cryptor.decrypt(encrypt_info_data)  
        data_json=json.loads(data)
        for k in encrypt_info_feilds:
            if k=="first_page":
                    ocrVehicleFirstPage=data_json[k]
            if k=="second_page":
                    ocrVehicleSecondPage=data_json[k]     
        #第一页
        required_list=["plate_no","vehicle_type","owner","address","use_character","model","vin","engine_no","register_date","issue_date"]
        ocrVehicleFirstPage_schema = resp.get_definitions_by_name("ocrVehicleFirstPage")  # 根据名字获取definitions
        ocrVehicleFirstPage_schema.update({"required": required_list})
        assert schema_validator(ocrVehicleFirstPage, ocrVehicleFirstPage_schema)
        #第二页
        required_list=["plate_no","apc","gross_mass","unladen_mass","overall_dimension","inspection_record","barcode"]
        ocrVehicleSecondPage_schema = resp.get_definitions_by_name("ocrVehicleSecondPage")  # 根据名字获取definitions
        ocrVehicleSecondPage_schema.update({"required": required_list})
        assert schema_validator(ocrVehicleSecondPage, ocrVehicleSecondPage_schema)




 
if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])
