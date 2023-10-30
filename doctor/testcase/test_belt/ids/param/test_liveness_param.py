import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.P0
class TestFaceLivenessApi(object):
    """ face Liveness Api测试"""

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


    invalidencrypt_info={
        "algorithm": "",
        "version": 0,
        "iv": "string",
        "encrypted_fields": [
        "string"
        ],
        "data": "string"
    }
    image5M = os.path.join(
            config.image_path, "go_image/ids_face/Q19.png")
    
    @pytest.mark.parametrize("invalidParam",[
        ('image', ""),
        ('image', "fdafdasfdsaf"),
        ('image', image5M),
        ('min_quality_level', ''),
        ('min_quality_level', 'YYY' ),
        ('disable_defake', ''),
        ('disable_defake', '342432' ),
        ('encrypt_info', '' ),
        ('encrypt_info', 'invalidencrypt_info' ),
    ])
    def test_api_Liveness_normal(self, invalidParam,config_obj, FaceApi):
        """  提供图片静默活体检测 """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q1.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = True
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 5,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        intef = FaceApi.FaceService_DetectLivenessPostApi(
            image=image, min_quality_level=min_quality_level, disable_defake=disable_defake, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200