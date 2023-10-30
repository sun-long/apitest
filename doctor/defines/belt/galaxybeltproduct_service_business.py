#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from commonlib import utils
from defines.belt.api.galaxybeltproduct_service_swagger import GalaxybeltproductSwaggerApi


"""
使用说明：


"""


class GalaxybeltproductSwaggerBusiness(GalaxybeltproductSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None, prefix_path=None):
        super(GalaxybeltproductSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息
        self.prefix_path = prefix_path
        # self.configMap = utils.readConfigMap("demo.yaml", "http://galaxy-adapter.sensegalaxy:8080")


    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        # self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

        # if inte_obj.path in self.configMap:
        #     info = self.configMap[inte_obj.path][inte_obj.method]
        #     inte_obj.set_headers('X-Belt-Action', info["action"])
        #     inte_obj.set_headers('X-Belt-Version', info["version"])
        #     inte_obj.set_path_prefix(info["paths"])
        # else:
        #     raise Exception("no support PATH:%s" % inte_obj.path)


        inte_obj.set_path_prefix(self.prefix_path)
        if inte_obj.path == '/openapi/v2/product/async/transact':
            inte_obj.set_headers('X-Belt-Action', 'AsyncTransact')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/async/{transactCode}/status':
            inte_obj.set_headers('X-Belt-Action', 'GetAsyncTransactStatus')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/camera':
            inte_obj.set_headers('X-Belt-Action', 'CheckCamera')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/conflict':
            inte_obj.set_headers('X-Belt-Action', 'CheckProductConflict')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/detail/recognize':
            inte_obj.set_headers('X-Belt-Action', 'RecognizeProductDetails')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/list':
            inte_obj.set_headers('X-Belt-Action', 'GetProductList')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/multiple/detail/recognize':
            inte_obj.set_headers('X-Belt-Action', 'RecognizeMultipleProductDetails')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/name':
            inte_obj.set_headers('X-Belt-Action', 'GetProductByName')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/recognize':
            inte_obj.set_headers('X-Belt-Action', 'Recognize')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/replenish':
            inte_obj.set_headers('X-Belt-Action', 'Replenish')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/sync/product':
            inte_obj.set_headers('X-Belt-Action', 'GetSyncProductRecordList')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/tenant/conflict':
            inte_obj.set_headers('X-Belt-Action', 'GetTenantConflict')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/product/transact':
            inte_obj.set_headers('X-Belt-Action', 'Transact')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        else:
            raise Exception("no support PATH:%s" % inte_obj.path)