#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rtsp_check.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/21 下午2:09   wangan      1.0         None
'''

# pip install opencv-python
import os

import cv2


def get_img_from_camera_net(rtsp, name, target_path=None):
    cap = cv2.VideoCapture(rtsp)
    i = 1
    while i < 2:
        ret, frame = cap.read()
        if target_path:
            _path = "%s/%s.jpg" % (target_path, name)
        else:
            _path = name + "_" + str(i) + '.jpg'
        cv2.imwrite(_path, frame)  # 存储为图像
        i += 1
    cap.release()


def check(file_list, rtsp_address, target_path):
    failed_list = []
    for name in file_list:
        rtsp = "rtsp://%s:8554/%s" % (rtsp_address, name)
        try:
            get_img_from_camera_net(rtsp, name, target_path=target_path)
            print("%s ok!" % rtsp)
        except:
            failed_list.append(rtsp)
            print("%s failed!" % rtsp)
    print("-----------------------------")
    print("Failed List:")
    for x in failed_list:
        print(x)

def traversal_files(path):
    file_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            file_list.append(name)

    print("file num:%s" % len(file_list))
    return file_list


if __name__ == '__main__':
    rtsp_address = "10.53.4.176"
    target = "/home/SENSETIME/wangan/belt/ff"
    file_list = traversal_files("/home/SENSETIME/wangan/belt/h264")
    check(file_list, rtsp_address, target)
