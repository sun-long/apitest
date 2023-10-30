#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import pytest
import requests
from commonlib.cache_dict import CacheDict
from defines.belt.authiam_service_business import AuthiamSwaggerBusiness
from defines.belt.argusdatacenter_service_business import ArgusdatacenterSwaggerBusiness
from defines.belt.argusips_service_business import ArgusipsSwaggerBusiness
from defines.belt.argusdb_service_business import ArgusdbSwaggerBusiness
from defines.belt.arguspedestrian_service_business import ArguspedestrianSwaggerBusiness
from defines.belt.argusrrs_service_business import ArgusrrsSwaggerBusiness
from defines.belt.authinternalauth_service_business import AuthinternalauthSwaggerBusiness
from defines.belt.lottery_service_business import LotterySwaggerBusiness
from defines.belt.billinternal_service_business import BillinternalSwaggerBusiness
from defines.belt.oplog_service_business import OplogSwaggerBusiness
from defines.belt.order_service_business import OrderSwaggerBusiness
from defines.belt.orderinternal_service_business import OrderinternalSwaggerBusiness
from defines.belt.product_service_business import ProductSwaggerBusiness
from defines.belt.rasmanager_service_business import RasmanagerSwaggerBusiness
from defines.belt.rasmanager_aide_service_business import RasmanagerAideSwaggerBusiness
from defines.belt.rasmanager_easybot_service_business import RasmanagerEasyBotSwaggerBusiness
from defines.belt.face_service_business import FaceSwaggerBusiness
from defines.belt.rascluster_service_business import RasclusterSwaggerBusiness
from defines.belt.rechargelog_service_business import RechargelogSwaggerBusiness
from defines.belt.spuop_service_business import SpuopSwaggerBusiness
from defines.belt.viperocr_service_business import ViperocrSwaggerBusiness
from defines.belt.adapter_service_business import AdapterSwaggerBusiness
from defines.belt.bill_service_business import BillSwaggerBusiness
from defines.belt.viperapplet_service_business import ViperappletSwaggerBusiness
from defines.belt.auth_service_business import AuthSwaggerBusiness
from defines.belt.user_service_business import UserSwaggerBusiness
from defines.belt.botmanager_service_business import BotmanagerSwaggerBusiness
from defines.belt.identity_service_business import IdentitySwaggerBusiness
from defines.belt.ocr_service_business import OcrSwaggerBusiness
from defines.belt.notificationinternal_service_business import NotificationinternalSwaggerBusiness
from defines.belt.device_service_business import DeviceSwaggerBusiness
from defines.belt.ipsocr_service_business import IpsocrSwaggerBusiness
from defines.belt.ipsapplet_service_business import IpsappletSwaggerBusiness
from defines.belt.notification_service_business import NotificationSwaggerBusiness
from defines.belt.viperopenapi_service_business import ViperopenapiSwaggerBusiness # 有bug
from defines.belt.videomanager_service_business import VideomanagerSwaggerBusiness
from defines.belt.deviceiotcenter_service_business import DeviceiotcenterSwaggerBusiness
from defines.belt.galaxybeltoplog_service_business import GalaxybeltoplogSwaggerBusiness
from defines.belt.galaxybeltproduct_service_business import GalaxybeltproductSwaggerBusiness
from defines.belt.galaxyoplog_service_business import GalaxyoplogSwaggerBusiness
from defines.belt.galaxyproduct_service_business import GalaxyproductSwaggerBusiness
from defines.belt.roadinspection_service_business import RoadinspectionSwaggerBusiness
from defines.belt.watermark_service_business import WatermarkSwaggerBusiness
from defines.belt.ctidservice_service_business import CtidServiceSwaggerBusiness

from commonlib.sign_utils import encode_jwt_token
from commonlib.sign_utils import getMd5

