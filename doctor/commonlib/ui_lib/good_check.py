#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   good_check.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/10/11 下午3:12   wangan      1.0         None
'''
from commonlib.ui_lib.base_ui import BaseUI


class GoodCheck(BaseUI):
    def __init__(self):
        """ good check"""
        super(GoodCheck, self).__init__()


    def parse_good(self, url, tags=None):
        """ """
        self.driver.get(url)
        if tags:
            for p in tags:
                self.driver.find_element_by_xpath('//div[contains(@class,"item") and @data-value="%s"]' % p).click()
        price = self.driver.find_element_by_xpath('//span[@class="p-price"]').text
        title = self.driver.find_element_by_xpath('//div[@class="sku-name"]').text
        exist = self.driver.find_element_by_xpath('//div[@class="store-prompt"]').text

        good = {
            'title': title,
            'price': price,
            'tag': tags,
            'exist': exist
        }
        print(good)
        return good





if __name__ == '__main__':
    gList = [
        ('10032953643823', ['亮黑', '12GB+256GB']),
        ('10032953643823', ['幻境', '12GB+256GB']),
    ]
    gc = GoodCheck()
    for g in gList:
        gc.parse_good('https://item.jd.com/%s.html' % g[0], tags=g[1])
    gc.quit()