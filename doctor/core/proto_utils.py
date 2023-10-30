# --*--coding: utf-8 --*--
import os
import sys
sys.path.append('../..')
from commonlib import config
from core.collection_grpc import CollectionsGrpc


import importlib


def load_proto(_dir):
    """ 加载proto导出的数据
    _dir: json文件目录

    """
    if not _dir.startswith("/"):
        _dir = os.path.join(config.pb_path, _dir)
    sys.path.append(_dir)
    # sys.path.insert(0, _dir)
    items, pb2_module, pb2_grpc_module, var_items = parse(_dir)
    col = CollectionsGrpc(items, pb2_module, pb2_grpc_module, var_items, _dir)
    # sys.path.remove(_dir)
    return col


def parse(proto_dir):
    """ 解析proto文件"""
    items = {}
    pb2_module = {}
    pb2_grpc_module = {}
    var_items = {}
    for root, dirs, files in os.walk(proto_dir):
        prefix = root.split(config.project_path)[-1].replace('/', '.').lstrip('.')
        if root != proto_dir:  # 目前只遍历一级目录
            continue
        for name in files:
            if not name.endswith('pb2.py') and not name.endswith('pb2_grpc.py'):
                continue
            file_name = name.split(".")[0]
            p_name = file_name.split("_")[0]
            if name.endswith('pb2.py'):
                m = importlib.import_module("%s.%s" % (prefix, file_name))
                # m = importlib.import_module(".%s" % file_name, package=prefix)
                # m = importlib.import_module(file_name)
                pb2_module[p_name] = m
                # 构建可用的message
                var_dict = {name: f for name, f in m.__dict__.items() if callable(f)}
                if var_dict:
                    var_items[p_name] = var_dict

                descriptor = getattr(m, 'DESCRIPTOR')
                if not descriptor or len(descriptor.services_by_name) == 0:
                    continue
                if p_name not in items:
                    items[p_name] = {
                        'pb': {},
                        'pb_grpc': {},
                        'pb_grpc_servicer': {}
                    }
                if 'module_obj' not in items:
                    items[p_name]['module_obj'] = m
                for service_name, service_obj in descriptor.services_by_name.items():
                    items[p_name]['pb'].update({service_name: service_obj})
            elif name.endswith('pb2_grpc.py'):
                m = importlib.import_module("%s.%s" % (prefix, file_name))
                # m = importlib.import_module(file_name)
                pb2_grpc_module[p_name] = m
                stub_dict = {name: f for name, f in m.__dict__.items() if callable(f) and 'Stub' in name}
                if not stub_dict:
                    continue
                if p_name not in items:
                    items[p_name] = {
                        'pb': {},
                        'pb_grpc': {},
                        'pb_grpc_servicer': {}
                    }
                items[p_name]['pb_grpc'].update(stub_dict)

                servicer_dict = {name: f for name, f in m.__dict__.items() if callable(f) and name.endswith('Servicer') }
                if not servicer_dict:
                    continue
                items[p_name]['pb_grpc_servicer'] = servicer_dict


    return items, pb2_module, pb2_grpc_module, var_items


if __name__ == '__main__':
    # collections = load_proto("rrs")
    # collections.save_message()

    collections = load_proto("device_manager")
    collections.save_message()
    # getDevice = collections.interface('DeviceManagerSrv', 'GetDevices')
    # getDevice.set_host('device-manager.argus-staging:8081')
    # getDevice.update_body('AK', "l1-f37b7f8c-w0f55aa0948a")
    # getDevice.update_body('deviceID', ["479572b9436a00006"])
    # res = getDevice.request()
    # print(res.json)
    # print(res.error_code)
    # print(res.error_msg)