@pytest.fixture(scope='function')
def RoadinspectionApi(config_obj, ext_info, akToken):
    """ RoadinspectionApi API """
    host = config_obj.EnvInfo.BeltCloud.EdgeRasService
    return RoadinspectionSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def ArgusdatacenterApi(config_obj, ext_info, akToken):
    """ ArgusdatacenterApi API """
    host = config_obj.EnvInfo.BeltCloud.argusService
    return ArgusdatacenterSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def ArgusdbApi(config_obj, ext_info, akToken):
    """ ArgusdbApi API """
    host = config_obj.EnvInfo.BeltCloud.argusService
    return ArgusdbSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def ArgusipsApi(config_obj, ext_info, akToken):
    """ ArgusipsApi API """
    host = config_obj.EnvInfo.BeltCloud.argusService
    return ArgusipsSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def ArguspedestrianApi(config_obj, ext_info, akToken):
    """ ArguspedestrianApi API """
    host = config_obj.EnvInfo.BeltCloud.argusService
    return ArguspedestrianSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def ArgusrrsApi(config_obj, ext_info, akToken):
    """ ArgusrrsApi API """
    host = config_obj.EnvInfo.BeltCloud.argusService
    return ArgusrrsSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def GalaxybeltoplogDynamicApi(config_obj, ext_info, akToken):
    """ GalaxybeltoplogApi API """
    host = config_obj.EnvInfo.BeltCloud.galaxyService
    return GalaxybeltoplogSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken,
                                          prefix_path="/dynamic")

@pytest.fixture(scope='function')
def GalaxybeltoplogStaticApi(config_obj, ext_info, akToken):
    """ GalaxybeltoplogApi API """
    host = config_obj.EnvInfo.BeltCloud.galaxyService
    return GalaxybeltoplogSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken,
                                          prefix_path="/static")

@pytest.fixture(scope='function')
def GalaxybeltproductStaticApi(config_obj, ext_info, akTokenGalaxy):
    """ GalaxybeltproductApi static API """
    host = config_obj.EnvInfo.BeltCloud.galaxyService
    return GalaxybeltproductSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akTokenGalaxy,
                                            prefix_path="/static")

@pytest.fixture(scope='function')
def GalaxybeltproductDynamicApi(config_obj, ext_info, akTokenGalaxy):
    """ GalaxybeltproductApi static API """
    host = config_obj.EnvInfo.BeltCloud.galaxyService
    return GalaxybeltproductSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akTokenGalaxy,
                                            prefix_path="/dynamic")


@pytest.fixture(scope='function')
def CtidServiceApi(config_obj, ext_info):
    """ CtidServiceApi API """
    host = config_obj.EnvInfo.BeltCloud.ctidService
    return CtidServiceSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info)

@pytest.fixture(scope='function')
def akTokenGalaxy(user_info_galaxy):
    """ aksktoken"""
    ak = user_info_galaxy.ak
    sk = user_info_galaxy.sk
    return encode_jwt_token(ak, sk)

@pytest.fixture(scope='function')
def user_info_galaxy(config_obj, request):
    """ yaml中摄像机信息"""
    return config_obj.get(request.param)

@pytest.fixture(scope='function')
def GalaxyoplogApi(config_obj, ext_info):
    """ GalaxyoplogApi API """
    host = config_obj.EnvInfo.Galaxy.beltAdapterService
    user_info = config_obj.EnvInfo.Galaxy.user1
    return GalaxyoplogSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, user_info=user_info)


@pytest.fixture(scope='function')
def Galaxyproduct1Api(config_obj, ext_info):
    """ GalaxyproductApi API """
    host = config_obj.EnvInfo.Galaxy.beltAdapterService
    user_info = config_obj.EnvInfo.Galaxy.user1
    return GalaxyproductSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, user_info=user_info)

@pytest.fixture(scope='function')
def getProductUrls(Galaxyproduct1Api, consoleAdminToken, cache_obj):
    """获取视频下载地址"""
    """ 
         requestID:747e2c5f-cd53-4b32-96a6-06dfc60d13de
    """
    key = '%s_xxxxx' % (sys._getframe().f_code.co_name)

    def cache_func():
        fileNameList = [
            "DYNAMIC_VIDEO/1678185062.7948818/1678185062.7948818_1678185074967_1.mp4",
            "DYNAMIC_VIDEO/1678185062.7948818/1678185062.7948818_1678185075368_2.mp4",
            "DYNAMIC_VIDEO/1678185062.7948818/1678185062.7948818_1678185075368_2.mp4"
        ]
        # 这里调pre的接口
        intef = Galaxyproduct1Api.modifyProduct_1PostApi(fileNameList=fileNameList, loginToken=consoleAdminToken,
                                                       sendRequest=False)
        intef.set_host('https://sensegalaxy-pre-release.sensetime.com')
        resp = intef.request()
        assert resp.status_code == 200
        productUrls = resp.json_get('data.productUrls')

        def clear_func():
            pass

        return productUrls, clear_func

    yield cache_obj.get_value(key, func=cache_func)


