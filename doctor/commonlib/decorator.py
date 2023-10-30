#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   decorator.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/26 上午9:54   wangan      1.0         None
'''
import json
import random
import time


from commonlib.log_utils import log, LogCollect
import signal
import functools
import platform

from core.ret_utils import CommonRet

class TimeoutException(Exception):
    pass

def dependon(depend=None, *args_depend, **kwargs_depend):
    """测试用例前的装饰器, 用于确定测试用例的依赖关系"""
    def wraper_func(test_func):
        @functools.wraps(test_func)
        def inner_func(self, *args, **kwargs):
            log().info("先执行" + depend.__name__)
            depend(self, *args_depend, **kwargs_depend)
            test_func(self, *args, **kwargs)

        return inner_func

    return wraper_func


def wait(timeout=5, interval=1, util_func=None, raise_exception=True):
    """等待装饰器 util_func 返回为True的时候， 退出"""
    def wraper_func(func):
        def handler(signum, frame):
            print('Signal handler called with signal %s' % signum)
            if raise_exception:
                log().error("[%s] Wait TimeOut. gt %ss!" % (func.__name__, timeout))
                assert None, "[%s] Wait TimeOut. gt %ss!" % (func.__name__, timeout)
                # raise TimeoutException("[%s] Wait TimeOut!" % func.__name__)
            else:
                log().info("[%s] Wait TimeOut!" % func.__name__)

        @functools.wraps(func)
        def inner_func(self, *args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            _timeout, _interval, _raise_exception, _call_back = timeout, interval, True, None
            _before_func, _after_func = None, None
            if "timeout" in kwargs:
                _timeout = kwargs["timeout"]
            if "interval" in kwargs:
                _interval = kwargs["interval"]
            if "raise_exception" in kwargs:
                _raise_exception = kwargs["raise_exception"]
            if "call_back" in kwargs:
                _call_back = kwargs['call_back']
            if "after_func" in kwargs:
                _after_func = kwargs['after_func']
            if "before_func" in kwargs:
                _before_func = kwargs['before_func']
            last_ret = None
            start = time.time()
            try:
                signal.alarm(_timeout)
                while True:
                    if _before_func:
                        _before_func()
                    ret = func(self, *args, **kwargs)
                    last_ret = ret  # TODO baoliusuoyourizhi
                    if _after_func:
                        _after_func()
                    if util_func and util_func(ret):
                        break
                    elif not util_func and ret:
                        break
                    time.sleep(_interval)
                signal.alarm(0)
                return ret
            except TimeoutException as e:
                if _raise_exception:
                    raise Exception('%s Time out caught!' % func.__name__)
            except Exception as e:
                signal.alarm(0)
                raise e
            finally:
                end = time.time()
                if hasattr(last_ret, "log_obj") and last_ret.log_obj and last_ret.log_obj.log_list:
                    last_ret.log_obj.print()
                log().info("[wait统计]%s 耗时%ss" % (func.__name__, end-start))
                if _call_back:
                    log().info("[call back启动]%s" % func.__name__)
                    _call_back()

        return inner_func

    def wraper_win_func(func):
        @functools.wraps(func)
        def inner_func(self, *args, **kwargs):
            _timeout, _interval, _raise_exception, _call_back = timeout, interval, True, None
            _before_func, _after_func = None, None
            if "timeout" in kwargs:
                _timeout = kwargs["timeout"]
            if "interval" in kwargs:
                _interval = kwargs["interval"]
            if "raise_exception" in kwargs:
                _raise_exception = kwargs["raise_exception"]
            if "call_back" in kwargs:
                _call_back = kwargs['call_back']
            if "after_func" in kwargs:
                _after_func = kwargs['after_func']
            if "before_func" in kwargs:
                _before_func = kwargs['before_func']
            last_ret = None
            start = time.time()
            try:
                while True:
                    if time.time() - start > _timeout:
                        raise TimeoutException
                    if _before_func:
                        _before_func()
                    ret = func(self, *args, **kwargs)
                    last_ret = ret  # TODO baoliusuoyourizhi
                    if _after_func:
                        _after_func()
                    if util_func and util_func(ret):
                        break
                    elif not util_func and ret:
                        break
                    time.sleep(_interval)
                return ret
            except TimeoutException as e:
                if _raise_exception:
                    raise Exception('%s Time out caught!' % func.__name__)
            except Exception as e:
                raise e
            finally:
                end = time.time()
                if hasattr(last_ret, "log_obj") and last_ret.log_obj and last_ret.log_obj.log_list:
                    last_ret.log_obj.print()
                log().info("[wait统计]%s 耗时%ss" % (func.__name__, end-start))
                if _call_back:
                    log().info("[call back启动]%s" % func.__name__)
                    _call_back()

        return inner_func


    plat = platform.system().lower()
    if plat == 'windows':
        return wraper_win_func
    else:
        return wraper_func


def wrap_request():
    """ 请求上下文处理
    :param
    :param
    :return:
    """

    def wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(self, *args, **kwargs):
            lc = LogCollect()
            lc.add_log("\n\n====================%s:%s====================" % (self.name, self.description))
            # lc.add_log("接口名称：%s" % self.name)
            # lc.add_log("接口描述：%s" % self.description)
            lc.add_log("PM信息：%s" % self.pm_info)
            lc.add_log("请求URL：[%s]%s" % (self.method, self.url_string()))
            if self.headers:
                lc.add_log("请求header：")
                for key, value in self.headers.items():
                    lc.add_log("%s:%s" % (key, value))
            if self.method.lower() in ["post", "put"]:
                req_message = self.body_log
                if req_message:
                    lc.add_log("请求报文： %s" % req_message)

                if self.files:
                    lc.add_log("请求报文-上传文件： %s" % json.dumps(self._get_upload_dict(), sort_keys=True, indent=2,
                                                            ensure_ascii=False))
            if self.print_status:
                lc.print()
            if getattr(self, '_ext_info', None):
                self._ext_info.addRequest(self)  # 将接口放到请求队列中

            if "ret_class" in kwargs and kwargs["ret_class"]:
                self._wrap_response_class = kwargs["ret_class"]
            else:
                self._wrap_response_class = CommonRet
            rate_limit_retry = 3
            start_time, end_time, r = None, None, None
            while rate_limit_retry > 0:
                start_time = time.time()
                r = func(self, *args, **kwargs)
                end_time = time.time()
                if r.status_code == 429:
                    time.sleep(1)
                    rate_limit_retry = rate_limit_retry -1
                    lc.add_log("[warning]ratelimit retry:%s" % rate_limit_retry)
                else:
                    break

            stream_list = []
            if self.stream_request:
                i = 0
                for chunk in r.iter_lines():
                    # 处理响应内容
                    i += 1
                    stream_list.append((i,  time.time() - end_time, chunk.decode("utf-8")))
            delay = round(end_time - start_time, 2)
            lc.add_log("Status_code：%s Reason: %s, time:%ss" % (r.status_code, r.reason, delay))
            ret = self._wrap_response_class(r, self)
            ret.time = delay
            ret.stream_list = stream_list # 流式返回list
            if ret.origin_resp.headers:
                lc.add_log("响应header：")
                for key, value in ret.origin_resp.headers.items():
                    if key == 'X-Belt-Request-Id' or 'X-Request-Id':
                        lc.add_log("%s:%s" % (key, value))
            if "Content-Type" in r.headers and "application/json" in r.headers["Content-Type"]:
                lc.add_log("响应报文： %s" % json.dumps(ret.resp_json, sort_keys=True, indent=2, ensure_ascii=False))
            elif "Content-Type" in r.headers and "application/octet-stream" in r.headers["Content-Type"]:
                lc.add_log("响应内容： octet-stream类型返回")
            else:
                if self.stream_request:
                    stream_str = ""
                    for s in stream_list:
                        stream_str += "[line:%s]delay:%.4f\n%s\n" % (s[0], s[1], s[2])
                    lc.add_log("[Warning]流式接口返回,响应内容:\n%s" % stream_str)
                else:
                    lc.add_log("[Warning]响应报文的Content-Type不是application/json")
                    lc.add_log("响应内容： %s" % ret.origin_resp.content.decode("utf-8"))

            if self.print_status:
                lc.print()
            ret.log_obj = lc  # 传递日志收集对象
            self._resp = ret  # 设置接口返回结果
            # time.sleep(0.2)
            # time.sleep(1) 改在swagger业务代码里
            return ret
        return inner_wrapper
    return wrapper

def wrap_locust_request():
    """ 请求上下文处理
    :param
    :param
    :return:
    """

    def wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(self, *args, **kwargs):
            lc = LogCollect()
            lc.add_log("\n\n====================%s:%s====================" % (self.name, self.description))
            # lc.add_log("接口名称：%s" % self.name)
            # lc.add_log("接口描述：%s" % self.description)
            lc.add_log("PM信息：%s" % self.pm_info)
            lc.add_log("请求URL：[%s]%s" % (self.method, self.url_string()))
            if self.headers:
                lc.add_log("请求header：")
                for key, value in self.headers.items():
                    lc.add_log("%s:%s" % (key, value))
            if self.method.lower() in ["post", "put"]:
                req_message = self.body_log
                if req_message:
                    lc.add_log("请求报文： %s" % req_message)

                if self.files:
                    lc.add_log("请求报文-上传文件： %s" % json.dumps(self._get_upload_dict(), sort_keys=True, indent=2,
                                                            ensure_ascii=False))
            if self.print_status:
                lc.print()
            if getattr(self, '_ext_info', None):
                self._ext_info.addRequest(self)  # 将接口放到请求队列中

            if "ret_class" in kwargs and kwargs["ret_class"]:
                self._wrap_response_class = kwargs["ret_class"]
            else:
                self._wrap_response_class = CommonRet
            r = func(self, *args, **kwargs)
            lc.add_log("Status_code：%s Reason: %s" % (r.status_code, r.reason))
            ret = self._wrap_response_class(r, self)
            if "Content-Type" in r.headers and "application/json" in r.headers["Content-Type"]:
                lc.add_log("响应报文： %s" % json.dumps(ret.resp_json, sort_keys=True, indent=2, ensure_ascii=False))
            else:
                lc.add_log("[Warning]响应报文的Content-Type不是application/json")
                lc.add_log("响应内容： %s" % ret.origin_resp.text)

            if self.print_status:
                lc.print()
            ret.log_obj = lc  # 传递日志收集对象
            self._resp = ret  # 设置接口返回结果
            return ret
        return inner_wrapper
    return wrapper

def wrap_curl_request():
    """ 请求上下文处理
    :param
    :param
    :return:
    """
    def wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(self, *args, **kwargs):
            lc = LogCollect()
            lc.add_log("\n\n====================%s:%s====================" % (self.name, self.description))
            # lc.add_log("接口名称：%s" % self.name)
            # lc.add_log("接口描述：%s" % self.description)
            lc.add_log("PM信息：%s" % self.pm_info)
            lc.add_log("请求URL：[%s]%s" % (self.method, self.url_string()))
            if self.headers:
                lc.add_log("请求header：")
                for key, value in self.headers.items():
                    lc.add_log("%s:%s" % (key, value))
            if self.method.lower() in ["post", "put"]:
                lc.add_log("请求报文： %s" % json.dumps(self.body, sort_keys=True, indent=2, ensure_ascii=False))
                if self.files:
                    lc.add_log("请求报文-上传文件： %s" % json.dumps(self._get_upload_dict(), sort_keys=True, indent=2))
            if self.print_status:
                lc.print()
            ret, output, err = func(self, *args, **kwargs)
            ret = self._wrap_response_class(ret, output, err, self)
            lc.add_log("Status_code：%s Reason: %s" % (ret.status_code, ""))
            if ret.ret and ret.status_code == 200 and ret.resp_json:
                lc.add_log("响应报文： %s" % json.dumps(ret.resp_json, sort_keys=True, indent=2, ensure_ascii=False))
            else:
                lc.add_log("响应内容： %s" % ret.text)

            if self.print_status:
                lc.print()
            ret.log_obj = lc  # 传递日志收集对象
            return ret
        return inner_wrapper
    return wrapper


def wrap_request_grpc():
    """ 请求上下文处理
    :param
    :param
    :return:
    """

    def wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(self, *args, **kwargs):
            from grpc._channel import _InactiveRpcError
            lc = LogCollect()
            lc.add_log("\n\n====================%s:%s:%s====================" % (self.service_name, self.method_name,
                                                                                 self.description))
            # lc.add_log("====================我是分割线====================")
            # lc.add_log("接口名称：%s.%s" % (self.service_name, self.method_name))
            # lc.add_log("接口描述：%s" % self.description)
            lc.add_log("请求Message： %s" % json.dumps(self.body, sort_keys=True, indent=2, ensure_ascii=False))
            if self.print_status:
                lc.print()
            r, errobj = None, None
            try:
                r = func(self, *args, **kwargs)
            except _InactiveRpcError as e:
                errobj = e
            ret = self._wrap_response_class(r, self, errobj)
            if ret.error_code == 0:
                lc.add_log("响应Message： %s" % json.dumps(ret.json_get(unescape=False), sort_keys=True, indent=2, ensure_ascii=False))
            else:
                lc.add_log("响应结果：")
                lc.add_log("error_code: %s " % ret.error_code)
                lc.add_log("detail: %s" % ret.error_msg)
                lc.add_log("RequestID: %s" % ret.request_id)
            if self.print_status:
                lc.print()
            ret.log_obj = lc  # 传递日志收集对象
            return ret
        return inner_wrapper
    return wrapper








def res_func(res):
    if res >= 5:
        return False
    else:
        return True

@wait(timeout=5, interval=1, util_func=res_func, raise_exception=True)
def demo_func(self, timeout=100, interval=20):
    print('a')
    return random.randint(0,10)

if __name__ == '__main__':
    resp = demo_func('a', timeout=10, interval=1)