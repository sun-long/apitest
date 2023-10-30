#!/usr/bin/env python
# -*- coding: utf-8 -*-
# content of conftest.py
import datetime
import os
import sys

import pytest
import pytest_html
import toml
from py._xmlgen import html
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__)))))
from core import toml_utils
from core.ext_info import ExtFunctionInfo
from commonlib.config import project_path
from commonlib import utils
from commonlib import config as cf

PRINT_PASS_LOG = False  # 是否打印通过用例的日志

def pytest_addoption(parser):
    """ pytest 添加命令行执行参数"""
    parser.addoption("--config", action="store", default="nova_online", help="config file path, default custom")
    parser.addoption("--html_online", action="store", default="dev", help="html file name online")
    parser.addoption("--record", action="store", default="yes", help="yes/no")
    parser.addoption("--user", action="store", default="default", help="toml file user info")
    parser.addoption("--print_pass_log", action="store", default="yes", help="yes/no")

def pytest_configure(config):
    # 核心是每次测试更改传入的参数
    config_type = config.getoption("--config")
    _time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    result_path = os.path.join(cf.result_path, config_type, _time) 
     # 生成目录
    config.option.result_path = result_path
    if config.getoption('--html_online') != "dev":
        config.option.result_path = os.path.join(cf.project_path, "result/temp")

    if config.getoption('--html'):
        config.option.htmlpath = os.path.join(result_path, config.option.htmlpath)
        config.option.covpath = os.path.join(result_path, "cov.log")
        config.option.log_file = os.path.join(result_path, "report.log")

    if config.getoption('--record'):
        config.option.pmrecord = config.getoption('--record')
        config.option.pmpath = os.path.join(result_path, "pm")

    if config.getoption('--html_online') != "dev":
        config.option.htmlpath = config.getoption('--html_online')
        config.option.covpath = "result/cov.log"
        config.option.pmrecord = config.getoption('--record')
        config.option.pmpath = os.path.join(cf.project_path, "result/pm")
        config.option.log_file = os.path.join(cf.project_path, "result/report.log")

    if config.getoption('--print_pass_log') == "yes":
        global PRINT_PASS_LOG
        PRINT_PASS_LOG = True


    config_obj = toml_utils.gen_config_obj(config_type)
    config.option.config_obj = config_obj

    if "ConfigMap" in config_obj:
        configMapKeyList = config_obj.ConfigMap["_keys"]
        for configMapKey in configMapKeyList:
            exec('config.option.%s = config_obj.ConfigMap.%s' % (configMapKey, configMapKey))

    if "_extra" in config_obj and "_keys" in config_obj._extra and config_obj._extra["_keys"]:
        for extra_key in config_obj._extra["_keys"]:
            if "_keys" in config_obj._extra[extra_key]:
                for extra_name in config_obj._extra[extra_key]["_keys"]:
                    obj = config_obj._extra[extra_key][extra_name]
                    if "ConfigMap" in obj:
                        for configMapKey in obj.ConfigMap["_keys"]:
                            exec('config.option.%s = obj.ConfigMap.%s' % (configMapKey, configMapKey))

    config._metadata["Product"] = "Belt-test"
    config._metadata["Config"] = config_type
    config._metadata["Tags"] = config.getoption("-m")
    config._metadata.pop('Plugins')
    config._metadata.pop('Platform')
    config._metadata.pop('Packages')

    # 初始化代码库目录 ，待完善
    utils.init_test_dir(config)


def pytest_generate_tests(metafunc):
    """ 生成测试参数"""
    config_obj = metafunc.config.option.config_obj
    if "ConfigMap" in config_obj:
        for configMapKey in config_obj.ConfigMap["_keys"]:
            if configMapKey in metafunc.fixturenames:
                if configMapKey == 'user_info' and metafunc.config.getoption('--user') != "default":
                    configMapList = metafunc.config.getoption('--user').split(";")
                else:
                    configMapList = metafunc.config.getoption(configMapKey)
                metafunc.parametrize(configMapKey, configMapList, indirect=True)

    if "_extra" in config_obj and "_keys" in config_obj._extra and config_obj._extra["_keys"]:
        for extra_key in config_obj._extra["_keys"]:
            if "_keys" in config_obj._extra[extra_key]:
                for extra_name in config_obj._extra[extra_key]["_keys"]:
                    obj = config_obj._extra[extra_key][extra_name]
                    if "ConfigMap" in obj:
                        for configMapKey in obj.ConfigMap["_keys"]:
                            if configMapKey in metafunc.fixturenames:
                                configMapList = metafunc.config.getoption(configMapKey)
                                metafunc.parametrize(configMapKey, configMapList, indirect=True)

