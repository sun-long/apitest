#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import shutil

from commonlib import utils, time_utils, config, file_utils
from commonlib.decorator import wait
from commonlib.oss import OssTool
from defines.belt.api.rasmanager_aide_service_swagger import RasmanagerAideSwaggerApi
from commonlib.log_utils import log
import json
import os

"""
使用说明：


"""

RASINGRESS_STATUS_AVAILABLE = 'AVAILABLE'
RASINGRESS_STATUS_UNAVAILABLE = 'UNAVAILABLE'


def getDeviceByIDUntilAvailableFunc(resp):
    """ 仅适用于仅有1个ingressType的情况"""
    if resp.status_code == 200 and \
            resp.error_code == 0 and \
            resp.json_get("device_detail.device.driver.ingresses.0.status") == RASINGRESS_STATUS_AVAILABLE:
        return True
    else:
        status = None
        try:
            status = resp.json_get("device_detail.device.driver.ingresses.0.status")
        except:
            pass
        log().info("status_code:%s, ingress_status:%s wait." % (resp.status_code, status))
        return False


def getDeviceByIDUntilNotFoundFunc(resp):
    """ 查询设备直到NotFound"""
    if resp.status_code == 404:
        return True
    else:
        return False


# resp是self.RasManager_GetAssignmentGetApi的返回结果
def getAssignmentsUntilRunningFunc(resp):
    """ 仅适用于仅有1个ingressType的情况"""
    if resp.status_code == 200 and \
            resp.json_get("assignment.state") == "AS_EL_RUNNING":
        return True
    else:
        return False

# resp是self.RasManager_GetAssignmentGetApi的返回结果
def GetDataCollectingTaskUntilSubmitedFunc(resp):
    """ 轮训数据回流任务状态，当状态为Submited的时候说明任务已完成"""
    if resp.status_code == 200 and \
            resp.json_get("task.status.state") == 'Submited':
        log().info("数据回流任务已经处理完成")
        return True
    else:
        log().info("数据回流任务已经处理尚未完成，请等待")
        return False




