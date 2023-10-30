# --*--coding: utf-8 --*--
import json
import os

from commonlib import config
from core.collection_swagger import CollectionsSwagger


def load_swagger(name):
    """ 加载swagger导出的数据
    _dir: json文件目录

    """
    _dir = name
    if not _dir.startswith("/"):
        _dir = os.path.join(config.swagger_path, _dir)
    items, values = parse(_dir)
    col = CollectionsSwagger(items, values)
    col.name = _dir
    col.swagger_dir_name = name
    return col


def read_json(_path):
    with open(_path, 'r') as f:
        results = json.loads(f.read())
        return results


def parse(_dir):
    items = {}
    values = {}
    if os.path.isdir(_dir):
        for root, dirs, files in os.walk(_dir):
            for name in files:
                if not name.endswith('json'):
                    continue
                watch_file_path = os.path.join(root, name)
                results = read_json(watch_file_path)
                items[name.split('.json')[0]] = results
    else:
        if not _dir.endswith('json'):
            raise Exception('not end json %s' % _dir)
        results = read_json(_dir)
        items[os.path.basename(_dir).split('.json')[0]] = results
    return items, values


if __name__ == '__main__':
    collections = load_swagger("minos")
    getDevice = collections.interface('account.swagger', 'AccountService_GetAks')
    getDevice.set_host('10.4.7.25')
    res = getDevice.request()
    print(res)