#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import pytest

from commonlib import utils, config, database
from commonlib.api_lib.argus.post_data_tool import PostDataTool
from model.mysqldb.service.device import DeviceData

sys.path.append('..')

from core.pm_utils import load_postman
from commonlib.log_utils import log

# collections = load_postman("<postman目录下的相对路径>")  # 如argus/devicemanager/
collections = load_postman("argus/console")
collections_device = load_postman("argus/devicemanager/")

CLOUDOSDB = database.connect_db(config.CLOUDOS_DATABASE)

@pytest.fixture(scope="module", autouse=True)
def init_module(config_obj):
    module_name = str(os.path.basename(__file__)).split('.')[0]
    log().info("==========%s模块级setup，测试环境%s==========" % (module_name, "test"))
    yield
    log().info("==========%s模块级teardown==========" % module_name)


class TestDemo(object):
    @pytest.fixture(scope="class", autouse=True)
    def init_func(self, config_obj):
        # 初始化测试集
        collections.init(self)
        collections.init(self, custom_func_name="console_init")
        collections_device.init(self, custom_func_name="device_init")

        # 所有test运行前运行一次，接收外部参数env_obj，初始化测试环境
        log().info("==========%s测试开始，测试环境%s==========" % (self.__class__.__name__, "test"))
        global env_config  # 全局变量
        env_config = config_obj

    def teardown_class(self):
        # 所有test运行完后运行一次
        log().info("==========%s测试结束==========\n" % self.__name__)

    def setup_method(self, method):
        # 每个测试用例执行之前做操作
        log().info("用例%s开始" % method.__name__)

    def teardown_method(self, method):
        # 每个测试用例执行之后做操作
        log().info("用例%s结束" % method.__name__)

    def console_init(self, inte_obj):
        """自定义接口对象初始化"""
        pass

    def device_init(self, inte_obj):
        """自定义接口对象初始化"""
        pass

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        pass

    @property
    def device_service(self):
        return DeviceData(CLOUDOSDB)

    @pytest.mark.P0case
    def test_InterfaceName_000_Desc(self):
        """测试InterfaceName接口"""
        # registerDevice = collections.interface('pm文件名', 'item.name名', resp_name='response下的name')
        # res = registerDevice.request()
        # assert res.status_code == 200
        # assert res.error_code == 0
        log().info("test_InterfaceName_000_Desc 执行")

    @pytest.mark.P0case
    def test_InterfaceName_001_Desc(self):
        """测试InterfaceName接口"""
        # registerDevice = collections.interface('pm文件名', 'item.name名', resp_name='response下的name')
        # res = registerDevice.request()
        # assert res.status_code == 200
        # assert res.error_code == 0
        log().info("test_InterfaceName_001_Desc 执行")

    @pytest.mark.P0case
    def test_mysqldb_001_Desc(self):
        """mysqldb操作实例"""
        # 获取指定ak的device_list
        device_list = self.device_service.d_get_by_id("l1-29302104-y0517d31514b", id_field="ak")
        log().info(device_list)
        pass

    def test_demo1(self):
        pdt = PostDataTool()
        pdt.set_config_obj_by_type('dev')
        pdt.post_data_from_yaml('demo.yaml')

if __name__ == '__main__':
    pass