@pytest.fixture(scope='function')
def RasmanagerAideApi(config_obj, ext_info, akToken):
    """ Rasmanager Aide Api API """
    host = config_obj.EnvInfo.BeltCloud.CrdService
    return RasmanagerAideSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def RasmanagerEasyBotApi(config_obj, ext_info, akToken):
    """ RasmanagerApi API """
    host = config_obj.EnvInfo.BeltCloud.CrdService
    return RasmanagerEasyBotSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def RasclusterApi(config_obj, ext_info, akToken):
    """ RasclusterApi API """
    host = config_obj.EnvInfo.BeltCloud.CrdService
    return RasclusterSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def ViperocrApi(config_obj, ext_info):
    """ ViperocrApi API """
    host = config_obj.EnvInfo.BeltCloud.RunTimeViperOcrService
    return ViperocrSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info)

@pytest.fixture(scope='function')
def WatermarkApi(config_obj, ext_info,akToken):
    """ WatermarkApi API """
    host = config_obj.EnvInfo.BeltCloud.EdgeService
    return WatermarkSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info,token=akToken)

@pytest.fixture(scope='function')
def FaceApi(config_obj, ext_info, akToken):
    """ FaceApi API """
    host = config_obj.EnvInfo.BeltCloud.EdgeService
    return FaceSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def OcrApi(config_obj, ext_info, akToken):
    """ OcrApi API """
    host = config_obj.EnvInfo.BeltCloud.EdgeService
    return OcrSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def IdentityApi(config_obj, ext_info, akToken):
    """ IdentityApi API """
    host = config_obj.EnvInfo.BeltCloud.EdgeService
    return IdentitySwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def AdapterApi(config_obj, ext_info):
    """ AdapterApi API """
    host = config_obj.EnvInfo.BeltCloud.AdapterService
    return AdapterSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info)


@pytest.fixture(scope='function')
def BillApi(config_obj, ext_info, loginToken):
    """ BillApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return BillSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginToken)

@pytest.fixture(scope='function')
def BillEnterpriseApi(config_obj, ext_info, loginEnterpriseToken):
    """ BillApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return BillSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginEnterpriseToken)

@pytest.fixture(scope='function')
def ViperappletApi(config_obj, ext_info):
    """ ViperappletApi API """
    host = config_obj.EnvInfo.BeltCloud.RunTimeViperAppletService
    return ViperappletSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info)


@pytest.fixture(scope='function')
def AuthApi(config_obj, ext_info, loginToken):
    """ AuthApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return AuthSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginToken)

@pytest.fixture(scope='function')
def AuthDoubleApi(config_obj, ext_info, loginDoubleToken):
    """ AuthApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return AuthSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginDoubleToken)

@pytest.fixture(scope='function')
def AuthEnterpriseApi(config_obj, ext_info, loginEnterpriseToken):
    """ AuthApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return AuthSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginEnterpriseToken)

@pytest.fixture(scope='function')
def AuthPersonApi(config_obj, ext_info, loginPersonToken):
    """ AuthApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return AuthSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginPersonToken)

@pytest.fixture(scope='function')
def UserApiMainUser(config_obj, ext_info, loginMainUserToken):
    """ UserApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return UserSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginMainUserToken)


@pytest.fixture(scope='function')
def UserApi(config_obj, ext_info, loginToken):
    """ UserApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return UserSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginToken)


@pytest.fixture(scope='function')
def BotmanagerApi(config_obj, ext_info, akToken):
    """ BotmanagerApi API """
    host = config_obj.EnvInfo.BeltCloud.CrdService
    return BotmanagerSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def RasmanagerApi(config_obj, ext_info, akToken):
    """ RasmanagerApi API """
    host = config_obj.EnvInfo.BeltCloud.CrdService
    return RasmanagerSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def NotificationinternalApi(config_obj, ext_info, internalLoginToken):
    """ NotificationinternalApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return NotificationinternalSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=internalLoginToken)


@pytest.fixture(scope='function')
def DeviceApi(config_obj, ext_info, akToken, RasmanagerApi):
    """ DeviceApi API """
    host = config_obj.EnvInfo.BeltCloud.CrdService
    ext_info.RasmanagerApi = RasmanagerApi
    return DeviceSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=akToken)


@pytest.fixture(scope='function')
def IpsocrApi(config_obj, ext_info):
    """ IpsocrApi API """
    host = config_obj.EnvInfo.BeltCloud.RunTimeProxyService
    return IpsocrSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info)


@pytest.fixture(scope='function')
def IpsappletApi(config_obj, ext_info):
    """ IpsappletApi API """
    host = config_obj.EnvInfo.BeltCloud.RunTimeProxyService
    return IpsappletSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info)


@pytest.fixture(scope='function')
def NotificationApi(config_obj, ext_info, loginToken):
    """ NotificationApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return NotificationSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginToken)

