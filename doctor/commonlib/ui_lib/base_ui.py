#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base_ui.py
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/12/2 下午4:38   wangan      1.0         None
'''
import os

from selenium import webdriver

from commonlib.config import project_path

import platform


class BaseUI(object):
    def __init__(self, driver_version=None):
        self._default_driver = self.gen_driver(driver_version)

    @property
    def driver(self):
        return self._default_driver

    @staticmethod
    def gen_driver(driver_version=None):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--window-size=1280,800")
        # options.add_argument('--disable-gpu')
        if driver_version:
            driver_name = "chromedriver%s" % driver_version
        else:
            driver_name = "chromedriver"
        plat = platform.system().lower()
        if plat == 'windows':
            driver_path = 'commonlib/driver/%s.exe' % driver_name
        else:
            driver_path = 'commonlib/driver/%s' % driver_name
        driver = webdriver.Chrome(executable_path=os.path.join(project_path, driver_path), options=options)
        # driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def quit(self):
        self.driver.quit()



# def demo(driver):
#     url = 'http://10.4.10.47/doc/page/login.asp'
#     driver.get(url)
#     driver.find_element_by_id('username').send_keys('admin')
#     driver.find_element_by_id('password').send_keys('t2mksense')
#     driver.find_element_by_xpath("//button[@type='button']").click()
#     driver.maximize_window()
#     # time.sleep(5)
#     driver.quit()


