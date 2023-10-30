# -*- coding: utf-8 -*-

import getopt
import sys

import time
import traceback


class ScriptAction(object):
    """ 脚本启动入口类
    """

    def __init__(self, info):
        """ 脚本信息
        :param info:
        """
        super(ScriptAction, self).__init__()
        self._info = info

    @property
    def info(self):
        """
        :return:
        """
        return self._info

    @staticmethod
    def log(msg, level="INFO"):
        """
        @note: simple log for job
        """
        print("[%-10s%s] %s" % (level, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))

    def Usage(self):
        """
        @note: Usage for
        """
        des = ""
        for item in self.info["detail"]:
            des += "%-20s %s\n" % (item["action"], item["des"])
        print("Usage: python %s [action] [option]" % self.info["script_name"])
        print("Action 可选列表：")
        print(des)

    def get_action_obj(self, action_name):
        for action_obj in self.info["detail"]:
            if action_name == action_obj["action"]:
                return action_obj
        return None

    def get_params(self, action_obj):
        params = ""
        name_list = []
        for tag, res in action_obj["option"].items():
            _str = tag
            if "default" not in res:
                _str += ":"
            params += _str
            name_list.append("%s=" % res["name"])
        return "h%s" % params, name_list

    def sub_usage(self, action_obj):
        params = ""
        des = "%-20s help\n" % "-h --help"
        for tag, option in action_obj["option"].items():
            _str = tag
            if "default" not in option:
                _str += ":"
            params += _str
            flag = "-%s --%s" % (tag, option["name"])
            des += "%-20s %s" % (flag, option["des"])
            if "must" in option and option["must"]:
                des += "[必填]"
            des += "\n"
        print("Usage: python %s %s [h%s]" % (self.info["script_name"], action_obj["action"], params))
        print(des)

    def run(self, argv=None):
        """
           @note: Main func
           """
        if argv is None:
            argv = sys.argv
        try:
            if len(argv) == 1:
                self.Usage()
                return 1
            action = argv[1]
            action_obj = self.get_action_obj(action)
            if not action_obj:
                self.log("action error", "ERROR")
                self.Usage()
                return 1
            params_str, name_list = self.get_params(action_obj)
            try:
                opts, args = getopt.getopt(argv[2:], params_str, name_list)
            except Exception as err_msg:
                self.Usage()
                return 1
            # get opt
            kw = {}
            for name, value in opts:
                print(name, value)
                if name in ("-h", "--help"):
                    self.sub_usage(action_obj)
                    return 0
                for tag, option in action_obj["option"].items():
                    if name in ("-%s" % tag, "--%s" % option["name"]):
                        if "default" in option:
                            kw.update({option["name"]: option["default"]})
                        else:
                            kw.update({option["name"]: value})

            for tag, option in action_obj["option"].items():
                if "must" in option and option["must"] and option["name"] not in kw:
                    self.sub_usage(action_obj)
                    return 1

            getattr(action_obj["module"], action_obj["action"])(**kw)

            time.sleep(1)
            return 0
        except Exception as e:
            err_msg = traceback.format_exc()
            self.log("%s" % err_msg, "ERROR")
            return 2