@pytest.fixture(scope='function')
def OrderApi(config_obj, ext_info, loginToken):
    """ OrderApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return OrderSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginToken)

@pytest.fixture(scope='function')
def OrderinternalApi(config_obj, ext_info, internalLoginToken):
    """ OrderApi API """
    host = config_obj.EnvInfo.BeltCloud.InternalService
    return OrderinternalSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=internalLoginToken)

@pytest.fixture(scope='function')
def AuthinternalauthApi(config_obj, ext_info, internalLoginToken):
    """ AuthinternalauthApi API """
    host = config_obj.EnvInfo.BeltCloud.InternalService
    return AuthinternalauthSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=internalLoginToken)

@pytest.fixture(scope='function')
def OplogApi(config_obj, ext_info, internalLoginToken):
    """ OplogApi API """
    host = config_obj.EnvInfo.BeltCloud.InternalService
    return OplogSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=internalLoginToken)

@pytest.fixture(scope='function')
def BillinternalApi(config_obj, ext_info, internalLoginToken):
    """ BillInternal API """
    host = config_obj.EnvInfo.BeltCloud.InternalService
    return BillinternalSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=internalLoginToken)


@pytest.fixture(scope='function')
def RechargelogApi(config_obj, ext_info, internalLoginToken):
    """ RechargelogApi API """
    host = config_obj.EnvInfo.BeltCloud.InternalService
    return RechargelogSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=internalLoginToken)

@pytest.fixture(scope='function')
def SpuopApi(config_obj, ext_info, internalLoginToken):
    """ SpuopApi API """
    host = config_obj.EnvInfo.BeltCloud.InternalService
    return SpuopSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=internalLoginToken)

@pytest.fixture(scope='function')
def RechargelogApiOpen(config_obj, ext_info, loginMainUserToken):
    """ RechargelogApiOpen API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return RechargelogSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info, token=loginMainUserToken)