def pytest_assertrepr_compare(op, left, right):
    if op == "==":
        return ["Expected:%s, Actual:%s (Should be equal)" % (right, left)]
    if op == "!=":
        return ["Expected:%s, Actual:%s (Should be not equal)" % (right, left)]
    if op == ">":
        return ["Expected:%s, Actual:%s (Should be greater than)" % (right, left)]
    if op == "<":
        return ["Expected:%s, Actual:%s (Should be less than)" % (right, left)]
    if op == ">=":
        return ["Expected:%s, Actual:%s (Should be greater than or equal)" % (right, left)]
    if op == "<=":
        return ["Expected:%s, Actual:%s (Should be less than or equal)" % (right, left)]


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(3, html.th('Param'))
    # cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):   #清除执行成功的用例logs
    global PRINT_PASS_LOG
    if report.passed:
        if not PRINT_PASS_LOG:
            del data[:]
            data.append(html.div('PASS', class_='empty log'))


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    # prefix.extend([html.p("所属部门: 测试组")])
    # prefix.extend([html.p("测试人员: ")])
    pass

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    if hasattr(report, "description") and report.description:
        cells.insert(1, html.td(report.description))
    else:
        cells.insert(1, html.td("no desc"))
    case_name = cells[2][0]
    param_name = ""
    if "::" in case_name:
        case_name = case_name.split("::")[-1]
        if "[" in case_name:
            param_name = case_name.split("[")[-1].strip("]")
            case_name = case_name.split("[")[0]
    cells[2] = html.td(case_name)
    # cells.insert(3, html.td(datetime.datetime.now(), class_='col-time'))
    cells.insert(3, html.td(param_name))
    cells.insert(5, html.td(html.a("postman", href="pm/%s.postman_collection.json" % report.head_line,
                            target="_blank",
                            class_='col-links')))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    if report.outcome != 'passed':
        title = report.head_line.encode('utf-8').decode('unicode_escape')
        title = "%s-%s" % (title, report.when)
        error_msg = report.longreprtext
        caplog = report.caplog
        context = "-"*10 + "Exception Code" + "-"*10 + "\n" + \
                  error_msg + \
                  "-"*10 + "CapLog" + "-"*10 + "\n" + \
                  caplog
        if 'Skipped' not in error_msg:
            result_path = item.config.option.result_path
            title = os.path.join(result_path, "error", title)
            utils.write_error_file_in_result(title, context)

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session):
    # 在测试用例执行完成后执行，由于pytesttestreport也有使用此钩子函数，属于要加上执行的顺序trylast=True
    # email = session.config.getoption('--sendemail')
    # if email:
    #     file = CommunFun().get_new_file("D:\\xxx\\xxx\\xxx\\reports")
    #     sendEmail().send_email(email_to="xxxx@qq.com", filepath=file)
    pass


@pytest.fixture(scope="session")
def config_obj(request):
    """ 配置文件转化为dict"""
    #这里默认读的config_type
    config_type = request.config.getoption("--config")
    co =  toml_utils.gen_config_obj(config_type)
    co.result_path = request.config.option.result_path # 添加测试结果目录
    co.config_yaml = request.config.option.config # 添加测试结果目录
    return co


@pytest.fixture(scope="function")
def ext_info(request, ext_info_session):
    """ function级公共处理信息"""
    ef = ExtFunctionInfo()
    ef.doBefore()
    yield ef
    #添加后置方法
    ef.doAfter()
    ext_info_session.extendRequest(ef.request_list)
    if request.config.option.pmrecord == "yes":
        ef.genPostManFileOld(request.keywords.node.location[2],
                             pm_dir=request.config.option.pmpath)


@pytest.fixture(scope="session")
def ext_info_session(request):
    """ session级公共处理信息"""
    ef = ExtFunctionInfo()
    ef.doBefore()
    yield ef
    ef.doAfter()

    test_mark = request.config.getoption("-m")
    #避免覆盖率统计获取不到对应的接口列表暂时简单处理
    if test_mark not in ["Regression","ConsoleRegression","checkin"]:
        test_mark = "Regression"

    ef.interfaceCov(request.config.option.covpath,test_mark)
    if request.config.option.pmrecord == "yes":
        ef.genPostManFileOld("all",
                             pm_dir=request.config.option.pmpath)

@pytest.fixture(scope="session")
def configType(request):
    """ 配置文件名称 dev:staging online: icloud"""
    return request.config.getoption("--config")


if __name__ == '__main__':
    config_file = os.path.join(project_path, "conf/%s.toml" % "argus")
    conf = toml.load(config_file)
