#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   cache_dict.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/25 上午10:24   wangan      1.0         None
'''
from commonlib.log_utils import log


class CacheDict(object):
    """ 数据缓存"""

    def __init__(self):
        self._cache_dict = {}
        self._clear_list = []

    def set_value(self, key, value):
        if key not in self._cache_dict:
            self._cache_dict[key] = {}
        self._cache_dict[key]['value'] = value

    def set_clear_func(self, key, clear_func):
        if key not in self._cache_dict:
            self._cache_dict[key] = {}
        self._cache_dict[key]['clear_func'] = clear_func
        self._clear_list.append(key)

    def get_value(self, key, func=None):
        """ 缓存取值
            当func 不为None的时候, 会执行func, func需要2个返回值, 第一个返回值为缓存的结果, 第二个返回值为clear函数(可以为None)
        """
        if key not in self._cache_dict:
            if func:
                value, clear_func = func()
                self.set_value(key, value)
                if clear_func:
                    self.set_clear_func(key, clear_func)
            else:
                return None
        return self._cache_dict[key]['value']

    def clear_func_by_key(self, key):
        if key not in self._cache_dict:
            return
        if 'clear_func' not in self._cache_dict[key]:
            return
        if key not in self._clear_list:
            return
        clear_func = self._cache_dict[key]['clear_func']

        ret = clear_func()
        self._clear_list.remove(key)
        log().info('[%s]clear up finish.' % key)
        return ret

    def clear_func_all(self):
        for key in reversed(self._clear_list):
            clear_func = self._cache_dict[key]['clear_func']
            clear_func()
            log().info('[%s]clear up finish.' % key)
        self._clear_list = []