@pytest.fixture(scope='function')
def ProductApi(config_obj, ext_info, loginToken):
    """ ProductApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return ProductSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=loginToken)

@pytest.fixture(scope='function')
def MainUserTokenForSpuop(loginTokenSpu):
    """ MainUserTokenForSpu """
    return loginTokenSpu

@pytest.fixture(scope='function')
def UserForFreeOrder(loginTokenFreeOrder):
    """ MainUserTokenForSpu """
    return loginTokenFreeOrder

@pytest.fixture(scope='function')
def PersonalTokenForSpuop(loginPersonToken):
    """ PersonalTokenForSpu"""
    return loginPersonToken

@pytest.fixture(scope='function')
def ViperopenapiApi(config_obj, ext_info):
    """ ViperopenapiApi API """
    host = config_obj.EnvInfo.BeltCloud.VipperService
    return ViperopenapiSwaggerBusiness(host, config_obj=config_obj, ext_info=ext_info)


@pytest.fixture(scope='function')
def LotteryApi(config_obj, ext_info, akToken):
    """ LotteryApi API """
    host = config_obj.EnvInfo.BeltCloud.EdgeRasService
    return LotterySwaggerBusiness(host, config_obj=config_obj,  token=akToken, ext_info=ext_info)


@pytest.fixture(scope="class")
def cache_obj():
    obj = CacheDict()
    yield obj
    obj.clear_func_all()


@pytest.fixture(scope='function')
def camera_info(config_obj, request):
    """ yaml中摄像机信息"""
    return config_obj.get(request.param)

@pytest.fixture(scope='function')
def recordTaskCamera_info(config_obj):
    """ yaml中录播任务摄像头信息"""
    return config_obj.Clients.SubDevice.recordTask


@pytest.fixture(scope='function')
def botApi(config_obj, request, RasmanagerEasyBotApi, RasmanagerAideApi):
    """ bot api"""
    if request.param == 'Bot.easyBot':
        return RasmanagerEasyBotApi
    elif request.param == 'Bot.aide':
        return RasmanagerAideApi
    else:
        raise Exception("invaild bot api")


@pytest.fixture(scope='function')
def botInfo(config_obj, request):
    """ bot api"""
    if request.param == 'Bot.easyBot':
        return config_obj.Bot.easyBot
    elif request.param == 'Bot.aide':
        return config_obj.Bot.aide
    else:
        raise Exception("invaild bot api")


@pytest.fixture(scope='function')
def cluster_info(config_obj, request):
    """ yaml中cluster信息"""
    return config_obj.get(request.param)


@pytest.fixture(scope='function')
def deviceKindAide(config_obj):
    """ 海目设备类型"""
    return config_obj.DeviceKindType.aide


@pytest.fixture(scope='function')
def deviceKindEasyBot(config_obj):
    """ EasyBot设备类型"""
    return config_obj.DeviceKindType.easyBot


@pytest.fixture(scope='function')
def EasyBotInfo(config_obj):
    """ Bot信息"""
    return config_obj.Bot.easyBot


@pytest.fixture(scope='function')
def AideBotInfo(config_obj):
    """ Bot信息"""
    return config_obj.Bot.aide


@pytest.fixture(scope='function')
def loginToken(config_obj, user_info, AuthiamApi, cache_obj):
    """ 测试环境登录图形验证码可以随便填，生产环境不可以"""
    key = '%s_console_%s' % (sys._getframe().f_code.co_name, user_info.username)

    def cache_func():
        userToken = user_info.userToken  # 读取配置文件
        if not userToken:
            # 获取captcha_id
            captcha_id = AuthiamApi.get_captcha(print_log=False)
            # 手机号登录
            resp = AuthiamApi.login_with_phone(user_info.username, user_info.password, captcha_id, "123456")
            # 用户名密码登录
            # resp = AuthiamApi.login_with_user(user_info.username, user_info.password, captcha_id, "123456")
            userToken = resp.json_get("access_token")

        def clear_func():
            pass
        return userToken, clear_func

    yield cache_obj.get_value(key, func=cache_func)

@pytest.fixture(scope='function')
def loginDoubleToken(config_obj, user_info_console, AuthiamApi, cache_obj):
    """ 测试环境登录图形验证码可以随便填，生产环境不可以"""
    key = '%s_console_%s' % (sys._getframe().f_code.co_name, user_info_console.username)

    def cache_func():
        userToken = user_info_console.userToken  # 读取配置文件
        if not userToken:
            # 获取captcha_id
            captcha_id = AuthiamApi.get_captcha(print_log=False)
            # 手机号登录
            resp = AuthiamApi.login_with_phone(user_info_console.username, user_info_console.password, captcha_id, "123456")
            # 用户名密码登录
            # resp = AuthiamApi.login_with_user(user_info.username, user_info.password, captcha_id, "123456")
            userToken = resp.json_get("access_token")

        def clear_func():
            pass
        return userToken, clear_func

    yield cache_obj.get_value(key, func=cache_func)

@pytest.fixture(scope='function')
def loginEnterpriseToken(config_obj, user_info_console_enterprise, AuthiamApi, cache_obj):
    """ 测试环境登录图形验证码可以随便填，生产环境不可以"""
    key = '%s_console_%s' % (sys._getframe().f_code.co_name, user_info_console_enterprise.username)

    def cache_func():
        userToken = user_info_console_enterprise.userToken  # 读取配置文件
        if not userToken:
            # 获取captcha_id
            captcha_id = AuthiamApi.get_captcha(print_log=False)
            # 手机号登录
            resp = AuthiamApi.login_with_phone(user_info_console_enterprise.username, user_info_console_enterprise.password, captcha_id, "123456")
            # 用户名密码登录
            # resp = AuthiamApi.login_with_user(user_info.username, user_info.password, captcha_id, "123456")
            userToken = resp.json_get("access_token")

        def clear_func():
            pass
        return userToken, clear_func

    yield cache_obj.get_value(key, func=cache_func)

@pytest.fixture(scope='function')
def loginPersonToken(config_obj, user_info_console_person, AuthiamApi, cache_obj):
    """ 测试环境登录图形验证码可以随便填，生产环境不可以"""
    key = '%s_console_%s' % (sys._getframe().f_code.co_name, user_info_console_person.username)

    def cache_func():
        userToken = user_info_console_person.userToken  # 读取配置文件
        if not userToken:
            # 获取captcha_id
            captcha_id = AuthiamApi.get_captcha(print_log=False)
            # 手机号登录
            resp = AuthiamApi.login_with_phone(user_info_console_person.username, user_info_console_person.password, captcha_id, "123456")
            # 用户名密码登录
            # resp = AuthiamApi.login_with_user(user_info.username, user_info.password, captcha_id, "123456")
            userToken = resp.json_get("access_token")

        def clear_func():
            pass
        return userToken, clear_func

    yield cache_obj.get_value(key, func=cache_func)
@pytest.fixture(scope='function')
def internalLoginToken(config_obj, internal_admin_user_info, AuthiamApi, cache_obj):
    """ 暂不使用"""
    key = '%s_internalConsole_%s' % (sys._getframe().f_code.co_name, internal_admin_user_info.username)

    def cache_func():
        userToken = internal_admin_user_info.userToken  # 读取配置文件
        if not userToken:
            # 获取captcha_id
            host = config_obj.EnvInfo.BeltCloud.deckService
            user_info = internal_admin_user_info
            url = "%s/belt-sso/v1/login" % host
            data = {
                "captcha":{
                    "id":"1",
                    "digits":"1"
                },
                "username": user_info.username,
                "password": getMd5(user_info.password),
                "source":"console-internal"
            }
            resp = requests.post(url, json=data)
            userToken = resp.json()["access_token"]

        def clear_func():
            pass

        return userToken, clear_func

    yield cache_obj.get_value(key, func=cache_func)

@pytest.fixture(scope='function')
def internalLoginTokenB(config_obj, internal_admin_user_info, AuthiamApi, cache_obj):
    """ 内部console token"""
    key = '%s_internalConsole_%s' % (sys._getframe().f_code.co_name, internal_admin_user_info.username)

    def cache_func():
        userToken = internal_admin_user_info.userToken  # 读取配置文件
        if not userToken:
            # 获取captcha_id
            captcha_id = AuthiamApi.get_captcha(print_log=False)
            # 手机号登录
            resp = AuthiamApi.login_with_phone(internal_admin_user_info.username, internal_admin_user_info.password, captcha_id, "123456", source="console")
            # 用户名密码登录
            # resp = AuthiamApi.login_with_user(internal_admin_user_info.username, internal_admin_user_info.password, captcha_id, "123456")
            userToken = resp.json_get("access_token")

        def clear_func():
            pass

        return userToken, clear_func

    yield cache_obj.get_value(key, func=cache_func)

@pytest.fixture(scope='function')
def loginMainUserToken(config_obj, user_info_console_mainUser, AuthiamApi, cache_obj):
    """ 测试环境登录图形验证码可以随便填，生产环境不可以"""
    key = '%s_console_%s' % (sys._getframe().f_code.co_name, user_info_console_mainUser.username)

    def cache_func():
        userToken = user_info_console_mainUser.userToken  # 读取配置文件
        if not userToken:
            # 获取captcha_id
            captcha_id = AuthiamApi.get_captcha(print_log=False)
            # 手机号登录
            resp = AuthiamApi.login_with_phone(user_info_console_mainUser.username, user_info_console_mainUser.password, captcha_id, "123456")
            # 用户名密码登录
            # resp = AuthiamApi.login_with_user(user_info.username, user_info.password, captcha_id, "123456")
            userToken = resp.json_get("access_token")

        def clear_func():
            pass
        return userToken, clear_func

    yield cache_obj.get_value(key, func=cache_func)


@pytest.fixture(scope='function')
def loginTokenSpu(config_obj, user_info_console_mainUser, AuthiamApi, cache_obj):
    """ 测试环境登录图形验证码可以随便填，生产环境不可以"""
    key = '%s_console_%s' % (sys._getframe().f_code.co_name, user_info_console_mainUser.userNameForDisable)

    def cache_func():
        userToken = user_info_console_mainUser.userToken  # 读取配置文件
        if not userToken:
            # 获取captcha_id
            captcha_id = AuthiamApi.get_captcha(print_log=False)
            # 手机号登录
            resp = AuthiamApi.login_with_user(user_info_console_mainUser.userNameForDisable,
                                               user_info_console_mainUser.password, captcha_id, "123456")
            # 用户名密码登录
            # resp = AuthiamApi.login_with_user(user_info.username, user_info.password, captcha_id, "123456")
            userToken = resp.json_get("access_token")

        def clear_func():
            pass

        return userToken, clear_func

    yield cache_obj.get_value(key, func=cache_func)

@pytest.fixture(scope='function')
def loginTokenFreeOrder(config_obj, user_info_console_mainUser, AuthiamApi, cache_obj):
    """ 测试环境登录图形验证码可以随便填，生产环境不可以"""
    key = '%s_console_%s' % (sys._getframe().f_code.co_name, user_info_console_mainUser.userNameForFreeOrder)

    def cache_func():
        userToken = user_info_console_mainUser.userToken  # 读取配置文件
        if not userToken:
            # 获取captcha_id
            captcha_id = AuthiamApi.get_captcha(print_log=False)
            # 手机号登录
            resp = AuthiamApi.login_with_user(user_info_console_mainUser.userNameForFreeOrder,
                                               user_info_console_mainUser.password, captcha_id, "123456")
            # 用户名密码登录
            # resp = AuthiamApi.login_with_user(user_info.username, user_info.password, captcha_id, "123456")
            userToken = resp.json_get("access_token")

        def clear_func():
            pass

        return userToken, clear_func

    yield cache_obj.get_value(key, func=cache_func)

@pytest.fixture(scope='function')
def AuthiamApi(config_obj, ext_info):
    """ AuthiamApi API """
    host = config_obj.EnvInfo.BeltCloud.Service
    return AuthiamSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info)

@pytest.fixture(scope='function')
def user_info(config_obj, request):
    """ yaml中摄像机信息"""
    return config_obj.get(request.param)

@pytest.fixture(scope='function')
def user_info_console(config_obj, request):
    """ yaml中console user,包括企业用户和个人用户 """
    return config_obj.get(request.param)

@pytest.fixture(scope='function')
def user_info_console_enterprise(config_obj):
    """ yaml中console enterprinse user,企业用户 """
    return config_obj.Console.User.testEnterprise

@pytest.fixture(scope='function')
def user_info_console_person(config_obj):
    """ yaml中console person user,个人用户 """
    return config_obj.Console.User.testPerson

@pytest.fixture(scope='function')
def user_info_console_mainUser(config_obj):
    """ yaml中console enterprinse user,企业用户 """
    return config_obj.Console.User.testConsoleMainUser

@pytest.fixture(scope='function')
def internal_admin_user_info(config_obj):
    """ 用户内部管理台admin"""
    return config_obj.Console.User.internalTestUser


@pytest.fixture(scope='function')
def akToken(config_obj, user_info):
    """ aksktoken"""
    # return config_obj.Console.User.testUser.userToken
    ak = user_info.ak
    sk = user_info.sk
    return encode_jwt_token(ak, sk)

@pytest.fixture(scope='function')
def akToken_ids(config_obj, user_info):
    """ aksktoken"""
    # return config_obj.Console.User.testUser.userToken
    ak = config_obj.Console.User.testUserids.ak
    sk = config_obj.Console.User.testUserids.sk
    return encode_jwt_token(ak, sk)

@pytest.fixture(scope='function')
def akWithAllowaccessToken(config_obj):
    """ 带allowaccess的token"""
    ak = config_obj.Console.User.testUser.ak
    sk = config_obj.Console.User.testUser.sk
    allowaccess = ["ListBot"]
    return encode_jwt_token(ak, sk, allowaccess=allowaccess)


@pytest.fixture(scope='function')
def AideCallbackAddress1(config_obj):
    """ callback地址"""
    return config_obj.Ras.callback.address1


@pytest.fixture(scope='function')
def centerInfo(config_obj):
    """ center信息"""
    return config_obj.EnvInfo.BeltCenter.master


@pytest.fixture(scope='function')
def edgeDefaultInfo(config_obj):
    """ edge信息"""
    return config_obj.EnvInfo.BeltEdge.hangzhou


@pytest.fixture(scope='function')
def VideomanagerApi(config_obj, ext_info, akToken):
    """ VideomanagerApi API """
    host = config_obj.EnvInfo.BeltCloud.CrdService
    return VideomanagerSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, token=akToken)

@pytest.fixture(scope='function')
def DeviceiotcenterApi(config_obj, ext_info,akToken):
    """ DeviceiotcenterApi API """
    host = config_obj.EnvInfo.BeltCloud.CrdService
    return DeviceiotcenterSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info,token=akToken)
