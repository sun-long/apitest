import os
import sys
import time

from commonlib import utils
from commonlib import config
import pytest
from defines.belt.galaxyproduct_service_business import GalaxyproductSwaggerBusiness
from commonlib.ui_lib.kibana import Kibana


interface_dict = {
    "static_device": [
        "/openapi/v1/product/detail/recognize",
        "/openapi/v1/product/multiple/detail/recognize",
        "/openapi/v1/product/recognize",
        "/openapi/v1/product/replenish",
        "/openapi/v1/product/transact",
        "/openapi/v2/product/detail/recognize",
        "/openapi/v2/product/multiple/detail/recognize",
        "/openapi/v2/product/recognize",
        "/openapi/v2/product/replenish",
        "/openapi/v2/product/transact",
    ],
    "static_no_device": [
        "/openapi/v1/product/camera",
        "/openapi/v1/product/conflict",
        "/openapi/v1/product/list",
        "/openapi/v1/product/name",
        "/openapi/v1/product/sync/product",
        "/openapi/v1/product/tenant/conflict",
        "/openapi/v2/product/camera",
        "/openapi/v2/product/conflict",
        "/openapi/v2/product/list",
        "/openapi/v2/product/name",
        "/openapi/v2/product/sync/product",
        "/openapi/v2/product/tenant/conflict",
    ],
    "dynamic_deivce": [
        "/openapi/v1/product/async/transact",
        "/openapi/v1/product/async/{transactCode}/status",
        # "/openapi/v1/product/replenish", # 动态不支持
        "/openapi/v1/product/transact",
        "/openapi/v2/product/async/transact",
        "/openapi/v2/product/async/{transactCode}/status",
        # "/openapi/v2/product/replenish", # 动态不支持
        "/openapi/v2/product/transact",
    ],
    "dynamic_no_deivce": [
        "/openapi/v1/product/camera",
        "/openapi/v1/product/conflict",
        "/openapi/v1/product/list",
        "/openapi/v1/product/name",
        "/openapi/v1/product/sync/product",
        "/openapi/v1/product/tenant/conflict",
        "/openapi/v2/product/camera",
        "/openapi/v2/product/conflict",
        "/openapi/v2/product/list",
        "/openapi/v2/product/name",
        "/openapi/v2/product/sync/product",
        "/openapi/v2/product/tenant/conflict",
    ],
}


@pytest.fixture(scope='function')
def GalaxyproductApi(config_obj, ext_info, galaxyTenant):
    """ GalaxyproductApi API """
    time.sleep(0.5)
    host = config_obj.EnvInfo.Galaxy.beltAdapterService
    user_info = galaxyTenant
    return GalaxyproductSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info, user_info=user_info)

@pytest.fixture(scope='function')
def galaxy_config_obj(config_obj):
    """galaxy测试数据配置文件"""
    return config_obj._extra.test_data.galaxy_test

@pytest.fixture(scope='function')
def consoleAdminToken(galaxy_config_obj, request):
    """ tenant"""
    return galaxy_config_obj.greyInfo.console_pre_token

@pytest.fixture(scope='function')
def galaxyTenant(galaxy_config_obj, request):
    """ tenant"""
    return galaxy_config_obj.get(request.param)

@pytest.fixture(scope='function')
def galaxyDevice(galaxy_config_obj, request):
    """ device"""
    return galaxy_config_obj.get(request.param)


@pytest.fixture(scope='function')
def greyMap(galaxy_config_obj, cache_obj):
    """ grey Map"""
    key = '%s_greyMap' % (sys._getframe().f_code.co_name)

    def cache_func():
        config_name = galaxy_config_obj.greyInfo.config_name
        result = utils.read_csv(os.path.join(config.project_path, "data/galaxy/greyMap.csv"))
        config_index = result[0].index(config_name)
        greyDict = {}
        for idx, info in enumerate(result):
            if idx == 0:
                continue
            tenant_name = info[0]
            device_name = info[1]
            group_name = info[2]
            if tenant_name not in greyDict:
                greyDict[tenant_name] = {}
            if device_name not in greyDict[tenant_name]:
                greyDict[tenant_name][device_name] = {}
            greyDict[tenant_name][device_name]["op"] = info[config_index]
            if info[config_index] in ["CP", "NONE"]:
                greyDict[tenant_name][device_name]["tag"] = galaxy_config_obj.greyInfo.galaxy_tag
            else:
                greyDict[tenant_name][device_name]["tag"] = galaxy_config_obj.greyInfo.belt_tag
            greyDict[tenant_name][device_name]["interface_group"] = interface_dict[group_name]

        def clear_func():
            pass

        return greyDict, clear_func

    yield cache_obj.get_value(key, func=cache_func)


@pytest.fixture(scope='function')
def getProductUrlsFromPreEnv(GalaxyproductApi, consoleAdminToken, cache_obj):
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
        intef = GalaxyproductApi.modifyProduct_1PostApi(fileNameList=fileNameList, loginToken=consoleAdminToken,
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
def kibanaObj(cache_obj):
    """ grey Map"""
    key = '%s_kibana' % (sys._getframe().f_code.co_name)

    def cache_func():
        ki = Kibana("admin", "c5h7ziki", 110)
        def clear_func():
            pass

        return ki, clear_func

    yield cache_obj.get_value(key, func=cache_func)
