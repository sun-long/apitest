#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file_utils.py
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/26 下午4:18   wangan      1.0     文件相关处理工具
'''
import os
import zipfile

from commonlib import config


def zip_file_extract(file_path, save_dir, suffix_list=None):
    """
        suffix List: ['txt', 'csv']
    """
    file_list = []
    if suffix_list and isinstance(suffix_list, str):
        suffix_list = [suffix_list]
    with zipfile.ZipFile(file=file_path, mode='r') as file_zip:
        for file in file_zip.namelist():
            #如果后缀是txt则解压，图片则忽略
            if suffix_list:
                if file.split(".")[-1] in suffix_list:
                    file_zip.extract(file, save_dir)
                    file_list.append(os.path.join(save_dir, file))
                    print("extract path:%s" % os.path.join(save_dir, file))
            else:
                file_zip.extract(file, save_dir)
                file_list.append(os.path.join(save_dir, file))
                print("extract path:%s" % os.path.join(save_dir, file))
    return file_list

if __name__ == '__main__':
    file_path = os.path.join(config.temp_path, "100_0_9322a58dbcadf471abda194d88cc2f7b.zip")
    save_dir = config.temp_path
    zip_file_extract(file_path, save_dir, suffix_list=['txt'])
