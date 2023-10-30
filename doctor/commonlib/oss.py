#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   oss.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/2 下午8:30   wangan      1.0         None
'''




class OssTool(object):
    def __init__(self, access_key_id, access_key_secret, endpoint, bucket_name):
        # self.access_key_id = 'LTAI4GEmepyBws22AgsUBYZP'
        # self.access_key_secret = 'ZdNNsq3r5s8IDXEGS7iHSfdhCxYi0x'
        # self.endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'
        # self.bucket_name = 'lf-fake-test'
        import oss2
        self.bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret),
                                  endpoint,
                                  bucket_name=bucket_name)

    def select_project_dir(self, project_dir):
        import oss2
        fpath_list = []
        for f in oss2.ObjectIterator(self.bucket, project_dir):
            fpath_list.append(f.key)
        return fpath_list

    def get_object_to_file(self, origin_path, save_path):
        """ 从oss指定路径获取文件"""
        file_name = self.bucket.get_object_to_file(origin_path, save_path)
        return file_name

def oss_up_cb(up_size, total_size):
    print(up_size, total_size)


if __name__ == '__main__':
    i=1
    # access_key_id = 'LTAI4GEmepyBws22AgsUBYZP'
    # access_key_secret = 'ZdNNsq3r5s8IDXEGS7iHSfdhCxYi0x'
    # endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'
    # bucket_name = 'lf-fake-test'
    # project_dir = 'monolith/siphon/205'
    # bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name=bucket_name)
    # for f in oss2.ObjectIterator(bucket, project_dir):
    #     i=1
    #     # 文件名
    #     fpath = f.key
    #     print(fpath)
    #     i=1
    #     # 删除
    #     # bucket.delete_object(fpath)
    #     # 下载
    #     local_dir = '/home/SENSETIME/liangchen.vendor/lc'
    #     fname = os.path.basename(fpath)
    #     if '' != fname:
    #         bucket.get_object_to_file(fpath, os.path.join(local_dir,os.path.basename(fpath)))
# 上传
# local_f = 'test.txt'
# cloud_f = project_dir + local_f
# bucket.put_object_from_file(cloud_f, local_f, progress_callback = oss_up_cb)
