#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   AES.py    
@Contact :   weishuting@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 下午6:52   weishuting      1.0         None
'''
# -*- coding: utf-8 -*-
import re
import ast
import time
from jsonschema import validate, ValidationError
import sys
import operator
import logging
from logging.handlers import RotatingFileHandler as LogHandler
import os



def log_config(f_level=logging.INFO, c_level=logging.CRITICAL, out_path='', filename='info', fix=False):
    logfile = os.path.join(out_path, filename) + '-' + time.strftime('%Y_%m%d_%H%M%S', time.localtime()) + '.txt' \
        if not fix else os.path.join(out_path, filename) + '.txt'

    # if not os.path.exists(logfile):
    #     os.mkdir(logfile)
    # print(os.getcwd())
    # print(logfile)
    logger = logging.getLogger(logfile)
    """
    1、依据logging包官方的注释，日志记录会向上传播到他的父节点也就是root logger
    2、当root logger 同时也被添加了屏幕输出handler的情况，日志就会输出第二次
    3、 root logger 若被多次添加屏幕输出handler，同一日志就会多次输出。
    pytest使用的为root logger，且添加了输出handler
    """
    logger.propagate = False
    logger.setLevel(logging.DEBUG)
    # if f_level is None:
    #     if c_level is None:
    #         logger.setLevel(logging.INFO)
    #     else:
    #         logger.setLevel(c_level)
    # else:
    #     logger.setLevel(f_level)

    formatter = logging.Formatter(
        '[%(levelname)s][%(process)d][%(thread)d]--%(asctime)s--[%(filename)s %(funcName)s %(lineno)d]: %(message)s')

    if c_level is not None:
        ch = logging.StreamHandler()
        ch.setLevel(c_level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    if f_level is not None:
        fh = LogHandler(logfile, maxBytes=100 * 1024 * 1024, backupCount=100)
        fh.setLevel(f_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger, logfile

def digit_number_validator(value,len):
    """
    :param len: 校验的位数
    :param value: 待校验的值为string类型
    :return boolean
    """
    int_count = 0
    for i in value:
    # 判断是否为数字
        int_count= int_count + 1
    if int_count==len:
        return True
    else:
        return False
  
def schema_validator(params, schema_json, fail_params=[], logger=None):
    """
    :param params: 实际返回值
    :param schema_json: 期望值列表或字符串
    :param fail_params
    :param logger
    :return boolean
    """
    try:
        validate(params, schema_json)
    except ValidationError as e:
        print("Json Schema Validation Failed")
        print(e)
        raise e
    return True


def type_validator(params, value, fail_params=[], logger=None):
    """
    功能：类型校验器
    :param params: 实际返回值
    :param value: 期望值列表或字符串
    :param fail_params
    :param logger
    :return boolean
    """
    mark = 0
    if isinstance(params, list):
        if value == "list":
            return True
        for each in params:
            if isinstance(value, list):
                if type(each).__name__ in value:
                        mark += 1
            else:
                if (type(each).__name__ == "int" and value == "float") or (each == 0 and value == "bool") or \
                        (each == "None" and (value == "dict" or value == "list")) or \
                        (type(each).__name__ == "long" and value == "int") or \
                        (type(each).__name__ == "int" and "linux" in sys.platform and value == "long"):
                    mark += 1
                else:
                    if type(each).__name__ == value:
                        mark += 1
        if len(params) == mark:
            return True
    else:
        if ((params == 0 or params == "False" or params == "True") and value == "bool") or \
                (type(params).__name__ == "int" and value == "float") or \
                (params == "None" and (value == "dict" or value == "list")) or \
                (type(params).__name__ == "long" and value == "int") or \
                (type(params).__name__ == "int" and "linux" in sys.platform and value == "long") or \
                (params == "False" and value == "bool"):
            return True
        elif type(params).__name__ == value:
            return True
    return False


def len_validator(params, value, fail_params=[], logger=None):
    """
    功能：长度校验器
    :param params: 实际返回值
    :param value: 期望值列表或字符串
    :param fail_params
    :param logger
    :return boolean
    """
    typo = "="
    if isinstance(value, str):
        basic = re.match(r'^(<|<=|>|>=|!=){1}(\d+)', value, re.I)
        comb = re.match(r'^(in|notin|<>){1}(.*)', value, re.I)
        if basic:
            typo = basic.group(1)
            value = int(basic.group(2))
        elif comb:
            typo = comb.group(1)
            value = comb.group(2)
        elif "*" in value or "/" in value or "+" in value or "-" in value:
            value = int(ast.literal_eval(value))
            typo = "="
    if isinstance(params, list) or isinstance(params, str):
        if type(value) is int and type == "=" and len(params) == value:
            return True
        else:
            return checker(typo, len(params), value, logger=logger)
    else:
        logger.error("参数不是list/str类型。")
        return False


def list_len_validator(params, value, fail_params=[], logger=None):
    """
    功能：列表长度校验器
    :param params: 实际返回值
    :param value: 期望值列表
    :param fail_params
    :param logger
    :return boolean
    """
    typo = "="
    basic = re.match(r'^(<|<=|>|>=|!=){1}(.*)', value, re.I)
    if basic:
        typo = basic.group(1)
        list_value_str = basic.group(2)
        try:
            value = len(ast.literal_eval(list_value_str))
        except:
            logger.error("%s" % list_value_str + "不是列表类型。")
            return False
    return checker(typo, len(params), value, logger=logger)


def between_validator(params, value, fail_params=[], logger=None):
    """
    功能：实际返回值在期望值的输入列表之间
    :param params: 实际返回值
    :param value: 期望值列表或字符串
    :param fail_params
    :param logger
    :return boolean
    """
    mark = 0
    if isinstance(params, list):
        for each in params:
            if not isinstance(params, int) or not isinstance(params, float):
                return False
            if isinstance(value,str):
                value = ast.literal_eval(value)
            if value[0] <= each <= value[1]:
                mark += 1
        if mark == len(params):
            return True
    else:
        if isinstance(params, int) or isinstance(params, float):
            if isinstance(value,str):
                value = ast.literal_eval(value)
            if value[0] <= params <= value[1]:
                return True
    return False


def equal_validator(params, value, fail_params=[], logger=None):
    """
    功能：期望值与实际返回值一致
    :param params: 实际返回值
    :param value: 期望值列表或字符串
    :param fail_params
    :param logger
    :return boolean
    """
    if isinstance(params, list) and isinstance(value, list):
        if not list(set(params).difference(set(value))):
            return True
    elif isinstance(params, str) and isinstance(value, str):
        if params.strip() == value.strip():
            return True
    elif isinstance(value, str) and isinstance(params, int):
        if "*" in value or "/" in value or "+" in value or "-" in value:
            try:
                value = ast.literal_eval(value)
            except Exception as e:
                pass
        if str(params) == str(value):
            return True
    elif isinstance(value, dict) and isinstance(params, dict):
        return operator.eq(params, value)
    else:
        if str(params) == str(value):
            return True
    return False


def not_equal_validator(params, value, fail_params=[], logger=None):
    """
    功能：期望值与实际返回值不一致
    :param params: 实际返回值
    :param value: 期望值列表或字符串
    :param fail_params
    :param logger
    :return boolean
    """
    try:
        if "*" in value or "/" in value or "+" in value or "-" in value:
            value = ast.literal_eval(value)
    except Exception as e:
        pass
    if params != value:
        return True
    else:
        return False


def greater_or_equal_validator(params, value, fail_params=[], logger=None):
    if greater_validator(params, value) or equal_validator(params, value):
        return True
    else:
        return False


def less_or_equal_validator(params, value, fail_params=[], logger=None):
    if less_validator(params, value) or equal_validator(params, value):
        return True
    else:
        return False


def response_in_expect_validator(params, value, fail_params=[], logger=None):
    """
    功能：校验实际返回值在期望列表值中存在
    :param params: 实际返回值
    :param value: 期望值列表或字符串
    :param fail_params
    :param logger
    :return boolean
    """
    if isinstance(value, int):
        logger.error("期望值不能为整形数据。")
        return False
    elif isinstance(params, dict):
        for each in value:
            return operator.eq(params, each)
        return False
    elif isinstance(params, list) and isinstance(value, list):
        if set(params).issubset(set(value)):
            return True
        return False
    elif isinstance(value, list):
        if params in value:
            return True
    elif isinstance(value, str):
        if params in value:
            return True
    return False


def response_not_in_expect_validator(params, value, fail_params=[], logger=None):
    """
    功能：校验实际返回值在期望列表值中不存在
    :param params: 实际返回值
    :param value: 期望值列表或字符串
    :param fail_params
    :param logger
    :return boolean
    """
    if isinstance(value, int):
        return False
    elif isinstance(params, dict):
        return False
    elif isinstance(value, list):
        if params not in value:
            return True
    elif isinstance(value, str):
        if params not in value:
            return True
    return False


def expect_not_in_response_validator(params, value, fail_params=[], logger=None):
    """
    功能：校验期望值不在实际返回值中（包含列表，字符串）
    :param params: 实际返回值
    :param value: 期望值（不存在的）
    :param fail_params
    :param logger
    :return: boolean
    """
    if isinstance(params, list):
        if value not in params:
            return True
    elif isinstance(params, str):
        if value not in params:
            return True
    elif params != value:
        return True
    return False


def expect_in_response_validator(params, value, fail_params=[], logger=None):
    """
    功能：校验期望返回值在实际列表值中存在
    :param params: 实际返回值
    :param value: 期望值列表
    :param fail_params
    :param logger
    :return boolean
    """
    if isinstance(params, list):
        if value in params:
            return True
    elif isinstance(params, str):
        if value in params:
            return True
    else:
        if value == params:
            return True
    return False


def greater_validator(params, value, fail_params=[], logger=None):
    if isinstance(value, int) or isinstance(value, float):
        if isinstance(params, list):
            for each in params:
                if not each > value:
                    return False
        elif not params > value:
            return False
    else:
        if isinstance(params, list):
            for each in params:
                if not each > value:
                    return False
        elif not params > ast.literal_eval(value):
            return False
    return True


def less_validator(params, value, fail_params=[], logger=None):
    if isinstance(value, int) or isinstance(value, float):
        if params < value:
            return True
    else:
        if params < ast.literal_eval(value):
            return True
    return False


# # add by luwenzhen, since@ 2018/07/23
# def greater_or_equal_validator(params, value):
#     if greater_validator(params, value) or equal_validator(params, value):
#         return True
#     else:
#         return False
#
#
# # add by luwenzhen, since@ 2018/07/23
# def less_or_equal_validator(params, value):
#     if less_validator(params, value) or equal_validator(params, value):
#         return True
#     else:
#         return False


def keys_include_in_dict(params, value, fail_params=[], logger=None):
    if isinstance(params, str):
        return False
    if isinstance(value, dict):
        return False
    if not value:
        return False
    elif isinstance(params, list):
        for item in params:
            if not isinstance(item, dict):
                return False
            else:
                if isinstance(value, list):
                    for each in value:
                        if isinstance(each, str) and each[-1] == '?':
                            continue
                        if each not in list(item.keys()):
                            return False
                else:
                    if value not in list(item.keys()):
                        return False
    elif isinstance(params, dict):
        if isinstance(value, list):
            for each in value:
                if isinstance(each, str) and each[-1] == '?':
                    continue
                elif each not in list(params.keys()):
                    return False
        else:
            if value not in list(params.keys()):
                return False
    return True


def reg_validator(params, value, fail_params=[], logger=None):
    # print decode_str(params)
    mark = 0
    logger.info(str(params))
    if isinstance(params, list):
        for each in params:
            # if type(each).__name__ == "unicode":
            #     each = each.encode("utf-8")
            try:
                val = re.match(value, each)
                if val.group(0):
                    mark += 1
            except Exception as e:
                logger.error(str(e))
                return False
        if mark == len(params):
            return True
    else:
        try:
            # if type(value).__name__ == "unicode":
            #     value = value.encode("utf-8")
            val = re.match(value, params)
            if val:
                return True
            else:
                logger.error(value)
                return False
        except Exception as e:
            logger.error(str(e))
            return False
    return False


def time_zone_regular_validator(params, value, fail_params=[], logger=None):
    try:
        nowSec = int(time.time())
        if value.lower() == "sec":
            if len(str(params)) > len(str(nowSec)):
                logger.info("不是一个秒级时间。")
                return False
            value = "%Y--%m--%d %H:%M:%S"
        elif value.lower() == "msec":
            if len(str(params)) <= len(str(nowSec)):
                logger.info("不是一个毫秒级时间。")
                return False
            params = int(params) / 1000
            value = "%Y--%m--%d %H:%M:%S"
        time.strftime(value, time.localtime(params))
        logger.info("时间格式字符串正确。")
        return True
    except:
        logger.error("不是一个有效的时间格式字符串。")
        return False


def id_card_regular_validator(params, value, fail_params=[], logger=None):
    try:
        res = idc_verify(params)
        if res and value:
            logger.info("身份证字符串格式正确, 与期望值相符。")
            return True
        elif res and not value:
            logger.info("身份证字符串格式正确, 但与期望值不符。")
            return False
        elif not res and not value:
            logger.info("身份证字符串格式错误, 但与期望值相符。")
            return True
        elif not res and value:
            logger.info("身份证字符串格式错误, 与期望值不符。")
            return False
    except:
        logger.error("不是一个有效的身份证字符串格式。")
        return False


def idc_verify(id_no):
    arr = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    last = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    xlen = len(id_no)
    if xlen != 18 and xlen != 15:
        return False

    try:
        if xlen == 18:
            x2 = id_no[6:14]
            x3 = time.strptime(x2, '%Y%m%d')
            if x2 < '19000101' or x3 > time.localtime():
                return False
        else:
            x2 = time.strptime(id_no[6:12], '%y%m%d')
    except Exception as e:
        return False

    if xlen == 18:
        y = 0
        for i in range(17):
            y += int(id_no[i]) * arr[i]

        if last[y % 11] != id_no[-1].upper():
            return False
    return True


class ValidatorRegistry(object):
    registry = {}

    @classmethod
    def register(cls, name, validate):
        cls.registry[name] = validate

    @classmethod
    def validate(cls, name, params, value, fail_params, logger):
        return cls.registry[name].validate(params, value, fail_params, logger)


def checker(typo, params, value, fail_params=[], logger=None):
    if type(params) is bool:
        if not params:
            params = False
        else:
            params = True
    elif isinstance(params, str) and not params:
        params = ""
    elif type(params) is int and not params:
        params = 0
    elif isinstance(params, float) and not params:
        params = 0.0
    elif isinstance(params, list) and not params:
        params = []
    elif isinstance(params, dict) and not params:
        params = {}
    elif params == "None":
        logger.info("return is null, not check.")
        return True
    typo = typo.lower()
    val = ValidatorRegistry()
    if typo == "<>":
        val.register("<>", between_validator(params, value, fail_params, logger))
    elif typo == "=":
        val.register("=", equal_validator(params, value, fail_params, logger))
    elif typo == ">":
        val.register(">", greater_validator(params, value, fail_params, logger))
    # add by luwenzhen, since @2018/07/23
    elif typo == ">=":
        val.register(">=", greater_or_equal_validator(params, value, fail_params, logger))
    elif typo == "<":
        val.register("<", less_validator(params, value, fail_params, logger))
    # add by luwenzhen, since @2018/07/23
    elif typo == "<=":
        val.register("<=", less_or_equal_validator(params, value, fail_params, logger))
    elif typo == "!=":
        val.register("!=", not_equal_validator(params, value, fail_params, logger))
    elif typo == "type":
        val.register("type", type_validator(params, value, fail_params, logger))
    elif typo == "re":
        val.register("re", reg_validator(params, value, fail_params, logger))
    elif typo == "len":
        val.register("len", len_validator(params, value, fail_params, logger))
    elif typo == "llc":
        val.register("llc", list_len_validator(params, value, fail_params, logger))
    elif typo == "in":
        val.register("in", response_in_expect_validator(params, value, fail_params, logger))
    elif typo == "notin":
        val.register("notin", response_not_in_expect_validator(params, value, fail_params, logger))
    elif typo == "notinclude":
        val.register("notinclude", expect_not_in_response_validator(params, value, fail_params, logger))
    elif typo == "include":
        val.register("include", expect_in_response_validator(params, value, fail_params, logger))
    elif typo == "includekey":
        val.register("includekey", keys_include_in_dict(params, value, fail_params, logger))
    elif typo == "timezone":
        val.register("timezone", time_zone_regular_validator(params, value, fail_params, logger))
    elif typo == "idc":
        val.register("idc", id_card_regular_validator(params, value, fail_params, logger))
    elif typo == "schema":
        val.register("schema", schema_validator(params, value, fail_params, logger))
    else:
        logger.info("Validator is not register, please check the case.")
    if params == "Optional" and not val.registry[typo]:
        return True
    return val.registry[typo]


if __name__ == "__main__":
    data = {
        "col_id": "ssss",
        "features": [{"type": "face", "version": 24501, "blob": "string"},
                     {"type": "face", "version": 1234, "blob": "string"}],
        "consistency": "READ_MASTER_ONLY",
        "top_k": 100,
        "min_score": 0.9,
        "return_raw_feature": True
    }
    id = ["jpg", {"bar": ["hello", None, 1233, 444]}]
    schema = {
        "type": "object",
        "properties": {
            "col_id": {
                "type": "string"
            },
            "features": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "version": {
                            "type": "integer",
                            "format": "int32"
                        },
                        "blob": {
                            "type": "string",
                            "format": "byte"
                        }
                    }
                }
            },
            "consistency": {
                "type": "string",
                "enum": [
                    "READ_ANY",
                    "READ_MASTER_ONLY",
                    "READ_SLAVE_ONLY"
                ],
                "default": "READ_ANY"
            },
            "top_k": {
                "type": "integer",
                "format": "int32",
                "description": "需要top_k个最相似的结果, 范围:(0, 1024]."
            },
            "min_score": {
                "type": "number",
                "format": "float"
            },
            "return_raw_feature": {
                "type": "boolean",
                "format": "boolean"
            }
        }
    }
    result=idc_verify("362531199607300322")
    # print(checker("schema", data, schema))
    # # from common.public import log_config
    # import logging
    # log = log_config(f_level=logging.INFO, c_level=logging.INFO, out_path='./', filename='log')[0]
    # pa = "20190619-9e3060c1-00a580ae003d-00000020-000027b8"
    # rex = "^(\\d{8})-([a-fA-F0-9]{8})-([a-fA-F0-9]{12})-([a-fA-F0-9]{8})-([a-fA-F0-9]{8})$"
    # # print(reg_validator(pa, rex))
    # # print(re.match(rex, pa).group(0))
    # print(checker("re", pa, rex, [], log))
    digit_number_validator(16,"123456")
