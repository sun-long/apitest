#!/usr/bin/env python
# -*-coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
@Authors:          wangan02(wangan02@baidu.com)
@Date:             2020/05/06 10:00:06
@Last Modified:    2020/05/06 10:00:06
@Summary:          main script
"""

import sys

from commonlib.script_action import ScriptAction
from scripts import client_tools, postman_tools

""" 启动文件使用说明
demo
INFO = {"script_name": "main.py", #本文件名称
        "detail":
            [
                {
                    "action": "gen_message", # 操作名称，需要对应模块中的方法名称
                    "module": grpc_tools, #待调用的模块名称
                    "des": "生成proto message数据包", #描述，会显示在帮助中
                    "option": {
                        "p": {"name": "product_name", "des": "项目名称", "must": True, default=1},
                        # name:参数名，要对应模块中的参数变量
                        # des：描述信息
                        # must：如果有该字段且该字段为True，则必须加该参数
                        # default： 如果有该字段，则不需要传入值，会默认赋值给该参数
                    }
                },
            ]
        }
"""

INFO = {"script_name": "main.py",
        "detail":
            [
                # {
                #     "action": "gen_message",
                #     "module": grpc_tools,
                #     "des": "生成proto message数据包",
                #     "option": {
                #         "p": {"name": "product_name", "des": "项目名称", "must": True},
                #     }
                # },
                {
                    "action": "gen_swagger",
                    "module": postman_tools,
                    "des": "生成postman by swagger",
                    "option": {
                        "n": {"name": "name", "des": "生成文件名称", "must": False},
                        "d": {"name": "sdir", "des": "swagger文件目录", "must": True},
                        "i": {"name": "host", "des": "服务器IP及端口", "must": False},
                        "f": {"name": "file", "des": "指定文件名", "must": False},

                    }
                },
                {
                    "action": "list_swagger",
                    "module": postman_tools,
                    "des": "生成swagger信息",
                    "option": {
                        "d": {"name": "sdir", "des": "swagger文件目录", "must": True},
                    }
                },
                {
                    "action": "update_swagger_json",
                    "module": postman_tools,
                    "des": "更新swagger json文件",
                    "option": {
                        "d": {"name": "sdir", "des": "swagger文件目录", "must": True},
                        "u": {"name": "username", "des": "sso登录名(该账号需开通相应权限)", "must": True},
                        "p": {"name": "password", "des": "sso密码", "must": True},
                        "d": {"name": "sdir", "des": "swagger文件目录", "must": True},
                        "f": {"name": "file", "des": "swagger文件名称,填写只更新该文件，不填写更新所有", "must": False},
                        "v": {"name": "chromeversion", "des": "chromeDriver驱动版本号，默认110,如果没有请先放到commonlib/driver/*",
                              "must": False},
                    }
                },
                # {
                #     "action": "post_data",
                #     "module": grpc_tools,
                #     "des": "推送数据",
                #     "option": {
                #         "p": {"name": "yaml_path", "des": "yaml文件名称或绝对路径", "must": True},
                #         "c": {"name": "config", "des": "tom配置文件名称", "must": False},
                #         "d": {"name": "device_id", "des": "device_id", "must": False},
                #         "a": {"name": "ak", "des": "ak", "must": False},
                #         "s": {"name": "sk", "des": "sk", "must": False},
                #         "t": {"name": "host", "des": "host", "must": False},
                #         "i": {"name": "static_id", "des": "静态库", "must": False},
                #         "r": {"name": "stream_id", "des": "动态库", "must": False},
                #     }
                # },
                {
                    "action": "download_package",
                    "module": client_tools,
                    "des": "推送数据",
                    "option": {
                        "u": {"name": "uuid", "des": "包uuid", "must": True},
                        "t": {"name": "target_dir", "des": "下载存储目录", "must": False},
                    }
                },
                {
                    "action": "deploy_product",
                    "module": client_tools,
                    "des": "部署端",
                    "option": {
                        "u": {"name": "uuid", "des": "包uuid", "must": True},
                        "v": {"name": "version", "des": "version版本", "must": True},
                        "i": {"name": "ip", "des": "ip", "must": True},
                        "p": {"name": "port", "des": "port", "must": True},
                        "s": {"name": "username", "des": "username", "must": True},
                        "w": {"name": "password", "des": "password", "must": True},
                        "d": {"name": "download_path", "des": "下载存储路径，可为空", "must": False},
                    }
                },
                {
                    "action": "build_package",
                    "module": client_tools,
                    "des": "打包",
                    "option": {
                        "b": {"name": "branch_name", "des": "构建分支名称", "must": True},
                        "c": {"name": "config_name", "des": "配置名称", "must": True},
                        "d": {"name": "description", "des": "描述信息", "must": True},
                    }
                },
                {
                    "action": "batch_build_package",
                    "module": client_tools,
                    "des": "批量打包",
                    "option": {
                        "b": {"name": "branch_name", "des": "构建分支名称", "must": True},
                        "u": {"name": "update", "des": "升级包", "must": False},
                        "e": {"name": "env_type", "des": "环境类型", "must": True},
                        "d": {"name": "description", "des": "描述信息后缀", "must": False},
                        "t": {"name": "test", "des": "描述信息", "must": False},
                    }
                },
                {
                    "action": "config_list",
                    "module": client_tools,
                    "des": "config列表",
                    "option": {
                        "b": {"name": "branch_name", "des": "构建分支名称", "must": True},
                    }
                },
                {
                    "action": "branch_list",
                    "module": client_tools,
                    "des": "branch列表",
                    "option": {
                        "b": {"name": "desc", "des": "dafd", "must": True},
                    }
                },
                {
                    "action": "build_result",
                    "module": client_tools,
                    "des": "查询构建结果",
                    "option": {
                        "p": {"name": "product_name", "des": "项目名称,可不填", "must": False},
                        "l": {"name": "last_count", "des": "显示条数", "must": True},
                    }
                },
                {
                    "action": "gen_api_template",
                    "module": postman_tools,
                    "des": "生成api模板",
                    "option": {
                        "s": {"name": "swagger_path", "des": "swagger名称或绝对路径", "must": True},
                    }
                },
                {
                    "action": "gen_case_template",
                    "module": postman_tools,
                    "des": "生成test_case模板",
                    "option": {
                        "s": {"name": "swagger_path", "des": "swagger名称或绝对路径", "must": True},
                    }
                },
                {
                    "action": "gen_conftest_template",
                    "module": postman_tools,
                    "des": "生成conftest模板",
                    "option": {
                        "s": {"name": "swagger_path", "des": "swagger名称或绝对路径", "must": True},
                    }
                },
                {
                    "action": "gen_all_template",
                    "module": postman_tools,
                    "des": "生成整套模板",
                    "option": {
                        "s": {"name": "swagger_path", "des": "swagger名称或绝对路径", "must": True},
                    }
                },
            ]
        }
if __name__ == "__main__":
    sys.exit(ScriptAction(INFO).run())
