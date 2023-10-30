# --*--coding: utf-8 --*--
import json
import os

from commonlib import config
from core.collection import Collections


def load_postman(_dir):
    """ 加载postman导出的数据
    _dir: json文件目录

    """
    if not _dir.startswith("/"):
        _dir = os.path.join(config.pm_path, _dir)
    items, values = parse(_dir)
    col = Collections(items, values)
    return col


def read_json(_path):
    with open(_path, 'r') as f:
        results = json.loads(f.read())
        return results


def parse(_dir):
    items = {}
    values = {}
    for root, dirs, files in os.walk(_dir):
        for name in files:
            file_name = name.split(".")
            if file_name[-2] == "postman_collection":
                watch_file_path = os.path.join(root, name)
                results = read_json(watch_file_path)
                items[results["info"]["name"]] = results["item"]
            if file_name[-2] == "postman_environment":
                watch_file_path = os.path.join(root, name)
                results = read_json(watch_file_path)
                values[results["name"]] = results["values"]
    return items, values


def get_interface_info(collections):
    items = collections.items
    result = []
    for _ , info1 in items.items():
        for _1, info2 in info1.items():
            group_name = info2['name']
            for i in info2['item']:
                interface_name = i['name']
                result.append((group_name, interface_name))
    return result

if __name__ == '__main__':
    collections = load_postman("viper")
    result = get_interface_info(collections)
    for x in result:
        print('%s\t%s' % (x[0], x[1]))

    # getDevice = collections.interface('Argus设备接入[6个]', 'GetDevices 获取设备列表')
    # res = getDevice.request()
    # print(res)