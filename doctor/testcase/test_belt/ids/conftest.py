#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import sys

import pytest

from commonlib import sign_utils
from commonlib.log_utils import log
from commonlib.sign_utils import encode_jwt_token
from defines.belt.face_service_business import FaceSwaggerBusiness


@pytest.fixture(scope='function')
def ids_config_obj(config_obj):
    """ids测试数据配置文件"""
    return config_obj._extra.test_data.ids_new


@pytest.fixture(scope='function')
def test_watermark_accuracy(ids_config_obj, request):
    """test_watermark_accuracy"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_have_watermarked(ids_config_obj, request):
    """test_have_watermarked"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_watermark(ids_config_obj, request):
    """test_watermark"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_hold_idcard_rotate(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_hold_idcard_1v1_suit(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_hold_idcard_1v1_not_suit(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_hold_idcard_no_face_in_idcard(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_hold_idcard(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)




@pytest.fixture(scope='function')
def test_hold_idcard_multiple_face(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_hold_idcard_one_face(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_hold_idcard_cropped(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)



@pytest.fixture(scope='function')
def test_hold_idcard_no_face(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)



@pytest.fixture(scope='function')
def test_hold_idcard_many_idcard(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_hold_idcard_small_face(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_hold_idcard_no_idcard(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_person_id_not_in_db(ids_config_obj, request):
    """test person id"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_person_id(ids_config_obj, request):
    """test person id"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_person_id_not_true(ids_config_obj, request):
    """test person id"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImages_multiple_faces(ids_config_obj, request):
    """test image for face1:1"""
    return ids_config_obj.get(request.param)
