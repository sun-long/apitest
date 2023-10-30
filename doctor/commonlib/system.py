#!/usr/bin/env python
#-*-coding: utf-8 -*-

import sys
import subprocess
import os
import select
import time


def ci_system(cmd, output=False, loglevel=None, errlevel="warning", \
        prompt="Run cmd", pflag=False, rt_log=False, logger=None, events=None):
    """
    @note: (阻塞)调用shell命令cmd
           如果要后台启动程序，请使用ci_system_async()

    @param
        output:
            - 为True时，返回cmd的 (return code, stdout output, stderr output)
            - 为False时，只返回cmd的return code。命令的输出被重定向到/dev/null
        loglevel:
            - 可以为None, "debug", "info", "success", "warning", "diagnose", "error", "critical"
            - 不为None时，执行的cmd被记入日志
        errlevel:
            - 可以为None, "debug", "info", "success", "warning", "diagnose", "error", "critical"
            - 不为None时，当cmd返回码不为0，则记录日志
        pflag: print flag。为True时打印cmd的屏幕输出
        rt_log: realtime logger
        logger: log object。默认为ci_log
        prompt: 日志提示符
    """
    if loglevel and hasattr(logger, loglevel):
        log_func = getattr(logger, loglevel)
        log_func("%s: %s", prompt, cmd)

    if errlevel and hasattr(logger, errlevel):
        err_func = getattr(logger, errlevel)
    else:
        err_func = None

    # if events is not None:
    #     return _ci_expect(cmd, events)

    if rt_log and logger:
        return _ci_system_rt_log(cmd, err_func, log_func)

    if output:
        return _ci_system_output(cmd, err_func, prompt, pflag)
    else:
        return _ci_system_output(cmd, err_func, prompt, pflag)[0]


def ci_system_async(cmd, loglevel=None, prompt="Run cmd", pflag=False, logger=None):
    """
    @note: 后台运行shell命令cmd

    @param
        loglevel:
            - 可以为None, "debug", "info", "success", "warning", "diagnose", "error", "critical"
            - 不为None时，执行的cmd被记入日志
        prompt: 日志提示符
        pflag: print flag。为True时打印cmd的屏幕输出
        logger: log object。默认为ci_log
    @return: 返回cmd的pid
    """
    if loglevel and hasattr(logger, loglevel):
        log_func = getattr(logger, loglevel)
        log_func("%s: %s", prompt, cmd)

    if pflag:
        dev = sys.stdout
    else:
        dev = open("/dev/null", "w")
    proc = subprocess.Popen(cmd, shell=True, stdout=dev, stderr=subprocess.STDOUT)
    return proc.pid


def _ci_system_output(cmd, err_func, prompt, pflag):
    """@return: 返回(return code, stdout output, stderr output)"""
    outdata_l = []
    errdata_l = []
    import fcntl
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # set proc stdout&stderr Non-Block
    for f in [proc.stdout, proc.stderr]:
        flags = fcntl.fcntl(f, fcntl.F_GETFL)
        fcntl.fcntl(f, fcntl.F_SETFL, flags | os.O_NONBLOCK)

    while True:
        # polling
        ret = proc.poll()
        r, w, x = select.select([proc.stdout, proc.stderr], [], [], 1)

        if proc.stdout in r:
            tmp_out = proc.stdout.read()
            outdata_l.append(tmp_out.decode())
            if pflag:
                sys.stdout.write(tmp_out.decode())

        if proc.stderr in r:
            tmp_err = proc.stderr.read()
            errdata_l.append(tmp_err.decode())
            if pflag:
                sys.stdout.write(tmp_err.decode())

        if ret is not None:
            # cmd end
            break

    outdata = "".join(outdata_l)
    errdata = "".join(errdata_l)

    if ret != 0 and err_func:
        # cmd ret not 0
        if errdata:
            err_func("Return %d when %s: %s\nError message: %s", ret, prompt, cmd, errdata)
        else:
            err_func("Return %d when %s: %s", ret, prompt, cmd)

    return ret, outdata, errdata

def _ci_system_rt_log(cmd, err_func, logfunc=None):
    """@return: 返回(return code, stdout output, stderr output)"""
    outdata_l = []
    errdata_l = []
    import fcntl
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # stderr�����ǵ�����PIPE

    # set proc stdout&stderr Non-Block
    for f in [proc.stdout, proc.stderr]:
        flags = fcntl.fcntl(f, fcntl.F_GETFL)
        fcntl.fcntl(f, fcntl.F_SETFL, flags | os.O_NONBLOCK)

    while True:
        # polling
        ret = proc.poll()
        r, w, x = select.select([proc.stdout, proc.stderr], [], [], 1)     # ��������1s��EOFҲ��linux��Ϊ������

        if proc.stdout in r:
            tmp_out = proc.stdout.read()
            outdata_l.append(tmp_out)

            if logfunc is not None:
                tmp_out_lines = tmp_out.split('\n')
                for tmp_out_line in tmp_out_lines:
                    if tmp_out_line == "" or tmp_out_line == "\n":
                        continue
                    logfunc(tmp_out_line)

        if proc.stderr in r:
            tmp_err = proc.stderr.read()
            errdata_l.append(tmp_err)

            if logfunc is not None:
                tmp_err_lines = tmp_err.split('\n')
                for tmp_err_line in tmp_err_lines:
                    if tmp_err_line == "" or tmp_err_line == "\n":
                        continue
                    err_func(tmp_err_line)

        if ret is not None:
            # cmd end
            break

    outdata = "" . join(outdata_l)
    errdata = "" . join(errdata_l)

    if ret != 0 and err_func:
        # cmd ret not 0
        if errdata:
            err_func("Return %d when Run [%s]: \nError message: %s" % (ret, cmd, errdata))
        else:
            err_func("Return %d when Run [%s]" % (ret, cmd))

    return ret

def __split(contents, split):
    """
    @note: 将换行的字符格式化为列表类型
    """
    if split is True:
        splitter = '\n'
        if contents.endswith('\r\n'):
            splitter = '\r\n'
        contents = filter(lambda x: x.strip(), contents.split(splitter))
    return contents