class RasmanagerAideSwaggerBusiness(RasmanagerAideSwaggerApi):
    """ 业务类代码写在这里"""

    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(RasmanagerAideSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        # self.TOKEN_NAME = "X-Belt-Token"
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

        aidePrefix = "%s/FallDetection" % inte_obj.path_prefix
        if inte_obj.path == '/v1/CreateAssignment':
            inte_obj.set_headers('X-Belt-Action', 'CreateFallDetectionAssignment')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(aidePrefix)
        elif inte_obj.path == '/v1/DeleteAssignment':
            inte_obj.set_headers('X-Belt-Action', 'DeleteFallDetectionAssignment')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(aidePrefix)
        elif inte_obj.path == '/v1/GetAssignment':
            inte_obj.set_headers('X-Belt-Action', 'GetFallDetectionAssignment')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(aidePrefix)
        elif inte_obj.path == '/v1/UpdateAssignment':
            inte_obj.set_headers('X-Belt-Action', 'UpdateFallDetectionAssignment')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(aidePrefix)
        elif inte_obj.path == '/v1/ListAssignments':
            inte_obj.set_headers('X-Belt-Action', 'ListFallDetectionAssignments')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(aidePrefix)
        else:
            inte_obj.set_headers('X-Belt-Action', inte_obj.path_action)
            inte_obj.set_headers('X-Belt-Version', inte_obj.path_version)

    # 创建一个assginment并删除
    def createAssignment(self, device_id, assignment_config=None, rotate_config=None, is_delete=True):
        """ 创建Assignment"""
        if assignment_config is None:
            assignment_config = {
                "data": {
                    "rules": [{
                        "roi": {
                            "vertices": [{
                                "x": 0,
                                "y": 0
                            },
                                {
                                    "x": 1,
                                    "y": 1
                                }
                            ]
                        },
                        "rule_id": "a",
                    }]
                },
                # "user_callback_url": "http://10.4.132.19:9999"
                # "user_callback_url": "http://10.114.1.38:9999"
                # "user_callback_url": "http://10.151.125.10:9999"
                # "user_callback_url": "http://10.151.3.74:9997"
                #"user_callback_url": "http://10.4.132.35:9999"
                # stage环境用下面这个
                #"user_callback_url":"http://test-callback-service.crd.svc.cluster.local:9999"
            }
        if not rotate_config:
            rotate_config = {
                "retention": {
                    "day": 7
                }
            }
            # rotate_config = None
        resp = self.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                       assignment_config=assignment_config,
                                                       rotate_config=rotate_config)

        #添加clear up
        def clearUp():
            self.RasManager_DeleteAssignmentPostApi(device_id=device_id)

        # is_delete决定这个任务是否要删除
        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        return resp

    @wait(timeout=180, interval=2, util_func=getDeviceByIDUntilAvailableFunc, raise_exception=True)
    def getDeviceByIDUntilAvailable(self, device_id):
        """ 查询设备直到设备可用"""
        return self.RasManager_GetDeviceDetailGetApi(device_id, print_log=False)

    @wait(timeout=120, interval=2, util_func=getDeviceByIDUntilNotFoundFunc, raise_exception=True)
    def getDeviceByIDUntilNotFound(self, device_id, loginToken=None):
        """ 查询设备直到设备可用"""
        return self.RasManager_GetDeviceDetailGetApi(device_id, print_log=False, loginToken=loginToken)

    @wait(timeout=180, interval=2, util_func=getAssignmentsUntilRunningFunc, raise_exception=True)
    def getAssignmentsUntilRunning(self, device_id=None, spu_name=None):
        """ 查询任务直到任务可用"""
        # 隔2秒掉一次RasManager_GetAssignmentGetApi，将返回结果传给getAssignmentsUntilRunningFunc，如果返回True则停止，否则一直轮询直到超时
        return self.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=spu_name, print_log=False)


    @wait(timeout=180, interval=2, util_func=GetDataCollectingTaskUntilSubmitedFunc, raise_exception=True)
    def getDataCollectingTaskUntilSubmited(self, task_id=None):
        """ 查询数据回流任务直到任务已提交"""
        # 隔2秒掉一次
        #resp = RasmanagerAideApi.RasManager_GetDataCollectingTaskGetApi，将返回结果传给GetDataCollectingTaskUntilSubmitedFunc，如果返回True则停止，否则一直轮询直到超时
        return self.RasManager_GetDataCollectingTaskGetApi(task_id=task_id,print_log=False)

    def deleteDeviceById(self, device_id):
        """ 根据id删除device"""
        resp = self.RasManager_GetDeviceDetailGetApi(device_id, print_log=False)
        if resp.status_code == 404:
            # 已经不存在就返回了
            return
        self.RasManager_DeleteDevicePostApi(device_id=device_id)
        self.getDeviceByIDUntilNotFound(device_id)

    def getAllAssignments(self, device_id=None, loginToken=None, print_log=True, interface_desc=None):
        """ 获取所有符合条件的Assignment"""
        offset = 0
        limit = 20
        assignment_list = []
        while True:
            resp = self.RasManager_ListAssignmentsGetApi(device_id=device_id, paging_offset=offset,
                                                         paging_limit=limit, loginToken=loginToken,
                                                         print_log=print_log, interface_desc=interface_desc)
            assert resp.status_code == 200
            assignment_list.extend(resp.json_get("assignments"))
            if offset + limit >= resp.json_get("paging.total"):
                break
            offset += limit
        return assignment_list

    def getAllDeviceDetail(self, spu_names=None, filter_with_spu=None, print_log=True):
        """ 获取所有符合条件的devices"""
        offset = 0
        limit = 20
        device_list = []
        while True:
            resp = self.RasManager_ListDeviceDetailsGetApi(spu_names=spu_names, filter_with_spu=filter_with_spu,
                                                           paging_offset=offset, paging_limit=limit,
                                                           print_log=print_log)
            assert resp.status_code == 200
            device_list.extend(resp.json_get("device_detail"))
            if offset + limit >= resp.json_get("paging.total"):
                break
            offset += limit
        return device_list

    def CreateDataCollectingTask(self, devices=None, start_time=None, end_time=None, value=None, operator=None,
                                 start_date=None, end_date=None,access_key=None,secret_key=None ):
        """创建数据回流任务"""
        task = {
            "name": "lc001",
            "desc": "lc001_desc",
            "spu_name": "FallDetection",
            "time_config": {
                "start_date": start_date,
                "end_date": end_date,
                "windows": [
                    {
                        "start_time": start_time,
                        "end_time": end_time
                    }
                ]
            },
            "target_config": {
                "target_type": 0,
                "ceph_config": {
                    "access_key": access_key,
                    "secret_key": secret_key,
                    "bucket": "monolith_t1",
                    "prefix": "belt/",
                    "protocol": "s3"
                },
                "cluster_name": "SH-Ceph1424SSD"
            },
            "data_type": 1,
            "devices": devices,
            "event_filter": {
                "key": "data.targets.confidence",
                "value": value,
                "operator": operator
            },
            "auth_id": "A202211179",
            "acl": [
                {
                    "ad": "liangchen.vendor",
                    "name": "梁晨",
                    "expire_time": "2023-12-31T00:00:00.000Z"
                }
            ]
        }
        resp = self.RasManager_CreateDataCollectingTaskPostApi(task=task)
        return resp

    def DeleteAllDataCollectingTask(self):
        resp = self.RasManager_ListDataCollectingTaskGetApi(paging_offset=0, paging_limit=100, paging_total=100)
        assginment_list = []
        for i in resp.json_get("tasks"):
            assginment_list.append(i["task_id"])

        log().info("当前一共存在%d个任务" % (len(assginment_list)))
        for i in assginment_list:
            self.RasManager_DeleteDataCollectingTaskPostApi(task_id=i)

        # 删除后再次查一下
        resp = self.RasManager_ListDataCollectingTaskGetApi(paging_offset=0, paging_limit=100, paging_total=100)
        log().info("当前一共存在%d个任务" % (len(assginment_list)))
        return resp

    def ListAllDataCollectingTask(self, paging_offset=0, paging_limit=100, paging_total=100):
        resp = self.RasManager_ListDataCollectingTaskGetApi(paging_offset=paging_offset, paging_limit=paging_limit,
                                                            paging_total=paging_total)
        assginment_list = []
        for i in resp.json_get("tasks"):
            assginment_list.append(i["task_id"])
        return assginment_list

    def download_oss(self, num=None, access_key_id=None, access_key_secret=None, endpoint=None, bucket_name=None):
        i = 1
        # 这块必须打/，否则会进入正则匹配monolith/siphon/20
        project_dir = 'monolith/siphon/{}/'.format(num)
        ot = OssTool(access_key_id=access_key_id,
                     access_key_secret=access_key_secret,
                     endpoint=endpoint,
                     bucket_name=bucket_name)
        # fpath_list=['monolith/siphon/100/100_0_9322a58dbcadf471abda194d88cc2f7b.zip']
        fpath_list = ot.select_project_dir(project_dir)
        # 保存的地方'/home/SENSETIME/liangchen.vendor/git/doctor/temp/dataCollect'
        save_dir = os.path.join(config.temp_path, "dataCollect")
        # tempzip_dir='/home/SENSETIME/liangchen.vendor/git/doctor/temp/dataCollect/tempzip'
        tempzip_dir = os.path.join(save_dir, "tempzip")
        # 如果目录存在，则删除
        if os.path.exists(save_dir):
            shutil.rmtree(save_dir)
        # 新建两个目录
        os.makedirs(save_dir)
        os.makedirs(tempzip_dir)

        # 判断返回列表长度，如果大于０证明有文件，再执行以下操作
        if len(fpath_list) > 0:
            fpath = fpath_list[0]  # TODO 如果1个都没有这里就报错了
            fname = os.path.basename(fpath)
            save_path = os.path.join(save_dir, fname)
            if fname:
                # 下载文件
                log().info("开始从oss浏览器下载文件，文件路径为%s" % fpath)
                ot.get_object_to_file(fpath, save_path)
        else:
            log().info("无法获取对应文件，请检查路径")

        # 打开压缩文件,将指定的txt文件解药到tempzip目录
        file_utils.zip_file_extract(save_path, tempzip_dir, suffix_list=['txt'])

        # 打开这个events.txt文件
        i=1
        event_file = os.path.join("/home/SENSETIME/liangchen.vendor/git/doctor/temp/dataCollect/tempzip", "events.txt")
        # TODO 验证 event_file 这个文件存在
        if os.path.exists(event_file):
            with open(event_file, "r", encoding="utf-8") as f:
                date_list = f.readlines()
            confidence_list = []
            for i in date_list:
                i = json.loads(i)
                confidence_list.append(i["task"]["data"]["targets"][0]["confidence"])
            print(confidence_list)
            return confidence_list
        else:
            log().info("不存在events.txt这个文件，请检查下载是否成功")

        #递归删除文件
        #shutil.rmtree(save_dir)


if __name__ == '__main__':
    c = RasmanagerAideSwaggerBusiness(RasmanagerAideSwaggerApi)
    c.download_oss(num=100)
