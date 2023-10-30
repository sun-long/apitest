#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:lv
# @Time:2019/6/12
import time
import datetime
import random

from commonlib.log_utils import log


def sleep(_time=1):
    log().info('等待%s秒' % _time)
    time.sleep(_time)

def get_timestamp(ts=None, offset=None):
    """ 获取时间戳的通用方法
    ts支持以下类型：
        None：返回当前时间戳
        int、float：返回该时间戳
        str：
            2021-01-01 10：00：00 返回该时间的时间戳
            10：00 返回当天10点的时间戳
    """
    if ts is None:
        timestamp = get_now_timestamp()
    elif isinstance(ts, int):
        timestamp = ts
    elif isinstance(ts, float):
        timestamp = int(ts)
    elif isinstance(ts, str):
        if '-' in ts:
            timestamp = get_timestamp_by_str(ts)
        else:
            timestamp = get_today_timestamp(ts)
    else:
        raise Exception("提供的时间类型错误.")
    if offset:
        timestamp = timestamp + offset
    return timestamp


def get_now_weekday():
    return datetime.datetime.now().isoweekday()


def get_now_timestamp():
    '''获取当前时间的时间戳'''
    return int(time.mktime(datetime.datetime.now().timetuple()))


def get_today_timestamp(_time_str=None):
    '''获取当日的时间戳'''
    ts = int(time.mktime(datetime.date.today().timetuple()))
    if not _time_str:
        return ts

    _time_list = _time_str.split(":")
    if len(_time_list) >= 3:
        hour, minute, sec = int(_time_list[0]), int(_time_list[1]), int(_time_list[2])
    elif len(_time_list) == 2:
        hour, minute, sec = int(_time_list[0]), int(_time_list[1]), 0
    else:
        hour, minute, sec = int(_time_list[0]), 0, 0
    return ts + hour * 3600 + minute * 60 + sec


def get_timestamp_by_str(tss1):
    """根据字符串获取时间戳"""
    # 字符类型的时间
    # tss1 = '2013-10-10 23:40:00'
    # 转为时间数组
    timeArray = None
    for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d %H', '%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%SZ'):
        try:
            timeArray = time.strptime(tss1, fmt)
            break
        except ValueError:
            pass
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def get_str_by_timestamp(ts=None, offset=0, formate=None):
    """ 根据时间戳获取指定格式的字符串"""
    if not ts:
        ts = get_now_timestamp()
        ts = ts - 8 * 60 * 60
    if isinstance(ts, str):
        ts = get_timestamp_by_str(ts)

    ts += offset
    dateArray = datetime.datetime.fromtimestamp(ts)
    if formate:
        otherStyleTime = dateArray.strftime(formate)
    else:
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime


def get_yesterday_timestamp():
    '''获取昨日的时间戳'''
    today = get_today_timestamp()
    return today - 86400


def get_ago_timestamp(days):
    '''获取当前日期前多少天的时间戳'''
    today = get_today_timestamp()
    return today - days * 86400


def get_after_timestamp(days):
    '''获取当前日期后多少天的时间戳'''
    today = get_today_timestamp()
    return today + days * 86400


def timestamp_date_difference(start_time, end_time):
    '''计算两个时间戳的日差'''
    return int((start_time - end_time) / 86400)


def get_age_on_date(certificateNumber):
    '''根据身份证号获取年龄,对月对日'''
    birthday_year = int(certificateNumber[6:10])
    birthday_month = int(certificateNumber[10:12])
    birthday_day = int(certificateNumber[12:14])
    today = datetime.date.today().strftime('%Y%m%d')
    current_year = int(today[0:4])
    current_month = int(today[4:6])
    current_day = int(today[6:8])
    age = current_year - birthday_year
    if birthday_month > current_month:
        age = age - 1
    elif birthday_month == current_month and birthday_day > current_day:
        age = age - 1
    return age


def get_age(certificateNumber):
    '''根据身份证号获取年龄'''
    year = certificateNumber[6:10]
    date = datetime.date.today()
    current_yesr = datetime.date.isocalendar(date)[0]
    age = current_yesr - int(year)
    return age


def current_milli_time():
    '''获取时间戳（毫秒）'''
    return int(round(time.time() * 1000))


def get_time_str(formate=None):
    if formate:
        return datetime.datetime.now().strftime(formate)
    return datetime.datetime.now().strftime('%Y%m%d-%H%M%S')


def get_id(pre):
    '''生成id'''
    return pre + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(0, 99))


if __name__ == '__main__':
    utc = "2021-08-31T07:14:26.934528077Z"
    utc = utc.split(".")[0] if "." in utc else utc
    timeStamp = int(time.mktime(time.strptime(utc, '%Y-%m-%dT%H:%M:%S')))
    res = get_timestamp_by_str('2021-08-31T07:14:26.934528077Z')
    print(res)
