#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from commonlib.api_lib.base_api import BaseApi
from commonlib.config import ids_image_path
from commonlib.api_lib.AES_new import *
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
# from PIL import Image, ImageDraw, ImageFont

@pytest.mark.Regression
class TestOcrCarPlateApi(object):
    """ ocr CarPlate Api测试"""

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

    @pytest.mark.P0 
    def test_api_OCRService_normal_blue_OCRCarPlate(self, config_obj, OcrApi):
        """  正向：正确识别图片中的蓝牌及车牌号 """
        imagepath = os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_blue.jpg")
        image = BaseApi.imageToBase64(imagepath)
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        # image_draw(imagepath, resp.json_get("car_plates.0.roi.vertices"))
        assert resp.status_code == 200
        assert resp.json_get("car_plates.0.color") == "BLUE"
        assert resp.json_get("car_plates.0.number") == "苏ED8WQ6"
        assert resp.json_get("car_plates.0.confidence") >= 0.99
        # assert resp.json_get("car_plates.0.roi.vertices") == [{"x": 127,"y": 125},{"x": 277,"y": 168}]
        assert resp.json_get("car_plates.0.is_valid") == True
        
    
    @pytest.mark.P0 
    def test_api_OCRService_normal_green_OCRCarPlate(self, config_obj, OcrApi):
        """  正向：正确识别图片中的绿牌及车牌号JPG """
        imagepath = os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_green.jpg")
        image = BaseApi.imageToBase64(imagepath)
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("car_plates.0.color") == "GREEN"
        assert resp.json_get("car_plates.0.number") == "云AD16666"
        assert resp.json_get("car_plates.0.confidence") >= 0.99
        # assert resp.json_get("car_plates.0.roi.vertices") == [{"x":210, "y":221}, {"x":447, "y":285}]
        assert resp.json_get("car_plates.0.is_valid") == True 
        
    @pytest.mark.P0     
    def test_api_OCRService_normal_AES_256_CBC(self, config_obj, OcrApi,user_info):
        """  正向：正确识别图片中的蓝牌及车牌号AES_256_CBC加密 """
        image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_blue.jpg"))
        jstr = {
            "image": image,
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["image","car_plates"],
            "data": cypher
 
        }  
        resp = OcrApi.OCRService_OCRCarPlatePostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("encrypt_info.algorithm")=="AES_256_CBC"
        encrypted_data = resp.json_get("encrypt_info.data")
        decrypted_data = cryptor.decrypt(encrypted_data)
        car_plates_json=json.loads(decrypted_data)["car_plates"][0]
        log().info(f"car_plates_json:{car_plates_json}")    
        assert car_plates_json["color"] == "BLUE"
        assert car_plates_json["number"] == "苏ED8WQ6"
        assert car_plates_json["confidence"] >= 0.99
        # assert car_plates_json["roi"]["vertices"] == [{"x": 127,"y": 124},{"x": 278,"y": 168}]
        assert car_plates_json["is_valid"] == True
        
    @pytest.mark.P0    
    def test_api_OCRService_normal_AES_256_GCM(self, config_obj, OcrApi,user_info):
        """  正向：正确识别图片中的绿牌及车牌号AES_256_GCM加密 """
        image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_green.jpg"))
        jstr = {
            "image": image,
        }
        cryptor = AESGCMCryptor(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": ["image","car_plates"],
            "data": cypher
        }
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("encrypt_info.algorithm")=="AES_256_GCM"
        encrypted_data = resp.json_get("encrypt_info.data")
        decrypted_data = cryptor.decrypt(encrypted_data)
        car_plates_json=json.loads(decrypted_data)["car_plates"][0]
        log().info(f"car_plates_json:{car_plates_json}")    
        assert car_plates_json["color"] == "GREEN"
        assert car_plates_json["number"] == "云AD16666"
        assert car_plates_json["confidence"] >= 0.99
        # assert car_plates_json["roi"]["vertices"] == [{"x":210, "y":221}, {"x":447, "y":285}]
        assert car_plates_json["is_valid"] == True
        
    @pytest.mark.P1
    def test_api_OCRService_normal_yellow_green_OCRCarPlate(self, config_obj, OcrApi):
        """  正向：正确识别图片中的黄绿牌及车牌号JPEG """
        imagepath = os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_yellow_blue.jpeg")
        image = BaseApi.imageToBase64(imagepath)
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("car_plates.0.color") == "YELLOW_GREEN"
        assert resp.json_get("car_plates.0.number") == "川B12122F"
        assert resp.json_get("car_plates.0.confidence") >= 0.99
        # assert resp.json_get("car_plates.0.roi.vertices") == [{"x":454, "y":633}, {"x":855, "y":747}]
        assert resp.json_get("car_plates.0.is_valid") == True 
        
    @pytest.mark.P1
    def test_api_OCRService_normal_yellow_OCRCarPlate(self, config_obj, OcrApi):
        """  正向：正确识别图片中的黄牌及车牌号 """
        imagepath = os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_yellow.jpeg")
        image = BaseApi.imageToBase64(imagepath)
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("car_plates.0.color") == "YELLOW"
        assert resp.json_get("car_plates.0.number") == "京ADP329"
        assert resp.json_get("car_plates.0.confidence") >= 0.99
        # assert resp.json_get("car_plates.0.roi.vertices") == [{"x":169, "y":288}, {"x":354, "y":351}]
        assert resp.json_get("car_plates.0.is_valid") == True     

    def test_api_OCRService_normal_double_line_OCRCarPlate(self, config_obj, OcrApi):
        """  正向：正确识别图片中的双行黄色车牌 """
        imagepath = os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_double_line.jpeg")
        image = BaseApi.imageToBase64(imagepath)
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200   
        assert resp.json_get("car_plates.0.color") == "YELLOW"  
        assert resp.json_get("car_plates.0.number") == "京ADP329"   
        assert resp.json_get("car_plates.0.confidence") >= 0.999
        # assert resp.json_get("car_plates.0.roi.vertices") == [{"x":403, "y":281}, {"x":555, "y":352}]
        assert resp.json_get("car_plates.0.is_valid") == True 
        
    @pytest.mark.P1
    def test_api_OCRService_normal_white_OCRCarPlate(self, config_obj, OcrApi):
        """  正向：正确识别图片中的白色牌及车牌号PNG """
        imagepath = os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_white_3.png")
        image = BaseApi.imageToBase64(imagepath)
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("car_plates.0.color") == "WHITE"
        assert resp.json_get("car_plates.0.number") == "鲁B2127警"
        assert resp.json_get("car_plates.0.confidence") >= 0.998
        # assert resp.json_get("car_plates.0.roi.vertices") == [{"x":264, "y":108}, {"x":400, "y":168}]
        assert resp.json_get("car_plates.0.is_valid") == True         
        
            
    @pytest.mark.P1
    def test_api_OCRService_normal_black_OCRCarPlate(self, config_obj, OcrApi):
        """  正向：正确识别图片中的黑色牌及车牌号BMP """
        # imagepath = os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_black.bmp")
        imagepath = os.path.join(ids_image_path,"ocr/car_plate/normal_car_plate_black_1.bmp")
        image = BaseApi.imageToBase64(imagepath)
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("car_plates.0.color") == "BLACK"
        # assert resp.json_get("car_plates.0.number") == "粤B70146"
        assert resp.json_get("car_plates.0.number") == "粤Z9332澳"
        assert resp.json_get("car_plates.0.confidence") >= 0.999
        # assert resp.json_get("car_plates.0.roi.vertices") == [{"x":137, "y":81}, {"x":833, "y":464}]
        assert resp.json_get("car_plates.0.is_valid") == True  
        
    @pytest.mark.P1
    def test_api_OCRService_temporary_OCRCarPlate(self, config_obj, OcrApi):
        """  正向：正确识别图片中的临时车牌 """
        image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/car_plate/temporary_car_plate_02.jpeg"))
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200      
        # assert resp.json_get("car_plates.0.color") == "WHITE"
        assert resp.json_get("car_plates.0.number") == "桂B3574J"
        assert resp.json_get("car_plates.0.confidence") >= 0.99
        # assert resp.json_get("car_plates.0.roi.vertices") == [{"x":161, "y":148}, {"x":261, "y":190}]
        assert resp.json_get("car_plates.0.is_valid") == True  
        
    @pytest.mark.skip(reason="车牌识别，不支持带角度的图片")
    @pytest.mark.parametrize("rotatedImage", [
        "normal_car_plate_90.jpg",
        "normal_car_plate_180.jpg",
        "normal_car_plate_270.jpg"
    ])
    def test_api_OCRService_rotated_OCRCarPlate(self, config_obj, OcrApi,rotatedImage):
        """  正向：车牌图片带角度90,180,270 """
        image = BaseApi.imageToBase64(os.path.join(ids_image_path,f"ocr/car_plate/{rotatedImage}"))
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("car_plates.0.color") == "BLUE"
        assert resp.json_get("car_plates.0.number") == "苏ED8WQ6"
        assert resp.json_get("car_plates.0.confidence") >= 0.9999
        assert resp.json_get("car_plates.0.roi.vertices") == [{"x": 127,"y": 124},{"x": 278,"y": 168}]
        assert resp.json_get("car_plates.0.is_valid") == True
          
        
    @pytest.mark.P1
    @pytest.mark.parametrize("invalidImage", [
        "invalid_car_plate_1.jpg",
        "invalid_car_plate_2.jpg",
        "invalid_car_plate_3.jpg"
    ])
    def test_api_OCRService_isinvalid_OCRCarPlate(self, config_obj, OcrApi,invalidImage):
        """  正向：传统车牌不可信第一位invalid、第二位invalid、序号长度错"""
        image = BaseApi.imageToBase64(os.path.join(ids_image_path,f"ocr/car_plate/{invalidImage}"))
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("car_plates.0.is_valid") == False          
         
    @pytest.mark.P1
    def test_api_OCRService_image_none(self, config_obj, OcrApi):
        """  异常：未输入image """
        image = None
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "image data is empty"
        assert resp.json_get("error.details.0.reason") == 12003006
        assert resp.json_get("error.message") == "E12003006: image data is empty"      
        
    @pytest.mark.P1    
    def test_api_OCRService_invalid_param(self, config_obj, OcrApi):
        """  异常：输入参数image非图片 """
        image = "invalid"
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid image"
        assert resp.json_get("error.details.0.reason") == 12003007
        assert resp.json_get("error.message") == "E12003007: invalid image"  
        
    @pytest.mark.P1
    @pytest.mark.parametrize("invalidImageTpye", [
        "unsupport_gif.gif",
        "unsupport_tif.tif",
        "unsupport_webp.webp"
    ])
    def test_api_OCRService_invalidtype_OCRCarPlate(self, config_obj, OcrApi,invalidImageTpye):
        """  异常：输入参数image不支持的图片格式 """
        image = BaseApi.imageToBase64(os.path.join(ids_image_path,f"ocr/car_plate/{invalidImageTpye}"))
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid image"
        assert resp.json_get("error.details.0.reason") == 12003007
        assert resp.json_get("error.message") == "E12003007: invalid image"        
                
        
    @pytest.mark.P1    
    def test_api_OCRService_no_car_plate(self, config_obj, OcrApi):
        """  异常：输入无车牌图片 """
        image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/car_plate/no_car_plate.jpg"))
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no car plate detected"
        assert resp.json_get("error.details.0.reason") == 12003110
        assert resp.json_get("error.message") == "E12003110: no car plate detected"        
        
    @pytest.mark.P1    
    def test_api_OCRService_invalid_image_too_big(self, config_obj, OcrApi):
        """  异常：输入图片过大超出4M """
        image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/beyond_size_7M.jpg"))
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "image size is exceeded"
        assert resp.json_get("error.details.0.reason") == 12003005
        assert resp.json_get("error.message") == "E12003005: image size is exceeded"     
        
    def test_api_OCRService_invalid_image_low_resolutions(self, config_obj, OcrApi):
        """  异常：输入图片低分辨率<60*60 """
        image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/car_plate/low_resolution_car_plate.jpg"))
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "low image resolution"
        assert resp.json_get("error.details.0.reason") == 12003009
        assert resp.json_get("error.message") == "E12003009: low image resolution"       
        
        
# def image_draw(imgpath,box):
#     im = Image.open(imgpath)
#     draw = ImageDraw.Draw(im)
#     draw.rectangle([box[0]["x"],box[0]["y"], box[1]["x"],box[1]["y"]],  outline="#FFFFFF", width=3)
#     # 显示图片
#     #im.show()
#     im.save(os.path.dirname(imgpath)+"/labelbox_"+os.path.basename(imgpath))

               
    