@pytest.fixture(scope='function')
def test_hold_idcard_fake(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_hold_idcard_low_resolution(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_hold_idcard_error_format(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_hold_idcard_outsize(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_hold_idcard_common(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_hold_idcard_format(ids_config_obj, request):
    """test image for ocr hold idcard"""
    return ids_config_obj.get(request.param)
#ocr
@pytest.fixture(scope='function')
def testImage_ocr_bankcard_format(ids_config_obj, request):
    """test image for ocr bankcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_bankcard_type(ids_config_obj, request):
    """test image for ocr bankcard"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_bankcard_roi(ids_config_obj, request):
    """test image for ocr bankcard"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_bankcard_common(ids_config_obj, request):
    """test image for ocr bankcard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_business_license(ids_config_obj, request):
    """test image for ocr business_license"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_business_roi(ids_config_obj, request):
    """test image for ocr business_license"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_business_license_common(ids_config_obj, request):
    """test image for ocr business_license"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_driving_license_01(ids_config_obj, request):
    """test image for ocr business_license"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_driving_license_roi(ids_config_obj, request):
    """test image for ocr business_license"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_driving_license_first(ids_config_obj, request):
    """test image for ocr business_license of first """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_driving_license_second(ids_config_obj, request):
    """test image for ocr business_license of  second"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_driving_license_common(ids_config_obj, request):
    """test image for ocr business_license"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_hk_macau_exit_entry_permit(ids_config_obj, request):
    """test image for ocr hk_macau_exit_entry_permit"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_hk_macau_exit_entry_permit_roi(ids_config_obj, request):
    """test image for ocr hk_macau_exit_entry_permit"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_hk_macau_exit_entry_permit_common(ids_config_obj, request):
    """test image for ocr hk_macau_exit_entry_permit"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_taiwan_exit_entry_permit(ids_config_obj, request):
    """test image for ocr taiwan_exit_entry_permit"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_taiwan_exit_entry_permit_roi(ids_config_obj, request):
    """test image for ocr taiwan_exit_entry_permit"""
    return ids_config_obj.get(request.param)



@pytest.fixture(scope='function')
def testImage_ocr_taiwan_exit_entry_permit_common(ids_config_obj, request):
    """test image for ocr taiwan_exit_entry_permit"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_idcard_01(ids_config_obj, request):
    """test image for ocr idcard for different image format which is FRONT"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_idcard_02(ids_config_obj, request):
    """test image for ocr idcard for different image format which is BACK"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_idcard_03(ids_config_obj, request):
    """test image for ocr idcard for checking quality"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_idcard_04(ids_config_obj, request):
    """test image for ocr idcard for different source"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_idcard_common(ids_config_obj, request):
    """test image for ocr idcard for different source"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_idcard_roi(ids_config_obj, request):
    """test image for ocr idcard for roi"""
    return ids_config_obj.get(request.param)
@pytest.fixture(scope='function')
def testImage_ocr_idcard_rect_roi(ids_config_obj, request):
    """test image for ocr idcard for roi"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_idcard_quality(ids_config_obj, request):
    """test image for ocr idcard for quality"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_passport(ids_config_obj, request):
    """test image for ocr passport"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_passpor_roi(ids_config_obj, request):
    """test image for ocr passport"""
    return ids_config_obj.get(request.param)



@pytest.fixture(scope='function')
def testImage_ocr_idcard_back_long_time(ids_config_obj, request):
    """test image for idcard back long time"""
    return ids_config_obj.get(request.param)



@pytest.fixture(scope='function')
def testImage_ocr_passport_common(ids_config_obj, request):
    """test image for ocr passport"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_vehicle_license_01(ids_config_obj, request):
    """test image for ocr vehicle_license"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_vehicle_license_roi(ids_config_obj, request):
    """test image for ocr vehicle_license"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_vehicle_license_first(ids_config_obj, request):
    """test image for ocr vehicle_license first"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_vehicle_license_second(ids_config_obj, request):
    """test image for ocr vehicle_license second"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_ocr_vehicle_license_extra(ids_config_obj, request):
    """test image for ocr vehicle_license extra"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testImage_ocr_vehicle_license_common(ids_config_obj, request):
    """test image for ocr vehicle_license first or second"""
    return ids_config_obj.get(request.param)


# 身份验证
@pytest.fixture(scope='function')
def expiry_date_right(ids_config_obj, request):
    """right expiry date """
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def expiry_date_wrong(ids_config_obj, request):
    """wrong expiry date """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCardFace_common_image_beyond_sie(ids_config_obj, request):
    """testVerifyIDCard out of size"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testVerifyIDCard_official(ids_config_obj, request):
    """testVerifyIDCard official"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCard_official_suit_wrong(ids_config_obj, request):
    """testVerifyIDCard wrong official """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCard_official_birth_wrong(ids_config_obj, request):
    """testVerifyIDCard wrong official """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCard_official_number_wrong(ids_config_obj, request):
    """testVerifyIDCard wrong official """
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testVerifyIDCard_official_name_wrong(ids_config_obj, request):
    """testVerifyIDCard wrong name """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCard_common(ids_config_obj, request):
    """testVerifyIDCard"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCardFace_official(ids_config_obj, request):
    """testVerifyIDCardFace """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCardFace_image_suit_wrong(ids_config_obj, request):
    """testVerifyIDCardFace """
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def testVerifyIDCardFace_suit_wrong(ids_config_obj, request):
    """testVerifyIDCardFace """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCardFace_official_resize(ids_config_obj, request):
    """testVerifyIDCardFace """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCardFace(ids_config_obj, request):
    """testVerifyIDCardFace """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testVerifyIDCardFace_common(ids_config_obj, request):
    """testVerifyIDCardFace """
    return ids_config_obj.get(request.param)

#face1:n
@pytest.fixture(scope='function')
def testImage_rotate(ids_config_obj, request):
    """testImage for face1:1 of rotate """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImages_format(ids_config_obj, request):
    """testImage for face1:1 of different format """
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImages_same(ids_config_obj, request):
    """testImage for face1:1 of same"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImages_similar(ids_config_obj, request):
    """testImage for face1:1 of similar"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImages_different(ids_config_obj, request):
    """testImage for face1:1 of different"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImage_rotate(ids_config_obj, request):
    """testImage for face1:1 of 90_180_270"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def testImages_badQuality(ids_config_obj, request):
    """testImage for face1:1 of badQuality """
    return ids_config_obj.get(request.param)

#face1:n
@pytest.fixture(scope='function')
def test_tag(ids_config_obj, request):

    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_topk(ids_config_obj, request):
    """test topk for face1:n when search person"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_tag_search_person(ids_config_obj, request):
    """test tag for face1:n when search person"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_tag_update_person(ids_config_obj, request):
    """test tag for face1:n when update person"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_invalid_tag_update_person(ids_config_obj, request):
    """test invalid tag for face1:n when update person"""
    return ids_config_obj.get(request.param)


@pytest.fixture(scope='function')
def test_invalid_extra_info(ids_config_obj, request):
    """test invalid extra_info for face1:n when update person"""
    return ids_config_obj.get(request.param)

@pytest.fixture(scope='function')
def test_extra_info(ids_config_obj, request):
    """test extra_info for face1:n when update person"""
    return ids_config_obj.get(request.param)
        
@pytest.fixture(scope='function')
def create_session(config_obj,IdentityApi,cache_obj):
    """ before create session for h5 internal api test """
    key = '%s_%s' % (sys._getframe().f_code.co_name, 'biztoken')

    def cache_func():
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
                "certificate_types":[
                     "IDCARD"],
            "expiry_date": "",
            "certificate_type":"IDCARD"
            }

        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        biz_token = resp.json_get("biz_token")
        log().info("class biz_token:%s" % biz_token)
        return biz_token,None
    yield cache_obj.get_value(key, func=cache_func)    

@pytest.fixture(scope='function')
def db_operation(config_obj, FaceApi, cache_obj):
    """ before test create db and tag, after test del db"""
    key = '%s_%s' % (sys._getframe().f_code.co_name, 'git')

    def cache_func():
        name = "autotest4" + sign_utils.getUuid(5)
        resp = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description="automation test db")
        db_id = resp.json_get("id")
        tag_ids = []
        # for i in range(11):
        #     resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=f"标签{i}")
        #     tag_ids.append(resp.resp_json["tag_id"])
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name="测试标签")
        tag_ids.append(resp.resp_json["tag_id"])
        log().info("class db_id:%s" % db_id)
        log().info("class tag_ids:%s" % tag_ids)

        def clear_func():
            resp = FaceApi.FaceService_DeletePersonDBPostApi(id=db_id)

        return (db_id, tag_ids, name), clear_func

    yield cache_obj.get_value(key, func=cache_func)
